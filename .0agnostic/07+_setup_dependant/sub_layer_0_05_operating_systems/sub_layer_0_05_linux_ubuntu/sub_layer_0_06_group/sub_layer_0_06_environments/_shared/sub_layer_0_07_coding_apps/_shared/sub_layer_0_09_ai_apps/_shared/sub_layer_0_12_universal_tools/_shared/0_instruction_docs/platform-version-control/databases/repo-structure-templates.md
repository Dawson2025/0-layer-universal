---
resource_id: "55982b9c-b2be-463d-b128-6549bce15f56"
resource_type: "document"
resource_name: "repo-structure-templates"
---
# Repository Structure Templates
*Organizing Database Files in Your Version Control System*

<!-- section_id: "904c17d5-f42a-40b4-b8a9-b0b21e443eb9" -->
## Overview

This guide provides repository structure templates for organizing database files, migrations, seeds, and configuration across different project types and database platforms.

<!-- section_id: "bd440046-c8d6-4428-8d00-83598d2dfd74" -->
## Template Categories

1. [Simple Single-Database Project](#simple-single-database-project)
2. [Multi-Database Monorepo](#multi-database-monorepo)
3. [Microservices with Separate Databases](#microservices-with-separate-databases)
4. [Platform-Specific Structures](#platform-specific-structures)

---

<!-- section_id: "6d458039-3f21-44cc-91ad-8ca5a71cb6bf" -->
## Simple Single-Database Project

Best for: Small projects, single team, one database

<!-- section_id: "a268f04d-3160-4df6-9e92-d4bb01bf68c8" -->
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

<!-- section_id: "6713af8d-4d97-49aa-811d-57e930b04dc7" -->
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

<!-- section_id: "85725a96-0286-4cb7-82a5-a132174e3dca" -->
## Multi-Database Monorepo

Best for: Projects with multiple databases (e.g., main DB + analytics DB)

<!-- section_id: "ec21b6fd-8589-43b0-9d36-02d991b2f3b1" -->
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

<!-- section_id: "eddbe68a-1958-4c0b-b7a2-81f820aca7b1" -->
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

<!-- section_id: "d76061b9-d34c-4547-9646-88ec78578443" -->
## Microservices with Separate Databases

Best for: Microservices architecture, each service has its own database

<!-- section_id: "fdd94088-6215-4073-80d9-36a192d0b337" -->
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

<!-- section_id: "c1a72723-fe0e-4145-96ea-dbcedae43d70" -->
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

<!-- section_id: "228f5f8e-0747-4447-bc7f-6f505b2dd255" -->
## Platform-Specific Structures

<!-- section_id: "d71e01f6-3972-4bda-b970-dc5de23f6d86" -->
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

<!-- section_id: "4a9c71a6-e198-4c24-abc2-18c9f39d2700" -->
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

<!-- section_id: "44a81aa3-69b1-4c2e-8eb6-c697ea0890bd" -->
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

<!-- section_id: "9c541161-fdb4-4c43-8e4d-4bfcebf46364" -->
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

<!-- section_id: "fb42cee0-4be3-41e9-aae1-a0de75e48450" -->
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

<!-- section_id: "4228dd56-662e-4f70-a5db-c195f8b30273" -->
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

<!-- section_id: "f0e51ee6-d1f6-4485-b310-db6430a80836" -->
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

<!-- section_id: "fbd0c014-1399-42d1-a8c1-c0b8aa8157a3" -->
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

<!-- section_id: "614c4236-4de3-45d3-84b4-d553e4ccb2df" -->
## Common Directory Patterns

<!-- section_id: "ef453edb-9abd-47c6-b0d9-8d6b60e9b913" -->
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

<!-- section_id: "b91454af-b148-4d6d-a6fd-dfa1f56037a1" -->
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

<!-- section_id: "6ecf0759-ead4-4c8c-854c-ff39a0299072" -->
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

<!-- section_id: "8210b85e-06d5-400f-af99-a06a182a350e" -->
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

<!-- section_id: "afd0accf-afeb-4272-8d3a-edf3a4ef1b1a" -->
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

<!-- section_id: "b8846523-bb5f-4e54-87e6-85d59d1be030" -->
## Best Practices

<!-- section_id: "6fff1f50-aa59-4dcc-adee-37510f989891" -->
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

<!-- section_id: "30552c7e-5675-4cdf-bfe8-7b0e520b5b73" -->
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

<!-- section_id: "b6593aa3-574e-46e4-ba71-f29e1a9ab60b" -->
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

<!-- section_id: "dd8dd773-3ba5-4890-b019-55b6c094f850" -->
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

<!-- section_id: "d2d154b4-503c-4a5d-8eb8-1306346506d6" -->
## Recommended Structures by Project Type

<!-- section_id: "7f74db81-e43c-4996-b6b4-8b826ebf47b9" -->
### Small Web Application
```
project/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
└── README.md
```

<!-- section_id: "03a0c23c-7b88-4819-9f42-8aab9a981c3b" -->
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

<!-- section_id: "286124cb-b041-445f-9122-4a877e5f82f8" -->
### Microservices
```
monorepo/
├── services/
│   └── */database/migrations/
└── shared/
    └── database-utils/
```

<!-- section_id: "a369071c-f6e5-4b75-bac6-a2f88fab22c9" -->
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

