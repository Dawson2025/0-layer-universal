---
resource_id: "bc1c2c95-70c9-4a54-af23-3ddbc1321740"
resource_type: "document"
resource_name: "ENVIRONMENTS_AND_INTEGRATIONS"
---
# Project Environments and Integrations
**Project**: I-Eat University Food Delivery Platform
**Last Updated**: 2025-01-24
**Version**: 1.0

---

<!-- section_id: "44ecd61b-cc56-4a65-a653-f73ccd114afd" -->
## Overview

The I-Eat project operates across **4 distinct environments**, each serving a specific purpose in the development and deployment pipeline. Each environment has its own Supabase project and configuration for isolated testing and deployment.

---

<!-- section_id: "30fe660d-d4c1-42e6-984d-25272650854c" -->
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

<!-- section_id: "7b2dc8a4-3ae1-4157-8789-992346497a5c" -->
## 1. Local Development Environment

<!-- section_id: "75ee828d-2588-452f-a973-8dafcc486e9c" -->
### Purpose
Fast, local development using Vite dev server with Supabase local development.

<!-- section_id: "47d07a36-6c5e-4b06-af89-d1a1c99f35f5" -->
### Configuration
- **Vite Dev Server**: `localhost:5173` (default Vite port)
- **Supabase Local**: `localhost:54321` (Supabase CLI)
- **Database**: Local PostgreSQL via Supabase CLI
- **Storage**: Local file storage
- **Auth**: Local Supabase Auth

<!-- section_id: "1109586a-b196-49a6-9339-64d17c8dcdfd" -->
### Use Cases
- Daily development work
- Rapid prototyping
- Component development
- Hot Module Replacement (HMR)
- Local testing

<!-- section_id: "a93792ce-8ef2-4aea-a7e8-0c5a39a7f798" -->
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

<!-- section_id: "36572cdd-1bf8-43e1-8235-ab3eb334aab6" -->
### Advantages
- ✅ Fast HMR (~100ms updates)
- ✅ Free (no Supabase costs)
- ✅ Works offline
- ✅ Safe to experiment
- ✅ Real-time development feedback

<!-- section_id: "06b988aa-07a9-4fd7-b44f-b36a87d18585" -->
### Configuration Files
- `vite.config.js` - Vite configuration
- `supabase/config.toml` - Supabase local configuration
- `.env.local` - Local environment variables

---

<!-- section_id: "5fc96eb2-824c-465e-a3be-ba6985193d14" -->
## 2. Development/Testing Environment

<!-- section_id: "f94cdc4a-6c55-472f-b8a6-dc506427e177" -->
### Purpose
Real Supabase environment for testing features before staging deployment.

<!-- section_id: "99e61a79-d81b-4cce-af55-c55766bf7205" -->
### Configuration
- **Supabase Project**: `i-eat-dev`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-dev
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (Email/Password, Google, GitHub)
- **Storage**: Enabled for food images and documents
- **Edge Functions**: Available for custom logic

<!-- section_id: "f6bc5b86-c813-41d8-bc9a-9d03bf6ae8e3" -->
### Credentials
- **API Keys**: Stored in environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "886439f1-aa8c-4285-8eea-ef0ad07625ab" -->
### Use Cases
- Testing features against real Supabase
- Verifying Supabase integrations work
- Testing Row Level Security (RLS) policies
- Testing database functions and triggers
- Integration testing
- Pre-deployment verification

<!-- section_id: "0b550cf6-a8ad-411c-bc10-73cfcea43f95" -->
### Running Tests
```bash
# Run development tests
npm run test:dev

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e:dev
```

<!-- section_id: "7bfdeb52-b655-4864-85be-e7419892e1f6" -->
### What Gets Tested
- ✅ Supabase connection and access
- ✅ All tables (users, orders, restaurants, drivers, etc.)
- ✅ Full CRUD operations
- ✅ Row Level Security policies
- ✅ Authentication flows
- ✅ Real-time subscriptions
- ✅ Storage operations

<!-- section_id: "e591e042-9d0d-49ad-849c-95c840654467" -->
### Deployment
```bash
# Deploy to development
npm run build
npm run deploy:dev

# Or use Vercel CLI
vercel --env=development
```

<!-- section_id: "a2390154-2ce9-4ce7-9ec4-15d8a5b3f676" -->
### Data Management
- **Test Data**: Can be freely created/deleted
- **Cleanup**: Automated via test fixtures
- **Persistent Data**: Should be marked with metadata to avoid deletion

<!-- section_id: "4d0e15f8-3818-4015-9a24-d871e1180350" -->
### Access Control
- **Developers**: Full read/write access
- **CI/CD**: Full read/write access via service role
- **Test Users**: Limited access via Supabase Auth

---

<!-- section_id: "ec017dc8-dec6-44cb-bc47-bafdfb93938f" -->
## 3. Staging Environment

<!-- section_id: "afa46529-319d-49bd-bdb0-6e781ffd8df3" -->
### Purpose
Pre-production environment that mirrors production configuration for final testing before release.

<!-- section_id: "c12357c9-0323-49e5-b2cf-990928905240" -->
### Configuration
- **Supabase Project**: `i-eat-staging`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-staging
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (same as production)
- **Storage**: Enabled for food images and documents
- **Edge Functions**: Production-like configuration

<!-- section_id: "380f3d66-e83f-4838-9338-ac1ab10d3abd" -->
### Credentials
- **API Keys**: Stored in environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "7d2dfc6e-d314-40a6-8663-1e873f0ed84f" -->
### Use Cases
- Final pre-production testing
- Testing deployment process
- Load testing
- Performance testing
- User acceptance testing (UAT)
- Testing production-like configurations

<!-- section_id: "d8ac518d-9bd4-4206-9744-263aa853d320" -->
### Running Tests
```bash
# Run staging tests
npm run test:staging

# Run E2E tests on staging
npm run test:e2e:staging
```

<!-- section_id: "a253c5ad-af6e-4c48-8605-50c89b3e0bcf" -->
### What Gets Tested
- ✅ Basic connectivity
- ✅ All tables accessible
- ✅ CRUD operations
- ✅ Production-like RLS policies
- ✅ Performance benchmarks
- ✅ Real-time functionality

<!-- section_id: "c3c1f4eb-4e2f-438d-8534-8a50bb34b03a" -->
### Deployment
```bash
# Deploy to staging environment
npm run build
npm run deploy:staging

# Or use Vercel CLI
vercel --env=staging
```

<!-- section_id: "de1e6328-9c46-4eb8-9bc8-6b237b2aa34d" -->
### Data Management
- **Test Data**: Should mirror production patterns
- **Cleanup**: Regular cleanup cycles
- **Retention**: Data older than 30 days can be purged

<!-- section_id: "addfa8e8-3d88-4e2f-afb8-1fea78a1a496" -->
### Access Control
- **Developers**: Limited access (read-only preferred)
- **QA Team**: Full testing access
- **CI/CD**: Full deployment access
- **Stakeholders**: Read-only access for review

<!-- section_id: "a4b19abc-8c0a-4a12-a178-ad94becea0a5" -->
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

<!-- section_id: "eefec314-34de-4e0e-9401-ee106d11a6a4" -->
## 4. Production Environment

<!-- section_id: "920b5e9e-2cb4-43f8-976f-8bdc876273d8" -->
### Purpose
Live production environment serving real users.

<!-- section_id: "50870c9e-2826-44f0-8cee-09f99fddc636" -->
### Configuration
- **Supabase Project**: `i-eat-prod`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-prod
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (production security)
- **Storage**: Enabled (production bucket)
- **Edge Functions**: Production configuration

<!-- section_id: "842f9db1-f49c-42d8-95ce-769669eab33d" -->
### Credentials
- **API Keys**: Stored in secure environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "66ebc433-1df6-4a6d-b963-3c21b4b3088e" -->
### Use Cases
- Live user data
- Production deployments
- Monitoring and health checks
- Read-only smoke tests

<!-- section_id: "2d861558-fbc8-49cd-bb4c-0a0367cad366" -->
### Running Tests (READ-ONLY)
```bash
# Requires explicit confirmation flag
ALLOW_PROD_TESTS=yes_i_know_what_im_doing \
npm run test:prod:smoke
```

<!-- section_id: "620469fb-711a-4a53-b269-d2008ed5ef82" -->
### What Gets Tested (READ-ONLY)
- ✅ Supabase accessible
- ✅ All tables readable
- ✅ Queries functional
- ❌ NO writes
- ❌ NO deletes
- ❌ NO modifications

<!-- section_id: "281b10e7-7752-4deb-be33-754dc3c3ccd2" -->
### Deployment
```bash
# Deploy to production (requires approval)
npm run build
npm run deploy:prod

# Or use Vercel CLI
vercel --prod
```

<!-- section_id: "450e5102-fd74-473b-9ee2-d19230a90dcf" -->
### Data Management
- **User Data**: Protected, GDPR compliant
- **Backups**: Daily automated backups
- **Retention**: Per data retention policy
- **Cleanup**: Only via approved maintenance windows

<!-- section_id: "51df466f-5d56-4bd0-8456-14281f0ba3fe" -->
### Access Control
- **Developers**: NO direct access (use staging)
- **Admins**: Read-only access via Supabase Dashboard
- **CI/CD**: Deployment access only (no data access)
- **Monitoring**: Read-only health check access

<!-- section_id: "50564b48-1f53-438d-a6ab-53d79aa6f638" -->
### Security
- **API Keys**: Minimal permissions (read-only if possible)
- **RLS Policies**: Strict production policies
- **API Keys**: Restricted by domain/IP
- **Audit Logging**: All access logged

---

<!-- section_id: "7d24388b-8fca-4492-a854-bfab082aabe5" -->
## Integrations

<!-- section_id: "42f8da7c-59bd-4335-a6cd-7de014addf02" -->
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

<!-- section_id: "357cbd67-a404-4979-af4b-35c7cb57c5bd" -->
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

<!-- section_id: "0b464856-397d-4dcc-b805-4529dd57c355" -->
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

<!-- section_id: "8c9af22f-c63e-4e6a-a8e2-a7f67a360589" -->
## Environment Variables

<!-- section_id: "b15e603a-03ad-4371-8d45-86db93979122" -->
### Development
```bash
VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-maps-key
```

<!-- section_id: "9c964614-fdbb-4903-8c8f-5f900383414a" -->
### Staging
```bash
VITE_SUPABASE_URL=your-staging-supabase-url
VITE_SUPABASE_ANON_KEY=your-staging-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-staging-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-maps-key
```

<!-- section_id: "f91247ea-6bfa-424f-aa1f-fe2e8f7cf6f3" -->
### Production
```bash
VITE_SUPABASE_URL=your-prod-supabase-url
VITE_SUPABASE_ANON_KEY=your-prod-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-prod-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-prod-maps-key
```

---

<!-- section_id: "256fd9ef-d702-444c-93d2-c3d9298833ef" -->
## Configuration Files

<!-- section_id: "802566af-be31-4499-bfd7-7364140175af" -->
### Project Root
- `vite.config.js` - Vite configuration
- `supabase/config.toml` - Supabase configuration
- `.env.example` - Environment variables template
- `package.json` - Dependencies and scripts

<!-- section_id: "156f897d-3794-4ce6-bdd9-1b0a2a15b279" -->
### Supabase Configuration
- `supabase/migrations/` - Database migrations
- `supabase/seed.sql` - Seed data
- `supabase/functions/` - Edge functions

---

<!-- section_id: "277002cb-3fe4-42ab-add0-d5d0230b8f43" -->
## Testing Strategy by Environment

| Environment | Tests | Duration | When to Run | Write Operations |
|-------------|-------|----------|-------------|------------------|
| **Local (Vite)** | Unit + Integration | ~30s | Every commit | ✅ Allowed |
| **Development** | Full test suite | ~2min | Weekly, pre-deploy | ✅ Allowed |
| **Staging** | E2E tests | ~5min | Before production deploy | ✅ Allowed (test data) |
| **Production** | Smoke tests | ~1min | After production deploy | ❌ READ-ONLY |

---

<!-- section_id: "7b8555a0-411a-494e-aa4f-026d428520ab" -->
## Deployment Pipeline

<!-- section_id: "33d68709-efee-4006-a415-7c577c30a768" -->
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

<!-- section_id: "a4bac031-36d3-44f5-983c-7257d4f194b0" -->
## Quick Reference

<!-- section_id: "859c69c1-8f43-47c4-aae2-8416ce0042dd" -->
### Daily Development
```bash
# Start development server
cd website
npm run dev

# Run tests
npm run test
npm run test:e2e
```

<!-- section_id: "e5c292a0-e114-4754-b57d-18b68aec3de5" -->
### Pre-Deployment
```bash
# Deploy to staging
npm run deploy:staging

# Test staging
npm run test:staging
```

<!-- section_id: "7d14467d-a8f4-47ac-ab93-4d8ed94dd5e1" -->
### Production Deployment
```bash
# Deploy to production (after staging approval)
npm run deploy:prod

# Verify production health
npm run test:prod:smoke
```

---

<!-- section_id: "0bdb29ea-d84d-4fc1-ae90-1e5732da5075" -->
## Next Steps

<!-- section_id: "61823181-c118-4b17-9f45-4c503767d84a" -->
### Immediate (Needs Setup)
- 🔄 Create Supabase projects for all environments
- 🔄 Configure environment variables
- 🔄 Set up Vercel deployment
- 🔄 Configure Stripe integration

<!-- section_id: "bb82d971-66c4-4145-94c6-ffca8244bf88" -->
### Before Production
- 🔄 Set up monitoring and alerts
- 🔄 Configure backup strategy
- 🔄 Implement security policies
- 🔄 Set up CI/CD pipeline

---

<!-- section_id: "4885d98f-2758-49e1-8c1b-eaf4fcf2af4d" -->
## Related Documentation

- **Project Constitution**: `constitution.md`
- **Quick Start Guide**: `QUICK_START.md`
- **Testing Guide**: `../README_TESTING.md`
- **Feature Documentation**: `../trickle_down_2_features/`

---

**For Questions or Issues**: See project documentation or contact project maintainers.
