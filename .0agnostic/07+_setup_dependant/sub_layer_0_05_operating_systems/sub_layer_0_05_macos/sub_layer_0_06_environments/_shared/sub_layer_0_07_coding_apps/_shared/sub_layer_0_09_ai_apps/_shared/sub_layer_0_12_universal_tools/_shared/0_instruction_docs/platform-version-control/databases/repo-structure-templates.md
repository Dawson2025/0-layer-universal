---
resource_id: "cc6b1cf6-c1f9-4a7c-9baa-59f698c9e79e"
resource_type: "document"
resource_name: "repo-structure-templates"
---
# Repository Structure Templates
*Organizing Database Files in Your Version Control System*

## Overview

This guide provides repository structure templates for organizing database files, migrations, seeds, and configuration across different project types and database platforms.

## Template Categories

1. [Simple Single-Database Project](#simple-single-database-project)
2. [Multi-Database Monorepo](#multi-database-monorepo)
3. [Microservices with Separate Databases](#microservices-with-separate-databases)
4. [Platform-Specific Structures](#platform-specific-structures)

---

## Simple Single-Database Project

Best for: Small projects, single team, one database

### Structure

```
project/
├── database/
│   ├── migrations/
│   │   ├── 20251027-0001-create-users-table.sql
│   │   ├── 20251027-0002-add-indexes.sql
│   │   └── 20251028-0001-add-posts-table.sql
│   ├── schema/
│   │   └── schema.sql                      # Current schema snapshot
│   ├── seeds/
│   │   ├── dev/
│   │   │   ├── users.sql
│   │   │   └── posts.sql
│   │   └── prod/
│   │       └── lookup-data.sql
│   └── config/
│       ├── database.yml                     # DB connection
│       └── .env.example
├── .gitignore
└── README.md
```

### Usage

```bash
# Create new migration
touch database/migrations/$(date +%Y%m%d-%H%M%S)-description.sql

# Apply migrations
./scripts/migrate.sh

# Seed data
./scripts/seed.sh
```

---

## Multi-Database Monorepo

Best for: Projects with multiple databases (e.g., main DB + analytics DB)

### Structure

```
project/
├── databases/
│   ├── main/
│   │   ├── migrations/
│   │   │   ├── 20251027-0001-create-users.sql
│   │   │   └── 20251028-0001-add-indexes.sql
│   │   ├── seeds/
│   │   │   └── dev/users.sql
│   │   └── config.toml
│   │
│   ├── analytics/
│   │   ├── migrations/
│   │   │   ├── 20251027-0001-create-events-table.sql
│   │   │   └── 20251028-0001-add-aggregates.sql
│   │   └── schema/
│   │       └── analytics-schema.sql
│   │
│   └── cache/
│       ├── redis-config.conf
│       └── scripts/
│           └── init-cache.sh
│
├── scripts/
│   ├── migrate-all.sh
│   ├── backup-all.sh
│   └── reset-dev.sh
│
├── .github/
│   └── workflows/
│       └── migrate.yml
│
└── README.md
```

### Usage

```bash
# Migrate all databases
./scripts/migrate-all.sh

# Migrate specific database
cd databases/main && flyway migrate

# Backup all databases
./scripts/backup-all.sh
```

---

## Microservices with Separate Databases

Best for: Microservices architecture, each service has its own database

### Structure

```
monorepo/
├── services/
│   ├── user-service/
│   │   ├── database/
│   │   │   ├── migrations/
│   │   │   │   ├── V1__Create_users.sql
│   │   │   │   └── V2__Add_profiles.sql
│   │   │   ├── seeds/
│   │   │   │   └── dev-users.sql
│   │   │   └── flyway.conf
│   │   └── .env
│   │
│   ├── order-service/
│   │   ├── database/
│   │   │   ├── migrations/
│   │   │   │   ├── V1__Create_orders.sql
│   │   │   │   └── V2__Add_payment_info.sql
│   │   │   └── schema.sql
│   │   └── .env
│   │
│   └── analytics-service/
│       ├── database/
│       │   ├── bigquery/
│       │   │   ├── views/
│       │   │   │   └── v_user_stats.sql
│       │   │   └── datasets/
│       │   │       └── analytics.yaml
│       │   └── pipelines/
│       │       └── etl-config.yaml
│       └── .env
│
├── shared/
│   ├── database-utils/
│   │   ├── migrate.js
│   │   └── seed.js
│   └── scripts/
│       └── migrate-all-services.sh
│
└── docker-compose.yml
```

### Usage

```bash
# Migrate specific service
cd services/user-service && flyway migrate

# Migrate all services
./shared/scripts/migrate-all-services.sh

# Service-specific migration
cd services/analytics-service && ./scripts/deploy-views.sh
```

---

## Platform-Specific Structures

### Supabase Project

```
supabase-project/
├── supabase/
│   ├── config.toml
│   ├── migrations/
│   │   ├── 20251027000001_create_users.sql
│   │   ├── 20251027000002_create_profiles.sql
│   │   └── 20251028000001_add_rls_policies.sql
│   ├── seed.sql
│   └── functions/
│       └── hello-world/
│           └── index.ts
├── .env.local
└── README.md
```

### Firebase Project

```
firebase-project/
├── database/
│   ├── database.rules.json
│   ├── database.development.rules.json
│   └── database.production.rules.json
│
├── firestore/
│   ├── firestore.rules
│   ├── firestore.indexes.json
│   └── backup/
│       └── collections/
│
├── functions/
│   ├── src/
│   └── package.json
│
├── firebase.json
├── .firebaserc
└── README.md
```

### Firebase + Firestore Structure

```
firebase-app/
├── database/
│   ├── firestore.rules
│   ├── firestore.indexes.json
│   ├── firestore.indexes.dev.json
│   └── security/
│       ├── production-rules.js
│       └── dev-rules.js
│
├── backup/
│   └── exports/
│       ├── 2025-10-27/...
│       └── 2025-10-28/...
│
├── scripts/
│   ├── deploy-rules.sh
│   ├── export-data.sh
│   └── import-data.sh
│
└── firebase.json
```

### Flyway Project

```
flyway-project/
├── db/
│   ├── migration/
│   │   ├── V1__Create_users_table.sql
│   │   ├── V2__Add_email_index.sql
│   │   ├── V3__Create_orders_table.sql
│   │   └── V4__Add_foreign_keys.sql
│   │
│   ├── baseline/
│   │   └── baseline.sql
│   │
│   ├── schema/
│   │   └── schema.sql
│   │
│   └── repeatable/
│       ├── R__Create_view.sql
│       └── R__Update_functions.sql
│
├── flyway.conf
├── pom.xml                          # Maven config
└── src/
    └── main/
        └── resources/
            └── application.properties
```

### Liquibase Project

```
liquibase-project/
├── src/main/resources/
│   ├── db/
│   │   ├── changelog/
│   │   │   ├── db.changelog-master.xml
│   │   │   ├── changelog-v1/
│   │   │   │   ├── changeset-001-users.xml
│   │   │   │   └── changeset-002-indexes.xml
│   │   │   └── changelog-v2/
│   │   │       └── changeset-003-posts.xml
│   │   │
│   │   └── liquibase.properties
│   │
│   └── application.yml
│
├── changelog.xml
├── liquibase.properties
└── pom.xml
```

### Django Project

```
django-project/
├── myapp/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_user_email.py
│   │   └── 0003_add_indexes.py
│   │
│   ├── models.py
│   └── admin.py
│
├── database/
│   ├── seeds/
│   │   └── fixtures/
│   │       ├── users.json
│   │       └── posts.json
│   │
│   └── backups/
│       └── 2025-10-27.sql
│
├── manage.py
└── settings.py
```

### Rails Project

```
rails-app/
├── db/
│   ├── migrate/
│   │   ├── 20251027000001_create_users.rb
│   │   ├── 20251027000002_create_posts.rb
│   │   └── 20251028000003_add_timestamps_to_users.rb
│   │
│   ├── schema.rb
│   │
│   ├── seeds.rb
│   │   └── development.rb
│   │
│   └── fixtures/
│       ├── users.yml
│       └── posts.yml
│
├── config/
│   ├── database.yml
│   └── application.rb
│
└── Gemfile
```

### Prisma Project

```
prisma-app/
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   │   ├── 20251027000001_init/
│   │   │   └── migration.sql
│   │   ├── 20251028000001_add_posts/
│   │   │   └── migration.sql
│   │   └── migration_lock.toml
│   │
│   └── seed.ts
│
├── src/
│   └── index.ts
│
├── .env
└── package.json
```

## Common Directory Patterns

### Migrations Directory

**Timestamped (Recommended)**:
```
migrations/
├── 20251027-143022-create-users-table.sql
├── 20251027-150000-add-indexes.sql
└── 20251028-100000-add-foreign-keys.sql
```

**Sequential**:
```
migrations/
├── 001_create_users_table.sql
├── 002_add_indexes.sql
└── 003_add_foreign_keys.sql
```

**Vendor-Specific**:
```
migrations/
├── V1__Create_users_table.sql          # Flyway
├── db.changelog-master.xml             # Liquibase
└── 20251027000001_create_users_table.sql  # Rails
```

### Seeds Directory

```
seeds/
├── development/
│   ├── users.sql
│   └── posts.sql
├── staging/
│   └── lookup-data.sql
├── production/
│   └── reference-data.sql
└── fixtures/
    ├── users.json
    └── products.json
```

### Schema Directory

```
schema/
├── schema.sql                        # Full schema
├── tables.sql                        # Tables only
├── views.sql                         # Views
├── functions.sql                     # Functions
├── indexes.sql                       # Indexes
├── constraints.sql                   # Constraints
└── data-types.sql                    # Custom types
```

### Configuration

```
config/
├── database.yml                       # Rails-style
├── application.properties            # Spring/Flyway
├── .env.example                      # Environment vars
├── prod.toml                         # Prod config
├── dev.toml                          # Dev config
└── test.toml                         # Test config
```

## Large-Scale Enterprise Structure

```
enterprise-db-project/
├── databases/
│   ├── production/
│   │   ├── main/
│   │   │   └── migrations/
│   │   ├── analytics/
│   │   │   └── migrations/
│   │   └── cache/
│   │       └── config/
│   │
│   ├── staging/
│   │   └── [mirror of production]
│   │
│   └── development/
│       └── [development databases]
│
├── shared/
│   ├── base-schemas/
│   │   ├── common-tables.sql
│   │   └── shared-types.sql
│   │
│   ├── utils/
│   │   ├── migration-runner.sh
│   │   ├── backup-script.sh
│   │   └── test-migrations.sh
│   │
│   └── docs/
│       └── database-guidelines.md
│
├── scripts/
│   ├── deploy-all.sh
│   ├── rollback.sh
│   ├── backup.sh
│   └── test-all.sh
│
├── docs/
│   ├── schema-docs/
│   │   └── tables.md
│   ├── migration-guide.md
│   └── troubleshooting.md
│
└── .github/
    └── workflows/
        ├── test-migrations.yml
        ├── deploy-staging.yml
        └── deploy-production.yml
```

## Best Practices

### 1. Naming Conventions

```bash
# ✅ Good
20251027-143022-create-users-table.sql
20251027-150000-add-email-index.sql

# ✅ Also Good
V1__Create_users_table.sql
db.changelog-v1.xml

# ❌ Bad
migration.sql
users.sql
new-changes.sql
```

### 2. Directory Organization

```bash
# ✅ Separate concerns
database/
├── migrations/     # Schema changes
├── seeds/                # Data
├── schema/               # Current state
├── backups/              # Exports
└── config/               # Configuration

# ❌ Don't mix
database/
├── migrations/
│   ├── 001_create_users.sql
│   ├── seed_users.sql      # Seeds in migrations
│   └── schema.sql           # Schema in migrations
```

### 3. Git Integration

```gitignore
# Database backups (don't commit)
*.sql.gz
*.dump
backup/
exports/

# Environment-specific
.env
.env.local
*.pem
*.key

# Lock files (tool-specific)
migration_lock.toml
flyway.schemaHistory
```

### 4. Documentation

Each structure should include:

```markdown
# database/README.md

## Structure

- `migrations/` - Database migration files
- `seeds/` - Seed data for development
- `schema/` - Schema snapshots
- `config/` - Configuration files

## Usage

### Create Migration
./scripts/new-migration.sh "description"

### Apply Migrations
./scripts/apply-migrations.sh

### Seed Data
./scripts/seed-dev.sh
```

## Recommended Structures by Project Type

### Small Web Application
```
project/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
└── README.md
```

### SaaS Application
```
project/
├── databases/
│   ├── main/
│   │   └── migrations/
│   ├── analytics/
│   │   └── migrations/
│   └── config/
└── scripts/
    └── deploy.sh
```

### Microservices
```
monorepo/
├── services/
│   └── */database/migrations/
└── shared/
    └── database-utils/
```

### Enterprise
```
enterprise/
├── databases/
│   ├── production/
│   ├── staging/
│   └── development/
├── shared/
│   └── schemas/
└── scripts/
    └── deploy-all.sh
```

---

*For implementation examples, see [CI/CD Integration Guide](./ci-cd-integration-guide.md). For platform-specific details, see [Platform-Specific Guides](./platform-specific-guides.md).*

