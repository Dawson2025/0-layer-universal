---
resource_id: "c5439573-01b6-4f4a-a056-27a4ddef36f8"
resource_type: "readme
document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "f71c8a92-0f93-4be6-bba6-e660287f6953" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "bc9a2ea0-2520-48cb-bbb5-55ab117bd93d" -->
## Why Database Version Control Matters

<!-- section_id: "51add821-b230-45d5-8f4f-5488dd3e7c98" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "8a510212-d1e6-4c0d-a76d-9ec19987746f" -->
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

<!-- section_id: "e6d486bc-01fe-408f-a8f0-41b001d6ef82" -->
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

<!-- section_id: "afedf191-a525-4209-8ff7-f2a74ca95504" -->
## Quick Start

<!-- section_id: "5acdbe02-075f-45d0-a764-076100fe69e8" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "2ae56d1a-2d8f-463f-822f-535105fc5da7" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "b27c56ce-f1a3-4b9c-bab0-5863bb81bb38" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "df4bec42-07a0-456c-9d64-3bbe3925b90f" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "51002b86-4ea5-4edc-958d-9e0baa66bd56" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "ef0a8174-33f7-4e1e-bbec-00aa30cf0fd0" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "4261ff29-6d4b-4795-8c67-9cd9a84d495d" -->
## Core Concepts

<!-- section_id: "df27d810-dd86-44f1-84b6-6211feb32642" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "c48498f7-8170-4d7d-b7f5-1be75f3ad1b8" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "d947826d-904a-444d-8a40-58209ce3d342" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "6cd95a00-ab9a-47f2-aff5-22223b964775" -->
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

<!-- section_id: "a4581863-f404-4c2f-8e3d-55065f28feb0" -->
## Platform Selection Guide

<!-- section_id: "8d32b0d3-fd39-4860-959b-7e95238f34c7" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "c1095ab2-526b-4a25-8100-f6bde15637ef" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "30419e1c-a36f-48b3-88c2-5471df9426c2" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "90e5ef38-3f76-4743-a5cf-ca02f5aa7c3f" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "6a4630a1-f737-4f07-bdec-82a9b5c02dff" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "4f8bdf6e-da13-43b5-8d54-8e3c9e774569" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "6044cdf5-257b-4185-9002-d230441d7435" -->
## Best Practices

<!-- section_id: "13d4327a-af16-4dbf-9929-9d97b6cfed6a" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "df1e54bc-ca00-4765-8e67-798c00899f3c" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "3f488f82-4344-4264-bd3a-2db4b5891e24" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "157733ae-f3c7-4cea-b47c-45ad80d4cc15" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "aed07f3a-2c37-4c73-930c-083c35fb4540" -->
## Tools Comparison

<!-- section_id: "42d7e226-e32f-46dd-9565-b1a843f2ec16" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "da2be1eb-fddb-4151-b46b-a7c0bcbf32de" -->
## Repository Structure

<!-- section_id: "62d48676-4dd8-46db-a943-5339a26990a1" -->
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

<!-- section_id: "b8337a0f-c48e-4fd6-9537-d84bd97b08da" -->
## CI/CD Integration

<!-- section_id: "09c5fa71-2f21-42dc-b378-fb45120de2ff" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "901f9cbc-86eb-4139-9826-74744ba89462" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "1384ba86-fcf3-4835-ac68-50da6e777c37" -->
## Common Issues

<!-- section_id: "3e0ba390-cfa7-4b56-b6ab-689ae285d8e9" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "d0f0bb53-893e-431c-a7b3-0259a18ada1a" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "f6eef8c5-2340-45c8-8c39-5cd5d8521347" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "39df45c7-fa02-40d2-9bcb-ec4d767d368f" -->
## Quick Reference

<!-- section_id: "9b41b18d-5b44-417b-954c-c021be79ecc0" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "40a0c8d6-63cc-46b1-8d96-9b6274c78280" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "4eae77aa-b961-4038-8175-4473428a7699" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "76d42db4-4dfa-4553-9145-43492477142c" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "f189ef8f-b1b0-48d3-98d1-2c6a2041f7e5" -->
## Resources

<!-- section_id: "ab091e7b-fc10-49d6-8934-30eb6087dc25" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "14a5c3ca-aee1-4ea5-a185-412a778507dd" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "5ead48ad-7597-4d92-b006-f7ac13e89890" -->
## Getting Help

<!-- section_id: "6cce5505-6111-4230-9784-22d32eab8f8f" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "35f4ede9-36a0-4c36-af24-d89c5e264c7d" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

