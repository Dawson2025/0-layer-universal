---
resource_id: "0fa24ad3-1c0e-4b4e-ab96-5f7ceab267be"
resource_type: "readme_document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "b7b03155-1be4-46d9-9894-970cf1c90210" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "f8f97a74-a9ef-4d63-9440-a3d4faf9a74b" -->
## Why Database Version Control Matters

<!-- section_id: "47fe4128-7cff-4325-8cfc-7b0ee82d82a4" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "de1c8dc2-19ea-443f-8df4-8df5d0659614" -->
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

<!-- section_id: "19d31f70-6270-4cd1-a597-e8de24f1f038" -->
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

<!-- section_id: "e4000ccf-06fe-478c-8735-c528bf04a235" -->
## Quick Start

<!-- section_id: "811f4404-610d-49bf-93ae-f532379cdcdb" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "e2a58cc5-e4b8-4cd6-a466-7590612dbd0b" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "0091e938-93db-4734-9af2-c1bde32711c0" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "2e73746e-c535-431f-a0aa-d3268014baa7" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "e618e949-1c2a-43ff-8461-a265a188b581" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "297090de-fbf4-4cea-b794-e7360e734a2d" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "1e3e2783-ff4b-4d5a-a9e3-0f92128f06c2" -->
## Core Concepts

<!-- section_id: "8d26dd32-3237-4142-8636-c556ed204e47" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "1e5955ad-a4c0-418c-82bd-e4f34587705a" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "e50dd4fb-7a84-4f55-967b-c72d416ee17b" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "3f9ed031-2158-44d1-aad5-e7a5c656cd8b" -->
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

<!-- section_id: "0faf67a5-2711-4bab-b14d-586bfd770529" -->
## Platform Selection Guide

<!-- section_id: "3655e959-ce52-4056-a559-10d6dc2dbc7d" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "2732e87b-db2e-44dd-a972-34b27c1c8f11" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "573311de-e6ae-40fb-8af7-540f63730ef0" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "c74307ba-dbee-45f1-afc2-eb0fcde852ec" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "0c5a62ba-71bd-4175-8ed6-c51565a272e3" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "8625e297-ea54-4801-a3f7-7fab3ac81f8d" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "2e81706d-d3d0-40a0-bc17-96329e6b7d60" -->
## Best Practices

<!-- section_id: "4c90984f-bc6f-4763-8b18-232c454f5089" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "794557e7-b0c7-4334-8714-5af197e57e09" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "99a86136-a415-4533-95dc-03aca704404a" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "882e4773-b6bd-4b68-a074-827b47072be3" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "d669d028-7371-4358-b976-5dd9301eb990" -->
## Tools Comparison

<!-- section_id: "e2af73d1-659d-4d8a-983d-c66fe21954cb" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "c8a76938-095f-4157-9e7f-a6b23fd5d114" -->
## Repository Structure

<!-- section_id: "c703d7c8-b205-4e46-abc6-b40a9100e24c" -->
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

<!-- section_id: "bc092722-68f9-4014-9a33-34d632d38cbd" -->
## CI/CD Integration

<!-- section_id: "4b011f98-6e1e-4dd0-90a0-e3e5cbd25dd9" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "7fcbd8d6-1320-4e30-af3e-2e75d0725ef5" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "d765c2f4-d03f-4e5f-880b-ceed7784635c" -->
## Common Issues

<!-- section_id: "92863835-b7fd-41bf-a39c-139e56b4690b" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "2752ecb3-1459-4e38-a3e4-7c54a635f27a" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "8074b183-7182-4a48-8276-ce5d0a6d51aa" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "d8912a89-61d8-4296-87c5-f9f780fc6c5a" -->
## Quick Reference

<!-- section_id: "de1ebd25-6cc6-4422-81e0-dac45feb0f5d" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "c10f1f8a-257e-4e65-a973-98b762b64570" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "9a099ff3-7635-4956-b7da-dad9abd1e43a" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "935c8e00-28ef-4eee-a271-53ca721f1ae3" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "a25e86de-13c6-4c70-b9c4-0cbf043ecdd3" -->
## Resources

<!-- section_id: "c1b80a98-3bc8-4bf6-941b-fb19ce87fad5" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "f18db4ab-2d68-4b03-95b5-dfc786620f4d" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "6a5278cb-eef4-4ba9-b063-0dcac63325e6" -->
## Getting Help

<!-- section_id: "7eb5fefb-cf4a-43fe-ace5-274c18c7a1c0" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "fcf2e443-8d64-48f9-9e71-daebfbbf0f43" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

