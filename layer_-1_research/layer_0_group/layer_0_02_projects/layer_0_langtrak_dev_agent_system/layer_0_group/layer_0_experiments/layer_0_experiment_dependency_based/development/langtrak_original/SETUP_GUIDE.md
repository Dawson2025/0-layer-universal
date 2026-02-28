# Lang-Trak Setup Guide

## Prerequisites

- Python 3.8+
- Node.js 22+ (via nvm recommended)
- SQLite3
- Git

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Dawson2025/lang-trak-in-progress.git
cd lang-trak-in-progress

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (for testing)
npm install

# Start the development server
./start_dev.sh
```

The app will be available at http://localhost:5002

---

## Common Issues & Solutions

### Issue 1: Flask App Returns 404 on All Routes

**Symptoms:**
- Server starts successfully
- All routes return 404 Not Found
- No errors in console

**Root Cause:**
Module-level routes not registered to the correct Flask app instance.

**Solution:**
Ensure `app.py` calls `create_app()` at module load time:

```python
# At the end of app.py (around line 5327)
init_users_table()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

**Fixed in commit:** `8c63c249`

---

### Issue 2: SQLite Migration Error - "Cannot add a UNIQUE column"

**Symptoms:**
```
sqlite3.OperationalError: Cannot add a UNIQUE column
```

**Root Cause:**
SQLite doesn't support adding columns with UNIQUE constraint via ALTER TABLE.

**Solution:**
Remove UNIQUE from ALTER TABLE statement:

```python
# In init_users_table() function
cursor.execute("ALTER TABLE groups ADD COLUMN invite_code TEXT")  # No UNIQUE
```

**Fixed in commit:** `8c63c249`

---

### Issue 3: NameError - get_firebase_config not defined

**Symptoms:**
```
NameError: name 'get_firebase_config' is not defined
```

**Root Cause:**
Missing function for client-side Firebase configuration.

**Solution:**
Add the function to `app.py`:

```python
def get_firebase_config():
    """Return client-side Firebase configuration."""
    return {
        "apiKey": "AIzaSyCXoBKM6UQx5wCvBYQ_KvhCPmjcNyis9XE",
        "authDomain": "lang-trak-dev.firebaseapp.com",
        "projectId": "lang-trak-dev",
        "storageBucket": "lang-trak-dev.firebasestorage.app",
        "messagingSenderId": "894561101654",
        "appId": "1:894561101654:web:fc234c159fd669749d98f7"
    }
```

**Fixed in commit:** `8c63c249`

---

### Issue 4: BuildError - Could not build url for endpoint 'index'

**Symptoms:**
```
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'index'
```

**Root Cause:**
Index route not registered due to malformed indentation in `create_app()`.

**Solution:**
Add module-level index route:

```python
@app.route('/')
def index():
    """Main menu - redirects to login or dashboard"""
    user = get_user_info()
    if not user['is_authenticated']:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))
```

**Fixed in commit:** `8c63c249`

---

### Issue 5: Firebase MCP Server - "npx: executable file not found"

**Symptoms:**
- Firebase MCP server shows error in Antigravity
- Error: `exec: 'npx': executable file not found in $PATH`

**Root Cause:**
Node.js installed via nvm isn't in Antigravity's PATH.

**Solution:**
Create symlinks in `~/.local/bin/`:

```bash
ln -sf ~/.nvm/versions/node/v22.21.1/bin/node ~/.local/bin/node
ln -sf ~/.nvm/versions/node/v22.21.1/bin/npm ~/.local/bin/npm
ln -sf ~/.nvm/versions/node/v22.21.1/bin/npx ~/.local/bin/npx
```

Then configure Firebase MCP in `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "firebase": {
      "command": "npx",
      "args": ["-y", "@gannonh/firebase-mcp"],
      "env": {
        "SERVICE_ACCOUNT_KEY_PATH": "/path/to/firebase-service-account-dev.json"
      }
    }
  }
}
```

**Note:** Use `@gannonh/firebase-mcp`, not `@modelcontextprotocol/server-firebase` (doesn't exist).

---

### Issue 6: Port Already in Use

**Symptoms:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**
```bash
# Find and kill process on port 5002
lsof -ti:5002 | xargs kill -9

# Or use a different port
PORT=5003 python app.py
```

---

### Issue 7: Firebase Emulator Connection Issues

**Symptoms:**
- Firebase operations fail
- "Connection refused" errors

**Solution:**
Ensure Firebase emulators are running and environment variables are set:

```bash
# start_dev.sh sets these automatically
export FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
export FIREBASE_AUTH_EMULATOR_HOST="127.0.0.1:9099"
export FIREBASE_STORAGE_EMULATOR_HOST="127.0.0.1:9199"
```

---

## Development Workflow

### Starting the Server

**Recommended:** Use the start script
```bash
./start_dev.sh
```

**Manual start:**
```bash
source .venv/bin/activate
PORT=5002 python app.py
```

### Running Tests

```bash
# Run all user story tests
python scripts/automation/run_user_stories.py

# Run specific feature tests
pytest tests/integration/test_authentication.py
```

### Database Management

```bash
# View users
sqlite3 phoneme_tracker.db "SELECT * FROM users;"

# Reset database
rm phoneme_tracker.db
python app.py  # Will recreate with init_users_table()
```

---

## Project Structure

```
lang-trak-in-progress/
├── app.py                 # Main Flask application
├── start_dev.sh          # Development server startup script
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies (testing)
├── config/
│   └── firebase/         # Firebase service account credentials
├── features/             # Feature modules
│   ├── projects/
│   ├── words/
│   └── admin/
├── services/
│   └── firebase/         # Firebase integration
├── templates/            # HTML templates
├── static/              # CSS, JS, images
└── tests/               # Test suites
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 5000 | Flask server port |
| `FLASK_SECRET_KEY` | (set in code) | Session encryption key |
| `FIRESTORE_EMULATOR_HOST` | 127.0.0.1:8080 | Firestore emulator |
| `FIREBASE_AUTH_EMULATOR_HOST` | 127.0.0.1:9099 | Auth emulator |
| `FIREBASE_STORAGE_EMULATOR_HOST` | 127.0.0.1:9199 | Storage emulator |

---

## Troubleshooting Checklist

- [ ] Virtual environment activated?
- [ ] All dependencies installed? (`pip install -r requirements.txt`)
- [ ] Port 5002 available?
- [ ] Database initialized? (check for `phoneme_tracker.db`)
- [ ] Firebase service account credentials present?
- [ ] Using `./start_dev.sh` or setting environment variables manually?

---

## Getting Help

1. Check this guide for common issues
2. Review [feature documentation](0_context/layer_2_features/README.md)
3. Check [testing guides](0_context/layer_2_features/)
4. Review git commit history for recent fixes

---

**Last Updated:** 2025-12-23
