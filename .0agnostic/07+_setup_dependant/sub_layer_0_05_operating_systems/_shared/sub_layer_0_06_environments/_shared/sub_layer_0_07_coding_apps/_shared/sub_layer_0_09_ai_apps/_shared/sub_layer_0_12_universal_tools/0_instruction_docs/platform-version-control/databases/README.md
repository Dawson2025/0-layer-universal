---
resource_id: "d88a2b1d-2f54-40d5-b435-1745310f2096"
resource_type: "readme_document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "de678fd5-c160-46e8-8ac8-2605bfd63f29" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "8afafea9-9a2d-4349-986d-93b3bddf6b1e" -->
## Why Database Version Control Matters

<!-- section_id: "d29d7ba1-b1a2-48cb-bd44-efb573602608" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "3c13b657-7cb1-4ea3-9380-9d643e08d5ad" -->
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

<!-- section_id: "bfc20c16-c78b-47a5-b77b-758e8764d457" -->
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

<!-- section_id: "9d853e1b-f12c-4071-b93a-7b6224f79663" -->
## Quick Start

<!-- section_id: "8a7aced5-34b8-4532-bc99-4beb6fbf71c5" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "9c5b7205-c611-4b0e-b10a-4b5d56a46b25" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "3a7b149d-b972-47eb-b2b2-e22a87558912" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "8ddcfc07-db2b-4c5e-bd19-91617f023f70" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "4c9f8e12-1aa5-472d-9db6-0f9407f54d07" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "42e5080d-8620-4e8e-8e29-b2fc914ba190" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "602fbdb3-6027-410d-84e5-ce8e96e77fb5" -->
## Core Concepts

<!-- section_id: "584bd221-426c-4d85-9b33-99a752407205" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "446d7e50-15de-48f6-b5b6-b8eca087eb31" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "ca19b1a2-1081-41b4-8445-4173e0a1f5b3" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "41173d9a-635e-4961-b5e3-50e08e8065ef" -->
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

<!-- section_id: "8997f586-dd30-4cb2-a3ac-623fedc057b0" -->
## Platform Selection Guide

<!-- section_id: "86bcdf77-7e4d-4127-947c-c48846fc73f7" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "2d3503a0-d6c8-41b5-b6ad-42fee931930a" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "7c2ea4cd-0dd1-4f9b-ab50-6b89a9425908" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "6652c0c1-ec2d-44e1-8ce5-450485a3ed3a" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "46ceb587-4ae1-4738-a095-4ceec4f60b78" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "90d564c8-cd2b-4cdb-b424-219d35aa7da2" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "22e115e1-9e3a-401d-8be8-7db225ad0e9a" -->
## Best Practices

<!-- section_id: "f9f7683a-ae2e-4c21-8bd5-8ba28248c484" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "5c366bf9-c644-421c-bfdc-730cdb1cd1ed" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "50141d60-9c46-4f3c-beee-1c2b36774d48" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "e0ea4d6b-d73c-4d8c-a47b-2ef826bcf670" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "df4a22ae-e157-4a41-9cd5-e5d162b3f06c" -->
## Tools Comparison

<!-- section_id: "02d761e1-66f0-4b13-8bec-2730d86255a4" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "80d21935-93e4-4a81-8a6b-e125312e2889" -->
## Repository Structure

<!-- section_id: "5b931117-1cbe-45e2-bd2c-4217a13e9d3e" -->
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

<!-- section_id: "3c90bc20-5d53-4b31-ac5c-e43fecf94464" -->
## CI/CD Integration

<!-- section_id: "b8fdfe05-ea0d-4e7a-af8e-3df68ddbd65a" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "ff9540ba-98c1-405a-af7d-cef26d9c2bda" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "a7485184-30d2-49ce-90ba-58e3ee2a23b8" -->
## Common Issues

<!-- section_id: "a732ffcf-88c9-48a5-b547-155f5552ca31" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "f1c094da-b5ea-4aa9-a490-ba3d1458249c" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "d4c1b58c-6487-4880-a84c-7a9db4d0f6f0" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "4ff4846f-8361-4180-8cdb-c5cee5a278b9" -->
## Quick Reference

<!-- section_id: "a5c3dddf-7d50-445b-91ad-9660d36454e4" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "3b5e5d54-f177-4bba-97f0-9fda9f8e0c3c" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "b3edb186-0ca3-4368-8c9a-528235e860d5" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "cc5e0839-7c3f-485c-aba1-8953aa363793" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "7e5be82c-8f41-4d77-8976-a38f00613768" -->
## Resources

<!-- section_id: "dfc80995-9157-4cd5-b694-5ac8d21368b5" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "2be55b9c-ee70-4403-8bf7-f40d616d48b1" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "b81bfc68-0eec-43a0-9694-937fab8de472" -->
## Getting Help

<!-- section_id: "1467f4a9-d7b9-476c-bbd1-65c46f609b96" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "febe7ecb-dcbd-43ab-b65a-e185904563f1" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

