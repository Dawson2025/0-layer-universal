---
resource_id: "7c58068a-803a-447d-9d13-e12d670d6492"
resource_type: "document"
resource_name: "DEPLOYMENT_GUIDE"
---
# Production Deployment Guide
**Language Tracker Application**  
**Last Updated**: October 21, 2025

---

<!-- section_id: "ef7fd66d-9cef-4b03-9f12-96a8e6894f95" -->
## Quick Deploy

```bash
# From project root
bash scripts/deploy/deploy-production.sh
```

---

<!-- section_id: "2cdc0e81-06ea-4a71-b792-3bf908b7120c" -->
## Deployment Options

<!-- section_id: "dfa197f9-80c5-4934-aec7-a2fc1922d0f4" -->
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

<!-- section_id: "22cb32db-02ba-40c6-8d56-e8164e2b827d" -->
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

<!-- section_id: "8299ab2c-1916-43a5-bbd6-49daefc241fb" -->
### Option 3: Development Mode

**Best for**: Testing, development

```bash
source .venv/bin/activate
PORT=5000 python3 app.py
```

**Note**: Not recommended for production (single-threaded, no auto-restart)

---

<!-- section_id: "6a17662d-392f-4ca1-9e72-383b0ed35a92" -->
## Pre-Deployment Checklist

<!-- section_id: "c6fb7085-24d1-4809-9c08-299483f54fe2" -->
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

<!-- section_id: "6a0f2a3e-e554-44a5-977b-982bc23d6e30" -->
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

<!-- section_id: "3a1716f1-cb1e-40a3-8c85-4e4842b080d3" -->
### 3. Database Initialization

The SQLite database auto-initializes on first run, or initialize manually:

```bash
source .venv/bin/activate
python3 -c "import main; print('Database initialized')"
```

---

<!-- section_id: "e619de47-667f-4ca2-a309-8e0c66a56df9" -->
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

<!-- section_id: "bede780d-3ba2-47c8-906e-9a3b35f461a7" -->
## Deployment Steps

<!-- section_id: "1b6aa9f7-8d29-4c2e-8b0c-5fb405614d37" -->
### Step 1: Prepare Environment

```bash
cd /home/dawson/code/lang-trak-in-progress

# Activate virtual environment
source .venv/bin/activate

# Install production dependencies
pip install -r requirements-prod.txt
```

---

<!-- section_id: "72a585ca-fb36-47eb-bc00-a5cc02c9a4ce" -->
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

<!-- section_id: "1c5f8b11-7a46-4767-a59c-e437674c33b3" -->
### Step 3: Initialize Database

```bash
# Database auto-initializes, or run manually:
python3 << EOF
import main
EOF
```

---

<!-- section_id: "a7fc9f31-512c-4cab-b32d-cbb666bb6294" -->
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

<!-- section_id: "f5014927-6dce-4b26-9c5f-7ce076cd8a2f" -->
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

<!-- section_id: "a7ad61a2-536b-49b3-adfb-06f77006c731" -->
## Production Configuration

<!-- section_id: "2052a3c9-05c4-45f0-9494-66bacd31f3a1" -->
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

<!-- section_id: "5161f5ab-ee89-42e6-b663-a3d9a1180adb" -->
## Monitoring & Maintenance

<!-- section_id: "bbb6effd-a1b6-4b86-a5cd-8d93cea27e14" -->
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

<!-- section_id: "9499ccb9-29c5-45c7-b02d-e7b74c8d9355" -->
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

<!-- section_id: "7912ce93-c980-4dc5-aa27-71ccfa3a5971" -->
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

<!-- section_id: "f39696a6-a750-4a74-a6f9-6bd4b724ed47" -->
## Deployment Platforms

<!-- section_id: "4d6e3c6d-1ae9-46fd-bc38-eb350abbd81f" -->
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

<!-- section_id: "9640d417-cd2b-4ad7-839e-ff1321ce7167" -->
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

<!-- section_id: "6728129a-06b1-425d-9deb-d94129eef8ff" -->
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

<!-- section_id: "7b3dbd0e-ff02-4c18-bf51-520221a06e01" -->
## Performance Tuning

<!-- section_id: "fe7dffed-4483-4d7f-9d4d-0c2275c860a4" -->
### Optimize Worker Count

```python
# In gunicorn.conf.py
workers = (2 * CPU_CORES) + 1  # Default
# Increase for I/O bound: workers = (4 * CPU_CORES) + 1
# Decrease for memory constraints: workers = CPU_CORES
```

<!-- section_id: "ea535c83-e331-43f9-89fb-8c5b0eb2525a" -->
### Database Optimization

```bash
# SQLite performance tuning
sqlite3 data/phonemes.db "VACUUM;"
sqlite3 data/phonemes.db "ANALYZE;"
```

<!-- section_id: "c2ac3f0d-fda0-4246-afc9-3f732bd30a8b" -->
### Enable Caching

Add to app.py:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

---

<!-- section_id: "a822f9db-fa49-4a84-bf13-c4c84f61b80c" -->
## Troubleshooting

<!-- section_id: "16a8d183-3276-4abf-861f-73a4dafdb18b" -->
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

<!-- section_id: "fe2c6b37-0287-4d3c-9f62-34cd49f72425" -->
## Post-Deployment Verification

<!-- section_id: "e49892f5-83d7-4448-9e48-54afaed47b06" -->
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

<!-- section_id: "cb737f16-c222-4653-abcb-a307d0f87ce2" -->
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

<!-- section_id: "00b719f7-ce6f-4a40-a3e5-d2c66ba9596e" -->
## Success Criteria

✅ Deployment successful if:
- Application responds on configured port
- Health endpoint returns 200 OK
- Login page loads successfully
- Workers are running (check `ps aux | grep gunicorn`)
- Logs show no critical errors
- Database queries succeed

---

<!-- section_id: "982e2efa-d500-4b6c-a452-87aeac31d1b8" -->
## Support & Maintenance

<!-- section_id: "22d5d24d-eb1f-4d12-9d7b-689ac1e7a992" -->
### Backup Strategy

```bash
# Daily database backup
cp data/phonemes.db data/phonemes.db.$(date +%Y%m%d)

# Weekly automated backup (add to crontab)
0 2 * * 0 cp /path/to/data/phonemes.db /backups/phonemes.db.$(date +\%Y\%m\%d)
```

<!-- section_id: "d0b2c737-d506-4794-93c6-3f2b1470fbed" -->
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

<!-- section_id: "5528f4c2-7039-4151-ad2f-87eb5dfbed66" -->
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

