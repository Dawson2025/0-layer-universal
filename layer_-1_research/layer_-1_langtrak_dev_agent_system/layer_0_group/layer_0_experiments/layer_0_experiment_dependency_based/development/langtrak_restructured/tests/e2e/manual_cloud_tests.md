# Manual Cloud E2E Test Checklist

This document contains manual tests for cloud features that require browser interaction and cannot be fully automated due to Google OAuth requirements.

**Test Date:** _____________  
**Tester:** _____________  
**App URL:** http://127.0.0.1:5000 (or production URL)

---

## Prerequisites
- [ ] App is running (`python3 app.py` or production server)
- [ ] Google account: 2025computer2025@gmail.com
- [ ] Firebase console access: https://console.firebase.google.com/project/lang-trak-dev

---

## Test 1: Google OAuth Sign-In

**Steps:**
1. Navigate to http://127.0.0.1:5000/login
2. Click "Sign in with Google" button
3. Complete Google OAuth flow
4. Verify redirect to dashboard

**Expected:**
- [ ] Google OAuth popup opens
- [ ] Can sign in with Google account
- [ ] Redirected to dashboard after sign-in
- [ ] User name displayed in dashboard

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

---

## Test 2: Create Cloud Project

**Steps:**
1. On dashboard, click "Create New Project"
2. Enter project name: `Manual_Test_Cloud_${TIMESTAMP}`
3. Select "Cloud" storage type
4. Click "Create"

**Expected:**
- [ ] Project created successfully
- [ ] Project appears in projects list
- [ ] Project shows cloud icon/indicator
- [ ] Can click on project to open it

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

**Firebase Verification:**
- [ ] Open Firebase console → Firestore → `projects` collection
- [ ] Find project by name
- [ ] Record document ID: _____________

---

## Test 3: Add Words & Phonemes to Cloud Project

**Steps:**
1. Open the cloud project created in Test 2
2. Click "Add New Word"
3. Create word with following data:
   - English: "hello"
   - Translation: "greeting"
   - IPA: /hɛˈloʊ/
   - Syllables: [CV, CV] (he-lo)
   - Phonemes: h, ɛ, l, oʊ
4. Click "Save"
5. Verify word appears in words list
6. Create 2 more words (different structures)

**Expected:**
- [ ] Can create word with multiple syllables
- [ ] Phonemes saved correctly
- [ ] Words appear in project word list
- [ ] Can view word details

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

**Firebase Verification:**
- [ ] Open Firebase console → Firestore → `words` collection
- [ ] Filter by project_id (from Test 2)
- [ ] Verify 3 words exist
- [ ] Check phoneme data is correct
- [ ] Record word IDs: _____________, _____________, _____________

---

## Test 4: Upload Video to Cloud Storage

**Steps:**
1. In the cloud project, select a word
2. Click "Add Video" or video upload section
3. Upload a small test video file (< 10MB)
4. Wait for upload to complete
5. Verify video preview appears

**Expected:**
- [ ] Can select video file
- [ ] Upload progress shown
- [ ] Upload completes successfully
- [ ] Video preview/thumbnail appears
- [ ] Can play video

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

**Firebase Storage Verification:**
- [ ] Open Firebase console → Storage
- [ ] Navigate to videos folder
- [ ] Find uploaded video file
- [ ] Record file path: _____________

---

## Test 5: Create Custom Phoneme Template

**Steps:**
1. Navigate to Templates section
2. Click "Create New Template"
3. Enter template name: `E2E_Template_${TIMESTAMP}`
4. Add phonemes:
   - Consonants: p, t, k, m, n
   - Vowels: a, e, i, o, u
5. Set syllable structures: CV, CVC, V
6. Click "Save Template"

**Expected:**
- [ ] Template creation form appears
- [ ] Can add/remove phonemes
- [ ] Can set syllable structures
- [ ] Template saves successfully
- [ ] Template appears in templates list

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

---

## Test 6: Upload Template to Cloud

**Steps:**
1. Open the template created in Test 5
2. Click "Upload to Cloud" or "Share to Cloud"
3. Set visibility: Public
4. Add description: "E2E test template"
5. Click "Upload"

**Expected:**
- [ ] Upload dialog appears
- [ ] Can set public/private
- [ ] Can add description
- [ ] Upload succeeds
- [ ] "Uploaded to cloud" indicator appears

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

**Firebase Verification:**
- [ ] Open Firebase console → Firestore → `templates` collection
- [ ] Find template by name
- [ ] Verify `is_public: true`
- [ ] Record template ID: _____________

---

## Test 7: Download & Use Cloud Template

**Steps:**
1. Navigate to "Browse Cloud Templates" or Templates → Cloud
2. Find a public template (can be the one from Test 6)
3. Click "Download" or "Use Template"
4. Create new project using this template
5. Verify project uses template phonemes

**Expected:**
- [ ] Can browse public templates
- [ ] Can view template details
- [ ] Can download/import template
- [ ] New project created with template
- [ ] Project phonemes match template

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

---

## Test 8: Local → Cloud Migration

**Steps:**
1. Create a LOCAL project with 2-3 words
2. Open project settings/menu
3. Click "Migrate to Cloud"
4. Confirm migration
5. Wait for migration to complete
6. Verify project now shows as "Cloud" project
7. Verify all words migrated

**Expected:**
- [ ] Migration option available for local projects
- [ ] Migration progress shown
- [ ] Migration completes successfully
- [ ] Project becomes cloud project
- [ ] All words preserved
- [ ] All phoneme data preserved

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

**Firebase Verification:**
- [ ] Verify migrated project in Firestore `projects`
- [ ] Verify migrated words in Firestore `words`
- [ ] Record project ID: _____________

---

## Test 9: Cloud → Local Fork/Download

**Steps:**
1. Open a cloud project (use one from previous tests)
2. Click "Fork to Local" or "Download as Local"
3. Confirm fork/download
4. Wait for process to complete
5. Verify new local project created
6. Verify all data copied

**Expected:**
- [ ] Fork/download option available
- [ ] Process completes successfully
- [ ] New local project created
- [ ] All words copied
- [ ] All phoneme data copied
- [ ] Original cloud project unchanged

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

---

## Test 10: Delete Cloud Resources

**Steps:**
1. Delete a word from cloud project
2. Delete a video from cloud storage
3. Delete a cloud template
4. Delete entire cloud project

**Expected:**
- [ ] Can delete individual words
- [ ] Can delete videos
- [ ] Can delete templates
- [ ] Can delete entire project
- [ ] Confirmation dialogs appear
- [ ] Deletions succeed

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

**Firebase Verification:**
- [ ] Verify word removed from Firestore
- [ ] Verify video removed from Storage
- [ ] Verify template removed from Firestore
- [ ] Verify project removed from Firestore

---

## Test 11: View & Verify Phoneme Frequencies in Cloud

**Steps:**
1. Open a cloud project with multiple words
2. Navigate to Admin Tools → Phoneme Frequencies
3. View phoneme frequency data
4. Create a new word with specific phonemes
5. Click "Recalculate Frequencies"
6. Verify frequencies updated

**Expected:**
- [ ] Can view phoneme frequencies
- [ ] Frequencies show correct counts
- [ ] Recalculation works
- [ ] UI updates after recalculation

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

---

## Test 12: TTS with Cloud Projects

**Steps:**
1. Open a cloud project
2. Select a word
3. Click "Play Pronunciation" (TTS)
4. Test individual phoneme pronunciation
5. Test full word pronunciation

**Expected:**
- [ ] TTS works for cloud projects
- [ ] Individual phonemes play correctly
- [ ] Full words play correctly
- [ ] Audio quality is acceptable

**Actual Result:** _____________

**Status:** ⬜ PASS ⬜ FAIL

---

## Final Verification: Firebase Data Inspection

**Steps:**
1. Open Firebase Console → Firestore
2. Check `projects` collection
3. Check `words` collection
4. Check `phonemes` collection (if separate)
5. Check `templates` collection
6. Open Firebase Storage
7. Check `videos` folder

**Checklist:**
- [ ] All test projects present in Firestore
- [ ] All test words present in Firestore
- [ ] All test templates present in Firestore
- [ ] All test videos present in Storage
- [ ] Data structure is correct
- [ ] No data corruption

**Document IDs Found:**

Projects: _____________

Words: _____________

Templates: _____________

Videos: _____________

---

## Summary

| Test | Status | Notes |
|------|--------|-------|
| 1. Google OAuth | ⬜ PASS ⬜ FAIL | |
| 2. Create Cloud Project | ⬜ PASS ⬜ FAIL | |
| 3. Add Words & Phonemes | ⬜ PASS ⬜ FAIL | |
| 4. Upload Video | ⬜ PASS ⬜ FAIL | |
| 5. Create Template | ⬜ PASS ⬜ FAIL | |
| 6. Upload Template | ⬜ PASS ⬜ FAIL | |
| 7. Use Cloud Template | ⬜ PASS ⬜ FAIL | |
| 8. Local → Cloud | ⬜ PASS ⬜ FAIL | |
| 9. Cloud → Local | ⬜ PASS ⬜ FAIL | |
| 10. Delete Resources | ⬜ PASS ⬜ FAIL | |
| 11. Phoneme Frequencies | ⬜ PASS ⬜ FAIL | |
| 12. TTS Cloud | ⬜ PASS ⬜ FAIL | |

**Overall Pass Rate:** _____ / 12

**Critical Issues Found:** _____________

**Recommendations:** _____________

---

## Cleanup

After completing all tests, clean up test data:

- [ ] Delete all test projects from Firebase
- [ ] Delete all test words from Firestore
- [ ] Delete all test templates from Firestore
- [ ] Delete all test videos from Storage
- [ ] Verify cleanup complete in Firebase console

**Cleanup Commands:**

```bash
# Run cleanup script
python3 scripts/cleanup-test-data.py --marker "Manual_Test_Cloud"
```

---

**Test Completed:** _____________  
**Signature:** _____________

