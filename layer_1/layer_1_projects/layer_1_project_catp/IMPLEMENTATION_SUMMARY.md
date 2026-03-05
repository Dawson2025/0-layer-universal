---
resource_id: "bb57000e-c1ae-46e5-ba59-640a1ca6a166"
resource_type: "document"
resource_name: "IMPLEMENTATION_SUMMARY"
---
# Firestore-Based Timing Data Collection - Implementation Summary

## Overview
Implemented a complete end-to-end flow where the Chrome extension collects student timing data directly from Canvas pages (via DOM scraping) and stores it in Firestore. The backend automatically calculates statistics when new data arrives, eliminating the need for the Canvas API key.

## Architecture

### Data Flow
1. **Frontend (Chrome Extension)** → Scrapes assignment info from Canvas page
2. **Frontend** → User submits timing data
3. **Frontend** → Writes to Firestore: `assignment_times/{courseId}_{assignmentId}/times/{studentId}`
4. **Backend (Firestore Trigger)** → Automatically triggered on new timing data
5. **Backend** → Calculates mean, median, mode from all submissions
6. **Backend** → Writes statistics to Firestore: `assignment_statistics/{courseId}_{assignmentId}`
7. **Frontend** → Real-time listener updates UI with new statistics

## Frontend Changes

### Modified Files

#### `/task-timer-frontend/classInfo.js`
- Added extraction of `courseId` and `assignmentId` from URL
- Added getter functions: `getCourseId()`, `getAssignmentId()`, `getClassName()`, `getAssignmentName()`

#### `/task-timer-frontend/timer.js`
- Added `getCurrentSeconds()` export to access current timer value
- Added `getTimerId()` export to get assignment ID

#### `/task-timer-frontend/firestoreSync.js` (NEW)
- `writeTimingData()` - Writes student timing submissions to Firestore
- `listenToStatistics()` - Real-time listener for statistics updates
- `getStatistics()` - One-time statistics fetch
- Automatic student ID generation and persistence

#### `/task-timer-frontend/content.js`
- Integrated Firestore imports
- Modified form submission to write to Firestore
- Added real-time statistics listener
- Display statistics from Firestore instead of backend API
- Shows "Submitted!" feedback after successful submission

#### `/task-timer-frontend/package.json`
- Added `firebase` dependency (^10.7.1)

## Backend Changes

### Modified Files

#### `/assignment-time/functions/statisticsCalculator.js` (NEW)
- `calculateMean()` - Calculate average time
- `calculateMedian()` - Calculate median time
- `calculateMode()` - Calculate most frequent time
- `calculateStatistics()` - Returns all stats + count, min, max

#### `/assignment-time/functions/index.js`
- Changed import from `./dataScienceOperations` to `./statisticsCalculator`
- Added `exports.onTimingDataWrite` - Firestore trigger function that:
  - Listens to `assignment_times/{assignmentDocId}/times/{studentId}`
  - Aggregates all timing data for the assignment
  - Calculates statistics
  - Writes results to `assignment_statistics/{assignmentDocId}`

#### `/assignment-time/firestore.rules` (NEW)
- Public read/write access to `assignment_times` (for student submissions)
- Public read access to `assignment_statistics`
- Write access to statistics only via backend functions

## Firestore Collections

### `assignment_times/{courseId}_{assignmentId}/times/{studentId}`
```javascript
{
  studentId: "student_1234567890_abc123",
  courseId: "123456",
  assignmentId: "789012",
  assignmentName: "Essay 1",
  className: "CS101",
  timeSeconds: 3600,
  timestamp: ServerTimestamp,
  submittedAt: "2025-11-10T12:00:00Z"
}
```

### `assignment_statistics/{courseId}_{assignmentId}`
```javascript
{
  mean: 3542,           // seconds
  median: 3480,         // seconds
  mode: 3600,           // seconds
  count: 15,            // number of submissions
  min: 1800,            // seconds
  max: 5400,            // seconds
  assignmentName: "Essay 1",
  className: "CS101",
  courseId: "123456",
  assignmentId: "789012",
  lastUpdated: ServerTimestamp,
  updatedAt: "2025-11-10T12:05:00Z"
}
```

## Benefits

### ✅ No Canvas API Key Required
- Frontend scrapes data directly from Canvas page DOM
- Students can submit timing data without backend API calls to Canvas
- Works entirely through Firestore

### ✅ Real-Time Updates
- Statistics update automatically when new data arrives
- Frontend uses Firestore listeners for instant updates
- No polling or manual refresh needed

### ✅ Scalable Architecture
- Firestore triggers handle statistics calculation automatically
- Each assignment has independent statistics
- Supports unlimited concurrent users

### ✅ Privacy
- Each student gets a unique anonymous ID
- No personal information required
- Data is aggregated for statistics

## How to Deploy

### Frontend
```bash
cd task-timer-frontend
npm install
npm run test  # Builds bundle.js
# Load the extension in Chrome from this directory
```

### Backend
```bash
cd assignment-time/functions
npm install
firebase deploy --only functions,firestore:rules
```

## Testing the Flow

1. **Load Extension**: Chrome → Extensions → Developer Mode → Load Unpacked → Select `task-timer-frontend/`

2. **Navigate to Canvas Assignment**: Go to any `*.instructure.com/courses/*/assignments/*` page

3. **Submit Timing Data**:
   - Enter assignment name
   - Enter hours, minutes, seconds
   - Click "Add Time"
   - Should see "Submitted!" message

4. **Verify Backend**:
   - Check Firebase Console → Firestore
   - Should see data in `assignment_times/{courseId}_{assignmentId}/times/{studentId}`
   - Should see calculated statistics in `assignment_statistics/{courseId}_{assignmentId}`

5. **Verify Frontend Display**:
   - Mean/Median/Mode should update in sidebar
   - Should see console log: "Statistics updated: X submissions"

## Future Enhancements

- [ ] Add data validation and sanitization
- [ ] Implement user authentication
- [ ] Add ability to view historical submissions
- [ ] Export statistics to CSV
- [ ] Add more statistical measures (standard deviation, percentiles)
- [ ] Implement admin dashboard for viewing all assignment statistics

## Files Changed

### Frontend
- ✅ `classInfo.js` - Modified
- ✅ `timer.js` - Modified
- ✅ `firestoreSync.js` - Created
- ✅ `content.js` - Modified
- ✅ `package.json` - Modified
- ✅ `bundle.js` - Rebuilt (1000.4kb)

### Backend
- ✅ `functions/statisticsCalculator.js` - Created
- ✅ `functions/index.js` - Modified
- ✅ `firestore.rules` - Created

## Build Results
- Frontend bundle: ✅ **1000.4kb** (built successfully)
- Linter errors: ✅ **0 errors**
- All dependencies installed: ✅ **Yes**

## Ready for Testing
The implementation is complete and ready for end-to-end testing once deployed to Firebase!

