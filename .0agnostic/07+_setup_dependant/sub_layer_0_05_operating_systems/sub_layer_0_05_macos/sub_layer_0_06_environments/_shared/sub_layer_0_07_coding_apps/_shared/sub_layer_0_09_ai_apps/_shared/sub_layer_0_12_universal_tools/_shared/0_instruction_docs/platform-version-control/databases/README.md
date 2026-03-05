---
resource_id: "c189159e-0ba9-4df6-9ac5-24785b327dce"
resource_type: "readme
document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "ef2b1a46-963d-431b-87a3-221fad9ec18c" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "feb6db23-8fd0-4e52-bc24-01e1479799c8" -->
## Why Database Version Control Matters

<!-- section_id: "3272c745-698c-4fb9-82c9-18fa3ad3e3c8" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "94b8b10b-cc8b-465f-9ef1-589b9d055deb" -->
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

<!-- section_id: "c964b1f6-53b0-4fa6-b935-c3162b80f25b" -->
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

<!-- section_id: "ec1ed083-8388-4dfd-9d65-eaf69bd8e3da" -->
## Quick Start

<!-- section_id: "3edbc3b3-c511-415d-a62b-7624db9c8ecf" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "c2506897-5a47-42a9-b844-1f95f04d8597" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "14c9c8a0-af3a-4496-9419-203c4823f5d5" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "9a6bae45-94a1-4a77-bcb1-fbaeed5862af" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "4482fca9-a40d-4406-97a7-db8e520d55af" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "049337a2-7f42-4a0e-92b2-c8074034d90f" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "4d160e93-f71c-4816-8495-943c73bf5982" -->
## Core Concepts

<!-- section_id: "3a17446e-4053-4e56-9cf8-ee7c274d79ac" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "60aca525-78fe-4794-b95d-42cc8e8273a6" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "26579c29-8468-475a-beb2-eb85dc1325ef" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "6a781b19-d1b8-4cf0-900d-63a1bbf1fee5" -->
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

<!-- section_id: "83739017-5dd3-4ea7-9cfc-a78a234c6782" -->
## Platform Selection Guide

<!-- section_id: "0222ec88-1d18-4e13-9c74-9b227e8b6e90" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "73c8a7d4-f0cc-4ad5-a1eb-e14eb3857452" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "159ce78c-1cae-49d6-9038-1a3370786a53" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "2fa28d08-442c-4449-b1f6-8af846fec556" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "e0eb555d-2717-4b0b-835a-565fea83b0b8" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "c426b432-c575-469b-baf1-012024f36c12" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "53ef79b9-90c3-4b65-a3fd-d547c5ff519c" -->
## Best Practices

<!-- section_id: "05bfd944-713b-46d0-8fef-d14d4a771ba3" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "5f80a211-362f-4cbe-8e12-373061709a8e" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "6985a4a8-445c-4e26-a8b9-1cd0f056eaa8" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "0605c118-9d5a-4b30-80a7-f9eae47a45f3" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "01fbb489-c481-43da-90e4-d2afb4c3022a" -->
## Tools Comparison

<!-- section_id: "01f453e4-7f34-4d23-abdd-0f2c53036eaf" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "502bf7e0-e678-4ba0-9ffd-8cf335765cb8" -->
## Repository Structure

<!-- section_id: "5f72e2f3-c6a4-49a5-a9a6-fcb60474e6e8" -->
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

<!-- section_id: "fc9a5979-713a-4db9-8c7c-23fb7418a2f8" -->
## CI/CD Integration

<!-- section_id: "31c2fe1a-7664-400a-a09b-b5cca829ce20" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "44f49549-ee34-4277-8250-a00802f25550" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "127e6510-eada-42d1-8bd5-2a1d05d30337" -->
## Common Issues

<!-- section_id: "f49f8da7-bbc7-4709-a1a2-d04b740852a0" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "b613d3c9-2259-4bab-96a3-1d9bc2a43c88" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "d937b937-4a6c-4c7e-855f-eb54b8cc3cab" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "83fd63bb-3505-42bc-b5f9-c97f67949e51" -->
## Quick Reference

<!-- section_id: "49546a70-2d72-490d-b4aa-c36c84576491" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "84cb805b-0991-4d0c-a197-5340898efb6f" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "47128c3e-9249-427b-abc2-f248df0ee12f" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "c7c036dc-52f1-4134-89e5-a0a2252c564e" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "0a221590-2734-405a-8278-6c4775f51635" -->
## Resources

<!-- section_id: "0b8e6896-77f3-4bb5-a9c8-d1b1f0babdd9" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "fb3da9f1-95b2-48f2-b27d-d1991a2e7707" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "c87b33f6-c474-449f-ab0b-f7fbc7d67240" -->
## Getting Help

<!-- section_id: "ba2ab89b-d157-4da4-bd88-11cf0eef54a0" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "73dce037-9705-48ea-b789-94a92c103cc7" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

