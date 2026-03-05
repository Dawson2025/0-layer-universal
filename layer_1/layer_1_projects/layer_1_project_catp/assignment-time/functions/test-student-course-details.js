// resource_id: "8b0bfe4f-a04b-40e8-b923-aa2e9d8eeb97"
// resource_type: "document"
// resource_name: "test-student-course-details"
const { initializeApp, getApps } = require('firebase-admin/app');
const { getFirestore } = require('firebase-admin/firestore');
const axios = require('axios');
const assert = require('node:assert');

async function seedFirestore(db) {
  const courses = db.collection('canvas_courses');
  const assignments = db.collection('canvas_assignments');

  const courseDoc = courses.doc('101');
  await courseDoc.set({
    id: 101,
    name: 'Intro to Coding',
    course_code: 'CS101',
    enrollment_term_id: 20241,
    workflow_state: 'available',
    termName: 'Winter 2024',
    termStartAt: '2024-01-08T07:00:00Z',
    termEndAt: '2024-04-10T06:00:00Z',
    teachers: [
      {
        id: 5001,
        name: 'Ada Lovelace',
        sortable_name: 'Lovelace, Ada',
        email: 'ada@example.edu'
      }
    ],
    enrollments: [
      {
        id: 1,
        user_id: 42,
        type: 'StudentEnrollment',
        enrollment_state: 'active',
        grades: {
          html_url: 'https://byui.instructure.com/courses/101/grades',
          current_score: 95.2,
          current_grade: 'A'
        }
      }
    ]
  });

  await assignments.doc('2001').set({
    id: 2001,
    course_id: 101,
    course_name: 'Intro to Coding',
    name: 'Project 1',
    due_at: '2024-02-01T07:00:00Z',
    points_possible: 100,
    html_url: 'https://byui.instructure.com/courses/101/assignments/2001',
    submission: {
      submitted_at: '2024-01-31T20:15:00Z',
      score: 93,
      grade: 'A',
      graded_at: '2024-02-02T18:00:00Z',
      late: false,
      missing: false,
      excused: false
    }
  });

  await assignments.doc('2002').set({
    id: 2002,
    course_id: 101,
    course_name: 'Intro to Coding',
    name: 'Quiz 1',
    due_at: '2024-01-20T07:00:00Z',
    points_possible: 20,
    submission: {
      submitted_at: null,
      score: null,
      grade: null,
      graded_at: null,
      late: true,
      missing: true,
      excused: false
    }
  });
}

async function main() {
  const projectId = process.env.GCLOUD_PROJECT || 'assignment-time';
  process.env.FIRESTORE_EMULATOR_HOST = process.env.FIRESTORE_EMULATOR_HOST || 'localhost:8080';

  if (getApps().length === 0) {
    initializeApp({ projectId });
  }

  const db = getFirestore();
  await seedFirestore(db);

  const functionBase = 'http://localhost:5001/assignment-time/us-central1';
  const response = await axios.get(`${functionBase}/getStudentCourseDetails`, {
    params: {
      includeEmpty: 'true'
    }
  });

  const data = response.data;
  console.log('Function response:', JSON.stringify(data, null, 2));

  assert.strictEqual(data.success, true, 'Expected success=true');
  assert.ok(Array.isArray(data.courses), 'courses should be an array');
  assert.strictEqual(data.courses.length, 1, 'Should return the seeded course');

  const course = data.courses[0];
  assert.strictEqual(course.name, 'Intro to Coding');
  assert.strictEqual(course.teachers[0].name, 'Ada Lovelace');
  assert.strictEqual(course.overallCourseGrade, 'A');
  assert.strictEqual(course.assignments.length, 2, 'Should include two assignments');

  const graded = course.assignments.find(item => item.id === 2001);
  assert.ok(graded, 'Expected Project 1 assignment');
  assert.strictEqual(graded.submitted, true, 'Project 1 should be submitted');
  assert.strictEqual(graded.graded, true, 'Project 1 should be graded');
  assert.strictEqual(graded.submission.score, 93);

  const missing = course.assignments.find(item => item.id === 2002);
  assert.ok(missing, 'Expected Quiz 1 assignment');
  assert.strictEqual(missing.missing, true, 'Quiz 1 should be marked missing');
}

main().catch(error => {
  console.error('Local test failed:', error);
  process.exit(1);
});
