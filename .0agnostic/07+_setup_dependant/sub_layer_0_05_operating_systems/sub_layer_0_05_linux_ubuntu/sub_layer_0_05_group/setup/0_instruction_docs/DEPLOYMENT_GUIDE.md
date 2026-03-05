---
resource_id: "10abdfac-124e-4929-99c8-ea43f57b656e"
resource_type: "document"
resource_name: "DEPLOYMENT_GUIDE"
---
# Production Deployment Guide
**Language Tracker Application**  
**Last Updated**: October 21, 2025

---

<!-- section_id: "cf2cb911-cbe3-4705-ab67-e2365b6ead73" -->
## Quick Deploy

```bash
# From project root
bash scripts/deploy/deploy-production.sh
```

---

<!-- section_id: "76bb1684-7c48-4ed4-a9aa-7ddadca2bd8d" -->
## Deployment Options

<!-- section_id: "f25c3fee-a504-41a3-b535-a4e643a5e806" -->
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

<!-- section_id: "3a1c75e9-9d6d-40ab-b68f-539d2c41358a" -->
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

<!-- section_id: "706a7371-1797-47be-8f88-47f2b7dba81d" -->
### Option 3: Development Mode

**Best for**: Testing, development

```bash
source .venv/bin/activate
PORT=5000 python3 app.py
```

**Note**: Not recommended for production (single-threaded, no auto-restart)

---

<!-- section_id: "2346407f-fae6-4f4e-b019-9d9ab00d1c8e" -->
## Pre-Deployment Checklist

<!-- section_id: "0115b4ff-9e55-48d5-9b15-45e0189fc49e" -->
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

<!-- section_id: "c6d51d79-aad1-45ce-b641-de49cc9fcddb" -->
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

<!-- section_id: "72d906b9-79e9-4b24-adfc-3cec05cf24e9" -->
### 3. Database Initialization

The SQLite database auto-initializes on first run, or initialize manually:

```bash
source .venv/bin/activate
python3 -c "import main; print('Database initialized')"
```

---

<!-- section_id: "82ba7a44-b226-47db-8533-aab7dd5bf783" -->
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

<!-- section_id: "63ba020f-b243-4b17-aa03-62ed7fb82c06" -->
## Deployment Steps

<!-- section_id: "10b5abe5-57df-4295-a5c0-2088000f2492" -->
### Step 1: Prepare Environment

```bash
cd /home/dawson/code/lang-trak-in-progress

# Activate virtual environment
source .venv/bin/activate

# Install production dependencies
pip install -r requirements-prod.txt
```

---

<!-- section_id: "17b125df-64c9-4133-9a2f-1999c525886e" -->
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

<!-- section_id: "2c74d877-ffd7-4204-9600-0580543b3b28" -->
### Step 3: Initialize Database

```bash
# Database auto-initializes, or run manually:
python3 << EOF
import main
EOF
```

---

<!-- section_id: "4ea3a281-c087-4828-ab09-024e723bf84f" -->
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

<!-- section_id: "0d3c681b-e91a-43ee-bdfd-13ba19713542" -->
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

<!-- section_id: "49d69ea9-3739-4c9d-a22f-4617a0c3392c" -->
## Production Configuration

<!-- section_id: "c805ca80-a86a-4c53-9c18-6db343b9529e" -->
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

<!-- section_id: "22f6a554-f4fd-4e39-93fb-8dd7b5f3e184" -->
## Monitoring & Maintenance

<!-- section_id: "a5b60c17-b37b-4b09-91b4-8576a4a03578" -->
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

<!-- section_id: "ea7341bc-54d5-4bea-b47d-b2a618762b9f" -->
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

<!-- section_id: "419502fe-2473-42b1-918a-988e27b33bbf" -->
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

<!-- section_id: "4372ca70-0766-4fc7-8137-9fb8298cdd49" -->
## Deployment Platforms

<!-- section_id: "c7ca85f4-bc8f-4d95-b24d-1c0cd79b1288" -->
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

<!-- section_id: "e057640f-4bec-4022-8327-c36ced74dc83" -->
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

<!-- section_id: "63285eb0-9472-4de0-b306-19f8fca3a73d" -->
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

<!-- section_id: "93d2f263-2ba8-4e8d-a660-78ea12a3513d" -->
## Performance Tuning

<!-- section_id: "d6829557-6cd1-4ac9-8f18-afc3aa57c977" -->
### Optimize Worker Count

```python
# In gunicorn.conf.py
workers = (2 * CPU_CORES) + 1  # Default
# Increase for I/O bound: workers = (4 * CPU_CORES) + 1
# Decrease for memory constraints: workers = CPU_CORES
```

<!-- section_id: "200b767c-5e2c-447d-b7b4-d9dfe3ca6183" -->
### Database Optimization

```bash
# SQLite performance tuning
sqlite3 data/phonemes.db "VACUUM;"
sqlite3 data/phonemes.db "ANALYZE;"
```

<!-- section_id: "b48cc729-cfb8-44fe-b05a-9aecd319ee78" -->
### Enable Caching

Add to app.py:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

---

<!-- section_id: "bb741038-cd6f-43b9-b210-a8cf47803567" -->
## Troubleshooting

<!-- section_id: "aae9a5f4-870a-460b-9165-10cb8ecee66b" -->
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

<!-- section_id: "9fc8f9e0-4210-4ab1-a143-2b4d0c69a17d" -->
## Post-Deployment Verification

<!-- section_id: "dd44fd06-8ff1-43ff-b4d1-84ff3c8a09d9" -->
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

<!-- section_id: "be8906a7-cf03-486d-9c7b-4820edd84058" -->
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

<!-- section_id: "bbf3d22c-31a8-4c22-9d71-85bdbd45230d" -->
## Success Criteria

✅ Deployment successful if:
- Application responds on configured port
- Health endpoint returns 200 OK
- Login page loads successfully
- Workers are running (check `ps aux | grep gunicorn`)
- Logs show no critical errors
- Database queries succeed

---

<!-- section_id: "e9f9bb20-265e-4065-adf7-ccfa2fa4c113" -->
## Support & Maintenance

<!-- section_id: "0d9ff825-9157-4a08-93be-65eeb68be1f6" -->
### Backup Strategy

```bash
# Daily database backup
cp data/phonemes.db data/phonemes.db.$(date +%Y%m%d)

# Weekly automated backup (add to crontab)
0 2 * * 0 cp /path/to/data/phonemes.db /backups/phonemes.db.$(date +\%Y\%m\%d)
```

<!-- section_id: "adf57fe9-c87e-4e8d-bdd3-bdaa20211386" -->
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

<!-- section_id: "b7d67cb2-972b-47ef-9f8f-bd94a8ed218b" -->
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

