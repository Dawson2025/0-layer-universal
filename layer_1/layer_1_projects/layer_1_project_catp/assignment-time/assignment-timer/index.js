// resource_id: "466768c5-3485-472f-be63-c87f2ecf63a8"
// resource_type: "document"
// resource_name: "index"
#!/usr/bin/env node

import inquirer from 'inquirer';
import chalk from 'chalk';
import figlet from 'figlet';
import axios from 'axios';
import { initializeApp, getApps, getApp } from 'firebase-admin/app';
import { getFirestore, Timestamp } from 'firebase-admin/firestore';

const ENVIRONMENTS = [
  {
    key: 'dev',
    name: 'Development',
    projectId: 'assignment-time-dev',
    functionsBaseUrl: 'https://us-central1-assignment-time-dev.cloudfunctions.net'
  },
  {
    key: 'test',
    name: 'Testing',
    projectId: 'assignment-time-test',
    functionsBaseUrl: 'https://us-central1-assignment-time-test.cloudfunctions.net'
  },
  {
    key: 'prod',
    name: 'Production',
    projectId: 'assignment-time',
    functionsBaseUrl: 'https://us-central1-assignment-time.cloudfunctions.net'
  }
];

const environmentByKey = ENVIRONMENTS.reduce((acc, env) => {
  acc[env.key.toLowerCase()] = env;
  acc[env.projectId.toLowerCase()] = env;
  return acc;
}, {});

let currentEnvironment = null;
let db = null;
let FIREBASE_FUNCTIONS_BASE_URL = ENVIRONMENTS.find(env => env.key === 'prod').functionsBaseUrl;

// Global state
let currentTimer = null;
let selectedAssignment = null;
let startTime = null;

function getDefaultEnvironment() {
  const hints = [
    process.env.CLEAR_ASSIGN_ENV,
    process.env.CLEARASSIGN_ENV,
    process.env.GOOGLE_CLOUD_PROJECT,
    process.env.GCLOUD_PROJECT,
    process.env.GCP_PROJECT
  ];

  for (const hint of hints) {
    if (!hint) {
      continue;
    }
    const env = environmentByKey[hint.trim().toLowerCase()];
    if (env) {
      return env;
    }
  }

  return environmentByKey['prod'];
}

async function applyEnvironment(env) {
  if (!env) {
    throw new Error('Unknown environment configuration');
  }

  if (getApps().length > 0) {
    const existingApp = getApp();
    if (existingApp.options.projectId !== env.projectId) {
      await existingApp.delete();
      initializeApp({ projectId: env.projectId });
    }
  } else {
    initializeApp({ projectId: env.projectId });
  }

  db = getFirestore();
  FIREBASE_FUNCTIONS_BASE_URL = env.functionsBaseUrl;
  process.env.GOOGLE_CLOUD_PROJECT = env.projectId;
  currentEnvironment = env;
  selectedAssignment = null;
  if (currentTimer) {
    clearInterval(currentTimer);
    currentTimer = null;
  }
  startTime = null;
}

async function ensureEnvironmentSelected() {
  if (currentEnvironment) {
    return currentEnvironment;
  }

  const defaultEnv = getDefaultEnvironment();
  const skipPrompt =
    !!process.env.CLEAR_ASSIGN_ENV &&
    typeof process.env.CLEAR_ASSIGN_ENV_PROMPT === 'string' &&
    process.env.CLEAR_ASSIGN_ENV_PROMPT.toLowerCase() === 'false';

  if (skipPrompt) {
    await applyEnvironment(defaultEnv);
    return currentEnvironment;
  }

  const { envKey } = await inquirer.prompt([
    {
      type: 'list',
      name: 'envKey',
      message: 'Select backend environment:',
      choices: ENVIRONMENTS.map(env => ({
        name: `${env.name} (${env.projectId})`,
        value: env.key
      })),
      default: defaultEnv.key
    }
  ]);

  const chosen = environmentByKey[envKey.toLowerCase()];
  await applyEnvironment(chosen);
  console.log(chalk.gray(`Using ${chosen.name} environment (${chosen.projectId})`));
  return currentEnvironment;
}

// Utility functions
function formatTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = Math.floor(seconds % 60);
  
  if (hours > 0) {
    return `${hours}h ${minutes}m ${secs}s`;
  } else if (minutes > 0) {
    return `${minutes}m ${secs}s`;
  } else {
    return `${secs}s`;
  }
}

function displayHeader() {
  console.clear();
  console.log(chalk.cyan(figlet.textSync('Clear-Assign', { horizontalLayout: 'full' })));
  console.log(chalk.gray('Track your assignment completion times'));
  if (currentEnvironment) {
    console.log(chalk.gray(`Environment: ${currentEnvironment.name} (${currentEnvironment.projectId})`));
  }
  console.log('');
}

async function fetchAssignments() {
  try {
    const response = await axios.get(`${FIREBASE_FUNCTIONS_BASE_URL}/getAssignmentsFromFirestore`);
    return response.data.assignments || [];
  } catch (error) {
    console.error(chalk.red('Error fetching assignments:'), error.message);
    return [];
  }
}

async function fetchCourses() {
  try {
    const response = await axios.get(`${FIREBASE_FUNCTIONS_BASE_URL}/getCoursesFromFirestore`);
    return response.data.courses || [];
  } catch (error) {
    console.error(chalk.red('Error fetching courses:'), error.message);
    return [];
  }
}

function startTimer() {
  if (currentTimer) {
    console.log(chalk.yellow('Timer is already running!'));
    return;
  }
  
  startTime = Date.now();
  currentTimer = setInterval(() => {
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    process.stdout.write(`\r${chalk.green('⏱️  Timer running:')} ${chalk.bold(formatTime(elapsed))}`);
  }, 1000);
  
  console.log(chalk.green('\n✅ Timer started!'));
}

function stopTimer() {
  if (!currentTimer) {
    console.log(chalk.yellow('No timer is currently running!'));
    return null;
  }
  
  clearInterval(currentTimer);
  currentTimer = null;
  
  const elapsed = Math.floor((Date.now() - startTime) / 1000);
  console.log(chalk.green(`\n✅ Timer stopped! Total time: ${chalk.bold(formatTime(elapsed))}`));
  
  return elapsed;
}

async function getCourseInstructors(courseId) {
  try {
    const response = await axios.get(`${FIREBASE_FUNCTIONS_BASE_URL}/getCourseInstructors?courseId=${courseId}`);
    return response.data.instructors || [];
  } catch (error) {
    console.log(chalk.yellow('Could not fetch instructor information'));
    return [];
  }
}

async function saveTiming(assignmentId, assignmentName, courseId, courseName, timeInSeconds) {
  try {
    // Get instructor information
    const instructors = await getCourseInstructors(courseId);
    const instructorNames = instructors.map(inst => inst.name).join(', ');
    
    const timingData = {
      assignmentId: assignmentId,
      assignmentName: assignmentName,
      courseId: courseId,
      courseName: courseName,
      instructors: instructorNames,
      instructorCount: instructors.length,
      timeInSeconds: timeInSeconds,
      timestamp: Timestamp.now(),
      userId: 'anonymous' // For now, we'll use anonymous. Later can be user-specific
    };
    
    await db.collection('assignment_timings').add(timingData);
    console.log(chalk.green('✅ Timing data saved to database!'));
    if (instructorNames) {
      console.log(chalk.blue(`👨‍🏫 Instructors: ${instructorNames}`));
    }
  } catch (error) {
    console.error(chalk.red('Error saving timing data:'), error.message);
  }
}

async function selectCourse() {
  const courses = await fetchCourses();
  
  if (courses.length === 0) {
    console.log(chalk.yellow('No courses found. Please sync your Canvas data first.'));
    return null;
  }
  
  const courseChoices = courses.map(course => ({
    name: `${course.course_code} - ${course.name}`,
    value: course
  }));
  
  const { selectedCourse } = await inquirer.prompt([{
    type: 'list',
    name: 'selectedCourse',
    message: 'Select a course:',
    choices: courseChoices
  }]);
  
  return selectedCourse;
}

async function selectAssignment(courseId) {
  const assignments = await fetchAssignments();
  const courseAssignments = assignments.filter(assignment => assignment.course_id === courseId);
  
  if (courseAssignments.length === 0) {
    console.log(chalk.yellow('No assignments found for this course.'));
    return null;
  }
  
  const assignmentChoices = courseAssignments.map(assignment => ({
    name: `${assignment.name} (${assignment.points_possible} pts)`,
    value: assignment
  }));
  
  const { selectedAssignment } = await inquirer.prompt([{
    type: 'list',
    name: 'selectedAssignment',
    message: 'Select an assignment:',
    choices: assignmentChoices
  }]);
  
  return selectedAssignment;
}

async function showMainMenu() {
  displayHeader();
  
  if (selectedAssignment) {
    console.log(chalk.blue(`📚 Current Assignment: ${selectedAssignment.name}`));
    console.log(chalk.blue(`📖 Course: ${selectedAssignment.course_name}`));
    console.log(chalk.blue(`⏰ Timer Status: ${currentTimer ? chalk.green('Running') : chalk.red('Stopped')}\n`));
  }
  
  const choices = [
    { name: '📚 Select Assignment', value: 'select' },
    { name: currentTimer ? '⏹️  Stop Timer' : '▶️  Start Timer', value: 'timer' },
    { name: '📊 View My Timing History', value: 'history' },
    { name: '🔄 Sync Canvas Data', value: 'sync' },
    { name: '❌ Exit', value: 'exit' }
  ];
  
  const { action } = await inquirer.prompt([{
    type: 'list',
    name: 'action',
    message: 'What would you like to do?',
    choices: choices
  }]);
  
  return action;
}

async function syncCanvasData() {
  console.log(chalk.blue('🔄 Syncing Canvas data...'));
  
  try {
    // Sync courses
    console.log('Fetching courses...');
    await axios.get(`${FIREBASE_FUNCTIONS_BASE_URL}/fetchCanvasCourses`);
    
    // Sync assignments for all courses
    console.log('Fetching assignments...');
    await axios.get(`${FIREBASE_FUNCTIONS_BASE_URL}/syncAllAssignments`);
    
    console.log(chalk.green('✅ Canvas data synced successfully!'));
  } catch (error) {
    console.error(chalk.red('Error syncing data:'), error.message);
  }
  
  await inquirer.prompt([{
    type: 'input',
    name: 'continue',
    message: 'Press Enter to continue...'
  }]);
}

async function viewHistory() {
  try {
    console.log(chalk.blue('📊 Fetching your timing history...'));
    
    const snapshot = await db.collection('assignment_timings')
      .orderBy('timestamp', 'desc')
      .limit(20)
      .get();
    
    if (snapshot.empty) {
      console.log(chalk.yellow('No timing history found.'));
    } else {
      console.log(chalk.cyan('\n📊 Recent Timing History:\n'));
      
      snapshot.forEach(doc => {
        const data = doc.data();
        const time = formatTime(data.timeInSeconds);
        const rawTimestamp = data.timestamp;
        let date = 'Unknown date';
        if (rawTimestamp) {
          if (typeof rawTimestamp.toDate === 'function') {
            date = rawTimestamp.toDate().toLocaleString();
          } else if (rawTimestamp instanceof Date) {
            date = rawTimestamp.toLocaleString();
          } else {
            const parsedDate = new Date(rawTimestamp);
            if (!Number.isNaN(parsedDate.getTime())) {
              date = parsedDate.toLocaleString();
            }
          }
        }
        const instructorInfo = data.instructors ? chalk.magenta(` [${data.instructors}]`) : '';
        console.log(`${chalk.blue(data.assignmentName)} - ${chalk.green(time)}${instructorInfo} - ${chalk.gray(date)}`);
      });
    }
  } catch (error) {
    console.error(chalk.red('Error fetching history:'), error.message);
  }
  
  await inquirer.prompt([{
    type: 'input',
    name: 'continue',
    message: 'Press Enter to continue...'
  }]);
}

async function handleAction(action) {
  switch (action) {
    case 'select':
      const course = await selectCourse();
      if (course) {
        const assignment = await selectAssignment(course.id);
        if (assignment) {
          selectedAssignment = assignment;
          console.log(chalk.green(`✅ Selected: ${assignment.name}`));
        }
      }
      break;
      
    case 'timer':
      if (!selectedAssignment) {
        console.log(chalk.yellow('Please select an assignment first!'));
        await inquirer.prompt([{
          type: 'input',
          name: 'continue',
          message: 'Press Enter to continue...'
        }]);
        break;
      }
      
      if (currentTimer) {
        const elapsed = stopTimer();
        if (elapsed && selectedAssignment) {
          await saveTiming(
            selectedAssignment.id,
            selectedAssignment.name,
            selectedAssignment.course_id,
            selectedAssignment.course_name,
            elapsed
          );
        }
      } else {
        startTimer();
      }
      break;
      
    case 'history':
      await viewHistory();
      break;
      
    case 'sync':
      await syncCanvasData();
      break;
      
    case 'exit':
      if (currentTimer) {
        stopTimer();
      }
      console.log(chalk.cyan('👋 Thanks for using Clear-Assign!'));
      process.exit(0);
      break;
  }
}

// Main application loop
async function main() {
  console.log(chalk.cyan('🚀 Starting Clear-Assign...\n'));
  
  await ensureEnvironmentSelected();

  while (true) {
    try {
      const action = await showMainMenu();
      await handleAction(action);
    } catch (error) {
      if (error.isTtyError) {
        console.log(chalk.red('Prompt couldn\'t be rendered in the current environment'));
      } else {
        console.error(chalk.red('An error occurred:'), error.message);
      }
    }
  }
}
// Handle Ctrl+C gracefully
process.on('SIGINT', () => {
  if (currentTimer) {
    stopTimer();
  }
  console.log(chalk.cyan('\n👋 Thanks for using Clear-Assign!'));
  process.exit(0);
});

// Start the application
main().catch(console.error);
