---
resource_id: "8c7e7dd8-f319-44a4-9ce0-39771a852f68"
resource_type: "document"
resource_name: "FIREBASE_SETUP"
---
# Firebase Setup Guide

Complete Firebase setup documentation for Lang Trak.

<!-- section_id: "564a67db-609b-487a-94c5-c0960aca5bb4" -->
## Quick Links

- [Quick Start Guide](QUICK_START.md) - Get up and running in 5 minutes
- [Development Workflow](DEV_WORKFLOW.md) - Daily development commands
- [Production Readiness](PRODUCTION_READINESS.md) - Deployment procedures
- [Best Practices](GOOGLE_FIREBASE_BEST_PRACTICES.md) - Google's recommendations
- [Operational Status](OPERATIONAL_STATUS.md) - Current system status

<!-- section_id: "f58bdffe-aacf-4fff-a095-c600e143d743" -->
## Firebase Environment Setup

This project uses Google's recommended Firebase best practices with:
- **Emulators for unit testing only** (fast, free, isolated)
- **Real Firebase projects** for development, staging, and production

<!-- section_id: "a92a467e-776f-47a9-b723-3c77cf3249e1" -->
### Environment Scripts (Run in WSL)



<!-- section_id: "cda3618b-c373-4c92-a06b-53e2e4c4de93" -->
### Firebase Projects

| Environment | Project ID | Purpose |
|-------------|------------|---------|
| **Test** | Local emulator | Unit tests only |
| **Development** | lang-trak-dev | Daily development |
| **Staging** | lang-trak-staging | Pre-production testing |
| **Production** | lang-trak-prod | Live application |

<!-- section_id: "ffa01c4b-9600-42ee-80e0-ba2050f7a6df" -->
## Documentation Structure

- **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
- **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Complete Firebase documentation (this file)
- **[DEV_WORKFLOW.md](DEV_WORKFLOW.md)** - Daily development workflow
- **[GOOGLE_FIREBASE_BEST_PRACTICES.md](GOOGLE_FIREBASE_BEST_PRACTICES.md)** - Architecture decisions
- **[PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)** - Deployment procedures
- **[OPERATIONAL_STATUS.md](OPERATIONAL_STATUS.md)** - System status

<!-- section_id: "0e5c6229-7541-485c-b707-0e91e28f00a3" -->
## Getting Started

1. **New to the project?** Start with [QUICK_START.md](QUICK_START.md)
2. **Need detailed setup?** Read this document (FIREBASE_SETUP.md)
3. **Daily development?** Use [DEV_WORKFLOW.md](DEV_WORKFLOW.md)
4. **Deploying to production?** Follow [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)

---

**Status:** ✅ Fully Operational  
**Last Updated:** December 2024
