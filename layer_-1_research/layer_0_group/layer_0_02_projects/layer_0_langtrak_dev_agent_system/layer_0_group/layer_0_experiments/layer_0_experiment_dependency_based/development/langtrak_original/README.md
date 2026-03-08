---
resource_id: "7c709897-f299-4336-8c41-6a6745d180ec"
resource_type: "readme_document"
resource_name: "README"
---
# Language-Tracker-App-MCP

<!-- section_id: "d27651d5-3254-452f-a7e3-8bff8c1025ae" -->
## 🚀 Quick Start

To preview the web interface locally:

\\ash
source .venv/bin/activate  # or use python3 directly if you prefer
PORT=5002 python app.py
# PORT=5001 python3 app.py  # fallback when \python\ isn't available
\
Then open http://localhost:5002 in your browser.

<!-- section_id: "a414145b-7b81-4297-a47f-ecdb81dc2ed3" -->
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

<!-- section_id: "d08a87fb-559c-4bf4-a549-270780cf26d5" -->
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
<!-- section_id: "0c921778-19bf-4a19-9c0a-341e18a92dd4" -->
## 📚 Documentation

See full documentation in \docs/README.md\.
