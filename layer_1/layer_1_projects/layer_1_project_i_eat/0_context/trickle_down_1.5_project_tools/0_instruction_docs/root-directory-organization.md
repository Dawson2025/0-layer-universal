---
resource_id: "18045c5b-71f4-43b6-a328-7a28d9b72751"
resource_type: "document"
resource_name: "root-directory-organization"
---
# Root Directory Organization Guide
*Proper Organization of Files in Project Root Directory*

<!-- section_id: "9f10fa10-f892-4845-a607-22479595d35d" -->
## 🎯 Purpose

This document outlines which files should remain in the project root directory and which files should be organized into the trickle-down documentation structure.

<!-- section_id: "2b385d11-cea9-400a-942e-52a7fc20b631" -->
## 📁 Files That Should Remain in Root

<!-- section_id: "6ffe80fe-511c-4302-9827-248c2ce38f77" -->
### **Essential Application Files**
These files are required for the application to function and must remain in the root directory:

- `README.md` - Main project documentation and entry point
- `app.py` - Main Flask application file
- `main.py` - Alternative main application file
- `conftest.py` - Pytest configuration
- `setup.py` - Python package setup

<!-- section_id: "745d9021-8f88-44a4-9ce4-b39267ae1344" -->
### **Configuration Files (Essential)**
These configuration files are required for the application to run:

- `gunicorn.conf.py` - Gunicorn server configuration
- `pytest.ini` - Pytest testing configuration
- `requirements.txt` - Python dependencies
- `requirements-prod.txt` - Production Python dependencies
- `package.json` - Node.js dependencies
- `package-lock.json` - Node.js dependency lock file

<!-- section_id: "3005e72e-29e9-49f1-a2b9-638abde60fca" -->
### **Git Configuration (Essential)**
- `.gitignore` - Git ignore rules (required for version control)

<!-- section_id: "41b3eadf-a614-4d6e-95bc-02b0f828e2f7" -->
## 📁 Files That Were Moved to Organized Structure

<!-- section_id: "2e48a349-12c6-4fc0-8e85-3e1c33be711a" -->
### **Configuration Files** → `trickle_down_1.5_project_tools/0_instruction_docs/configs/`
- `.mcp.json` - MCP server configuration
- `architecture-plan.json` - System architecture planning
- `demo-architecture-plan.json` - Demo architecture planning
- `firebase-admin-config.json` - Firebase admin configuration
- `firebase.json` - Firebase project configuration
- `master-orchestration-config.json` - Master orchestration configuration
- `mcp-config-enhanced.json` - Enhanced MCP configuration
- `monitoring-config.json` - Monitoring configuration
- `orchestration-config.json` - Orchestration configuration
- `security-config.json` - Security configuration
- `simple_auth_config.json` - Simple authentication configuration

<!-- section_id: "c89d5bc7-094e-4cb1-8c88-8a50ede775c8" -->
### **Script Files** → `trickle_down_1.5_project_tools/0_instruction_docs/scripts/`
- `firebase_complete_demo.py` - Firebase complete demo script
- `firebase_master_orchestrator.py` - Firebase master orchestrator
- `firebase_orchestration_system.py` - Firebase orchestration system
- `firebase_visual_orchestrator.py` - Firebase visual orchestrator
- `install-playwright.sh` - Playwright installation script
- `run-all-tests.sh` - Test runner script

<!-- section_id: "0009d20f-9ff5-4b62-8f9a-521b0b7340ab" -->
### **Log Files** → `trickle_down_1.5_project_tools/0_instruction_docs/logs/`
- `automation-test-after-fix.log` - Automation test log
- `flask.log` - Flask application log
- `flask.pid` - Flask process ID
- `gunicorn.pid` - Gunicorn process ID

<!-- section_id: "348273be-353b-4f17-9f30-afa7c1e1ba9b" -->
### **Data Files** → `trickle_down_1.5_project_tools/0_instruction_docs/data/`
- `comprehensive-report-20251023-151108.json` - Comprehensive report
- `comprehensive-report-20251023-151426.json` - Comprehensive report
- `demo-results.json` - Demo results
- `orchestration-report.json` - Orchestration report
- `master-system-report-20251023-151324.json` - Master system report
- `master-system-report-20251023-151423.json` - Master system report
- `all_stories.txt` - All stories data
- `cookies-test.txt` - Cookies test data
- `test-cookies.txt` - Test cookies data

<!-- section_id: "ff9c5009-a43e-422b-8fbd-184e8833e933" -->
### **Backup Files** → `trickle_down_1.5_project_tools/0_instruction_docs/backups/`
- `README.md.backup` - Backup of README file
- `app.py.backup` - Backup of app.py file

<!-- section_id: "ff149453-19ff-400b-b02c-72a882269268" -->
### **Screenshot Files** → `trickle_down_1.5_project_tools/0_instruction_docs/screenshots/`
- `deployment-plan-development-environment.png` - Development deployment plan
- `deployment-plan-full-deployment.png` - Full deployment plan
- `deployment-plan-production-environment.png` - Production deployment plan
- `deployment-plan-staging-environment.png` - Staging deployment plan
- `firebase-dashboard-20251023-151107.png` - Firebase dashboard screenshot
- `firebase-dashboard-20251023-151108.png` - Firebase dashboard screenshot
- `firebase-dashboard-20251023-151323.png` - Firebase dashboard screenshot
- `firebase-dashboard-20251023-151415.png` - Firebase dashboard screenshot
- `firebase-dashboard-20251023-151422.png` - Firebase dashboard screenshot
- `firebase-dashboard-20251023-151423.png` - Firebase dashboard screenshot

<!-- section_id: "470db85d-1c49-4c03-a14b-50188a2b2952" -->
### **Database Files** → `trickle_down_2_features/0_instruction_docs/data/`
- `main.db` - Main application database
- `phonemes.db` - Phonemes database

<!-- section_id: "fd592f8d-bb8b-498f-b3af-0b363c39aff9" -->
## 🎯 Organization Principles

<!-- section_id: "cb34a7ed-01f9-4292-88c7-c4c2fe4de876" -->
### **Keep in Root If:**
- File is essential for application startup
- File is required by build tools or package managers
- File serves as the main entry point for the project
- File is a standard configuration file for the technology stack

<!-- section_id: "21147fde-6aa8-45d5-92d5-23cb53a428b9" -->
### **Move to Organized Structure If:**
- File is documentation or reference material
- File is a script or utility not essential for startup
- File is a log or temporary data file
- File is a configuration file for specific features or tools
- File is a report or generated data file

<!-- section_id: "4eec567e-cc0a-4d44-b56f-8e7440eefcff" -->
## 📊 Organization Results

<!-- section_id: "a72790ac-57c6-4098-9d63-fe13a993b0b7" -->
### **Before Organization:**
- 43+ files scattered in root directory
- Mix of essential and non-essential files
- Difficult to identify core application files

<!-- section_id: "961b6363-72de-433d-9781-a1129bb79983" -->
### **After Organization:**
- **12 essential files** remain in root directory
- **40+ files** moved to organized trickle-down structure
- **Clear separation** between essential and organizational files
- **Easy identification** of core application components

<!-- section_id: "2fbd1a1a-b11e-49e6-85b7-4f96a1fe30a1" -->
## 🔗 Related Documentation

- **Project Tools**: `../trickle_down_1.5_project_tools/0_instruction_docs/`
- **Feature Data**: `../trickle_down_2_features/0_instruction_docs/data/`
- **Documentation Protocol**: `../trickle_down_0_universal_instructions/0_instruction_docs/post-completion-documentation-protocol.md`

---

**Maintained By**: Project Organization System
**Last Updated**: 2025-01-23
**Next Review**: 2025-02-23
