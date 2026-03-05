---
resource_id: "694d65c3-9f16-40c2-9d40-93f7caf83085"
resource_type: "document"
resource_name: "database-integration"
---
# Database Integration in Platform Version Control
*How Databases Fit into the Broader Platform Version Control System*

<!-- section_id: "63177f8e-06ee-4c53-bf1a-71e5b3fd51cb" -->
## Overview

Databases are a critical component of your application platform stack, but they don't exist in isolation. This guide explains how database version control integrates with your broader platform version control strategy.

<!-- section_id: "ec61145c-c763-4b51-8f51-5c7d08c5f892" -->
## Integration Points

<!-- section_id: "40bd9065-9e54-4112-8e81-9e9838816b37" -->
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

<!-- section_id: "d7931d75-e96e-4be6-adf5-48ef312b4e42" -->
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

<!-- section_id: "f7f6923a-2ad5-43fd-953c-967a5b772e39" -->
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

<!-- section_id: "9380ae85-33aa-455e-beb7-3594f3454323" -->
## Database Version Control Principles

<!-- section_id: "ecc8a895-279f-465f-b941-56ad268b9d28" -->
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

<!-- section_id: "b1aaa85f-caff-4e5e-9f1e-6876b2cb148f" -->
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

<!-- section_id: "274acd0f-4b6c-4a6d-8092-fd9a9fec4430" -->
### 3. Data Versioning Strategy

- **Schema changes**: Always in migrations
- **Seed data**: Version controlled but separate from schema
- **Production data**: Backed up but not in Git
- **Reference data**: Version controlled

<!-- section_id: "d820060a-41bb-422d-982c-f9d600d33f5d" -->
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

<!-- section_id: "4ed4c120-ef31-4bde-940b-87f1ca20d7d7" -->
## Platform-Specific Integration

<!-- section_id: "0ec07298-0534-40b8-8057-48ed3a3cb824" -->
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

<!-- section_id: "211f59e8-4ea1-4433-9f9d-e01868543226" -->
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

<!-- section_id: "eb112ef0-4837-494c-9320-2f04583ade05" -->
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

<!-- section_id: "a30157f3-d725-4b19-84e3-0ae2548d8143" -->
## Database + Platform Coordination

<!-- section_id: "9175593c-69e1-4ef6-a7ef-a984756b9960" -->
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

<!-- section_id: "42a5a7ba-abb1-4689-90e9-b65db665c0d9" -->
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

<!-- section_id: "e0a5b789-4443-49df-a134-a611ac2edca2" -->
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

<!-- section_id: "e3a629d0-e274-4f01-8edc-ddd40eb1832d" -->
## Environment Management

<!-- section_id: "a2b32ea9-8b8b-4fbb-b623-a1093ee72776" -->
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

<!-- section_id: "7db48267-2bcd-43fb-8a2f-36a35c85a84a" -->
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

<!-- section_id: "eef26ada-a1e4-4265-b323-bf6e366fbcee" -->
## Repository Structure

<!-- section_id: "fd1c6613-42ef-4f17-be93-934d9c82e3a3" -->
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

<!-- section_id: "061b65c8-40eb-463f-82d5-4825201b70d8" -->
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

<!-- section_id: "a700e5f8-97f0-403d-8467-8f502bb8dad9" -->
## Best Practices

<!-- section_id: "91e54d44-8d31-4232-974e-1c0a0368fe4a" -->
### 1. Separate Concerns

- Database migrations: `databases/migrations/`
- Application config: `platforms/`
- Infrastructure: `infrastructure/`
- Secrets: Secret managers (not Git)

<!-- section_id: "4537baec-b223-4413-a36b-a50f56e3b01b" -->
### 2. Coordinate Changes

When changing multiple platforms:
1. Create feature branch
2. Update database migrations
3. Update application code
4. Update platform configurations
5. Test integration
6. Deploy together or in coordinated order

<!-- section_id: "e620a6de-799d-466a-89b5-aa00248ba793" -->
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

<!-- section_id: "684c2bfd-d71e-437d-9091-a4e18452dd4c" -->
### 4. Version Everything Together

```bash
# Tag together
git tag -a v1.0.0 -m "Release 1.0.0"
# Includes:
# - Application code v1.0.0
# - Database schema v1.0.0
# - Platform configs v1.0.0
```

<!-- section_id: "d7c605f3-7226-4bbd-9baf-1c93d3ef5c91" -->
### 5. Test Integration

```bash
# Test database + app integration
npm run test:db
npm run test:integration
```

<!-- section_id: "b9c3eba3-ea3f-4a56-9e04-e0f02be23f31" -->
## Common Scenarios

<!-- section_id: "f4cd7d13-fd9c-4fab-816c-e8258c04936e" -->
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

<!-- section_id: "772f40db-6f10-4ead-ab0f-1bef1ad8215e" -->
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

<!-- section_id: "0df47dde-f37c-4c35-b0f7-0a0c207d9aa7" -->
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

<!-- section_id: "5275db87-f48b-4491-8bf0-5d42c6b2f974" -->
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

