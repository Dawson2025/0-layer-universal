---
resource_id: "a7b01228-9193-404a-925c-baff9d54f6fb"
resource_type: "document"
resource_name: "FIREBASE_SETUP"
---
# Firebase Setup Guide

Complete Firebase setup documentation for Lang Trak.

<!-- section_id: "ebefe9a6-db83-4cdc-a18b-7f18b23438e3" -->
## Quick Links

- [Quick Start Guide](QUICK_START.md) - Get up and running in 5 minutes
- [Development Workflow](DEV_WORKFLOW.md) - Daily development commands
- [Production Readiness](PRODUCTION_READINESS.md) - Deployment procedures
- [Best Practices](GOOGLE_FIREBASE_BEST_PRACTICES.md) - Google's recommendations
- [Operational Status](OPERATIONAL_STATUS.md) - Current system status

<!-- section_id: "4f29eb98-ff31-4ff1-9d6b-0ef6bfcf4b7e" -->
## Firebase Environment Setup

This project uses Google's recommended Firebase best practices with:
- **Emulators for unit testing only** (fast, free, isolated)
- **Real Firebase projects** for development, staging, and production

<!-- section_id: "caafefa7-aac0-47d3-89cf-b741c45a04fa" -->
### Environment Scripts (Run in WSL)



<!-- section_id: "094a810b-2a83-4e84-aecb-c7ba36b78b6f" -->
### Firebase Projects

| Environment | Project ID | Purpose |
|-------------|------------|---------|
| **Test** | Local emulator | Unit tests only |
| **Development** | lang-trak-dev | Daily development |
| **Staging** | lang-trak-staging | Pre-production testing |
| **Production** | lang-trak-prod | Live application |

<!-- section_id: "577a66c8-703d-4762-99ef-3c038f5ead9a" -->
## Documentation Structure

- **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
- **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Complete Firebase documentation (this file)
- **[DEV_WORKFLOW.md](DEV_WORKFLOW.md)** - Daily development workflow
- **[GOOGLE_FIREBASE_BEST_PRACTICES.md](GOOGLE_FIREBASE_BEST_PRACTICES.md)** - Architecture decisions
- **[PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)** - Deployment procedures
- **[OPERATIONAL_STATUS.md](OPERATIONAL_STATUS.md)** - System status

<!-- section_id: "b616b16e-76a4-4a85-90d8-7d4aabd81b7e" -->
## Getting Started

1. **New to the project?** Start with [QUICK_START.md](QUICK_START.md)
2. **Need detailed setup?** Read this document (FIREBASE_SETUP.md)
3. **Daily development?** Use [DEV_WORKFLOW.md](DEV_WORKFLOW.md)
4. **Deploying to production?** Follow [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)

---

**Status:** ✅ Fully Operational  
**Last Updated:** December 2024
