---
resource_id: "0d9a80d6-26c5-4bfa-aa06-70c57609fe69"
resource_type: "document"
resource_name: "DEPLOYMENT_GUIDE"
---
# Production Deployment Guide
**Language Tracker Application**  
**Last Updated**: October 21, 2025

---

<!-- section_id: "64984f10-5146-4813-abe8-db20a30d14ce" -->
## Quick Deploy

```bash
# From project root
bash scripts/deploy/deploy-production.sh
```

---

<!-- section_id: "f2e1f473-302e-4f43-81fd-b10fd21b7ff6" -->
## Deployment Options

<!-- section_id: "c4da64bf-26fd-416d-b493-940de8840a65" -->
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

<!-- section_id: "c7bd6428-bfca-4191-aafb-a7d946cb81be" -->
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

<!-- section_id: "fc9d661a-add5-4790-94ec-f087c8e567e2" -->
### Option 3: Development Mode

**Best for**: Testing, development

```bash
source .venv/bin/activate
PORT=5000 python3 app.py
```

**Note**: Not recommended for production (single-threaded, no auto-restart)

---

<!-- section_id: "4ee45ff2-cf0f-48f7-92fc-4ffa6b076409" -->
## Pre-Deployment Checklist

<!-- section_id: "9c3b92b6-8694-46ff-ae93-87aad275d1f8" -->
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

<!-- section_id: "bc1a50f7-de3b-46d5-9a1e-034240977b32" -->
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

<!-- section_id: "873be9dc-f03f-4bf9-8dc7-be521c4c06fe" -->
### 3. Database Initialization

The SQLite database auto-initializes on first run, or initialize manually:

```bash
source .venv/bin/activate
python3 -c "import main; print('Database initialized')"
```

---

<!-- section_id: "c4081316-1c5a-4419-8d8f-75a679258e24" -->
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

<!-- section_id: "4d7b5423-006c-48c9-a841-9680f7a90af1" -->
## Deployment Steps

<!-- section_id: "27221f72-0582-460d-b676-5b921f871dce" -->
### Step 1: Prepare Environment

```bash
cd /home/dawson/code/lang-trak-in-progress

# Activate virtual environment
source .venv/bin/activate

# Install production dependencies
pip install -r requirements-prod.txt
```

---

<!-- section_id: "806d32a9-6083-4140-b445-0c24f0736ce8" -->
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

<!-- section_id: "e440a2ce-e225-44cc-921f-7a5b5c0afbb6" -->
### Step 3: Initialize Database

```bash
# Database auto-initializes, or run manually:
python3 << EOF
import main
EOF
```

---

<!-- section_id: "f45813e2-e6fc-4894-bed4-94838c791752" -->
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

<!-- section_id: "5d5f540c-bfc0-424f-9a45-26920c55f64e" -->
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

<!-- section_id: "91e68e6b-53b2-4fdd-a143-9ea520c14d97" -->
## Production Configuration

<!-- section_id: "25c4cc95-60ed-4038-9496-3102205eeaa7" -->
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

<!-- section_id: "c7090d36-bafa-4870-ae15-415497641595" -->
## Monitoring & Maintenance

<!-- section_id: "70d53e20-6828-4370-bb99-4e7237cda231" -->
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

<!-- section_id: "cbb9faae-39ce-404c-90a0-2cd2b76de48b" -->
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

<!-- section_id: "2955f5c4-ba7d-4ff2-93a1-a151276deeb8" -->
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

<!-- section_id: "3da8387d-bb8a-4de5-ae1d-3cc22b25e040" -->
## Deployment Platforms

<!-- section_id: "08cfc373-36a5-47e4-84e3-12760e204648" -->
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

<!-- section_id: "eb3a59b4-eb80-49de-bfe6-986c2017676d" -->
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

<!-- section_id: "bf3d566d-1b7f-4d39-bd00-1be07aae2286" -->
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

<!-- section_id: "fa482802-bc5c-4e45-aeab-df704671e43d" -->
## Performance Tuning

<!-- section_id: "3ee2e58d-7d30-4e1a-a04d-788cd21f9bb6" -->
### Optimize Worker Count

```python
# In gunicorn.conf.py
workers = (2 * CPU_CORES) + 1  # Default
# Increase for I/O bound: workers = (4 * CPU_CORES) + 1
# Decrease for memory constraints: workers = CPU_CORES
```

<!-- section_id: "1c841c97-860c-4093-a41b-2fe26b3d627a" -->
### Database Optimization

```bash
# SQLite performance tuning
sqlite3 data/phonemes.db "VACUUM;"
sqlite3 data/phonemes.db "ANALYZE;"
```

<!-- section_id: "164cb2b4-d449-4121-a62d-b2ec24518240" -->
### Enable Caching

Add to app.py:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

---

<!-- section_id: "d899d33b-9ae7-45be-ac35-efc27bc498f7" -->
## Troubleshooting

<!-- section_id: "e1aa70e9-cb08-4cc0-a69c-2ef147a6b86d" -->
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

<!-- section_id: "1d81a51f-085a-412e-9c52-d286e8bd1437" -->
## Post-Deployment Verification

<!-- section_id: "63e44176-57bf-41f7-a28f-990c9c2482fd" -->
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

<!-- section_id: "84cd128a-b8e4-4318-b4fb-7c0a6caaf575" -->
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

<!-- section_id: "32250c99-9d39-47df-99f4-5b310a877456" -->
## Success Criteria

✅ Deployment successful if:
- Application responds on configured port
- Health endpoint returns 200 OK
- Login page loads successfully
- Workers are running (check `ps aux | grep gunicorn`)
- Logs show no critical errors
- Database queries succeed

---

<!-- section_id: "1b9093ee-aa73-45c8-a903-2a68c450ec19" -->
## Support & Maintenance

<!-- section_id: "9aa45c0b-7819-49ae-ad9c-173ef9f433d1" -->
### Backup Strategy

```bash
# Daily database backup
cp data/phonemes.db data/phonemes.db.$(date +%Y%m%d)

# Weekly automated backup (add to crontab)
0 2 * * 0 cp /path/to/data/phonemes.db /backups/phonemes.db.$(date +\%Y\%m\%d)
```

<!-- section_id: "defe17f7-3f72-4125-ac6a-1455b1f0d484" -->
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

<!-- section_id: "582ee73b-5949-4ec9-9c87-886339e5aeb4" -->
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

