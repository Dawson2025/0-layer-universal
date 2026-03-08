---
resource_id: "d6352507-2f26-412c-9fa6-3cba7b6ae0a8"
resource_type: "readme_document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "31651908-d473-4223-b134-cb0d65370f7d" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "fd5fc11f-76af-4fcc-a25e-931869abc479" -->
## Why Database Version Control Matters

<!-- section_id: "ee063235-3f8d-4aee-b5ad-92329c439c5d" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "880d43c2-4d94-41f0-a5da-152ffdc89a5b" -->
## Supported Platforms

| Platform | Database Type | Primary Tool | Migration Format |
|----------|---------------|--------------|------------------|
| **Supabase** | PostgreSQL | Supabase CLI | SQL Migrations |
| **Firebase** | Realtime Database | Firebase CLI | JSON Config |
| **Firestore** | NoSQL | Firebase CLI | Indexes + Rules |
| **Cloud SQL (GCP)** | MySQL/PostgreSQL | Flyway/Liquibase | SQL Migrations |
| **BigQuery** | Data Warehouse | BigQuery CLI | SQL/JSON |
| **Vertex AI** | ML Models | Vertex AI Tools | YAML/Python |
| **instant.db** | NoSQL | instant.db CLI | JSON |

<!-- section_id: "f0cbed62-eef6-4b72-bd46-f7a93e62cc36" -->
## Documentation Structure

```
database-version-control/
├── README.md                          # This overview
├── universal-db-version-control-guide.md  # Core concepts and universal practices
├── platform-specific-guides.md        # Detailed per-platform workflows
├── migration-tools-comparison.md      # Tool selection and comparison
├── repo-structure-templates.md        # Repository organization patterns
├── ci-cd-integration-guide.md         # Automation and deployment
└── troubleshooting-guide.md           # Common issues and solutions
```

<!-- section_id: "e6576dfc-2bf2-4bcf-8b3f-3bb933c97f5e" -->
## Quick Start

<!-- section_id: "9ae269ef-9274-4b0e-ba58-6135931e16d5" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "c7b05077-d735-459d-98c2-344bcc80493b" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "c07d6a0c-17cf-4ce1-82b0-6df50906c1ad" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "1063321c-b513-4c0b-afc8-14f17174f4a1" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "724031ff-011d-4838-bcae-1113f1262af4" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "df964d49-2687-4e17-8be5-bae0e6efbda3" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "820ac3d0-32ef-4ada-b48c-3a465316c981" -->
## Core Concepts

<!-- section_id: "a8c9bbad-9fde-4ebc-9fe5-8100d4b003df" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "1906daf5-14e4-4783-996b-86eb5d442314" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "41829b25-2709-4466-80f2-c8cbf86e5419" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "14250cd1-3023-48b5-a303-2c0e302a59af" -->
## Common Workflow

```
1. Create Migration
   ↓
2. Review in Pull Request
   ↓
3. Test in Development Environment
   ↓
4. Deploy to Staging
   ↓
5. Test in Staging
   ↓
6. Deploy to Production
   ↓
7. Monitor and Verify
```

<!-- section_id: "bd30d31b-cbe5-4b94-afcb-6f2cd82d59b9" -->
## Platform Selection Guide

<!-- section_id: "d04d9c11-43a0-43fd-82fb-eed0eaa500bf" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "846d3760-41f4-4745-9507-82ff6bab7393" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "ddd65f30-e161-4c50-a029-6ed9535a294e" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "fb1b88eb-84c8-402c-b703-2bc07bba843a" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "7e777f64-5d95-463b-b25c-1d26e90759fe" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "e3ba5487-c551-42d3-bc2d-eff9a997ec94" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "1cddfcaa-05db-46fb-a406-512a13107795" -->
## Best Practices

<!-- section_id: "614826ab-afa4-4a0e-9d49-f20a0d68ffea" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "c8356562-bb8d-46ec-98b8-3457c93cc1c2" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "7de5e0de-0ca2-4534-b1bd-16a8a7a76f2f" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "82be1655-bcb3-4179-9eea-62d3b4a3f58c" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "56d83afb-3ea4-4c7e-bf96-2b8fb1171cbd" -->
## Tools Comparison

<!-- section_id: "b13d04eb-b622-402d-9414-ceee629c1278" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "a855501e-9994-4066-91f0-bd5cd2847716" -->
## Repository Structure

<!-- section_id: "57c525a2-79c9-4157-a5fc-317ae69ea717" -->
### Recommended Structure
```
/db/
  /migrations/
    20251027-add-users-table.sql
    20251028-change-orders-index.sql
  /schema/
    schema.sql
    firestore-indexes.json
    instantdb-schema.json
  /seed/
    seed-users.sql
    seed-products.json
  /config/
    supabase.env
    firebase.json
    vertex-pipeline.yaml
```

See [Repository Structure Templates](./repo-structure-templates.md) for complete examples.

<!-- section_id: "9cfd3680-468a-4a27-9409-cc70f769369f" -->
## CI/CD Integration

<!-- section_id: "b8fe4629-b2ea-4254-b539-f07c3759073f" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "023499a3-81fa-4325-8758-06fc4cab5815" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "63a4e0ca-3c13-4c7b-af9c-82724b56eb1e" -->
## Common Issues

<!-- section_id: "b9e36ff0-004c-424a-a4cc-9cf5c2e45fa7" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "5f921b2d-95dc-4954-bb95-7260c0cfc579" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "3e0e349b-7b3f-4461-828e-092caa4ae0c2" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "5d95d329-c86b-4c8c-aa63-1fb02d53a41a" -->
## Quick Reference

<!-- section_id: "98f0fdee-ba05-4c38-b80f-7d4b958ab644" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "2a8375f2-68c5-41ec-9f2b-ebc3c1e7c5ec" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "cf8833b1-b4d9-44eb-818b-b628316b9992" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "97190bdb-e5fb-404c-9015-bec4aa93cc1a" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "2eef7066-3eb1-4b24-bf58-fc24df944914" -->
## Resources

<!-- section_id: "b06b49eb-3df6-41a2-928f-f6a39dfd799b" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "15a04fee-3599-4f2c-b0d4-17250c9f33d3" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "becb2485-4de3-44c1-b264-f74500911bdd" -->
## Getting Help

<!-- section_id: "5d56217e-9ac4-410a-994c-7f53d35e8bba" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "d42bd5a3-76ef-4685-8a47-811dbe4201c9" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

