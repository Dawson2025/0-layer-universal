---
resource_id: "53180cdc-1276-4525-80a1-be8a87c922da"
resource_type: "document"
resource_name: "ENVIRONMENTS_AND_INTEGRATIONS"
---
# Project Environments and Integrations
**Project**: I-Eat University Food Delivery Platform
**Last Updated**: 2025-01-24
**Version**: 1.0

---

<!-- section_id: "5a455a84-e210-4e19-90f4-b2050565aaab" -->
## Overview

The I-Eat project operates across **4 distinct environments**, each serving a specific purpose in the development and deployment pipeline. Each environment has its own Supabase project and configuration for isolated testing and deployment.

---

<!-- section_id: "74fe2995-071a-45bb-ba42-5ca971b017f4" -->
## Environment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Development Pipeline                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Local Dev → Testing → Staging → Production                  │
│     ↓          ↓         ↓          ↓                        │
│  Vite Dev   i-eat-dev  i-eat-staging  i-eat-prod            │
│  (localhost)  (Supabase)  (Supabase)   (Supabase)           │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "34442ce7-db39-482a-9dca-9c66f3d02b04" -->
## 1. Local Development Environment

<!-- section_id: "f2c171eb-a689-4983-bb48-75033d7d89aa" -->
### Purpose
Fast, local development using Vite dev server with Supabase local development.

<!-- section_id: "00ee4f21-3abd-4fda-8677-4b9c8721c56f" -->
### Configuration
- **Vite Dev Server**: `localhost:5173` (default Vite port)
- **Supabase Local**: `localhost:54321` (Supabase CLI)
- **Database**: Local PostgreSQL via Supabase CLI
- **Storage**: Local file storage
- **Auth**: Local Supabase Auth

<!-- section_id: "94629760-a101-495d-8a2f-386a47ba5c7d" -->
### Use Cases
- Daily development work
- Rapid prototyping
- Component development
- Hot Module Replacement (HMR)
- Local testing

<!-- section_id: "efae0524-43d5-41f3-8f0e-2162b714b348" -->
### Running Locally
```bash
# Start Vite dev server
cd website
npm install
npm run dev

# Start Supabase locally (optional)
supabase start

# Run tests
npm run test
npm run test:e2e
```

<!-- section_id: "264663e5-6b0b-47ca-999f-8d3e37bc7c97" -->
### Advantages
- ✅ Fast HMR (~100ms updates)
- ✅ Free (no Supabase costs)
- ✅ Works offline
- ✅ Safe to experiment
- ✅ Real-time development feedback

<!-- section_id: "d02f6e37-6200-43b0-9157-27535e8beca6" -->
### Configuration Files
- `vite.config.js` - Vite configuration
- `supabase/config.toml` - Supabase local configuration
- `.env.local` - Local environment variables

---

<!-- section_id: "48d848f1-35fd-44b7-9a14-39afed863560" -->
## 2. Development/Testing Environment

<!-- section_id: "de79b7d8-a2f9-4b65-8fb3-a37fba2e6d99" -->
### Purpose
Real Supabase environment for testing features before staging deployment.

<!-- section_id: "f713cae1-9210-443e-8c86-d11ca06f3b4d" -->
### Configuration
- **Supabase Project**: `i-eat-dev`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-dev
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (Email/Password, Google, GitHub)
- **Storage**: Enabled for food images and documents
- **Edge Functions**: Available for custom logic

<!-- section_id: "f416e2c5-0c89-436b-8471-530c4e4f4b61" -->
### Credentials
- **API Keys**: Stored in environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "a1d9235e-511a-4df2-8746-11206dcb39ed" -->
### Use Cases
- Testing features against real Supabase
- Verifying Supabase integrations work
- Testing Row Level Security (RLS) policies
- Testing database functions and triggers
- Integration testing
- Pre-deployment verification

<!-- section_id: "86ad1e04-3a87-4df8-86dc-b1bced1dc441" -->
### Running Tests
```bash
# Run development tests
npm run test:dev

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e:dev
```

<!-- section_id: "2be90454-7455-4e33-a117-3ab1104114a5" -->
### What Gets Tested
- ✅ Supabase connection and access
- ✅ All tables (users, orders, restaurants, drivers, etc.)
- ✅ Full CRUD operations
- ✅ Row Level Security policies
- ✅ Authentication flows
- ✅ Real-time subscriptions
- ✅ Storage operations

<!-- section_id: "863f93e4-0db6-47d2-976c-37cfc637c96b" -->
### Deployment
```bash
# Deploy to development
npm run build
npm run deploy:dev

# Or use Vercel CLI
vercel --env=development
```

<!-- section_id: "4d0327e4-9115-4d5a-bf65-ce0376cb8ecb" -->
### Data Management
- **Test Data**: Can be freely created/deleted
- **Cleanup**: Automated via test fixtures
- **Persistent Data**: Should be marked with metadata to avoid deletion

<!-- section_id: "d8becc62-aaf4-433f-88e6-b77e5838c3de" -->
### Access Control
- **Developers**: Full read/write access
- **CI/CD**: Full read/write access via service role
- **Test Users**: Limited access via Supabase Auth

---

<!-- section_id: "e397b172-3887-4b32-bac0-762cb6446a08" -->
## 3. Staging Environment

<!-- section_id: "e6166032-dd5f-47d5-8bba-10d061cccf01" -->
### Purpose
Pre-production environment that mirrors production configuration for final testing before release.

<!-- section_id: "45f4d2a2-ac48-4511-aaeb-c597221c2681" -->
### Configuration
- **Supabase Project**: `i-eat-staging`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-staging
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (same as production)
- **Storage**: Enabled for food images and documents
- **Edge Functions**: Production-like configuration

<!-- section_id: "da677f06-8717-47ce-a270-0c4b8644cb3d" -->
### Credentials
- **API Keys**: Stored in environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "37b7863f-af88-47ac-bcc8-f581468cf350" -->
### Use Cases
- Final pre-production testing
- Testing deployment process
- Load testing
- Performance testing
- User acceptance testing (UAT)
- Testing production-like configurations

<!-- section_id: "c47e48a9-00aa-4b98-afaa-651d66326ce7" -->
### Running Tests
```bash
# Run staging tests
npm run test:staging

# Run E2E tests on staging
npm run test:e2e:staging
```

<!-- section_id: "eec68f94-7ee0-4116-88c1-7c66f5ddd7cd" -->
### What Gets Tested
- ✅ Basic connectivity
- ✅ All tables accessible
- ✅ CRUD operations
- ✅ Production-like RLS policies
- ✅ Performance benchmarks
- ✅ Real-time functionality

<!-- section_id: "7ac3bc5f-4f4a-4e54-93de-9786f40dd4f8" -->
### Deployment
```bash
# Deploy to staging environment
npm run build
npm run deploy:staging

# Or use Vercel CLI
vercel --env=staging
```

<!-- section_id: "7f1a143c-d03e-483f-9ea2-72066de15abb" -->
### Data Management
- **Test Data**: Should mirror production patterns
- **Cleanup**: Regular cleanup cycles
- **Retention**: Data older than 30 days can be purged

<!-- section_id: "87ff8951-7bbd-4acb-a1eb-04f96010269e" -->
### Access Control
- **Developers**: Limited access (read-only preferred)
- **QA Team**: Full testing access
- **CI/CD**: Full deployment access
- **Stakeholders**: Read-only access for review

<!-- section_id: "550df7a2-56d0-49c0-8bf9-38027e026a66" -->
### Setup Instructions
```bash
# 1. Create Supabase project (if not exists)
# Go to https://supabase.com/dashboard/
# Create project: i-eat-staging

# 2. Enable services
# - Database (PostgreSQL)
# - Authentication
# - Storage
# - Edge Functions (optional)

# 3. Configure environment variables
# Copy .env.example to .env.staging
# Add Supabase credentials

# 4. Deploy database schema
supabase db push --env=staging

# 5. Run verification tests
npm run test:staging
```

---

<!-- section_id: "1f185578-53c0-4589-ac5c-332cba0cd359" -->
## 4. Production Environment

<!-- section_id: "afb524ca-4007-4918-9400-74b07975b26d" -->
### Purpose
Live production environment serving real users.

<!-- section_id: "baf7e895-119e-460b-9aa9-3c2b0259d80d" -->
### Configuration
- **Supabase Project**: `i-eat-prod`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-prod
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (production security)
- **Storage**: Enabled (production bucket)
- **Edge Functions**: Production configuration

<!-- section_id: "cd3a9a57-6871-475d-847a-bd594319a368" -->
### Credentials
- **API Keys**: Stored in secure environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "f46ef3fb-198c-4af3-ac68-83a36513e147" -->
### Use Cases
- Live user data
- Production deployments
- Monitoring and health checks
- Read-only smoke tests

<!-- section_id: "c0195dcf-968e-4ac1-8892-c1df3be52f4b" -->
### Running Tests (READ-ONLY)
```bash
# Requires explicit confirmation flag
ALLOW_PROD_TESTS=yes_i_know_what_im_doing \
npm run test:prod:smoke
```

<!-- section_id: "df464f61-9313-452f-abce-e739cc8faab9" -->
### What Gets Tested (READ-ONLY)
- ✅ Supabase accessible
- ✅ All tables readable
- ✅ Queries functional
- ❌ NO writes
- ❌ NO deletes
- ❌ NO modifications

<!-- section_id: "f800adb4-cb60-47c4-b6ef-d3eacf8b41e4" -->
### Deployment
```bash
# Deploy to production (requires approval)
npm run build
npm run deploy:prod

# Or use Vercel CLI
vercel --prod
```

<!-- section_id: "9d1dc780-94d6-49ef-a6f1-eadedcafa02a" -->
### Data Management
- **User Data**: Protected, GDPR compliant
- **Backups**: Daily automated backups
- **Retention**: Per data retention policy
- **Cleanup**: Only via approved maintenance windows

<!-- section_id: "79a3112f-930b-412e-bf0d-10acd8011e8b" -->
### Access Control
- **Developers**: NO direct access (use staging)
- **Admins**: Read-only access via Supabase Dashboard
- **CI/CD**: Deployment access only (no data access)
- **Monitoring**: Read-only health check access

<!-- section_id: "e2ac9b2b-50e3-4a5b-8e46-26fd149e070a" -->
### Security
- **API Keys**: Minimal permissions (read-only if possible)
- **RLS Policies**: Strict production policies
- **API Keys**: Restricted by domain/IP
- **Audit Logging**: All access logged

---

<!-- section_id: "83e8fa1f-f67b-462e-a426-003e2f54972b" -->
## Integrations

<!-- section_id: "214b15ed-431a-4163-9905-fd590cb80bf6" -->
### Supabase Services

#### PostgreSQL Database
- **Purpose**: Primary database for all app data
- **Tables**:
  - `users` - User profiles and authentication
  - `restaurants` - Food vendor information
  - `menu_items` - Food items and pricing
  - `orders` - Order management
  - `order_items` - Individual order items
  - `deliveries` - Delivery tracking
  - `drivers` - Driver profiles and status
  - `points` - Points system and transactions
  - `campus_locations` - University building/room data

#### Supabase Authentication
- **Providers**:
  - Email/Password
  - Google Sign-In
  - GitHub (for developers)
  - (Future: Apple, Microsoft)
- **Authorized Domains**:
  - Development: `localhost`, `127.0.0.1`
  - Staging: `i-eat-staging.vercel.app`
  - Production: `i-eat.app`

#### Supabase Storage
- **Purpose**: Media file storage
- **Buckets**:
  - `food-images` - Restaurant and menu item photos
  - `user-uploads` - Profile pictures and documents
  - `driver-documents` - Driver verification documents
- **Security**: Row Level Security (RLS) policies

#### Supabase Edge Functions
- **Purpose**: Serverless functions for custom logic
- **Use Cases**:
  - Order processing
  - Payment processing
  - Real-time notifications
  - Points calculations

<!-- section_id: "e0452569-fae9-4b25-b131-eef18affeb72" -->
### External Integrations

#### Payment Processing
- **Service**: Stripe
- **Purpose**: Handle payments and points redemption
- **Configuration**: Webhook endpoints for order updates

#### Maps and Location Services
- **Service**: Google Maps API / Mapbox
- **Purpose**: Campus navigation and delivery tracking
- **Features**: Geocoding, directions, real-time tracking

#### Push Notifications
- **Service**: Expo Notifications / Firebase Cloud Messaging
- **Purpose**: Real-time order updates and delivery notifications
- **Platforms**: iOS, Android, Web

#### Email Services
- **Service**: SendGrid / Resend
- **Purpose**: Order confirmations, password resets, notifications
- **Templates**: Order confirmations, delivery updates

<!-- section_id: "5d20192e-25b6-4c32-8656-f3857f707185" -->
### Development Tools

#### Testing Framework
- **Jest**: Unit testing
- **React Testing Library**: Component testing
- **Playwright**: E2E testing
- **Coverage**: Test coverage reporting

#### CI/CD
- **GitHub Actions**: Automated testing and deployment
- **Vercel**: Frontend deployment
- **Supabase**: Database migrations and deployments

---

<!-- section_id: "0221331b-94bd-4944-af0a-6ee0806d8e75" -->
## Environment Variables

<!-- section_id: "5b727887-deff-4c76-be5a-8c30d914b524" -->
### Development
```bash
VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-maps-key
```

<!-- section_id: "d884e207-107e-44af-927c-57d9bbc3e18b" -->
### Staging
```bash
VITE_SUPABASE_URL=your-staging-supabase-url
VITE_SUPABASE_ANON_KEY=your-staging-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-staging-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-maps-key
```

<!-- section_id: "f9b92da7-5472-40d9-8af3-68ce3d7ffcd1" -->
### Production
```bash
VITE_SUPABASE_URL=your-prod-supabase-url
VITE_SUPABASE_ANON_KEY=your-prod-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-prod-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-prod-maps-key
```

---

<!-- section_id: "560db836-8cfb-4352-8638-6e2a40f24fff" -->
## Configuration Files

<!-- section_id: "4d5d4b23-c79e-404a-91e1-edcc92d9bb36" -->
### Project Root
- `vite.config.js` - Vite configuration
- `supabase/config.toml` - Supabase configuration
- `.env.example` - Environment variables template
- `package.json` - Dependencies and scripts

<!-- section_id: "fc30aa35-682f-4737-ae56-344b013f057a" -->
### Supabase Configuration
- `supabase/migrations/` - Database migrations
- `supabase/seed.sql` - Seed data
- `supabase/functions/` - Edge functions

---

<!-- section_id: "76912a14-d4e9-4da4-b4f7-1c8ee54098d0" -->
## Testing Strategy by Environment

| Environment | Tests | Duration | When to Run | Write Operations |
|-------------|-------|----------|-------------|------------------|
| **Local (Vite)** | Unit + Integration | ~30s | Every commit | ✅ Allowed |
| **Development** | Full test suite | ~2min | Weekly, pre-deploy | ✅ Allowed |
| **Staging** | E2E tests | ~5min | Before production deploy | ✅ Allowed (test data) |
| **Production** | Smoke tests | ~1min | After production deploy | ❌ READ-ONLY |

---

<!-- section_id: "d72ec4f2-bd42-4d8e-b280-be85fb588e0d" -->
## Deployment Pipeline

<!-- section_id: "5c2a28c5-f628-4915-80a6-91d635883803" -->
### Standard Flow
```
1. Develop → Local (Vite dev server)
   ├── Run unit tests
   └── Verify locally

2. Commit → Development
   ├── CI runs tests
   ├── Merge to main
   └── Deploy to development

3. Test → Staging
   ├── Deploy to staging
   ├── Run E2E tests
   └── UAT verification

4. Release → Production
   ├── Create release tag
   ├── Run full test suite
   ├── Deploy to production
   └── Run smoke tests
```

---

<!-- section_id: "cf7cca9c-8b56-40c1-b9d7-ed1bfabe306d" -->
## Quick Reference

<!-- section_id: "0dfb4ddd-81ae-4622-b3a2-dbbfd4184047" -->
### Daily Development
```bash
# Start development server
cd website
npm run dev

# Run tests
npm run test
npm run test:e2e
```

<!-- section_id: "379822f8-7219-4c04-ab05-869bdd17b3a9" -->
### Pre-Deployment
```bash
# Deploy to staging
npm run deploy:staging

# Test staging
npm run test:staging
```

<!-- section_id: "41d9510a-5af4-4da0-89d4-e97e58760cf9" -->
### Production Deployment
```bash
# Deploy to production (after staging approval)
npm run deploy:prod

# Verify production health
npm run test:prod:smoke
```

---

<!-- section_id: "31d9d10e-16b2-46a0-9e50-c2e3a4b93325" -->
## Next Steps

<!-- section_id: "ed76fb25-38f8-4231-8161-3b9d721a66cf" -->
### Immediate (Needs Setup)
- 🔄 Create Supabase projects for all environments
- 🔄 Configure environment variables
- 🔄 Set up Vercel deployment
- 🔄 Configure Stripe integration

<!-- section_id: "dc891c70-cac0-4206-bcd6-4d3f0be7ba25" -->
### Before Production
- 🔄 Set up monitoring and alerts
- 🔄 Configure backup strategy
- 🔄 Implement security policies
- 🔄 Set up CI/CD pipeline

---

<!-- section_id: "6dd24838-1e3e-46cf-a45b-ad4916ecdec4" -->
## Related Documentation

- **Project Constitution**: `constitution.md`
- **Quick Start Guide**: `QUICK_START.md`
- **Testing Guide**: `../README_TESTING.md`
- **Feature Documentation**: `../trickle_down_2_features/`

---

**For Questions or Issues**: See project documentation or contact project maintainers.
