---
resource_id: "7b1dc22f-edaa-46c0-94b6-d8c34adb3d6e"
resource_type: "readme_document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "8118b0c5-6e6c-48f7-9177-43e20b90389a" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "80ef5bc4-7df2-4ce4-978f-51827eccfeb7" -->
## Why Database Version Control Matters

<!-- section_id: "b2c2547f-5eba-429c-b78c-88decaa1dbbb" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "653271ba-d1d1-4316-854c-9a2e82245ad4" -->
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

<!-- section_id: "725f5303-d92b-47a5-9a8d-a787506363b4" -->
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

<!-- section_id: "55f15059-d41b-4e06-9e1f-12f7fc230ca1" -->
## Quick Start

<!-- section_id: "37fc749b-1786-4182-8b14-0b3b5cf15229" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "24e74528-c095-44eb-ae51-9e9452d0a78f" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "bcb8812b-3460-4e31-833f-9bdedfd9acf8" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "03c478b7-8318-4ef9-84eb-44556130e6aa" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "c8341922-853b-4357-aee8-a77199ea61ce" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "491b53ff-c3f1-44e6-a348-ee1739cc4def" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "0b85ce4e-f1d7-4dc4-b2d8-4ea5777a1de4" -->
## Core Concepts

<!-- section_id: "3aaf89e6-f32a-44a3-9f1c-93a90d83b7c1" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "cbc71f4f-25bf-4880-b2fd-91c89f478386" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "8efbd6fb-8025-42ad-ae27-950f31142713" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "c8c559b5-49ec-45a6-8b3f-7ea29080746e" -->
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

<!-- section_id: "eaf786a9-eb22-4b5f-98af-05f8fc5ef005" -->
## Platform Selection Guide

<!-- section_id: "4e1311b5-363c-44e0-a25c-3cdc28cab264" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "cd0476df-1eef-4929-97b3-c654d7b5944d" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "741b34f8-cad8-4e8f-8919-d757a66ab146" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "57928a09-99eb-4ddd-96a9-0bf110ae9c56" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "d27b06c4-0d4c-40b1-bac5-bde69464abd5" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "7cc7fe4c-ab0b-447d-813a-ed3e1c2bca75" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "f81077d7-5b06-4948-bf70-143caa66c1c6" -->
## Best Practices

<!-- section_id: "888f45d0-d314-46f1-9710-5da45a2967ff" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "5dc05491-a3b0-4456-a287-dba3e1888a13" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "004efb76-3870-4ef3-86b0-e28e70f41b5d" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "a2009302-ce7d-4109-8d52-f9f7280544cb" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "f1fc48aa-3429-4b6e-a7b4-03e20d1acb1a" -->
## Tools Comparison

<!-- section_id: "59807ded-3443-4752-b8b1-9b0dfb0679d4" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "700eef53-71ea-4f15-befa-313d5726d1e3" -->
## Repository Structure

<!-- section_id: "1c62a14d-842d-4935-b7f0-c4713daf0603" -->
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

<!-- section_id: "63dcd1ce-a79e-466e-86d5-8ae02bb9c256" -->
## CI/CD Integration

<!-- section_id: "c6c73421-d2a0-4da3-92cf-ab2582f18a97" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "8c97ce5f-28fb-4e33-8349-0c87ba10ae51" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "978027ce-c912-45ab-94c7-115797524164" -->
## Common Issues

<!-- section_id: "da0d44a3-d430-4f3e-a1da-ffd4f267bc46" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "2a440a00-f339-4bda-936c-0eb738e7303e" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "1b376a36-9145-48ce-8365-32cc1373533d" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "f67d7145-810f-41d1-93ce-dc419aed3cd4" -->
## Quick Reference

<!-- section_id: "8cc1e779-1a47-4c71-9178-65d4a0d3ebef" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "d91ca8e8-f3b1-44bc-9fa0-4dea06d83e78" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "554c66f8-a4ec-45cd-a438-c0eb1e6cb000" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "d804f244-4195-405d-a296-a9466644bd2c" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "8d47df8c-d98d-4d06-8a43-5ca9ab27a1fe" -->
## Resources

<!-- section_id: "bd36fdc2-d588-4105-8a32-3ab15a912e13" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "95e2142f-4e57-464d-ab5f-8a88d873ea72" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "23d41d65-e559-478a-977c-1a4de27c34f7" -->
## Getting Help

<!-- section_id: "26865ebf-7d64-4a48-9bb3-7c588005bfcd" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "d21fc3b9-0423-4575-a2c7-4b206c97d033" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

