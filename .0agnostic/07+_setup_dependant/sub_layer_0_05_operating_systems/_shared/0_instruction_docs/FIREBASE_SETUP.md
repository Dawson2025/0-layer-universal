---
resource_id: "de3fea04-feda-4ede-8669-76b620a64eed"
resource_type: "document"
resource_name: "FIREBASE_SETUP"
---
# Firebase Setup Guide

Complete Firebase setup documentation for Lang Trak.

<!-- section_id: "d735e367-8f41-4a27-bde7-a4f65688619d" -->
## Quick Links

- [Quick Start Guide](QUICK_START.md) - Get up and running in 5 minutes
- [Development Workflow](DEV_WORKFLOW.md) - Daily development commands
- [Production Readiness](PRODUCTION_READINESS.md) - Deployment procedures
- [Best Practices](GOOGLE_FIREBASE_BEST_PRACTICES.md) - Google's recommendations
- [Operational Status](OPERATIONAL_STATUS.md) - Current system status

<!-- section_id: "ac930227-5ead-404c-97b0-1b48c3c13338" -->
## Firebase Environment Setup

This project uses Google's recommended Firebase best practices with:
- **Emulators for unit testing only** (fast, free, isolated)
- **Real Firebase projects** for development, staging, and production

<!-- section_id: "946ad3df-82e2-4349-87ed-94b2be85393f" -->
### Environment Scripts (Run in WSL)



<!-- section_id: "383279b2-02de-4378-825d-e8504ccc5abe" -->
### Firebase Projects

| Environment | Project ID | Purpose |
|-------------|------------|---------|
| **Test** | Local emulator | Unit tests only |
| **Development** | lang-trak-dev | Daily development |
| **Staging** | lang-trak-staging | Pre-production testing |
| **Production** | lang-trak-prod | Live application |

<!-- section_id: "a7065ea0-fe35-4608-92ad-3c6613ea547a" -->
## Documentation Structure

- **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
- **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Complete Firebase documentation (this file)
- **[DEV_WORKFLOW.md](DEV_WORKFLOW.md)** - Daily development workflow
- **[GOOGLE_FIREBASE_BEST_PRACTICES.md](GOOGLE_FIREBASE_BEST_PRACTICES.md)** - Architecture decisions
- **[PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)** - Deployment procedures
- **[OPERATIONAL_STATUS.md](OPERATIONAL_STATUS.md)** - System status

<!-- section_id: "15322a78-1f46-48de-a4cf-a794084ebcbc" -->
## Getting Started

1. **New to the project?** Start with [QUICK_START.md](QUICK_START.md)
2. **Need detailed setup?** Read this document (FIREBASE_SETUP.md)
3. **Daily development?** Use [DEV_WORKFLOW.md](DEV_WORKFLOW.md)
4. **Deploying to production?** Follow [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)

---

**Status:** ✅ Fully Operational  
**Last Updated:** December 2024
