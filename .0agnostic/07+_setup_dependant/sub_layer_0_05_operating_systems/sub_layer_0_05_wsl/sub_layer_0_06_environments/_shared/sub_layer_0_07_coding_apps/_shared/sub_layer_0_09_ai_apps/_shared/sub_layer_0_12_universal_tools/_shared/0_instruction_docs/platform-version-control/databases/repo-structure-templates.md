---
resource_id: "16d9e47d-8bf6-4e84-beca-e8a0aa95e564"
resource_type: "document"
resource_name: "repo-structure-templates"
---
# Repository Structure Templates
*Organizing Database Files in Your Version Control System*

<!-- section_id: "3067dfbd-6704-40a8-9850-757c0d4b6055" -->
## Overview

This guide provides repository structure templates for organizing database files, migrations, seeds, and configuration across different project types and database platforms.

<!-- section_id: "32fa4f7a-6b53-46c5-bc9e-f7c6c308b639" -->
## Template Categories

1. [Simple Single-Database Project](#simple-single-database-project)
2. [Multi-Database Monorepo](#multi-database-monorepo)
3. [Microservices with Separate Databases](#microservices-with-separate-databases)
4. [Platform-Specific Structures](#platform-specific-structures)

---

<!-- section_id: "391097e2-c36c-474a-a100-47646ef75d92" -->
## Simple Single-Database Project

Best for: Small projects, single team, one database

<!-- section_id: "cd2fc5a8-1059-48a7-ba8a-7c08faec1a01" -->
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

<!-- section_id: "be57d22e-3a32-44b7-beea-93c518a714a4" -->
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

<!-- section_id: "c4501ca7-dab4-42da-92f2-34081ea7e41b" -->
## Multi-Database Monorepo

Best for: Projects with multiple databases (e.g., main DB + analytics DB)

<!-- section_id: "f8d52c8c-d367-4b93-92c2-f7a4057330db" -->
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

<!-- section_id: "e5b34603-e6ee-45b0-af35-257888ef3997" -->
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

<!-- section_id: "163ffa1f-0500-4974-9301-a0199e6615e4" -->
## Microservices with Separate Databases

Best for: Microservices architecture, each service has its own database

<!-- section_id: "3f88698d-9c2c-49ee-a520-48ba296ec2ea" -->
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

<!-- section_id: "986c3ed9-2bc1-4f2b-96a8-d012c91d9f64" -->
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

<!-- section_id: "29b6543e-a0af-4fca-9ec0-187460a86088" -->
## Platform-Specific Structures

<!-- section_id: "17d75874-198b-48b9-b278-6a45479a3f9b" -->
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

<!-- section_id: "903d8f4e-5215-43c4-8f21-23f16f8c7837" -->
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

<!-- section_id: "a7d7a1fc-08f1-4010-ad0f-db8121bc9dc7" -->
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

<!-- section_id: "f02dcb0c-35d4-4193-8ccd-b4b6c8b106da" -->
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

<!-- section_id: "9553518a-cd3a-4635-9ecb-72a6ab469157" -->
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

<!-- section_id: "472651f3-6e94-45af-82d2-c2a1b33a8743" -->
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

<!-- section_id: "9abc2a88-2bc7-4ed7-9dba-73f7e141a362" -->
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

<!-- section_id: "7620fb85-5d6b-4748-ad50-50db4f5f3a59" -->
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

<!-- section_id: "3a25cfbf-47f3-46c7-9768-190cb03dd006" -->
## Common Directory Patterns

<!-- section_id: "42685187-2012-4369-aa6b-98e3e25e0e1d" -->
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

<!-- section_id: "b034baa3-45ab-4bc6-8f39-05e6674221df" -->
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

<!-- section_id: "a20ba700-5959-4a77-a78f-b06044219c4e" -->
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

<!-- section_id: "52615864-008f-41ff-9f85-c52244c8ad17" -->
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

<!-- section_id: "d51d6d7b-7abf-4de8-be7e-0d9cc11d9ac2" -->
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

<!-- section_id: "36441e3a-b6f1-48e6-bf75-8e4bae094929" -->
## Best Practices

<!-- section_id: "4d18084e-ad3e-426a-8c81-eb96b2f17e9a" -->
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

<!-- section_id: "335127e7-03c2-4a1d-8518-21a8368b333b" -->
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

<!-- section_id: "84990bb9-ba15-47aa-9812-8ebc66c81945" -->
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

<!-- section_id: "32445c92-1b2a-4ff5-b038-f364acc7867d" -->
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

<!-- section_id: "8491d4ee-4ce5-41af-9293-d946b69dc478" -->
## Recommended Structures by Project Type

<!-- section_id: "7f14d1c0-a2b6-4fb1-9c28-f681af68480e" -->
### Small Web Application
```
project/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
└── README.md
```

<!-- section_id: "9269d9b0-a81e-4e3f-aaae-fd7d031c0478" -->
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

<!-- section_id: "6d09bba3-f94d-44ad-b966-b346d052631f" -->
### Microservices
```
monorepo/
├── services/
│   └── */database/migrations/
└── shared/
    └── database-utils/
```

<!-- section_id: "57888168-d936-4691-8ddb-f60273e2d70f" -->
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

