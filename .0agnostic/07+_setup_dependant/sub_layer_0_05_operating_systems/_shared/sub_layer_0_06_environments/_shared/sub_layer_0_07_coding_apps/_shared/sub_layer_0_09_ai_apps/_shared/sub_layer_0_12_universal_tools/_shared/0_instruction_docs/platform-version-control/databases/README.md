---
resource_id: "7de36932-78ae-44fb-86f1-843933d503c3"
resource_type: "readme
document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "9e6543fd-2e9a-441c-afb2-552750f14ffc" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "c716ebdb-9ebe-42e7-b707-60622d35b094" -->
## Why Database Version Control Matters

<!-- section_id: "210f20ef-5383-420a-99eb-9028bde34f32" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "d7b59ca8-343b-48a7-a465-37c91c32d3f1" -->
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

<!-- section_id: "a6ef56e9-450a-4a2d-b0c6-a12c68b4a43c" -->
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

<!-- section_id: "0d1c3f0e-bfe6-403a-8b6d-a41b07120145" -->
## Quick Start

<!-- section_id: "224b0fcf-6cf2-48fc-ada2-acf3998e2dc2" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "16a840f6-fdcd-45d7-bd14-e2c7191c5d34" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "694b9f73-67c6-48b8-8780-d2972fd48c2e" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "08e3c06f-d76d-4343-b4df-2d85f1ed6030" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "063ab5fb-666f-4995-8db1-807c2d724bea" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "337e499e-8495-4667-8048-b680fc52311a" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "7a5e1739-dcf4-4095-976a-7ce59303a617" -->
## Core Concepts

<!-- section_id: "7d08741c-abf2-4c3c-80c7-24d5a6ea1693" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "b933789c-588d-4b68-9ba1-d9b4bccb3f53" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "e91b971d-fc2f-4d94-96b1-a654fecb9262" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "d546a8a6-e87f-4e51-adc7-4e770d5a2770" -->
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

<!-- section_id: "885d9507-f678-4e3b-8ff4-ef3d5b121d95" -->
## Platform Selection Guide

<!-- section_id: "70059304-600c-49c6-a70e-5b6a5387e5dd" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "cd1c1889-03e9-4ddf-b179-5be1c4f641a9" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "4f33d8fc-3708-4827-8c15-82a28d6b8819" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "fee7f9a9-d7c2-4169-8544-2ee1fc17e0b4" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "45afcf0d-1834-454b-8d99-20630a709ed2" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "0e87ee5e-e53f-48a5-a07e-23aeb5cbbfef" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "4bc2d5cd-c64b-431c-aa8c-519d73ff8e7b" -->
## Best Practices

<!-- section_id: "fb8ada80-266c-4c2b-ac71-f50c470ba1c5" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "f22e843f-8c97-479a-ba3c-67893a9d48e9" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "966d798a-6f18-41c7-966c-bbafc410e6f1" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "deae0a9e-c819-4465-a892-f09563d4be7a" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "8c55cc43-6864-4876-a99e-c25a0110ab91" -->
## Tools Comparison

<!-- section_id: "69393abf-af1c-424b-b94d-7d56563a4987" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "8f5e00ae-ad56-440c-96f6-b4732d41e108" -->
## Repository Structure

<!-- section_id: "abf0584b-d2a4-4ecb-9516-4dd7f4f65a0b" -->
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

<!-- section_id: "4f43cd8c-6e37-4bad-bcf1-8e448507c9d2" -->
## CI/CD Integration

<!-- section_id: "8adcfd7f-118c-4edc-a108-2517b25de0ba" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "718af78d-2b6f-4fd1-886e-730c8cc062be" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "2d76ca5e-4984-4c47-a9a4-6dcd6af3069e" -->
## Common Issues

<!-- section_id: "f006f047-4baa-43d1-bfb9-f18b57ad1ce8" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "b660d0dd-5c31-4b7a-a126-5d7c72deaa41" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "6fddca9f-973b-4340-ad58-025785a686d9" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "d6c554e1-e163-4788-a320-19089c652f76" -->
## Quick Reference

<!-- section_id: "9408ec89-c510-4038-a349-2bfc566bf0cc" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "f2c83384-72e5-466d-b06b-127c4027b4dd" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "0931d82f-dbc9-4888-b727-552aa9664247" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "c139e881-234c-4f63-abc3-75072a5347ac" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "d8fed531-7ff2-4f12-8a8f-a34a469d8242" -->
## Resources

<!-- section_id: "b112cec0-d680-435f-94d6-2ffba1da421b" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "7957e5fe-7d59-4bec-aac4-e8303f3cc5db" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "0bb77e37-d242-498d-93f7-34786bff2b4d" -->
## Getting Help

<!-- section_id: "271bed80-2059-4dc2-aa45-32502af8a127" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "b3f3015d-f676-43c6-b276-abb1e4f03cb2" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

