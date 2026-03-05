---
resource_id: "0353f6b9-06a5-431e-a76c-88025649b2c2"
resource_type: "document"
resource_name: "repo-structure-templates"
---
# Repository Structure Templates
*Organizing Database Files in Your Version Control System*

<!-- section_id: "80c9369f-917a-4904-af7c-a48a96562edf" -->
## Overview

This guide provides repository structure templates for organizing database files, migrations, seeds, and configuration across different project types and database platforms.

<!-- section_id: "bdcd5fc1-e63b-425e-aa1b-17356f7ed85a" -->
## Template Categories

1. [Simple Single-Database Project](#simple-single-database-project)
2. [Multi-Database Monorepo](#multi-database-monorepo)
3. [Microservices with Separate Databases](#microservices-with-separate-databases)
4. [Platform-Specific Structures](#platform-specific-structures)

---

<!-- section_id: "6b6b6fdb-7c83-459c-9b23-969a0cd1f3bc" -->
## Simple Single-Database Project

Best for: Small projects, single team, one database

<!-- section_id: "06239614-c597-44b2-b575-31e75f8d4290" -->
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

<!-- section_id: "b86b9f14-f8a7-4dd4-844c-79becb31e982" -->
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

<!-- section_id: "0a8e8af9-7658-4c9b-9f59-07c1d6ed1582" -->
## Multi-Database Monorepo

Best for: Projects with multiple databases (e.g., main DB + analytics DB)

<!-- section_id: "305b1e57-5067-41d5-a00a-b81d6cbbadb4" -->
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

<!-- section_id: "2273c4e7-a597-4126-aba7-ab9347780e8a" -->
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

<!-- section_id: "03162203-7b21-4b2a-910e-20dcacce1633" -->
## Microservices with Separate Databases

Best for: Microservices architecture, each service has its own database

<!-- section_id: "c5ba79e2-c625-4018-a3b1-43591f9c4c64" -->
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

<!-- section_id: "8cf0b975-d8d8-46e2-beee-2252f7ce6a66" -->
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

<!-- section_id: "21587088-e249-4606-bba9-cfbe056ae323" -->
## Platform-Specific Structures

<!-- section_id: "3b8c7550-c43a-4ba6-bd85-53ecf34946bb" -->
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

<!-- section_id: "09259ceb-1138-4fa2-829b-913b0643c30c" -->
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

<!-- section_id: "cfbda658-77cd-413b-bbd2-7e70913bc4b1" -->
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

<!-- section_id: "67a18ae7-b0ee-4eb1-8ec9-0e826bb3a407" -->
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

<!-- section_id: "e501821f-b3d6-47e2-83a1-4ef261aad1aa" -->
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

<!-- section_id: "ce0c28b8-ab7c-48c5-ab12-dd2fb78dac0d" -->
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

<!-- section_id: "7fea25d5-51b0-45ba-948e-f666faa85aa2" -->
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

<!-- section_id: "1d8d28f1-88a1-4862-ad25-73c952787ba7" -->
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

<!-- section_id: "03ad4df3-6b52-4abf-b374-0b4134267f87" -->
## Common Directory Patterns

<!-- section_id: "11dfe948-9362-4890-85fd-1a1744bcf086" -->
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

<!-- section_id: "7dca7973-a23f-47c7-b34c-99c55cc7aa51" -->
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

<!-- section_id: "9857b82e-7d85-4e8d-b677-b5d81e0a2378" -->
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

<!-- section_id: "115d96ad-93c8-48e0-8006-857ced683481" -->
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

<!-- section_id: "b2dd95d7-3b04-436b-82bd-e49f44f801e1" -->
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

<!-- section_id: "72aa0cac-320f-4f5d-820c-25d0149c91bc" -->
## Best Practices

<!-- section_id: "a08479cf-3a2a-4158-9ce6-e6f4fce401c1" -->
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

<!-- section_id: "0046714f-3719-40bd-a9b3-6e05d11de086" -->
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

<!-- section_id: "add5d9a4-81ec-498c-9d38-e34460a1aa92" -->
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

<!-- section_id: "cedfed1c-0f5b-45b0-a635-63b2bc0c5288" -->
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

<!-- section_id: "254ee603-6397-42a8-adc4-9d843eb2821b" -->
## Recommended Structures by Project Type

<!-- section_id: "24aaa97e-1164-4c03-8d19-3dc8f5fc4167" -->
### Small Web Application
```
project/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── schema.sql
└── README.md
```

<!-- section_id: "58f8abbb-725a-4076-b742-e9528f62b7cc" -->
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

<!-- section_id: "5b3a4299-af32-4b4f-846d-0803a6af79c9" -->
### Microservices
```
monorepo/
├── services/
│   └── */database/migrations/
└── shared/
    └── database-utils/
```

<!-- section_id: "831a8d16-6500-4108-9d56-90c67c15f900" -->
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

