---
resource_id: "771ddb63-cf2c-4845-aebb-7f180e464269"
resource_type: "document"
resource_name: "root-directory-organization"
---
# Root Directory Organization Guide
*Proper Organization of Files in Project Root Directory*

<!-- section_id: "da0ef527-f551-41d2-91d8-61f278a2e7db" -->
## 🎯 Purpose

This document outlines which files should remain in the project root directory and which files should be organized into the trickle-down documentation structure.

<!-- section_id: "8ad9c859-d436-4aa3-b1a3-2bcae4459711" -->
## 📁 Files That Should Remain in Root

<!-- section_id: "d7799cbf-21f1-4a40-b390-ffed4917050d" -->
### **Essential Application Files**
These files are required for the application to function and must remain in the root directory:

- `README.md` - Main project documentation and entry point
- `app.py` - Main Flask application file
- `main.py` - Alternative main application file
- `conftest.py` - Pytest configuration
- `setup.py` - Python package setup

<!-- section_id: "a562f151-1ef6-4b97-8bd7-a67ca9642465" -->
### **Configuration Files (Essential)**
These configuration files are required for the application to run:

- `gunicorn.conf.py` - Gunicorn server configuration
- `pytest.ini` - Pytest testing configuration
- `requirements.txt` - Python dependencies
- `requirements-prod.txt` - Production Python dependencies
- `package.json` - Node.js dependencies
- `package-lock.json` - Node.js dependency lock file

<!-- section_id: "abe768b8-22ed-4862-b760-8f8ba239d007" -->
### **Git Configuration (Essential)**
- `.gitignore` - Git ignore rules (required for version control)

<!-- section_id: "ff12487d-4f13-4b4c-b2e1-6e9424cf4162" -->
## 📁 Files That Were Moved to Organized Structure

<!-- section_id: "ce5ac476-9796-4509-8103-ead3171ce4a6" -->
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

<!-- section_id: "2f0de470-5846-4c49-a3af-e8ffcb8a08b1" -->
### **Script Files** → `trickle_down_1.5_project_tools/0_instruction_docs/scripts/`
- `firebase_complete_demo.py` - Firebase complete demo script
- `firebase_master_orchestrator.py` - Firebase master orchestrator
- `firebase_orchestration_system.py` - Firebase orchestration system
- `firebase_visual_orchestrator.py` - Firebase visual orchestrator
- `install-playwright.sh` - Playwright installation script
- `run-all-tests.sh` - Test runner script

<!-- section_id: "f2877d0e-1501-4a3c-9c7e-79685c30430b" -->
### **Log Files** → `trickle_down_1.5_project_tools/0_instruction_docs/logs/`
- `automation-test-after-fix.log` - Automation test log
- `flask.log` - Flask application log
- `flask.pid` - Flask process ID
- `gunicorn.pid` - Gunicorn process ID

<!-- section_id: "d552c322-3dd4-4c01-a077-5788ab560fc5" -->
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

<!-- section_id: "f6fb08d0-80e7-4e19-a714-51ff161d69fc" -->
### **Backup Files** → `trickle_down_1.5_project_tools/0_instruction_docs/backups/`
- `README.md.backup` - Backup of README file
- `app.py.backup` - Backup of app.py file

<!-- section_id: "f35d415a-4d23-4da1-92af-08ae5d6b7fcc" -->
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

<!-- section_id: "d60eae39-c3cc-4be8-a236-a2fbb0efd25e" -->
### **Database Files** → `trickle_down_2_features/0_instruction_docs/data/`
- `main.db` - Main application database
- `phonemes.db` - Phonemes database

<!-- section_id: "e380b6e7-e74f-4d47-ada9-881692554e45" -->
## 🎯 Organization Principles

<!-- section_id: "4c4bd109-d97d-41ac-8dbf-fc1e52fdd5b9" -->
### **Keep in Root If:**
- File is essential for application startup
- File is required by build tools or package managers
- File serves as the main entry point for the project
- File is a standard configuration file for the technology stack

<!-- section_id: "deaae612-cf64-409c-ae1c-76296ecbe33d" -->
### **Move to Organized Structure If:**
- File is documentation or reference material
- File is a script or utility not essential for startup
- File is a log or temporary data file
- File is a configuration file for specific features or tools
- File is a report or generated data file

<!-- section_id: "7f4a3217-dfdf-43b7-9281-d9ffa76a4476" -->
## 📊 Organization Results

<!-- section_id: "bd502e3a-2d70-48f4-a112-3c2fac844c22" -->
### **Before Organization:**
- 43+ files scattered in root directory
- Mix of essential and non-essential files
- Difficult to identify core application files

<!-- section_id: "ddd5b917-966b-4634-a627-87f1d13a5d6d" -->
### **After Organization:**
- **12 essential files** remain in root directory
- **40+ files** moved to organized trickle-down structure
- **Clear separation** between essential and organizational files
- **Easy identification** of core application components

<!-- section_id: "6241c621-dbfb-46d3-b51c-f1cbe5d8324d" -->
## 🔗 Related Documentation

- **Project Tools**: `../trickle_down_1.5_project_tools/0_instruction_docs/`
- **Feature Data**: `../trickle_down_2_features/0_instruction_docs/data/`
- **Documentation Protocol**: `../trickle_down_0_universal_instructions/0_instruction_docs/post-completion-documentation-protocol.md`

---

**Maintained By**: Project Organization System
**Last Updated**: 2025-01-23
**Next Review**: 2025-02-23
