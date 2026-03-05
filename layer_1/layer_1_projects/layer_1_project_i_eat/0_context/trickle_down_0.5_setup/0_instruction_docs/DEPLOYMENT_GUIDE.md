---
resource_id: "953811f4-b921-4f4d-b8b3-b7a520f0ef81"
resource_type: "document"
resource_name: "DEPLOYMENT_GUIDE"
---
# Production Deployment Guide
**Language Tracker Application**  
**Last Updated**: October 21, 2025

---

<!-- section_id: "3f6d2e12-f0a8-4d53-b8da-6487e1d95b43" -->
## Quick Deploy

```bash
# From project root
bash scripts/deploy/deploy-production.sh
```

---

<!-- section_id: "f8e28256-e555-4db7-955a-f51b56fbc541" -->
## Deployment Options

<!-- section_id: "e828bcc4-691e-4c7b-a385-047de906b8dc" -->
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

<!-- section_id: "3a3112b7-68f9-4c01-95d4-a59a689cacb0" -->
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

<!-- section_id: "228bbf89-3e0f-493f-827e-f3b26ccfb310" -->
### Option 3: Development Mode

**Best for**: Testing, development

```bash
source .venv/bin/activate
PORT=5000 python3 app.py
```

**Note**: Not recommended for production (single-threaded, no auto-restart)

---

<!-- section_id: "a13f007c-b6b8-4a2a-bc4f-616aa963cfac" -->
## Pre-Deployment Checklist

<!-- section_id: "d1c15b32-47e8-483f-ace4-b83c35fe43a9" -->
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

<!-- section_id: "3feb08ea-7f90-4377-952c-ef204337db77" -->
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

<!-- section_id: "38a70d75-8321-4d44-a990-ce87ee989206" -->
### 3. Database Initialization

The SQLite database auto-initializes on first run, or initialize manually:

```bash
source .venv/bin/activate
python3 -c "import main; print('Database initialized')"
```

---

<!-- section_id: "139e2dbd-e5fc-4451-bc10-40c721a8a0fd" -->
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

<!-- section_id: "b273038d-f640-480d-b3c8-e06a755643ab" -->
## Deployment Steps

<!-- section_id: "da0dd443-35b3-4601-93f6-10ac3c0d0ae9" -->
### Step 1: Prepare Environment

```bash
cd /home/dawson/dawson-workspace/code/lang-trak-in-progress

# Activate virtual environment
source .venv/bin/activate

# Install production dependencies
pip install -r requirements-prod.txt
```

---

<!-- section_id: "56038284-add8-45d4-8c4d-f8ad1167e0d5" -->
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

<!-- section_id: "2b49770d-0582-4824-82f1-a051d696e9a3" -->
### Step 3: Initialize Database

```bash
# Database auto-initializes, or run manually:
python3 << EOF
import main
EOF
```

---

<!-- section_id: "386fa82b-6bc2-4f1c-ba4c-b0855ea2313d" -->
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

<!-- section_id: "abc0bd08-2260-4488-94f5-0e54e9cf4e47" -->
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

<!-- section_id: "03558e8a-ef32-4df4-8586-6ce5310932bf" -->
## Production Configuration

<!-- section_id: "7677cd1a-aa52-422b-be0e-0645ef4a124b" -->
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

<!-- section_id: "4bbe15f5-6f60-4fc4-8314-1d7d5f557b30" -->
## Monitoring & Maintenance

<!-- section_id: "eb832c6b-7847-43b8-ae47-f6b005651841" -->
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

<!-- section_id: "44086f68-eab2-469c-865a-9e838f3dfe70" -->
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

<!-- section_id: "e68be33c-9d80-4a44-83c3-189edfbdb5ce" -->
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

<!-- section_id: "4dffde60-5db8-42c6-adbb-c732e6fbc6d7" -->
## Deployment Platforms

<!-- section_id: "3c72a923-4d0c-4422-8070-925c520a8410" -->
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

<!-- section_id: "8586a466-fe67-451b-8213-3d3627de327b" -->
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

<!-- section_id: "73df52c9-6c60-4529-baa9-f93d75be9260" -->
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

<!-- section_id: "908e51bf-2edb-40b4-a29d-471388435954" -->
## Performance Tuning

<!-- section_id: "07d3f994-fabf-490a-82c6-a899d0248906" -->
### Optimize Worker Count

```python
# In gunicorn.conf.py
workers = (2 * CPU_CORES) + 1  # Default
# Increase for I/O bound: workers = (4 * CPU_CORES) + 1
# Decrease for memory constraints: workers = CPU_CORES
```

<!-- section_id: "5c582e9d-e3cd-4941-8b44-398dde3b00b5" -->
### Database Optimization

```bash
# SQLite performance tuning
sqlite3 data/phonemes.db "VACUUM;"
sqlite3 data/phonemes.db "ANALYZE;"
```

<!-- section_id: "3a94e863-bfc9-4297-b1b5-69eb64c83c29" -->
### Enable Caching

Add to app.py:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

---

<!-- section_id: "d6fa4a05-be24-4fab-a7e6-9b9759064b70" -->
## Troubleshooting

<!-- section_id: "339b79ff-bcc1-4c47-b055-3c4b08f6a589" -->
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

<!-- section_id: "9795cd99-52c6-4425-9f8e-df08a6f1c837" -->
## Post-Deployment Verification

<!-- section_id: "d9c35796-9700-4d4b-8608-9239d095d4c7" -->
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

<!-- section_id: "8913cea3-9914-4aca-a4cd-df1d87713182" -->
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

<!-- section_id: "4105c16e-ce50-409b-926f-fffef92fae06" -->
## Success Criteria

✅ Deployment successful if:
- Application responds on configured port
- Health endpoint returns 200 OK
- Login page loads successfully
- Workers are running (check `ps aux | grep gunicorn`)
- Logs show no critical errors
- Database queries succeed

---

<!-- section_id: "55b4fa65-7ba6-4129-9ea0-ada9a880f372" -->
## Support & Maintenance

<!-- section_id: "448bf148-aaa8-4956-ab59-23fa25cd1774" -->
### Backup Strategy

```bash
# Daily database backup
cp data/phonemes.db data/phonemes.db.$(date +%Y%m%d)

# Weekly automated backup (add to crontab)
0 2 * * 0 cp /path/to/data/phonemes.db /backups/phonemes.db.$(date +\%Y\%m\%d)
```

<!-- section_id: "18c2053c-9286-40bc-baed-f6927be6eb97" -->
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

<!-- section_id: "24da424c-ffa8-4f4f-b927-38a4b8cb740c" -->
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

