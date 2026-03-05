---
resource_id: "21c42889-b511-4677-be3c-7c99bb0cd13b"
resource_type: "readme
document"
resource_name: "README"
---
# Assignment Timer CLI

A command-line interface for tracking how long it takes to complete assignments. This tool integrates with your Canvas courses and stores timing data for future analysis.

## Features

- ⏱️ **Start/Stop Timer**: Simple timer functionality with real-time display
- 📚 **Assignment Selection**: Choose from your Canvas assignments
- 💾 **Data Storage**: Save timing data to Firebase Firestore
- 📊 **History View**: See your past timing records
- 🔄 **Canvas Sync**: Sync your latest Canvas data
- 🎨 **Beautiful Interface**: Clean, colorful CLI with emojis

## Installation

1. Navigate to the assignment-timer directory:
   ```bash
   cd assignment-timer
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Make sure your Firebase backend is running and has Canvas data synced.

## Usage

### Environment Selection
- When `clear-assign` starts you'll be prompted to choose Development, Testing, or Production backends.
- Set `CLEAR_ASSIGN_ENV` (e.g., `prod`, `test`, `dev`) to default to an environment. Add `CLEAR_ASSIGN_ENV_PROMPT=false` to skip the prompt for automation.

Start the application:
```bash
npm start
```

### Main Menu Options

1. **📚 Select Assignment**: Choose a course and assignment to time
2. **▶️ Start Timer**: Begin timing your assignment work
3. **⏹️ Stop Timer**: Stop the timer and save the timing data
4. **📊 View My Timing History**: See your past timing records
5. **🔄 Sync Canvas Data**: Update your courses and assignments from Canvas
6. **❌ Exit**: Close the application

### How to Use

1. **First Time Setup**:
   - Run "Sync Canvas Data" to fetch your courses and assignments
   - Select an assignment from the menu

2. **Timing an Assignment**:
   - Select the assignment you want to work on
   - Start the timer when you begin working
   - Stop the timer when you finish
   - The timing data is automatically saved

3. **Viewing History**:
   - Use "View My Timing History" to see your past timings
   - Helps you track your progress and estimate future assignments

## Data Storage

Timing data is stored in Firebase Firestore with the following structure:
```json
{
  "assignmentId": "12345",
  "assignmentName": "W01-Prepare: Course Overview",
  "courseId": 351068,
  "courseName": "Applied Programming",
  "timeInSeconds": 1800,
  "timestamp": "2025-01-24T10:30:00Z",
  "userId": "anonymous"
}
```

## Future Features

This timing data will be used to:
- Show average completion times for assignments
- Help students estimate how long assignments will take
- Identify assignments that typically take longer
- Provide insights for time management

## Keyboard Shortcuts

- **Ctrl+C**: Exit the application gracefully (stops timer if running)

## Requirements

- Node.js 16+ 
- Firebase project with Canvas integration
- Canvas API access (handled by backend)

## Troubleshooting

- **No assignments found**: Run "Sync Canvas Data" first
- **Firebase errors**: Ensure your backend is running and accessible
- **Timer not working**: Make sure you've selected an assignment first
