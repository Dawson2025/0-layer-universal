---
resource_id: "58be4217-5f88-402e-acf6-74483da8990b"
resource_type: "document"
resource_name: "repo-structure-templates"
---
# Repository Structure Templates
*Organizing Database Files in Your Version Control System*

<!-- section_id: "da7d731a-b20a-46ba-b684-2b75a98b2d53" -->
## Overview

This guide provides repository structure templates for organizing database files, migrations, seeds, and configuration across different project types and database platforms.

<!-- section_id: "99f9445a-0508-405c-aba8-a63943ab4da4" -->
## Template Categories

1. [Simple Single-Database Project](#simple-single-database-project)
2. [Multi-Database Monorepo](#multi-database-monorepo)
3. [Microservices with Separate Databases](#microservices-with-separate-databases)
4. [Platform-Specific Structures](#platform-specific-structures)

---

<!-- section_id: "8486ab65-e0e1-4654-9428-ed9cf1de51b0" -->
## Simple Single-Database Project

Best for: Small projects, single team, one database

<!-- section_id: "c4ceadfa-80c6-4f6b-88ca-bdeeacd2591f" -->
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

<!-- section_id: "d7c25a10-ada5-4dd8-a2d0-033a4f0d9001" -->
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

<!-- section_id: "8399e808-1749-4a78-988a-44fac418519f" -->
## Multi-Database Monorepo

Best for: Projects with multiple databases (e.g., main DB + analytics DB)

<!-- section_id: "f33e0144-670b-4f0d-ba38-eb2df0d3af92" -->
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

<!-- section_id: "a8b8c27b-6c19-4297-a6b7-04fc69d1cfe7" -->
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

<!-- section_id: "0061a2a1-45e9-48fb-bdd5-ca965431bb92" -->
## Microservices with Separate Databases

Best for: Microservices architecture, each service has its own database

<!-- section_id: "243c01a9-5751-4f83-a1fb-5cc5f16a115e" -->
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

<!-- section_id: "8ccc5e6f-4686-49ef-919a-9d7b87d11c90" -->
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

<!-- section_id: "25ae2236-b97f-4556-b53d-625443029e15" -->
## Platform-Specific Structures

<!-- section_id: "af1ac0c7-1746-4d63-9102-58913a09b7be" -->
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

<!-- section_id: "159ad325-8d6e-410e-acf6-f8173fed8ff3" -->
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

<!-- section_id: "e85b6e54-f29a-4adf-8b3b-5d45631ed939" -->
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

<!-- section_id: "1ef766c6-c68a-486b-8c5f-72ca8e43d0de" -->
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

<!-- section_id: "b158ae9f-53d9-4c1f-a2d4-84cf48f46218" -->
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

<!-- section_id: "263f4c64-1f0f-4b35-abbe-c14c257e8875" -->
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

<!-- section_id: "178b5ec0-f255-4bd9-a835-c461d345da3c" -->
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

<!-- section_id: "cb6fb242-a09b-4cdf-8511-80f7082d582e" -->
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

<!-- section_id: "fb9d46de-d591-4b5f-beaf-4d4a48985c95" -->
## Common Directory Patterns

<!-- section_id: "df553440-bdcb-4f28-b668-3c82ba2f878d" -->
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

<!-- section_id: "6a57d5b6-b5cf-4465-95e5-38a4f45d67a6" -->
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

<!-- section_id: "e97bfaca-0ab8-4e90-85fa-b749cd3cf2d7" -->
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

<!-- section_id: "1cad12de-308d-4172-9da2-b8be4f8c12fd" -->
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

<!-- section_id: "550533cc-a545-4e41-ad94-eb53fa1cfa58" -->
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

<!-- section_id: "6c17a4a1-3e01-4ee0-81bc-1fac2d099523" -->
## Best Practices

<!-- section_id: "43a9dfff-6de8-44ec-9b56-8b2834a1dfb7" -->
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

<!-- section_id: "9cd39968-b1b2-4c61-a914-f8df7147159e" -->
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

<!-- section_id: "ff1c3803-011b-464e-9f7c-810a0cbb3c63" -->
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

<!-- section_id: "334d28a8-1d9c-4dc1-81ca-6a279369dc3f" -->
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

<!-- section_id: "5b245184-d771-4901-a456-0d505dc40e07" -->
## Recommended Structures by Project Type

<!-- section_id: "9b5bf3ec-9ebc-40ae-bf03-b9387b8e8595" -->
### Small Web Application
```
project/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
└── README.md
```

<!-- section_id: "c5397872-6a33-477c-8389-c4c274439ec4" -->
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

<!-- section_id: "6ad77869-9b94-4e22-a13a-24e08f6e16ee" -->
### Microservices
```
monorepo/
├── services/
│   └── */database/migrations/
└── shared/
    └── database-utils/
```

<!-- section_id: "422e9681-8713-403b-8141-186c24664c3b" -->
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

