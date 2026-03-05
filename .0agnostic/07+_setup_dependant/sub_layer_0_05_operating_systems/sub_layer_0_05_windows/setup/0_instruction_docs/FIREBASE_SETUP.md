---
resource_id: "9b4b839b-d0af-4731-8599-bcfcaef9e338"
resource_type: "document"
resource_name: "FIREBASE_SETUP"
---
# Firebase Setup Guide

Complete Firebase setup documentation for Lang Trak.

<!-- section_id: "1937b4e4-6943-46d3-a65b-36a53236cef9" -->
## Quick Links

- [Quick Start Guide](QUICK_START.md) - Get up and running in 5 minutes
- [Development Workflow](DEV_WORKFLOW.md) - Daily development commands
- [Production Readiness](PRODUCTION_READINESS.md) - Deployment procedures
- [Best Practices](GOOGLE_FIREBASE_BEST_PRACTICES.md) - Google's recommendations
- [Operational Status](OPERATIONAL_STATUS.md) - Current system status

<!-- section_id: "05a3cac7-d717-4375-ab1f-cabfe53117b2" -->
## Firebase Environment Setup

This project uses Google's recommended Firebase best practices with:
- **Emulators for unit testing only** (fast, free, isolated)
- **Real Firebase projects** for development, staging, and production

<!-- section_id: "d9d80712-aaf9-4cb3-a4b0-ba7db2421b4e" -->
### Environment Scripts (Run in WSL)



<!-- section_id: "ac7ceb26-72fc-4ecd-a7aa-16b18f5d1b41" -->
### Firebase Projects

| Environment | Project ID | Purpose |
|-------------|------------|---------|
| **Test** | Local emulator | Unit tests only |
| **Development** | lang-trak-dev | Daily development |
| **Staging** | lang-trak-staging | Pre-production testing |
| **Production** | lang-trak-prod | Live application |

<!-- section_id: "0f0d8bbf-8fc4-47b6-a4ae-b91fa62d1bc6" -->
## Documentation Structure

- **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
- **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Complete Firebase documentation (this file)
- **[DEV_WORKFLOW.md](DEV_WORKFLOW.md)** - Daily development workflow
- **[GOOGLE_FIREBASE_BEST_PRACTICES.md](GOOGLE_FIREBASE_BEST_PRACTICES.md)** - Architecture decisions
- **[PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)** - Deployment procedures
- **[OPERATIONAL_STATUS.md](OPERATIONAL_STATUS.md)** - System status

<!-- section_id: "57842558-8585-41c0-8d27-0d6ed50ff6e2" -->
## Getting Started

1. **New to the project?** Start with [QUICK_START.md](QUICK_START.md)
2. **Need detailed setup?** Read this document (FIREBASE_SETUP.md)
3. **Daily development?** Use [DEV_WORKFLOW.md](DEV_WORKFLOW.md)
4. **Deploying to production?** Follow [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)

---

**Status:** ✅ Fully Operational  
**Last Updated:** December 2024
