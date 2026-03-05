---
resource_id: "c2c27c6c-9c6b-4478-9cd8-9a3f67096228"
resource_type: "document"
resource_name: "database-integration"
---
# Database Integration in Platform Version Control
*How Databases Fit into the Broader Platform Version Control System*

<!-- section_id: "c9f41086-25a7-49e8-a618-b1c9affbc85f" -->
## Overview

Databases are a critical component of your application platform stack, but they don't exist in isolation. This guide explains how database version control integrates with your broader platform version control strategy.

<!-- section_id: "4704f06c-19ef-466e-867d-7068dea5fda1" -->
## Integration Points

<!-- section_id: "e4307d42-f3ff-457c-a255-2f4bc59a8838" -->
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

<!-- section_id: "cb4b6ee9-8037-4702-89f5-73c302ff0729" -->
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

<!-- section_id: "4520ab3f-dc05-414c-ae93-fa2a6d8451ac" -->
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

<!-- section_id: "b02f3f8f-13bc-43af-9269-b44a32a25f4c" -->
## Database Version Control Principles

<!-- section_id: "7cf1e50d-a4e0-44ed-9e3e-5e3911c4848b" -->
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

<!-- section_id: "89d7ba37-13fb-4df4-88fd-49d7f641ab39" -->
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

<!-- section_id: "fc27a0d3-49a4-4fe6-b4cc-cc45bdd56dea" -->
### 3. Data Versioning Strategy

- **Schema changes**: Always in migrations
- **Seed data**: Version controlled but separate from schema
- **Production data**: Backed up but not in Git
- **Reference data**: Version controlled

<!-- section_id: "2e13cbc2-6003-4dd6-8fa8-6b2849315856" -->
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

<!-- section_id: "0d077e61-90bf-49b4-893f-f0ebddc7caf1" -->
## Platform-Specific Integration

<!-- section_id: "8961956c-3c8b-44e1-b7de-b87ef3bfa2ae" -->
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

<!-- section_id: "858de5bc-29bd-40b1-9eca-4fa8361862af" -->
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

<!-- section_id: "0bac207c-61fa-483d-98aa-a1697ba50b41" -->
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

<!-- section_id: "af3fecd3-5212-4d7f-a638-cec05163a529" -->
## Database + Platform Coordination

<!-- section_id: "6e239781-36d7-43b3-9872-af689a18b223" -->
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

<!-- section_id: "60fd0dc2-4e46-4088-9ac8-edfd71049634" -->
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

<!-- section_id: "a94a790f-ccc5-4b6d-a330-75eef7444a30" -->
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

<!-- section_id: "e47c7eaf-c6f5-4dc3-a894-fa530d24fa4b" -->
## Environment Management

<!-- section_id: "9016335c-72cb-4c30-95ea-59c784fb2ccb" -->
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

<!-- section_id: "75246102-f8aa-484a-a73c-362302ee21f3" -->
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

<!-- section_id: "19fdf963-8de8-45dd-b102-7cdb74920ee7" -->
## Repository Structure

<!-- section_id: "c4a2d5aa-04be-4769-8096-e1e0a6c3255f" -->
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

<!-- section_id: "e9942b56-797b-4415-bb5c-7516f9322ab0" -->
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

<!-- section_id: "974c0a8c-b299-43ed-ac97-e4d5ce3d8991" -->
## Best Practices

<!-- section_id: "7b05fafb-a3b6-4d4e-a6cb-9a63739d02ad" -->
### 1. Separate Concerns

- Database migrations: `databases/migrations/`
- Application config: `platforms/`
- Infrastructure: `infrastructure/`
- Secrets: Secret managers (not Git)

<!-- section_id: "fc4ce308-6a44-474a-a783-62064fb36e63" -->
### 2. Coordinate Changes

When changing multiple platforms:
1. Create feature branch
2. Update database migrations
3. Update application code
4. Update platform configurations
5. Test integration
6. Deploy together or in coordinated order

<!-- section_id: "b7e7059b-6099-4b28-a94b-117ec1a0e2c9" -->
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

<!-- section_id: "bac043af-9072-4f83-9919-2cd744c69a3f" -->
### 4. Version Everything Together

```bash
# Tag together
git tag -a v1.0.0 -m "Release 1.0.0"
# Includes:
# - Application code v1.0.0
# - Database schema v1.0.0
# - Platform configs v1.0.0
```

<!-- section_id: "ef1ba379-09b1-4248-9827-0533275fdf6e" -->
### 5. Test Integration

```bash
# Test database + app integration
npm run test:db
npm run test:integration
```

<!-- section_id: "136c3ed2-10d2-48b2-9303-750a863cab86" -->
## Common Scenarios

<!-- section_id: "5bc9a7b5-84de-45e6-8bdc-0b4751523413" -->
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

<!-- section_id: "c12829a2-f95e-473a-a532-dc172dc6f157" -->
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

<!-- section_id: "87a48c16-2629-4d45-a09b-1468ac520160" -->
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

<!-- section_id: "8440d769-b724-4103-9d3e-2f1a30dcac00" -->
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

