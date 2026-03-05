---
resource_id: "8311890e-00f5-482d-83ea-7a30b1bb6d6b"
resource_type: "document"
resource_name: "DEPLOYMENT_GUIDE"
---
# Production Deployment Guide
**Language Tracker Application**  
**Last Updated**: October 21, 2025

---

<!-- section_id: "4be009dd-8a0a-4268-979f-b6f9c7f68af6" -->
## Quick Deploy

```bash
# From project root
bash scripts/deploy/deploy-production.sh
```

---

<!-- section_id: "5acaf74d-d2ed-46a7-872a-7b196d558798" -->
## Deployment Options

<!-- section_id: "ab64a9ac-d44d-4b1e-80df-44dd2603a82c" -->
### Option 1: Simple Production Server (Recommended)

**Best for**: Initial deployment, small-medium traffic

```bash
# Install production dependencies
source .venv/bin/activate
pip install -r requirements-prod.txt

# Run with Gunicorn
gunicorn --config gunicorn.conf.py app:app
```

**Features**:
- Production-grade WSGI server
- Multiple worker processes
- Automatic worker restarts
- Comprehensive logging

---

<!-- section_id: "57099f6b-4221-404e-809d-6b2fa03423c9" -->
### Option 2: SystemD Service (Recommended for Long-term)

**Best for**: Production servers, automatic startup

```bash
# Generate service file
bash scripts/deploy/setup-systemd.sh

# Install service (requires sudo)
sudo cp /tmp/lang-trak.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable lang-trak
sudo systemctl start lang-trak

# Check status
sudo systemctl status lang-trak
```

**Features**:
- Automatic startup on boot
- Process monitoring and restart
- System integration
- Log management via journald

---

<!-- section_id: "e4017a72-a55e-4bb8-b956-bf96492db7dc" -->
### Option 3: Development Mode

**Best for**: Testing, development

```bash
source .venv/bin/activate
PORT=5000 python3 app.py
```

**Note**: Not recommended for production (single-threaded, no auto-restart)

---

<!-- section_id: "cdc3d0e1-4e5b-4b8b-bb05-79d3fa6f7d78" -->
## Pre-Deployment Checklist

<!-- section_id: "12365ac2-4b88-4af4-af46-c46b56db3965" -->
### 1. Environment Configuration

**Create `.env` file**:
```bash
cp .env.production.example .env
```

**Required Configuration**:
```bash
# Generate secret key
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))" >> .env

# Set Firebase project
echo "FIREBASE_PROJECT_ID=lang-trak-prod" >> .env
echo "GOOGLE_APPLICATION_CREDENTIALS=config/firebase/firebase-service-account-prod.json" >> .env
```

---

<!-- section_id: "4fd4f476-594b-4008-a675-139db3f51106" -->
### 2. Firebase Setup (if using cloud features)

**Service Account**:
1. Download service account JSON from Firebase Console
2. Save to `config/firebase/firebase-service-account-prod.json`
3. **Never commit this file!**

**Web SDK Configuration**:
Set these environment variables in your hosting platform:
```bash
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_APP_ID=your_app_id
VITE_FIREBASE_AUTH_DOMAIN=lang-trak-prod.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=lang-trak-prod
VITE_FIREBASE_STORAGE_BUCKET=lang-trak-prod.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
```

**Deploy Firestore Rules**:
```bash
firebase deploy --only firestore:rules --project lang-trak-prod
```

---

<!-- section_id: "1657ad5d-10e7-4c47-ad4e-c830aee12395" -->
### 3. Database Initialization

The SQLite database auto-initializes on first run, or initialize manually:

```bash
source .venv/bin/activate
python3 -c "import main; print('Database initialized')"
```

---

<!-- section_id: "6ba83018-5746-45c0-9d4d-37219a478900" -->
### 4. Dependencies

**Install production requirements**:
```bash
pip install -r requirements-prod.txt
```

**Includes**:
- Flask 2.3.2
- Gunicorn 21.2.0 (WSGI server)
- Firebase Admin SDK
- Azure Cognitive Services (TTS)
- All production dependencies

---

<!-- section_id: "a58fc415-7c02-4147-af0d-3adfa1d88130" -->
## Deployment Steps

<!-- section_id: "5fc03d69-b25c-4031-8793-f11a7ade4b84" -->
### Step 1: Prepare Environment

```bash
cd /home/dawson/code/lang-trak-in-progress

# Activate virtual environment
source .venv/bin/activate

# Install production dependencies
pip install -r requirements-prod.txt
```

---

<!-- section_id: "d1330054-415b-450f-826b-133252d0865c" -->
### Step 2: Configure Environment

```bash
# Copy example env file
cp .env.production.example .env

# Generate secret key
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))"
# Add the output to .env

# Configure Firebase (if using)
# Place service account JSON in config/firebase/
```

---

<!-- section_id: "cbcb66c9-2720-4efc-ae55-384890109ea2" -->
### Step 3: Initialize Database

```bash
# Database auto-initializes, or run manually:
python3 << EOF
import main
EOF
```

---

<!-- section_id: "61573404-78ab-4f24-9a7d-b357a4fcd1a0" -->
### Step 4: Start Production Server

**Option A: Foreground (for testing)**
```bash
gunicorn --config gunicorn.conf.py app:app
```

**Option B: Background (daemonized)**
```bash
gunicorn --config gunicorn.conf.py --daemon app:app

# Check it's running
ps aux | grep gunicorn
curl http://localhost:5000/health
```

**Option C: SystemD Service**
```bash
bash scripts/deploy/setup-systemd.sh
# Follow the instructions to install service
```

---

<!-- section_id: "28d621e4-64e8-4cbf-8cc2-84121a1afbcf" -->
### Step 5: Verify Deployment

```bash
# Health check
curl http://localhost:5000/health

# Check logs
tail -f logs/gunicorn-access.log
tail -f logs/gunicorn-error.log

# Test login page
curl -I http://localhost:5000/login
```

---

<!-- section_id: "9192aa2d-08f2-42e3-b88f-b1690b82a755" -->
## Production Configuration

<!-- section_id: "eca411ab-bb66-4ec6-9c5a-d9b2236b1cd4" -->
### Gunicorn Settings

**Configuration file**: `gunicorn.conf.py`

**Key settings**:
- **Workers**: Auto-calculated (CPU cores × 2 + 1)
- **Port**: From `PORT` env var (default: 5000)
- **Timeout**: 120 seconds
- **Max requests**: 1000 per worker (auto-restart)
- **Logging**: `logs/gunicorn-access.log` and `logs/gunicorn-error.log`

**Customize**:
Edit `gunicorn.conf.py` to adjust workers, timeout, logging, etc.

---

<!-- section_id: "ce8b13f0-1241-4283-86d4-0dd1568a294c" -->
## Monitoring & Maintenance

<!-- section_id: "469d9848-e643-4f13-8aa9-54c24b08bc01" -->
### Check Application Status

```bash
# With systemd
sudo systemctl status lang-trak

# With process management
ps aux | grep gunicorn
lsof -i:5000

# Health endpoint
curl http://localhost:5000/health
```

---

<!-- section_id: "ba80d468-421b-4499-9abb-3f1cf9e4de93" -->
### View Logs

```bash
# Gunicorn logs
tail -f logs/gunicorn-access.log
tail -f logs/gunicorn-error.log

# Flask application logs (if configured)
tail -f logs/app.log

# SystemD logs
sudo journalctl -u lang-trak -f
```

---

<!-- section_id: "e79cbe92-f369-4b44-a077-398bed065b3e" -->
### Restart Application

```bash
# With systemd
sudo systemctl restart lang-trak

# Manual (send HUP signal for graceful reload)
kill -HUP $(cat gunicorn.pid)

# Or stop and start
kill $(cat gunicorn.pid)
gunicorn --config gunicorn.conf.py app:app
```

---

<!-- section_id: "f4331e06-846b-4ac8-a24f-a8f74d0bdd67" -->
## Deployment Platforms

<!-- section_id: "aa5e2021-1eae-4e8a-a98b-68f56004f0dd" -->
### Deploy to Cloud Platforms

#### Google Cloud Run

```bash
# Install gcloud CLI
# Then deploy:
gcloud run deploy lang-trak \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars="FIREBASE_PROJECT_ID=lang-trak-prod"
```

#### Heroku

```bash
# Create Procfile
echo "web: gunicorn --config gunicorn.conf.py app:app" > Procfile

# Deploy
heroku create lang-trak
heroku config:set SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
git push heroku main
```

#### AWS EC2 / DigitalOcean

Use the SystemD service setup for these platforms.

---

<!-- section_id: "2efee90c-fcbf-4655-9b3f-241955e8420b" -->
## Security Checklist

Before deploying to production:

- [ ] **SECRET_KEY** set to random value (not default)
- [ ] **DEBUG** mode disabled (`FLASK_DEBUG=0`)
- [ ] **Firebase credentials** secured (not in git)
- [ ] **Service account JSON** has minimal permissions
- [ ] **HTTPS** enabled (use nginx/Apache as reverse proxy)
- [ ] **Firestore security rules** deployed
- [ ] **Environment variables** not committed to git
- [ ] **File uploads** limited to safe types
- [ ] **Regular backups** configured for SQLite database

---

<!-- section_id: "2f5a8ba3-45de-4ecd-9d4a-2c8979ef6387" -->
## Rollback Procedure

If deployment fails:

```bash
# Stop new deployment
sudo systemctl stop lang-trak  # or kill gunicorn

# Restore from backup
cp data/phonemes.db.backup data/phonemes.db

# Restart with previous version
git checkout previous-tag
sudo systemctl start lang-trak
```

---

<!-- section_id: "03f9a543-4b89-46ca-baea-e309546bedb8" -->
## Performance Tuning

<!-- section_id: "cbdc8949-de72-474b-bdb9-1e10707c10d3" -->
### Optimize Worker Count

```python
# In gunicorn.conf.py
workers = (2 * CPU_CORES) + 1  # Default
# Increase for I/O bound: workers = (4 * CPU_CORES) + 1
# Decrease for memory constraints: workers = CPU_CORES
```

<!-- section_id: "b9e85d8a-02e6-475b-941c-4efadb9c6ea8" -->
### Database Optimization

```bash
# SQLite performance tuning
sqlite3 data/phonemes.db "VACUUM;"
sqlite3 data/phonemes.db "ANALYZE;"
```

<!-- section_id: "368e5233-3cc1-4bbc-85ab-3664d51b5407" -->
### Enable Caching

Add to app.py:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

---

<!-- section_id: "3039bd7f-cdf8-4da7-be1c-1b96e79844ed" -->
## Troubleshooting

<!-- section_id: "a7ed0021-0857-41ef-a31a-63f8c98a6424" -->
### Common Issues

**Port already in use**:
```bash
lsof -ti:5000 | xargs kill -9
```

**Workers not starting**:
```bash
# Check logs
tail -f logs/gunicorn-error.log

# Reduce worker count in gunicorn.conf.py
workers = 2
```

**Database locked**:
```bash
# Check for existing connections
lsof data/phonemes.db

# Restart application
sudo systemctl restart lang-trak
```

**Static files not loading**:
```bash
# Check Flask static folder configuration
# Ensure static/ and templates/ directories exist
ls -la static/
ls -la templates/
```

---

<!-- section_id: "270dd23c-fe09-44d2-9bb3-e4fb52d48ad2" -->
## Post-Deployment Verification

<!-- section_id: "80585265-41fd-4f05-b60f-22b8bea95a10" -->
### Quick Smoke Test

```bash
# 1. Health check
curl http://localhost:5000/health
# Expected: {"status":"healthy"}

# 2. Login page loads
curl -I http://localhost:5000/login
# Expected: HTTP/1.1 200 OK

# 3. API responds
curl http://localhost:5000/api/tts/status
# Expected: {"backend":"azure","available":true}

# 4. Static files serve
curl -I http://localhost:5000/static/css/base.css
# Expected: HTTP/1.1 200 OK
```

<!-- section_id: "409f4067-32d6-430b-bb39-e42f63d2a8c7" -->
### Run Automation Tests

```bash
# Run full test suite against production
APP_BASE_URL=http://localhost:5000 \
  python3 scripts/automation/run_user_stories.py \
  --plan scripts/automation/story_plan.sample.json \
  --navigation-mode=direct \
  --concurrency 1
```

---

<!-- section_id: "4f1eb752-2597-40bd-af33-a31a61710ca4" -->
## Success Criteria

✅ Deployment successful if:
- Application responds on configured port
- Health endpoint returns 200 OK
- Login page loads successfully
- Workers are running (check `ps aux | grep gunicorn`)
- Logs show no critical errors
- Database queries succeed

---

<!-- section_id: "94d6905d-def2-4170-8366-d4b3caf89681" -->
## Support & Maintenance

<!-- section_id: "77eb95c5-a732-42b2-af7f-d45ddddeac7b" -->
### Backup Strategy

```bash
# Daily database backup
cp data/phonemes.db data/phonemes.db.$(date +%Y%m%d)

# Weekly automated backup (add to crontab)
0 2 * * 0 cp /path/to/data/phonemes.db /backups/phonemes.db.$(date +\%Y\%m\%d)
```

<!-- section_id: "aa8082d9-6dec-41f9-8ba8-b367757adb36" -->
### Update Procedure

```bash
# 1. Pull latest code
git pull origin main

# 2. Update dependencies
pip install -r requirements-prod.txt

# 3. Run migrations (if any)
# python scripts/migration/migrate.py

# 4. Restart service
sudo systemctl restart lang-trak

# 5. Verify
curl http://localhost:5000/health
```

---

<!-- section_id: "1f88262a-cad5-4c3a-b1ba-11fc8b8d97b3" -->
## Next Steps After Deployment

1. ✅ **Verify US-053** endpoint manually
2. 📊 **Monitor logs** for first 24 hours
3. 🔍 **Run manual testing** on key features
4. 📈 **Set up monitoring** (optional: New Relic, Datadog)
5. 🔄 **Configure backups** for database
6. 🌐 **Set up reverse proxy** (nginx/Apache for HTTPS)

---

**Deployment Status**: Ready ✅  
**Documentation**: Complete  
**Support**: See project README and docs/for_ai/ documentation

