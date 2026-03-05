---
resource_id: "2d0fc612-8c77-46dd-a855-ad9cf905cd2b"
resource_type: "readme
document"
resource_name: "README"
---
# Language-Tracker-App-MCP

## 🚀 Quick Start

To preview the web interface locally:

\\ash
source .venv/bin/activate  # or use python3 directly if you prefer
PORT=5002 python app.py
# PORT=5001 python3 app.py  # fallback when \python\ isn't available
\
Then open http://localhost:5002 in your browser.

## 🧪 **CRITICAL: Always Run Complete Testing First**
n## 🧪 **CRITICAL: Use This Script First**



Or manually:


**Before making any changes or reporting issues, ALWAYS run the comprehensive user story automation:**

\\ash
# Run ALL 71 user stories (grouped into 18 test suites)
source .venv/bin/activate
python scripts/automation/run_user_stories.py --navigation-mode=both
\
**This is the MAIN testing system that covers:**
- 71 individual user stories (US-001 to US-071)
- 18 test groups with both direct & realistic navigation 
- Complete end-to-end automation testing
- Full feature coverage validation

**Results will show:**
- ✅ Fully working features (both modes pass)
- ⚠️ Partially working features (direct mode only)
- ❌ Completely broken features (both modes fail)

**⚠️ DO NOT run individual tests first** - always start with the comprehensive suite to understand the complete system status.

### Other Testing Commands

After running the main suite, you can run these for specific debugging:

\\ash
# Quick smoke tests
npm run mcp:smoke

# Individual pytest tests
python -m pytest tests/ -v

# Individual browser automation
npm run stories:headed
\
## 📚 Documentation

See full documentation in \docs/README.md\.
