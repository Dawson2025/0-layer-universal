---
resource_id: "0a2932b1-572d-4bc7-ab68-f37ba20f221f"
resource_type: "readme_document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "c29a48db-4e7a-41f5-9c3b-8215383426ac" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "fea48d35-56d2-4948-93b5-2b43720e94b7" -->
## Why Database Version Control Matters

<!-- section_id: "27122eb0-40a8-4a29-b25b-b04ebc7ba742" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "fe8991d7-549b-4371-b468-09611c43ae8a" -->
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

<!-- section_id: "5e0518f0-4938-4244-929b-39940a95e4fd" -->
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

<!-- section_id: "cef7dc8d-2c5a-41b8-bea5-f486949dd749" -->
## Quick Start

<!-- section_id: "8a18cc1d-dcc6-437e-a438-3fa1dd7c5d60" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "4eeed7ca-0220-4268-ae44-608a691d4131" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "50fbf9b8-430f-4a9c-ad24-9661b8964da7" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "375a23e4-fec4-48a3-a16a-d8700341be6c" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "61dcda2d-000d-4b9f-a4d9-3694b88d725e" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "63d1a7a7-450b-4811-89b5-c151d6dcd373" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "dc573ac5-697f-4ccf-bf11-ee247a46a538" -->
## Core Concepts

<!-- section_id: "2308101b-5a84-4054-a08d-19f7e1ba1d99" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "1e5a7cfb-7015-4daf-bbdd-5ed5d9243ca1" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "00cf4773-cfb4-4536-946b-1c985e9df129" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "5c7ecb28-9e51-40e3-abc0-daaa3cb56a54" -->
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

<!-- section_id: "c5c77808-b4a0-4f91-a54c-0eaa7c15a3ea" -->
## Platform Selection Guide

<!-- section_id: "7a0cc55d-fe28-4063-b487-49eb1d4c9229" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "5c5955d6-3ec4-4a4c-82f9-67810fbdee81" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "478eb1e1-8636-4ff1-9e01-7fea59d77afd" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "cff89d21-74ce-4594-b7b6-7daa4b9661fc" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "11e1800c-858d-41e5-82bc-42c6bd7f0705" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "689ba5f2-1fb9-4443-a719-21cb609239d7" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "40bcc492-bc93-441a-9ba0-0e45f689a183" -->
## Best Practices

<!-- section_id: "e88ca745-7038-48ce-8a27-454a06c9906b" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "1616b829-3008-4761-a8a9-e3b594f74553" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "2e9a08d8-e238-4b73-85a6-3894785b970f" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "7867c547-0274-4825-a5a6-a4510a53a68f" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "56e36896-f8a4-4b45-a50d-558dafa5de7f" -->
## Tools Comparison

<!-- section_id: "12b2781c-0502-4720-b780-eb7b256cb2fb" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "d0c9060b-b821-4fba-967c-a72cabe3519f" -->
## Repository Structure

<!-- section_id: "946594cc-95fe-43b5-8b25-35a137d45af4" -->
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

<!-- section_id: "576f5612-4267-4583-9bdb-c34bd22685ce" -->
## CI/CD Integration

<!-- section_id: "1e0b0a06-25df-484b-a41b-5174222a8488" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "eccfe3ea-537b-4497-b1d3-2682dd0752d8" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "88ab8b11-1f42-4b19-b68c-714b1051a679" -->
## Common Issues

<!-- section_id: "d44af968-a384-419f-b938-b7fa250cd21f" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "ed0cb91d-844f-4558-b406-7d2c43254532" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "55165916-c369-4a0d-a310-a0abf2975c01" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "066d5643-aae5-488b-8344-974db3649d19" -->
## Quick Reference

<!-- section_id: "72019fd1-1914-4516-bcb4-a51059ff218d" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "73122799-39db-4496-b5aa-5461bdcbb88f" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "114e0a77-4d6a-4035-a4fb-b15603c8f68b" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "9199b8c5-40a4-492d-a55c-7181e6248be4" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "e6594867-c2ef-4765-856b-f6db4988708e" -->
## Resources

<!-- section_id: "17ad65bc-59ba-469d-a1e3-99b5201fbb2c" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "e1c83900-8361-4039-b8a1-3380464afd80" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "13b2ea2e-5f76-48a8-ac1c-099cd3bf92c1" -->
## Getting Help

<!-- section_id: "a123600a-4aa5-46c3-b9ee-aee613158d68" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "0d544f98-ba7e-4824-b2e0-e8a68162ccbc" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

