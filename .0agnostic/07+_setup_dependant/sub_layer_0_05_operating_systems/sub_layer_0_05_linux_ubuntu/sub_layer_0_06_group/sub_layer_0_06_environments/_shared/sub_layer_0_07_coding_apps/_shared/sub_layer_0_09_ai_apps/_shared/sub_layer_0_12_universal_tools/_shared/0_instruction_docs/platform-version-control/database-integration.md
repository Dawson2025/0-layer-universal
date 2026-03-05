---
resource_id: "073743bf-fee5-461b-8ab6-700f894966d1"
resource_type: "document"
resource_name: "database-integration"
---
# Database Integration in Platform Version Control
*How Databases Fit into the Broader Platform Version Control System*

<!-- section_id: "e821ecdc-3f6a-43d6-a42c-eaa22aab22b9" -->
## Overview

Databases are a critical component of your application platform stack, but they don't exist in isolation. This guide explains how database version control integrates with your broader platform version control strategy.

<!-- section_id: "b81d2ab6-c108-4541-bb61-37e77fd80882" -->
## Integration Points

<!-- section_id: "8b1fdedd-e71c-4eff-bca6-d46d9efa9ca5" -->
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

<!-- section_id: "2894d295-1afb-4202-8a79-7440de504509" -->
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

<!-- section_id: "be49f590-cf62-454a-9805-5a443417cfec" -->
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

<!-- section_id: "93294e63-5c28-42e5-9260-ff9d5a6cef31" -->
## Database Version Control Principles

<!-- section_id: "e317972c-80f0-4c60-b13b-648f81d99403" -->
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

<!-- section_id: "ec9b89b0-9fb9-4c20-b608-90c849112b57" -->
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

<!-- section_id: "a6c9fa59-c073-475b-975d-4797d5c9935a" -->
### 3. Data Versioning Strategy

- **Schema changes**: Always in migrations
- **Seed data**: Version controlled but separate from schema
- **Production data**: Backed up but not in Git
- **Reference data**: Version controlled

<!-- section_id: "621ca71c-45c1-4e4c-b4bf-19e61b79c2a2" -->
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

<!-- section_id: "b6e465ce-4d7c-40ff-b594-2359dd044424" -->
## Platform-Specific Integration

<!-- section_id: "65c68319-6c49-4830-84c1-0e3695c13759" -->
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

<!-- section_id: "cb00676c-35be-4163-b496-4bdd1cb62983" -->
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

<!-- section_id: "f03049a7-411a-4bd3-83fe-f08ead2aee51" -->
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

<!-- section_id: "5b50e83f-3640-47f6-8126-529d63ab34a7" -->
## Database + Platform Coordination

<!-- section_id: "9d8bc189-89b7-4ea4-8821-995a8b43296a" -->
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

<!-- section_id: "7aef48f2-af4e-454c-9e3c-6737ac446458" -->
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

<!-- section_id: "3b8fe1d5-8b54-4641-b110-7c4e2e14402b" -->
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

<!-- section_id: "96642d86-0169-4bf7-95f3-b71333009a51" -->
## Environment Management

<!-- section_id: "aecc6b00-c044-4fb2-b6f5-9fbdffa47d8e" -->
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

<!-- section_id: "1fd95c3c-816a-46d6-bb6a-952dc8e81473" -->
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

<!-- section_id: "61d6948c-90df-459f-ad00-0f629164fab2" -->
## Repository Structure

<!-- section_id: "d2b91d7f-f077-4dca-96e5-ef7a4aa8e916" -->
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

<!-- section_id: "6fc932dd-6c6f-4180-a012-03429bafcfdd" -->
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

<!-- section_id: "bc1c25b0-6a94-48c7-ad2d-b16cbdb1fb8a" -->
## Best Practices

<!-- section_id: "e4757c70-856c-4554-8793-61b55c05fe4d" -->
### 1. Separate Concerns

- Database migrations: `databases/migrations/`
- Application config: `platforms/`
- Infrastructure: `infrastructure/`
- Secrets: Secret managers (not Git)

<!-- section_id: "6e4cd6eb-6389-413d-bf74-ab80955a83fa" -->
### 2. Coordinate Changes

When changing multiple platforms:
1. Create feature branch
2. Update database migrations
3. Update application code
4. Update platform configurations
5. Test integration
6. Deploy together or in coordinated order

<!-- section_id: "288824aa-4d17-408c-9329-77ea25cc633d" -->
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

<!-- section_id: "0cdd9d10-57e7-431d-b0ab-acca3ef07522" -->
### 4. Version Everything Together

```bash
# Tag together
git tag -a v1.0.0 -m "Release 1.0.0"
# Includes:
# - Application code v1.0.0
# - Database schema v1.0.0
# - Platform configs v1.0.0
```

<!-- section_id: "94402658-b87b-471d-b1b8-d98879b6280d" -->
### 5. Test Integration

```bash
# Test database + app integration
npm run test:db
npm run test:integration
```

<!-- section_id: "ecda2f34-d59d-4504-8ec2-6a405fb3b229" -->
## Common Scenarios

<!-- section_id: "107e8faa-38a0-4748-bdb6-75dbe021c3fb" -->
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

<!-- section_id: "a8a31552-0e7b-48e2-8165-22d9e12863d3" -->
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

<!-- section_id: "7af1169b-2842-4478-b51c-abe5c085c48d" -->
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

<!-- section_id: "f3e46413-cf60-4d5c-aeaa-a32fa164ab1a" -->
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

