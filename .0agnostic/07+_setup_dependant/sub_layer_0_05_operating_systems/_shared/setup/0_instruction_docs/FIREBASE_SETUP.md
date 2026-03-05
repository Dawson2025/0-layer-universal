---
resource_id: "185ea669-2a75-4a44-bc12-24f3e6a8ccac"
resource_type: "document"
resource_name: "FIREBASE_SETUP"
---
# Firebase Setup Guide

Complete Firebase setup documentation for Lang Trak.

<!-- section_id: "f70f9121-cefa-4daa-a6bd-7db631e1d028" -->
## Quick Links

- [Quick Start Guide](QUICK_START.md) - Get up and running in 5 minutes
- [Development Workflow](DEV_WORKFLOW.md) - Daily development commands
- [Production Readiness](PRODUCTION_READINESS.md) - Deployment procedures
- [Best Practices](GOOGLE_FIREBASE_BEST_PRACTICES.md) - Google's recommendations
- [Operational Status](OPERATIONAL_STATUS.md) - Current system status

<!-- section_id: "4e38d809-16fb-4757-bf58-ebe5cc9f1424" -->
## Firebase Environment Setup

This project uses Google's recommended Firebase best practices with:
- **Emulators for unit testing only** (fast, free, isolated)
- **Real Firebase projects** for development, staging, and production

<!-- section_id: "eaa70307-ddbf-44ef-8bd5-d2604d524c5f" -->
### Environment Scripts (Run in WSL)



<!-- section_id: "5a70ffde-ddd3-424f-ac65-f9edf2a1a568" -->
### Firebase Projects

| Environment | Project ID | Purpose |
|-------------|------------|---------|
| **Test** | Local emulator | Unit tests only |
| **Development** | lang-trak-dev | Daily development |
| **Staging** | lang-trak-staging | Pre-production testing |
| **Production** | lang-trak-prod | Live application |

<!-- section_id: "6e25d19e-266c-40cb-a874-33239c903447" -->
## Documentation Structure

- **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
- **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Complete Firebase documentation (this file)
- **[DEV_WORKFLOW.md](DEV_WORKFLOW.md)** - Daily development workflow
- **[GOOGLE_FIREBASE_BEST_PRACTICES.md](GOOGLE_FIREBASE_BEST_PRACTICES.md)** - Architecture decisions
- **[PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)** - Deployment procedures
- **[OPERATIONAL_STATUS.md](OPERATIONAL_STATUS.md)** - System status

<!-- section_id: "34887d73-9112-42f8-b674-8afbd1f8a786" -->
## Getting Started

1. **New to the project?** Start with [QUICK_START.md](QUICK_START.md)
2. **Need detailed setup?** Read this document (FIREBASE_SETUP.md)
3. **Daily development?** Use [DEV_WORKFLOW.md](DEV_WORKFLOW.md)
4. **Deploying to production?** Follow [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)

---

**Status:** ✅ Fully Operational  
**Last Updated:** December 2024
