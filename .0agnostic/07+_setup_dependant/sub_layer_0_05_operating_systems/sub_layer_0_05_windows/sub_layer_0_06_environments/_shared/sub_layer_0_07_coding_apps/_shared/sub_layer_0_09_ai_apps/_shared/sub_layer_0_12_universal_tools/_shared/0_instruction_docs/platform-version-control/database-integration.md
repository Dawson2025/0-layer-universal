---
resource_id: "bc2e559e-58f0-4db7-b737-de1a153a07a9"
resource_type: "document"
resource_name: "database-integration"
---
# Database Integration in Platform Version Control
*How Databases Fit into the Broader Platform Version Control System*

<!-- section_id: "899be553-deaf-46d0-86a9-e08db0c5c8cb" -->
## Overview

Databases are a critical component of your application platform stack, but they don't exist in isolation. This guide explains how database version control integrates with your broader platform version control strategy.

<!-- section_id: "dff19f5f-4544-4d14-83ab-762a278e2ccb" -->
## Integration Points

<!-- section_id: "33e506d5-6046-499a-9a12-d1c1b6d93844" -->
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

<!-- section_id: "5bdd2970-6531-4314-94ab-47fc50a44e98" -->
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

<!-- section_id: "6fa08de1-5855-47f2-b8aa-9cfe5ff798eb" -->
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

<!-- section_id: "a4d3b549-eb3d-4a25-b99d-ed2b33de1529" -->
## Database Version Control Principles

<!-- section_id: "01bdc1b2-d921-42ba-9aad-b58c5ac20aa6" -->
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

<!-- section_id: "e6e3b921-6cdc-45db-a8c8-8d7e8ae52cb8" -->
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

<!-- section_id: "2308296e-dffd-4771-b9ea-a496244a1331" -->
### 3. Data Versioning Strategy

- **Schema changes**: Always in migrations
- **Seed data**: Version controlled but separate from schema
- **Production data**: Backed up but not in Git
- **Reference data**: Version controlled

<!-- section_id: "c4fd6ed5-6ad0-4710-b67d-10e961d1c651" -->
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

<!-- section_id: "1955d123-d487-4cef-95ef-b1aa64f6a008" -->
## Platform-Specific Integration

<!-- section_id: "33ff1f4d-9de2-48c8-80bb-fdb82df3425b" -->
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

<!-- section_id: "65a86411-8695-4d8c-bcea-d31037781db4" -->
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

<!-- section_id: "859a6a2d-d447-431d-8a5a-eca227c34b63" -->
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

<!-- section_id: "7afa72b9-c87e-4979-8f26-818807d0923c" -->
## Database + Platform Coordination

<!-- section_id: "e2fbca13-67e7-4dfc-b0b3-80caebfa59b1" -->
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

<!-- section_id: "3256fe4a-ffa6-480e-936c-6ae673e0abbe" -->
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

<!-- section_id: "f3f56f5d-4257-4cb5-935e-e7f60a063c20" -->
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

<!-- section_id: "f0664062-4b4f-494e-b181-052e79b0935e" -->
## Environment Management

<!-- section_id: "d905d5d1-bc07-40b3-ac3a-731cc5cf7207" -->
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

<!-- section_id: "b8162c9d-279e-4457-90f2-3b7681ec7d38" -->
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

<!-- section_id: "ec69adce-37c9-476a-a6c4-29b427cd95d2" -->
## Repository Structure

<!-- section_id: "09e5eff8-d77f-4543-a415-c5ae880f9b31" -->
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

<!-- section_id: "3cc9c503-7960-42f4-be20-a6def8b3bdd0" -->
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

<!-- section_id: "ea44b401-8525-4db2-b8b2-01ad18895429" -->
## Best Practices

<!-- section_id: "068bf4d0-a975-4ac9-a476-531a3a3dc371" -->
### 1. Separate Concerns

- Database migrations: `databases/migrations/`
- Application config: `platforms/`
- Infrastructure: `infrastructure/`
- Secrets: Secret managers (not Git)

<!-- section_id: "deb6adf2-7189-40ca-ae47-d2c20d56c5bd" -->
### 2. Coordinate Changes

When changing multiple platforms:
1. Create feature branch
2. Update database migrations
3. Update application code
4. Update platform configurations
5. Test integration
6. Deploy together or in coordinated order

<!-- section_id: "ae09766a-f216-4062-aca5-6c7ff2832039" -->
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

<!-- section_id: "054834e4-48be-41f4-890b-5026430fa5d4" -->
### 4. Version Everything Together

```bash
# Tag together
git tag -a v1.0.0 -m "Release 1.0.0"
# Includes:
# - Application code v1.0.0
# - Database schema v1.0.0
# - Platform configs v1.0.0
```

<!-- section_id: "47816d81-5284-46d5-a331-28d726d5eaaa" -->
### 5. Test Integration

```bash
# Test database + app integration
npm run test:db
npm run test:integration
```

<!-- section_id: "3505b743-c5f8-4daf-b016-fb0e18d50bb5" -->
## Common Scenarios

<!-- section_id: "488df418-e10e-4ad3-ac3e-858ab467bbe1" -->
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

<!-- section_id: "09c92c33-1922-49ce-988c-e3a831d8fbef" -->
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

<!-- section_id: "06aeb807-3692-43af-9b9b-7b71cfad9a9e" -->
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

<!-- section_id: "9c2611c2-09a5-4111-a790-971d297c330d" -->
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

