// resource_id: "451d9682-0b66-4403-8cc2-09e39cf0ad10"
// resource_type: "document"
// resource_name: "index"
const functions = require('firebase-functions');
const admin = require('firebase-admin');
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');
const axios = require('axios');
const { calculateStatistics } = require('./statisticsCalculator');

// Initialize Firebase Admin if not already initialized
if (!admin.apps.length) {
  admin.initializeApp();
}

const client = new SecretManagerServiceClient();
const db = admin.firestore();

// Canvas API base URL - BYU-Idaho Canvas instance
const CANVAS_BASE_URL = 'https://byui.instructure.com/api/v1';

// Helper function to get Canvas API key
async function getCanvasApiKey() {
  if (process.env.CANVAS_API_KEY) {
    return process.env.CANVAS_API_KEY.trim();
  }

  const projectId = process.env.GCLOUD_PROJECT || process.env.GCP_PROJECT || 'assignment-time';
  const secretName = 'CANVAS_API_KEY';
  const name = `projects/${projectId}/secrets/${secretName}/versions/latest`;

  const [version] = await client.accessSecretVersion({ name });
  return version.payload.data.toString().trim();
}

exports.helloWorld = functions.https.onRequest((req, res) => {
  res.send("Hello from Firebase!");
});

exports.testSecretAccess = functions.https.onRequest(async (req, res) => {
  try {
    const projectId = 'assignment-time';
    const secretName = 'CANVAS_API_KEY';
    
    // Get the current service account email
    const admin = require('firebase-admin');
    const serviceAccount = admin.app().options.credential;
    
    // Construct the secret name
    const name = `projects/${projectId}/secrets/${secretName}/versions/latest`;
    
    // Access the secret
    const [version] = await client.accessSecretVersion({ name });
    const secretValue = version.payload.data.toString();
    
    // Return success (don't expose the actual key for security)
    res.json({
      success: true,
      message: 'Successfully accessed CANVAS_API_KEY from Secret Manager',
      keyLength: secretValue.length,
      keyPrefix: secretValue.substring(0, 8) + '...'
    });
    
  } catch (error) {
    console.error('Error accessing secret:', error);
    
    // Get more detailed error information
    const errorDetails = {
      success: false,
      error: error.message,
      errorCode: error.code,
      details: 'Check IAM permissions for Secret Manager Secret Accessor role',
      troubleshooting: [
        '1. Verify the secret CANVAS_API_KEY exists in Secret Manager',
        '2. Check that Cloud Functions service account has Secret Manager Secret Accessor role',
        '3. Ensure the secret has a latest version',
        '4. Wait 1-2 minutes for IAM changes to propagate'
      ]
    };
    
    res.status(500).json(errorDetails);
  }
});

exports.debugPermissions = functions.https.onRequest(async (req, res) => {
  try {
    // Test basic Secret Manager access
    const projectId = 'assignment-time';
    const [secrets] = await client.listSecrets({
      parent: `projects/${projectId}`,
    });
    
    const secretNames = secrets.map(secret => secret.name.split('/').pop());
    
    res.json({
      message: 'Permission debugging info',
      projectId: projectId,
      availableSecrets: secretNames,
      hasCANVAS_API_KEY: secretNames.includes('CANVAS_API_KEY'),
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    res.status(500).json({
      error: error.message,
      errorCode: error.code,
      details: 'Cannot access Secret Manager at all - check basic IAM setup'
    });
  }
});

// Canvas API Integration Functions

// Fetch Canvas courses and store in Firestore
exports.fetchCanvasCourses = functions.https.onRequest(async (req, res) => {
  try {
    const apiKey = await getCanvasApiKey();
    const canvasUrl = `${CANVAS_BASE_URL}/courses`;
    
    const response = await axios.get(canvasUrl, {
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      params: {
        enrollment_type: 'student',
        enrollment_state: ['active', 'completed', 'inactive'],
        per_page: 100,
        include: ['teachers', 'instructors', 'enrollments', 'term']
      }
    });
    
    const courses = response.data;
    
    // Store courses in Firestore
    const batch = db.batch();
    const coursesRef = db.collection('canvas_courses');
    
    courses.forEach(course => {
      const courseDoc = coursesRef.doc(course.id.toString());
      batch.set(courseDoc, {
        id: course.id,
        name: course.name,
        course_code: course.course_code,
        enrollment_term_id: course.enrollment_term_id,
        start_at: course.start_at,
        end_at: course.end_at,
        workflow_state: course.workflow_state,
        termName: course.term?.name || null,
        termStartAt: course.term?.start_at || course.start_at || null,
        termEndAt: course.term?.end_at || course.end_at || null,
        overallCourseScore: course.enrollments?.[0]?.grades?.current_score ?? null,
        overallCourseGrade: course.enrollments?.[0]?.grades?.current_grade ?? null,
        lastFetched: admin.firestore.FieldValue.serverTimestamp(),
        ...course
      });
    });
    
    await batch.commit();
    
    res.json({
      success: true,
      message: `Successfully fetched and stored ${courses.length} courses`,
      courses: courses.map(course => ({
        id: course.id,
        name: course.name,
        course_code: course.course_code
      })),
      storedInFirestore: true
    });
    
  } catch (error) {
    console.error('Error fetching Canvas courses:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to fetch courses from Canvas API'
    });
  }
});

// Fetch assignments for a specific course and store in Firestore
exports.fetchCanvasAssignments = functions.https.onRequest(async (req, res) => {
  try {
    const courseId = req.query.courseId;
    if (!courseId) {
      return res.status(400).json({
        success: false,
        error: 'courseId query parameter is required'
      });
    }
    
    const apiKey = await getCanvasApiKey();
    const canvasUrl = `${CANVAS_BASE_URL}/courses/${courseId}/assignments`;
    
    const response = await axios.get(canvasUrl, {
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      params: {
        per_page: 100,
        include: ['submission', 'assignment_visibility']
      }
    });
    
    const assignments = response.data;
    
    // Store assignments in Firestore
    const batch = db.batch();
    const assignmentsRef = db.collection('canvas_assignments');
    
    assignments.forEach(assignment => {
      const assignmentDoc = assignmentsRef.doc(assignment.id.toString());
      batch.set(assignmentDoc, {
        id: assignment.id,
        course_id: parseInt(courseId),
        name: assignment.name,
        description: assignment.description,
        due_at: assignment.due_at,
        unlock_at: assignment.unlock_at,
        lock_at: assignment.lock_at,
        points_possible: assignment.points_possible,
        grading_type: assignment.grading_type,
        submission_types: assignment.submission_types,
        workflow_state: assignment.workflow_state,
        lastFetched: admin.firestore.FieldValue.serverTimestamp(),
        ...assignment
      });
    });
    
    await batch.commit();
    
    res.json({
      success: true,
      message: `Successfully fetched and stored ${assignments.length} assignments for course ${courseId}`,
      courseId: courseId,
      assignments: assignments.map(assignment => ({
        id: assignment.id,
        name: assignment.name,
        due_at: assignment.due_at,
        points_possible: assignment.points_possible
      })),
      storedInFirestore: true
    });
    
  } catch (error) {
    console.error('Error fetching Canvas assignments:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to fetch assignments from Canvas API'
    });
  }
});

// Get courses from Firestore
exports.getCoursesFromFirestore = functions.https.onRequest(async (req, res) => {
  try {
    const snapshot = await db.collection('canvas_courses').get();
    const courses = [];
    
    snapshot.forEach(doc => {
      courses.push({
        id: doc.id,
        ...doc.data()
      });
    });
    
    res.json({
      success: true,
      message: `Retrieved ${courses.length} courses from Firestore`,
      courses: courses,
      source: 'firestore'
    });
    
  } catch (error) {
    console.error('Error reading from Firestore:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to read courses from Firestore'
    });
  }
});

// Get detailed student course data with assignments and grades
exports.getStudentCourseDetails = functions.https.onRequest(async (req, res) => {
  try {
    const stateQuery = req.query.state;
    const includeEmpty = req.query.includeEmpty === 'true';

    const stateFilters = stateQuery
      ? stateQuery.split(',').map(state => state.trim().toLowerCase()).filter(Boolean)
      : [];

    const coursesSnapshot = await db.collection('canvas_courses').get();
    const assignmentsSnapshot = await db.collection('canvas_assignments').get();

    const assignmentsByCourse = new Map();
    assignmentsSnapshot.forEach(doc => {
      const assignmentData = doc.data();
      const courseId = assignmentData.course_id ?? assignmentData.courseId;
      if (courseId === undefined || courseId === null) {
        return;
      }
      const courseKey = courseId.toString();
      if (!assignmentsByCourse.has(courseKey)) {
        assignmentsByCourse.set(courseKey, []);
      }
      assignmentsByCourse.get(courseKey).push({
        id: assignmentData.id,
        name: assignmentData.name,
        courseId: courseId,
        courseName: assignmentData.course_name || assignmentData.courseName || null,
        dueAt: assignmentData.due_at || assignmentData.dueAt || null,
        unlockAt: assignmentData.unlock_at || assignmentData.unlockAt || null,
        lockAt: assignmentData.lock_at || assignmentData.lockAt || null,
        pointsPossible: assignmentData.points_possible ?? assignmentData.pointsPossible ?? null,
        htmlUrl: assignmentData.html_url || assignmentData.htmlUrl || null,
        gradingType: assignmentData.grading_type || assignmentData.gradingType || null,
        workflowState: assignmentData.workflow_state || assignmentData.workflowState || null,
        submission: assignmentData.submission
          ? {
              submittedAt: assignmentData.submission.submitted_at || null,
              score: assignmentData.submission.score ?? null,
              grade: assignmentData.submission.grade ?? null,
              gradedAt: assignmentData.submission.graded_at || null,
              late: assignmentData.submission.late ?? null,
              missing: assignmentData.submission.missing ?? null,
              excused: assignmentData.submission.excused ?? null
            }
          : null
      });
    });

    const courseDetails = [];
    coursesSnapshot.forEach(doc => {
      const courseData = doc.data();
      const courseKey = courseData.id ? courseData.id.toString() : null;
      if (!courseKey) {
        return;
      }

      const enrollmentStates = (courseData.enrollments || [])
        .map(enrollment => (enrollment.enrollment_state || enrollment.state || '').toLowerCase())
        .filter(Boolean);

      const courseStates = new Set([
        ...(courseData.workflow_state ? [courseData.workflow_state.toLowerCase()] : []),
        ...enrollmentStates
      ]);

      if (stateFilters.length && stateFilters.every(filter => filter !== 'all')) {
        const matchesState = stateFilters.some(filter => courseStates.has(filter));
        if (!matchesState) {
          return;
        }
      }

      const courseAssignments = assignmentsByCourse.get(courseKey) || [];
      if (!includeEmpty && courseAssignments.length === 0) {
        return;
      }

      const teachers = (courseData.teachers || courseData.instructors || []).map(teacher => ({
        id: teacher.id,
        name: teacher.name || teacher.display_name || null,
        sortableName: teacher.sortable_name || null,
        email: teacher.email || null,
        htmlUrl: teacher.html_url || null
      }));

      const normalizedAssignments = courseAssignments.map(assignment => {
        const submission = assignment.submission || null;

        return {
          ...assignment,
          courseName: assignment.courseName || courseData.name || null,
          courseCode: courseData.course_code || null,
          termName: assignment.termName || courseData.termName || courseData.term?.name || null,
          submitted: submission ? submission.submittedAt != null : false,
          graded: submission ? (submission.grade != null || submission.score != null || submission.gradedAt != null) : false,
          late: submission?.late ?? null,
          missing: submission?.missing ?? null,
          excused: submission?.excused ?? null
        };
      });

      courseDetails.push({
        id: courseData.id,
        name: courseData.name,
        courseCode: courseData.course_code,
        termName: courseData.termName || courseData.term?.name || null,
        termStartAt: courseData.termStartAt || courseData.term?.start_at || courseData.start_at || null,
        termEndAt: courseData.termEndAt || courseData.term?.end_at || courseData.end_at || null,
        enrollmentTermId: courseData.enrollment_term_id || null,
        workflowState: courseData.workflow_state || null,
        enrollmentStates: Array.from(courseStates),
        teachers: teachers,
        overallCourseScore: courseData.overallCourseScore ?? courseData.enrollments?.[0]?.grades?.current_score ?? null,
        overallCourseGrade: courseData.overallCourseGrade ?? courseData.enrollments?.[0]?.grades?.current_grade ?? null,
        assignments: normalizedAssignments
      });
    });

    courseDetails.sort((a, b) => {
      const aDate = a.termStartAt ? new Date(a.termStartAt).getTime() : 0;
      const bDate = b.termStartAt ? new Date(b.termStartAt).getTime() : 0;
      return bDate - aDate;
    });

    const totalAssignments = courseDetails.reduce((sum, course) => sum + course.assignments.length, 0);

    res.json({
      success: true,
      summary: {
        totalCourses: courseDetails.length,
        totalAssignments: totalAssignments
      },
      filters: {
        state: stateFilters.length ? stateFilters : ['all'],
        includeEmpty: includeEmpty
      },
      courses: courseDetails
    });
  } catch (error) {
    console.error('Error building student course details:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to assemble student course details from Firestore'
    });
  }
});

// Get assignments from Firestore
exports.getAssignmentsFromFirestore = functions.https.onRequest(async (req, res) => {
  try {
    const courseId = req.query.courseId;
    let query = db.collection('canvas_assignments');
    
    if (courseId) {
      query = query.where('course_id', '==', parseInt(courseId));
    }
    
    const snapshot = await query.get();
    const assignments = [];
    
    snapshot.forEach(doc => {
      assignments.push({
        id: doc.id,
        ...doc.data()
      });
    });
    
    res.json({
      success: true,
      message: `Retrieved ${assignments.length} assignments from Firestore`,
      courseId: courseId || 'all',
      assignments: assignments,
      source: 'firestore'
    });
    
  } catch (error) {
    console.error('Error reading assignments from Firestore:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to read assignments from Firestore'
    });
  }
});

// Get instructors for a specific course
exports.getCourseInstructors = functions.https.onRequest(async (req, res) => {
  try {
    const courseId = req.query.courseId;
    if (!courseId) {
      return res.status(400).json({
        success: false,
        error: 'courseId query parameter is required'
      });
    }
    
    const apiKey = await getCanvasApiKey();
    const canvasUrl = `${CANVAS_BASE_URL}/courses/${courseId}/users`;
    
    const response = await axios.get(canvasUrl, {
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      params: {
        enrollment_type: ['teacher', 'ta', 'designer'],
        per_page: 100
      }
    });
    
    const instructors = response.data;
    
    res.json({
      success: true,
      message: `Retrieved ${instructors.length} instructors for course ${courseId}`,
      courseId: courseId,
      instructors: instructors.map(instructor => ({
        id: instructor.id,
        name: instructor.name,
        sortable_name: instructor.sortable_name,
        short_name: instructor.short_name,
        email: instructor.email,
        role: instructor.enrollments?.[0]?.role || 'instructor'
      }))
    });
    
  } catch (error) {
    console.error('Error fetching course instructors:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to fetch instructors from Canvas API'
    });
  }
});

// Sync all assignments for all courses
exports.syncAllAssignments = functions.https.onRequest(async (req, res) => {
  try {
    // First get all courses from Firestore
    const coursesSnapshot = await db.collection('canvas_courses').get();
    const courses = [];
    
    coursesSnapshot.forEach(doc => {
      courses.push(doc.data());
    });
    
    if (courses.length === 0) {
      return res.status(400).json({
        success: false,
        error: 'No courses found in Firestore. Run fetchCanvasCourses first.'
      });
    }
    
    const apiKey = await getCanvasApiKey();
    const results = [];
    
    // Fetch assignments for each course
    for (const course of courses) {
      try {
        const canvasUrl = `${CANVAS_BASE_URL}/courses/${course.id}/assignments`;
        
        const response = await axios.get(canvasUrl, {
          headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
          },
          params: {
            per_page: 100,
            include: ['submission', 'assignment_visibility']
          }
        });
        
        const assignments = response.data;
        
        // Store assignments in Firestore
        const batch = db.batch();
        const assignmentsRef = db.collection('canvas_assignments');
        
        assignments.forEach(assignment => {
          const assignmentDoc = assignmentsRef.doc(assignment.id.toString());
          batch.set(assignmentDoc, {
            id: assignment.id,
            course_id: course.id,
            course_name: course.name,
            name: assignment.name,
            description: assignment.description,
            due_at: assignment.due_at,
            unlock_at: assignment.unlock_at,
            lock_at: assignment.lock_at,
            points_possible: assignment.points_possible,
            grading_type: assignment.grading_type,
            submission_types: assignment.submission_types,
            workflow_state: assignment.workflow_state,
            lastFetched: admin.firestore.FieldValue.serverTimestamp(),
            ...assignment
          });
        });
        
        await batch.commit();
        
        results.push({
          courseId: course.id,
          courseName: course.name,
          assignmentCount: assignments.length,
          success: true
        });
        
      } catch (courseError) {
        console.error(`Error fetching assignments for course ${course.id}:`, courseError);
        results.push({
          courseId: course.id,
          courseName: course.name,
          error: courseError.message,
          success: false
        });
      }
    }
    
    const successCount = results.filter(r => r.success).length;
    const totalAssignments = results.reduce((sum, r) => sum + (r.assignmentCount || 0), 0);
    
    res.json({
      success: true,
      message: `Synced assignments for ${successCount}/${courses.length} courses. Total assignments: ${totalAssignments}`,
      results: results,
      summary: {
        totalCourses: courses.length,
        successfulCourses: successCount,
        totalAssignments: totalAssignments
      }
    });
    
  } catch (error) {
    console.error('Error in syncAllAssignments:', error);
    res.status(500).json({
      success: false,
      error: error.message,
      details: 'Failed to sync assignments'
    });
  }
});

//running mean, median, mode

exports.calculateStats = functions.https.onRequest(async (req, res) => {
  // Add CORS headers
  res.set("Access-Control-Allow-Origin", "https://byui.instructure.com"); // or "*" for testing
  res.set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");

  // Handle preflight OPTIONS requests
  if (req.method === "OPTIONS") {
    return res.status(204).send("");
  }

  try {
    const times = req.body.times;
    if (!times || !Array.isArray(times) || times.length === 0) {
      return res.status(400).json({ success: false, error: "Invalid times array" });
    }

    // --- Mean, Median, Mode calculations ---
    // const mean = times.reduce((a, b) => a + b, 0) / times.length;

    // const sorted = [...times].sort((a, b) => a - b);
    // const mid = Math.floor(sorted.length / 2);
    // const median =
    //   sorted.length % 2 !== 0
    //     ? sorted[mid]
    //     : (sorted[mid - 1] + sorted[mid]) / 2;

    // const freq = {};
    // times.forEach((num) => (freq[num] = (freq[num] || 0) + 1));
    // const maxFreq = Math.max(...Object.values(freq));
    // const mode = parseFloat(Object.keys(freq).find((k) => freq[k] === maxFreq));

    const result = calculateStatistics(times);

    // --- Save to Firestore ---
    const docRef = db.collection("stats_results").doc();
    await docRef.set({
      times,
      ...result,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
    });

    res.json({ success: true, ...result });
  } catch (error) {
    console.error("Error calculating stats:", error);
    res.status(500).json({ success: false, error: error.message });
  }
});

/**
 * Firestore trigger: When timing data is written, recalculate statistics
 * Triggers on: assignment_times/{assignmentDocId}/times/{studentId}
 */
exports.onTimingDataWrite = functions.firestore
  .document('assignment_times/{assignmentDocId}/times/{studentId}')
  .onWrite(async (change, context) => {
    try {
      const assignmentDocId = context.params.assignmentDocId;
      console.log(`Processing timing data for assignment: ${assignmentDocId}`);
      
      // Get all timing data for this assignment
      const timesSnapshot = await db
        .collection('assignment_times')
        .doc(assignmentDocId)
        .collection('times')
        .get();
      
      if (timesSnapshot.empty) {
        console.log('No timing data found - skipping statistics calculation');
        return null;
      }
      
      // Extract time values and metadata
      const timeValues = [];
      let assignmentName = '';
      let className = '';
      let courseId = '';
      let assignmentId = '';
      
      timesSnapshot.forEach(doc => {
        const data = doc.data();
        if (data.timeSeconds) {
          timeValues.push(data.timeSeconds);
        }
        // Capture metadata from first document
        if (!assignmentName && data.assignmentName) {
          assignmentName = data.assignmentName;
        }
        if (!className && data.className) {
          className = data.className;
        }
        if (!courseId && data.courseId) {
          courseId = data.courseId;
        }
        if (!assignmentId && data.assignmentId) {
          assignmentId = data.assignmentId;
        }
      });
      
      console.log(`Found ${timeValues.length} timing submissions`);
      
      // Calculate statistics
      const stats = calculateStatistics(timeValues);
      
      // Write statistics to Firestore
      const statsRef = db.collection('assignment_statistics').doc(assignmentDocId);
      await statsRef.set({
        ...stats,
        assignmentName: assignmentName,
        className: className,
        courseId: courseId,
        assignmentId: assignmentId,
        lastUpdated: admin.firestore.FieldValue.serverTimestamp(),
        updatedAt: new Date().toISOString()
      });
      
      console.log(`Statistics updated for ${assignmentDocId}:`, stats);
      return null;
      
    } catch (error) {
      console.error('Error calculating statistics:', error);
      // Don't throw - let the trigger complete
      return null;
    }
  });
