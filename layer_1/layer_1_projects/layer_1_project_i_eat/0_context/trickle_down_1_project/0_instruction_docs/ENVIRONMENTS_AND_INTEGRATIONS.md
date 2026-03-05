---
resource_id: "0bf48321-e3a4-4b96-855f-223d78872a5e"
resource_type: "document"
resource_name: "ENVIRONMENTS_AND_INTEGRATIONS"
---
# Project Environments and Integrations
**Project**: I-Eat University Food Delivery Platform
**Last Updated**: 2025-01-24
**Version**: 1.0

---

<!-- section_id: "1c326cd9-085a-43d7-b2f1-d70048ce7c89" -->
## Overview

The I-Eat project operates across **4 distinct environments**, each serving a specific purpose in the development and deployment pipeline. Each environment has its own Supabase project and configuration for isolated testing and deployment.

---

<!-- section_id: "728aed5a-6060-4286-bf38-8b92622702fc" -->
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

<!-- section_id: "9f9e4c60-2679-4004-9cb1-b0165e493919" -->
## 1. Local Development Environment

<!-- section_id: "0f34549a-14b6-45c6-bb7b-47cabff6f374" -->
### Purpose
Fast, local development using Vite dev server with Supabase local development.

<!-- section_id: "6a44b577-31eb-42cb-806d-8bfca91df599" -->
### Configuration
- **Vite Dev Server**: `localhost:5173` (default Vite port)
- **Supabase Local**: `localhost:54321` (Supabase CLI)
- **Database**: Local PostgreSQL via Supabase CLI
- **Storage**: Local file storage
- **Auth**: Local Supabase Auth

<!-- section_id: "d6eef14a-693a-4059-ba17-4a9d9e25dcf4" -->
### Use Cases
- Daily development work
- Rapid prototyping
- Component development
- Hot Module Replacement (HMR)
- Local testing

<!-- section_id: "99a38d65-9fd9-4da0-a149-01aeccd324e8" -->
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

<!-- section_id: "f12965f3-1420-4039-9f0b-13717da61076" -->
### Advantages
- ✅ Fast HMR (~100ms updates)
- ✅ Free (no Supabase costs)
- ✅ Works offline
- ✅ Safe to experiment
- ✅ Real-time development feedback

<!-- section_id: "59e65a6a-8962-4083-86b2-304c8fad48c4" -->
### Configuration Files
- `vite.config.js` - Vite configuration
- `supabase/config.toml` - Supabase local configuration
- `.env.local` - Local environment variables

---

<!-- section_id: "df617cc5-dd6c-4611-9375-b4b672999f0a" -->
## 2. Development/Testing Environment

<!-- section_id: "6b867b55-4c73-4b0c-83c8-a433f7df120d" -->
### Purpose
Real Supabase environment for testing features before staging deployment.

<!-- section_id: "fb372bc3-b0c2-4f74-b6ba-8d25b4542b1d" -->
### Configuration
- **Supabase Project**: `i-eat-dev`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-dev
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (Email/Password, Google, GitHub)
- **Storage**: Enabled for food images and documents
- **Edge Functions**: Available for custom logic

<!-- section_id: "38bbe77f-1a00-4083-8b3e-79231d337c43" -->
### Credentials
- **API Keys**: Stored in environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "afc36b98-fcfd-4d86-86cf-4955bd866af1" -->
### Use Cases
- Testing features against real Supabase
- Verifying Supabase integrations work
- Testing Row Level Security (RLS) policies
- Testing database functions and triggers
- Integration testing
- Pre-deployment verification

<!-- section_id: "608cd1dd-287f-4aef-bdc7-7dc585a18b7e" -->
### Running Tests
```bash
# Run development tests
npm run test:dev

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e:dev
```

<!-- section_id: "c160678f-543e-4020-8b4b-33c67ad28cc0" -->
### What Gets Tested
- ✅ Supabase connection and access
- ✅ All tables (users, orders, restaurants, drivers, etc.)
- ✅ Full CRUD operations
- ✅ Row Level Security policies
- ✅ Authentication flows
- ✅ Real-time subscriptions
- ✅ Storage operations

<!-- section_id: "ee989e3c-975c-4145-b35f-6067f8cad94a" -->
### Deployment
```bash
# Deploy to development
npm run build
npm run deploy:dev

# Or use Vercel CLI
vercel --env=development
```

<!-- section_id: "12e5731f-6761-4999-b998-1e80f181a0f6" -->
### Data Management
- **Test Data**: Can be freely created/deleted
- **Cleanup**: Automated via test fixtures
- **Persistent Data**: Should be marked with metadata to avoid deletion

<!-- section_id: "48fbe4e4-9606-41a5-9108-668c6353c1cc" -->
### Access Control
- **Developers**: Full read/write access
- **CI/CD**: Full read/write access via service role
- **Test Users**: Limited access via Supabase Auth

---

<!-- section_id: "c5472135-3522-4c4c-ad5b-6833f8fcea39" -->
## 3. Staging Environment

<!-- section_id: "ec74235a-cde6-445e-8d3d-51f8000dc9a5" -->
### Purpose
Pre-production environment that mirrors production configuration for final testing before release.

<!-- section_id: "5bdaa546-7662-4542-ac40-21a89abc8c89" -->
### Configuration
- **Supabase Project**: `i-eat-staging`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-staging
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (same as production)
- **Storage**: Enabled for food images and documents
- **Edge Functions**: Production-like configuration

<!-- section_id: "0d89c942-bf2b-4a74-81b8-f22572feaef2" -->
### Credentials
- **API Keys**: Stored in environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "efb5c732-be17-475d-afe0-1c395816e537" -->
### Use Cases
- Final pre-production testing
- Testing deployment process
- Load testing
- Performance testing
- User acceptance testing (UAT)
- Testing production-like configurations

<!-- section_id: "3eb169ec-60fb-4b3a-9f70-c5de40830ce1" -->
### Running Tests
```bash
# Run staging tests
npm run test:staging

# Run E2E tests on staging
npm run test:e2e:staging
```

<!-- section_id: "72eb3ad9-5391-4b48-8ec7-d4c72a838931" -->
### What Gets Tested
- ✅ Basic connectivity
- ✅ All tables accessible
- ✅ CRUD operations
- ✅ Production-like RLS policies
- ✅ Performance benchmarks
- ✅ Real-time functionality

<!-- section_id: "025cce3f-b3b8-4abe-9d58-76767ab3bb79" -->
### Deployment
```bash
# Deploy to staging environment
npm run build
npm run deploy:staging

# Or use Vercel CLI
vercel --env=staging
```

<!-- section_id: "346d95af-7f19-4539-afc7-2895a8aae8ec" -->
### Data Management
- **Test Data**: Should mirror production patterns
- **Cleanup**: Regular cleanup cycles
- **Retention**: Data older than 30 days can be purged

<!-- section_id: "d22fc922-cd96-4640-b8a4-b3d07d6f439d" -->
### Access Control
- **Developers**: Limited access (read-only preferred)
- **QA Team**: Full testing access
- **CI/CD**: Full deployment access
- **Stakeholders**: Read-only access for review

<!-- section_id: "ebcfde96-19e1-4c67-878d-9bdd2502c83c" -->
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

<!-- section_id: "ca0b88f3-b098-48f8-aeff-083101f100e9" -->
## 4. Production Environment

<!-- section_id: "be18413d-c44f-4ac2-9c39-3a711d4f0f8e" -->
### Purpose
Live production environment serving real users.

<!-- section_id: "51ce2ad7-0a08-4cfe-9aa4-c1818dabf7da" -->
### Configuration
- **Supabase Project**: `i-eat-prod`
- **Project URL**: https://supabase.com/dashboard/project/i-eat-prod
- **Database**: PostgreSQL (Supabase managed)
- **Authentication**: Enabled (production security)
- **Storage**: Enabled (production bucket)
- **Edge Functions**: Production configuration

<!-- section_id: "bfb11d33-9a16-4d6d-b028-5876374ea9ca" -->
### Credentials
- **API Keys**: Stored in secure environment variables
- **Database URL**: `postgresql://...` (from Supabase dashboard)
- **Anon Key**: Public API key for client-side
- **Service Role Key**: Server-side operations

<!-- section_id: "e67bf417-b0f4-4d99-b3c8-73acac274e15" -->
### Use Cases
- Live user data
- Production deployments
- Monitoring and health checks
- Read-only smoke tests

<!-- section_id: "a5163063-22af-4f29-95ce-bd7782acd741" -->
### Running Tests (READ-ONLY)
```bash
# Requires explicit confirmation flag
ALLOW_PROD_TESTS=yes_i_know_what_im_doing \
npm run test:prod:smoke
```

<!-- section_id: "e508c899-f62b-40a6-9b9e-f71a667f073f" -->
### What Gets Tested (READ-ONLY)
- ✅ Supabase accessible
- ✅ All tables readable
- ✅ Queries functional
- ❌ NO writes
- ❌ NO deletes
- ❌ NO modifications

<!-- section_id: "76bbb100-87ce-42a4-add2-2b83d6ad5433" -->
### Deployment
```bash
# Deploy to production (requires approval)
npm run build
npm run deploy:prod

# Or use Vercel CLI
vercel --prod
```

<!-- section_id: "3426e962-7c20-4cc5-80c7-a032f211e716" -->
### Data Management
- **User Data**: Protected, GDPR compliant
- **Backups**: Daily automated backups
- **Retention**: Per data retention policy
- **Cleanup**: Only via approved maintenance windows

<!-- section_id: "b1cea641-3773-414a-9dd7-66770186a039" -->
### Access Control
- **Developers**: NO direct access (use staging)
- **Admins**: Read-only access via Supabase Dashboard
- **CI/CD**: Deployment access only (no data access)
- **Monitoring**: Read-only health check access

<!-- section_id: "b15a7990-9f94-4af2-bb1a-73ae799c2e5b" -->
### Security
- **API Keys**: Minimal permissions (read-only if possible)
- **RLS Policies**: Strict production policies
- **API Keys**: Restricted by domain/IP
- **Audit Logging**: All access logged

---

<!-- section_id: "8d915d54-0db0-4822-99d0-9411d300efa4" -->
## Integrations

<!-- section_id: "5199117d-e352-4558-ba41-a5c22822b99f" -->
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

<!-- section_id: "e280adbf-28cb-4d8e-a36c-46db1b5bee6d" -->
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

<!-- section_id: "deec3e81-34cb-4174-9671-49a159d73033" -->
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

<!-- section_id: "511cf594-4e69-4e65-b3b0-57b82508c48b" -->
## Environment Variables

<!-- section_id: "b15e0bfd-91bc-4c3a-b77e-8e09c10b1722" -->
### Development
```bash
VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-maps-key
```

<!-- section_id: "9eff10ff-07b2-4df9-b1af-975d324a0d6c" -->
### Staging
```bash
VITE_SUPABASE_URL=your-staging-supabase-url
VITE_SUPABASE_ANON_KEY=your-staging-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-staging-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-maps-key
```

<!-- section_id: "c9cbe268-7ec1-48c1-9b9c-3f74c054261b" -->
### Production
```bash
VITE_SUPABASE_URL=your-prod-supabase-url
VITE_SUPABASE_ANON_KEY=your-prod-anon-key
VITE_STRIPE_PUBLISHABLE_KEY=your-prod-stripe-key
VITE_GOOGLE_MAPS_API_KEY=your-prod-maps-key
```

---

<!-- section_id: "1cedecee-4ab5-4c85-be76-ea3f9b0e3ead" -->
## Configuration Files

<!-- section_id: "e471e46e-9749-4955-b5a3-bd4008ac2436" -->
### Project Root
- `vite.config.js` - Vite configuration
- `supabase/config.toml` - Supabase configuration
- `.env.example` - Environment variables template
- `package.json` - Dependencies and scripts

<!-- section_id: "968fae92-58db-456f-b3d7-eae800722e41" -->
### Supabase Configuration
- `supabase/migrations/` - Database migrations
- `supabase/seed.sql` - Seed data
- `supabase/functions/` - Edge functions

---

<!-- section_id: "b498e7e4-6630-4496-af31-35578e4cab07" -->
## Testing Strategy by Environment

| Environment | Tests | Duration | When to Run | Write Operations |
|-------------|-------|----------|-------------|------------------|
| **Local (Vite)** | Unit + Integration | ~30s | Every commit | ✅ Allowed |
| **Development** | Full test suite | ~2min | Weekly, pre-deploy | ✅ Allowed |
| **Staging** | E2E tests | ~5min | Before production deploy | ✅ Allowed (test data) |
| **Production** | Smoke tests | ~1min | After production deploy | ❌ READ-ONLY |

---

<!-- section_id: "7cfe81ed-4df9-48a3-98f9-dffc4ca5fa40" -->
## Deployment Pipeline

<!-- section_id: "17d9920e-147b-4e3f-9796-2d3da394ed3d" -->
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

<!-- section_id: "9c53d74d-26ad-4258-b0bb-24d169dbfd84" -->
## Quick Reference

<!-- section_id: "6c1a6a5c-aa30-46ed-8f11-b5d02a7087fe" -->
### Daily Development
```bash
# Start development server
cd website
npm run dev

# Run tests
npm run test
npm run test:e2e
```

<!-- section_id: "f5e275ff-29c4-4940-8ba7-a475b475f197" -->
### Pre-Deployment
```bash
# Deploy to staging
npm run deploy:staging

# Test staging
npm run test:staging
```

<!-- section_id: "fda3b058-226f-42d7-bb34-c50e89c1ab0b" -->
### Production Deployment
```bash
# Deploy to production (after staging approval)
npm run deploy:prod

# Verify production health
npm run test:prod:smoke
```

---

<!-- section_id: "eda61498-cba6-4287-8c44-4754cc6fd292" -->
## Next Steps

<!-- section_id: "108b490e-41fc-477a-b919-3a5a0c8d6df5" -->
### Immediate (Needs Setup)
- 🔄 Create Supabase projects for all environments
- 🔄 Configure environment variables
- 🔄 Set up Vercel deployment
- 🔄 Configure Stripe integration

<!-- section_id: "94626bae-9a63-4dc5-bbdd-9b6568588231" -->
### Before Production
- 🔄 Set up monitoring and alerts
- 🔄 Configure backup strategy
- 🔄 Implement security policies
- 🔄 Set up CI/CD pipeline

---

<!-- section_id: "223e8ba8-953c-4074-8080-9c8eed379d4c" -->
## Related Documentation

- **Project Constitution**: `constitution.md`
- **Quick Start Guide**: `QUICK_START.md`
- **Testing Guide**: `../README_TESTING.md`
- **Feature Documentation**: `../trickle_down_2_features/`

---

**For Questions or Issues**: See project documentation or contact project maintainers.
