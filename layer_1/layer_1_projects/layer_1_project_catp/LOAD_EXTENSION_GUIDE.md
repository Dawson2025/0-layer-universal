---
resource_id: "644ae2b2-54bf-4915-bd02-536861553fa1"
resource_type: "document"
resource_name: "LOAD_EXTENSION_GUIDE"
---
# 🎯 How to Load the Extension in Chrome

Since we're on WSL, here's the step-by-step process to load the extension:

<!-- section_id: "8f5c64b1-c966-4761-a246-708835c7dfe6" -->
## Option 1: Manual Load (Easiest - 30 seconds)

<!-- section_id: "9f22d9ee-04da-4ee9-a79f-e08773a0ce20" -->
### Step 1: Open Chrome Extensions Page
1. Open Google Chrome
2. Type in address bar: `chrome://extensions/`
3. Press Enter

<!-- section_id: "7bb2f532-c336-4e5a-89dd-dcd7309fec2e" -->
### Step 2: Enable Developer Mode
1. Look for the toggle switch in the **top-right corner** that says "Developer mode"
2. Click it to turn it **ON** (it should turn blue)

<!-- section_id: "808adf33-832d-4d02-b4c7-e99b4e443329" -->
### Step 3: Load the Extension
1. Click the **"Load unpacked"** button (top-left area)
2. In the file browser, navigate to:
   ```
   \\wsl.localhost\Ubuntu-24.04\home\dawson\code\catp\task-timer-frontend
   ```
   
   **Or paste this in the address bar:**
   ```
   \\wsl.localhost\Ubuntu-24.04\home\dawson\code\catp\task-timer-frontend
   ```

3. Click **"Select Folder"**

<!-- section_id: "9171ad32-9c9f-42dd-9e64-b36cf9a2292c" -->
### Step 4: Verify Extension Loaded
You should see a card that says:
```
Canvas Assignment Timer
Version 1.0
```

<!-- section_id: "7d69325e-33a4-43fc-be5f-64d76df7f178" -->
### Step 5: Test It!
1. Navigate to any Canvas assignment page with URL like:
   ```
   https://byui.instructure.com/courses/*/assignments/*
   ```
   (Replace * with actual course and assignment IDs)

2. You should see the **purple gradient sidebar** appear on the right side!

---

<!-- section_id: "b08dc8f1-c0c1-424c-bd62-09d7c903201d" -->
## Option 2: Direct Path (If Option 1 doesn't work)

If WSL path doesn't work, copy the extension folder to Windows:

<!-- section_id: "0a57d568-fbfa-45ab-84df-762acc9dca54" -->
### Step 1: Copy to Windows
```bash
# Run this in WSL terminal:
cp -r /home/dawson/dawson-workspace/code/catp/task-timer-frontend /mnt/c/Users/$USER/Desktop/task-timer-frontend
```

<!-- section_id: "0fd954a0-c4c8-43d9-9db4-8a31de800283" -->
### Step 2: Load from Windows Path
1. Open `chrome://extensions/`
2. Enable Developer mode
3. Click "Load unpacked"
4. Navigate to: `C:\Users\YourUsername\Desktop\task-timer-frontend`
5. Click "Select Folder"

---

<!-- section_id: "973342e6-80dc-4ad6-9995-8d3899ddd4a2" -->
## What You Should See

<!-- section_id: "5f3a9d33-dd55-4940-9796-6b2a605e1632" -->
### Before Loading Extension:
- Normal Canvas assignment page
- No sidebar

<!-- section_id: "6d88fa7b-7e65-4e20-8488-580b2633345b" -->
### After Loading Extension:
- **Purple gradient sidebar on the right**
- Shows: Mean Time, Median, Mode
- Timer counting up
- Bell curve visualization
- Form to submit your time
- "🔥 Connected to Firestore" indicator at bottom-right

---

<!-- section_id: "cd90de0c-a9bb-45fc-8d5c-c875210d69d9" -->
## Troubleshooting

<!-- section_id: "b639f2dd-e3b5-40f5-b6a5-624457fd78fc" -->
### Error: "Manifest file is missing or unreadable"
**Fix**: Make sure you selected the `task-timer-frontend` folder itself, not a parent or subfolder

<!-- section_id: "f6edc3b7-8967-4f61-b26b-cd380dcc7625" -->
### Error: "This extension may have been corrupted"
**Fix**: Make sure `bundle.js` exists (run `npm run test` to rebuild)

<!-- section_id: "6ea41e2b-af8a-4f87-8651-0eb2e44d385e" -->
### Sidebar not appearing on Canvas
**Check**:
1. Are you on a page matching: `*.instructure.com/courses/*/assignments/*`?
2. Is the extension enabled? (Check `chrome://extensions/`)
3. Try refreshing the page (F5)
4. Check browser console (F12) for any errors

<!-- section_id: "df2dc530-a26f-415a-929d-cc5f07d7495c" -->
### Can't access WSL path
**Solution**: Use Option 2 above to copy to Windows Desktop first

---

<!-- section_id: "6470a739-204d-4c41-9ee3-556544429e33" -->
## Testing Checklist

Once loaded, test these features:

- [ ] Sidebar appears on Canvas assignment page
- [ ] Timer is counting up
- [ ] Can pause/resume timer
- [ ] Can enter assignment name and time
- [ ] "Add Time" button shows "Submitted!" feedback
- [ ] Statistics display (may be 0h 0m 0s if no data yet)
- [ ] Bell curve shows
- [ ] Firestore indicator at bottom-right

---

<!-- section_id: "2b50f827-39a2-4cb9-befa-67c4325476b9" -->
## Quick Verification

**Extension Files Present:**
- ✅ `manifest.json`
- ✅ `bundle.js` (1001KB)
- ✅ `content.css`
- ✅ `firebase.js`
- ✅ All other assets

**Extension Status:**
Run in terminal to verify build:
```bash
cd /home/dawson/dawson-workspace/code/catp/task-timer-frontend
ls -lh bundle.js
# Should show: -rw-r--r-- 1 dawson dawson 1001K
```

---

<!-- section_id: "180623e1-47cb-442d-94ef-5e8baada4c96" -->
## Need Help?

If you're stuck, take a screenshot of:
1. Chrome extensions page showing the loaded extension
2. The Canvas page where it should appear
3. Browser console (F12 → Console tab) for any errors




