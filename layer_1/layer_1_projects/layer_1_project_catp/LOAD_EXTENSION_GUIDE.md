---
resource_id: "644ae2b2-54bf-4915-bd02-536861553fa1"
resource_type: "document"
resource_name: "LOAD_EXTENSION_GUIDE"
---
# 🎯 How to Load the Extension in Chrome

Since we're on WSL, here's the step-by-step process to load the extension:

## Option 1: Manual Load (Easiest - 30 seconds)

### Step 1: Open Chrome Extensions Page
1. Open Google Chrome
2. Type in address bar: `chrome://extensions/`
3. Press Enter

### Step 2: Enable Developer Mode
1. Look for the toggle switch in the **top-right corner** that says "Developer mode"
2. Click it to turn it **ON** (it should turn blue)

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

### Step 4: Verify Extension Loaded
You should see a card that says:
```
Canvas Assignment Timer
Version 1.0
```

### Step 5: Test It!
1. Navigate to any Canvas assignment page with URL like:
   ```
   https://byui.instructure.com/courses/*/assignments/*
   ```
   (Replace * with actual course and assignment IDs)

2. You should see the **purple gradient sidebar** appear on the right side!

---

## Option 2: Direct Path (If Option 1 doesn't work)

If WSL path doesn't work, copy the extension folder to Windows:

### Step 1: Copy to Windows
```bash
# Run this in WSL terminal:
cp -r /home/dawson/dawson-workspace/code/catp/task-timer-frontend /mnt/c/Users/$USER/Desktop/task-timer-frontend
```

### Step 2: Load from Windows Path
1. Open `chrome://extensions/`
2. Enable Developer mode
3. Click "Load unpacked"
4. Navigate to: `C:\Users\YourUsername\Desktop\task-timer-frontend`
5. Click "Select Folder"

---

## What You Should See

### Before Loading Extension:
- Normal Canvas assignment page
- No sidebar

### After Loading Extension:
- **Purple gradient sidebar on the right**
- Shows: Mean Time, Median, Mode
- Timer counting up
- Bell curve visualization
- Form to submit your time
- "🔥 Connected to Firestore" indicator at bottom-right

---

## Troubleshooting

### Error: "Manifest file is missing or unreadable"
**Fix**: Make sure you selected the `task-timer-frontend` folder itself, not a parent or subfolder

### Error: "This extension may have been corrupted"
**Fix**: Make sure `bundle.js` exists (run `npm run test` to rebuild)

### Sidebar not appearing on Canvas
**Check**:
1. Are you on a page matching: `*.instructure.com/courses/*/assignments/*`?
2. Is the extension enabled? (Check `chrome://extensions/`)
3. Try refreshing the page (F5)
4. Check browser console (F12) for any errors

### Can't access WSL path
**Solution**: Use Option 2 above to copy to Windows Desktop first

---

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

## Need Help?

If you're stuck, take a screenshot of:
1. Chrome extensions page showing the loaded extension
2. The Canvas page where it should appear
3. Browser console (F12 → Console tab) for any errors




