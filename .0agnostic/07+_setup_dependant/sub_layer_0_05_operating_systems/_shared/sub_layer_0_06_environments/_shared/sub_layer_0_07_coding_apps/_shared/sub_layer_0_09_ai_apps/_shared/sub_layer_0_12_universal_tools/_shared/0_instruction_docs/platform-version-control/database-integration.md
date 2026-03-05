---
resource_id: "076762ec-217c-488e-a5a5-4c44a1622699"
resource_type: "document"
resource_name: "database-integration"
---
# Database Integration in Platform Version Control
*How Databases Fit into the Broader Platform Version Control System*

<!-- section_id: "5673b412-3ba8-44bc-8ea4-941539748ce2" -->
## Overview

Databases are a critical component of your application platform stack, but they don't exist in isolation. This guide explains how database version control integrates with your broader platform version control strategy.

<!-- section_id: "3e42ab51-353a-491a-8afa-67b400c58da4" -->
## Integration Points

<!-- section_id: "a05e83ad-a714-44cf-b90c-e3aad7d7551f" -->
### 1. Databases as Platform Components

Your database is just one platform in your stack:

```
Application Platforms Stack:
├── Hosting (Vercel, Netlify, Railway)
├── Databases (Supabase, Firebase, PostgreSQL) ← One component
├── Authentication (Auth0, Clerk)
├── Storage (S3, Cloud Storage)
├── CDN (Cloudflare, CloudFront)
└── Third-Party Services (Stripe, SendGrid, etc.)
```

All need version control.

<!-- section_id: "376b5e3a-6489-49c9-8250-5abb94347723" -->
### 2. Coordinated Deployments

Database changes often need coordination with other platform changes:

```
Example: Adding authentication
├── 1. Deploy infrastructure (Terraform) → User tables
├── 2. Run database migrations → Create users table
├── 3. Deploy authentication service (Auth0) → Configure
├── 4. Deploy application (Vercel) → With auth UI
└── 5. Verify integration → Test end-to-end
```

<!-- section_id: "9a41c41e-a0f4-4158-8cf9-731663567c4e" -->
### 3. Environment Synchronization

Database and application platforms must stay in sync:

```
Development:
├── Database: Local PostgreSQL
├── App: Local dev server
└── Auth: Dev Auth0 tenant

Staging:
├── Database: Staging PostgreSQL
├── App: Staging deployment
└── Auth: Staging Auth0 tenant

Production:
├── Database: Production PostgreSQL
├── App: Production deployment
└── Auth: Production Auth0 tenant
```

<!-- section_id: "43b35324-c566-44a7-9fa1-9df17d1028c9" -->
## Database Version Control Principles

<!-- section_id: "0499ac16-df46-4954-8dd9-9118c92f82d5" -->
### 1. Migration-Based Approach

Every database change is a migration:

```sql
-- migration: 20251027-001-create-users-table.sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

<!-- section_id: "2c90ca8e-01da-4e8d-bd4b-24831c985428" -->
### 2. Schema Version Control

Version control your schema files:

```bash
databases/
├── migrations/
│   ├── 20251027-001-create-users.sql
│   └── 20251028-001-add-indexes.sql
├── schema/
│   └── schema.sql          # Current state snapshot
└── seeds/
    └── dev-data.sql
```

<!-- section_id: "14714199-522f-4951-9ffd-c7441b527d18" -->
### 3. Data Versioning Strategy

- **Schema changes**: Always in migrations
- **Seed data**: Version controlled but separate from schema
- **Production data**: Backed up but not in Git
- **Reference data**: Version controlled

<!-- section_id: "016d34d6-d38b-429c-a1cd-a488965c0605" -->
### 4. Integration with Platform CI/CD

Database migrations run alongside platform deployments:

```yaml
# GitHub Actions example
jobs:
  deploy:
    steps:
      - name: Deploy infrastructure
        run: terraform apply
      
      - name: Run database migrations
        run: npm run db:migrate
      
      - name: Deploy application
        run: vercel deploy --prod
```

<!-- section_id: "944e8532-7548-4d22-bc25-16f412260a45" -->
## Platform-Specific Integration

<!-- section_id: "62dd7dab-4b34-4634-9504-425a26c9b9a8" -->
### Supabase Integration

```bash
# Supabase config is in Git
supabase/
├── config.toml
├── migrations/
│   └── 20251027_create_users.sql
└── seed.sql

# Deploy along with app
vercel deploy && \
supabase db push
```

<!-- section_id: "647d008f-86ef-4681-a0d3-4a91e2662561" -->
### Firebase Integration

```javascript
// firebase.json versioned
{
  "database": {
    "rules": "database.rules.json"
  },
  "hosting": {
    "public": "public"
  }
}

// Deploy together
firebase deploy --only database,hosting
```

<!-- section_id: "35f9b22e-a210-4812-9134-0cefc4b12b7b" -->
### AWS RDS + Terraform

```hcl
# Database defined in Terraform
resource "aws_rds_instance" "main" {
  # ... config ...
}

# Migrations run after RDS creation
provisioner "local-exec" {
  command = "npm run migrate"
}
```

<!-- section_id: "44345e2f-58d9-4731-b1cb-4864068a648f" -->
## Database + Platform Coordination

<!-- section_id: "f6b00846-361d-461d-a89a-f69d5b93d688" -->
### Pattern 1: Sequential Deployment

Deploy in dependency order:

```bash
# 1. Provision infrastructure
terraform apply

# 2. Wait for database to be ready
until psql $DATABASE_URL -c "SELECT 1"; do sleep 1; done

# 3. Run migrations
npm run db:migrate

# 4. Deploy application
vercel deploy --prod
```

<!-- section_id: "1f532b29-94b3-460a-a572-ebf363e969c4" -->
### Pattern 2: Blue-Green Database

```bash
# Deploy new database (Blue)
terraform apply -target=aws_rds_instance.blue

# Run migrations on Blue
psql $BLUE_DATABASE_URL < migrations/001.sql

# Switch application to Blue
vercel env add DATABASE_URL $BLUE_DATABASE_URL

# Shut down old database (Green)
terraform destroy -target=aws_rds_instance.green
```

<!-- section_id: "1b3b3df6-97c3-4654-9041-5bb8d953ccda" -->
### Pattern 3: Feature Flags for Database Changes

```sql
-- Migration with feature flag
ALTER TABLE users ADD COLUMN display_name VARCHAR(255);

-- Application code checks flag
SELECT 
  CASE 
    WHEN feature_enabled('new_schema') THEN new_column
    ELSE old_column
  END
FROM users;
```

<!-- section_id: "c5115bc1-ff6e-4772-b149-a96f847d27bc" -->
## Environment Management

<!-- section_id: "cc86d3ec-912c-49b1-9b6f-1020147ee498" -->
### Configuration Per Environment

```yaml
# config/databases.yaml
environments:
  development:
    type: postgresql
    host: localhost
    port: 5432
    database: myapp_dev
    
  staging:
    type: postgresql
    host: staging.db.example.com
    database: myapp_staging
    
  production:
    type: postgresql
    host: prod.db.example.com
    database: myapp_prod
```

<!-- section_id: "9a4c8c72-f9a7-462a-9bab-36d994b7a37e" -->
### Secret Management for Databases

```bash
# Never commit passwords
# .env.example (committed)
DATABASE_URL=postgresql://user:password@host:5432/database

# .env.local (gitignored)
DATABASE_URL=postgresql://user:secret@host:5432/database

# Use secret managers in production
aws secretsmanager get-secret-value --secret-id database-password
```

<!-- section_id: "3af45392-acc2-447b-905e-0c56f85eb8e6" -->
## Repository Structure

<!-- section_id: "4444268f-9b2d-48f7-a65a-77d334c100ee" -->
### Integrated Structure

```
project/
├── platforms/
│   ├── vercel.json              # Hosting
│   ├── netlify.toml
│   └── aws/                     # Cloud
│       └── terraform/
│
├── databases/                   # Database version control
│   ├── supabase/
│   │   ├── config.toml
│   │   ├── migrations/
│   │   └── seed.sql
│   ├── postgresql/
│   │   ├── migrations/
│   │   └── schema.sql
│   └── firebase/
│       └── firestore.rules
│
├── auth/
│   └── auth0-config.json       # Auth platforms
│
└── services/
    ├── stripe/
    └── sendgrid/                # Third-party services
```

<!-- section_id: "aaace22b-364f-41b7-a561-4a7068cdfc26" -->
### With Database Documentation

Full database version control documentation is available in:
[`./databases/`](./databases/) subdirectory

This includes:
- Universal database version control principles
- Platform-specific guides (Supabase, Firebase, etc.)
- Migration tools comparison
- CI/CD integration for databases
- Repository structure templates
- Troubleshooting guide

<!-- section_id: "e1c53354-49a2-416e-a5d6-24723b57af8f" -->
## Best Practices

<!-- section_id: "c63f169c-b0e3-4539-b9b4-ef4725a717e3" -->
### 1. Separate Concerns

- Database migrations: `databases/migrations/`
- Application config: `platforms/`
- Infrastructure: `infrastructure/`
- Secrets: Secret managers (not Git)

<!-- section_id: "ce601b75-4b60-4e55-b165-17f618d9e997" -->
### 2. Coordinate Changes

When changing multiple platforms:
1. Create feature branch
2. Update database migrations
3. Update application code
4. Update platform configurations
5. Test integration
6. Deploy together or in coordinated order

<!-- section_id: "5967644d-00a7-4ab8-80f2-8b3b7a1b4ae1" -->
### 3. Document Dependencies

```markdown
# Platform Dependencies

## Database → Application

The application depends on these database tables:
- users (id, email, created_at)
- posts (id, user_id, content, created_at)
- comments (id, post_id, user_id, content)

## Deployment Order

1. Provision database (Terraform)
2. Run migrations
3. Deploy application (Vercel)
```

<!-- section_id: "2ee9f0eb-a10a-4eb1-9dc8-6da712a3b5db" -->
### 4. Version Everything Together

```bash
# Tag together
git tag -a v1.0.0 -m "Release 1.0.0"
# Includes:
# - Application code v1.0.0
# - Database schema v1.0.0
# - Platform configs v1.0.0
```

<!-- section_id: "bea74c23-bfd6-470f-a57a-2b66b5da8e38" -->
### 5. Test Integration

```bash
# Test database + app integration
npm run test:db
npm run test:integration
```

<!-- section_id: "0049f20f-7ea5-4362-ae4d-31b9bebc9cf5" -->
## Common Scenarios

<!-- section_id: "5cacd630-9188-47f3-802f-a0402395b586" -->
### Scenario 1: Adding a New Feature

```bash
# 1. Database change
git checkout -b feature/new-feature
edit databases/migrations/20251027-add-feature.sql

# 2. Application change
edit src/features/new-feature/

# 3. Platform config change (if needed)
edit vercel.json

# 4. Test locally
npm run test
npm run migrate

# 5. Deploy
git push origin feature/new-feature
# CI/CD deploys everything together
```

<!-- section_id: "f937e201-c3ca-4023-bf02-83426c4a9f77" -->
### Scenario 2: Database Migration in Production

```bash
# 1. Backup production database
pg_dump $PROD_DATABASE_URL > backup.sql

# 2. Test migration on staging
git checkout staging
npm run migrate

# 3. Verify staging works
npm run test

# 4. Apply to production
git checkout production
npm run migrate

# 5. Monitor and verify
# (Set up alerts and checks)
```

<!-- section_id: "17601e44-7d9f-4109-a434-3e6c2eaa02f1" -->
### Scenario 3: Platform Migration

```bash
# Migrating from Firebase to Supabase

# 1. Set up Supabase (new platform)
supabase init
supabase start

# 2. Create migration to match Firebase schema
# (Manual migration script)

# 3. Deploy to staging Supabase
supabase db push

# 4. Update application config
# Update DATABASE_URL to Supabase

# 5. Test thoroughly
# Run all tests

# 6. Deploy to production
# Switch production database URL
# Run final migration
# Verify and monitor
```

<!-- section_id: "33cdc7dc-1603-4c9e-be7f-aadadf870025" -->
## Summary

Database version control is:
- ✅ One component of your broader platform version control system
- ✅ Must be coordinated with other platform deployments
- ✅ Follows same principles as other platforms (everything as code)
- ✅ Requires careful environment management
- ✅ Benefits from integration with CI/CD
- ✅ Needs proper secret management
- ✅ Should be documented like other platforms

**Key Integration Points**:
- Database migrations run alongside application deployments
- Database configurations are version controlled like other platforms
- Environment parity applies to databases too
- Secrets are managed securely across all platforms
- CI/CD orchestrates database + platform deployments

---

*For detailed database version control guides, see the [`databases/`](./databases/) subdirectory. For broader platform version control, see [Universal Platform Version Control Guide](./universal-platform-version-control-guide.md).*

