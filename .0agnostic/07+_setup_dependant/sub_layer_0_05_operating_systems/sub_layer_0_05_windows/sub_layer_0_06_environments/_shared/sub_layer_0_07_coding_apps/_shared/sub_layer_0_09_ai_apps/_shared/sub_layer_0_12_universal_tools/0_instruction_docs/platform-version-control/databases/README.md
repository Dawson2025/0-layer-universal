---
resource_id: "bb90b340-3edc-49d4-8f2c-b3eee2776a18"
resource_type: "readme
document"
resource_name: "README"
---
# Database Version Control System
*Comprehensive Documentation for Managing Database Changes Across Multiple Platforms*

<!-- section_id: "ff17aedc-d9df-49a8-8601-2681e09eea35" -->
## Overview

Database version control is the practice of managing changes to database schema, data, and configuration using version control systems (like Git) and migration tools. This system provides universal and platform-specific guidance for version controlling databases across modern platforms including Supabase, Firebase, Firestore, Google Cloud SQL, BigQuery, Vertex AI, and instant.db.

<!-- section_id: "4b95a5af-c7c7-4275-a0c1-81888e151c43" -->
## Why Database Version Control Matters

<!-- section_id: "54b794e2-3824-40a6-ab4e-3ffd9f0669f1" -->
### Key Benefits
- **Reproducibility**: Deploy the same database schema across all environments
- **Audit Trail**: Track every change to database structure and configuration
- **Collaboration**: Enable team members to work on database changes safely
- **Rollback Capability**: Quickly revert problematic changes
- **Documentation**: Database schema serves as living documentation
- **CI/CD Integration**: Automate database deployments
- **Conflict Prevention**: Detect and resolve schema conflicts before production

<!-- section_id: "4cb788fd-d3a1-44e4-896c-2bd665671e5f" -->
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

<!-- section_id: "b377eacf-a96d-490c-a701-f511ad0b159d" -->
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

<!-- section_id: "1a16932f-0ed9-46af-9781-6c8011b63036" -->
## Quick Start

<!-- section_id: "daff6eb4-b2a7-4eef-9fd6-4e34571a1333" -->
### 1. Understanding Core Concepts
Read the [Universal Database Version Control Guide](./universal-db-version-control-guide.md) for fundamental concepts and strategies applicable to all platforms.

<!-- section_id: "e72145ce-ddbf-482f-a9ee-323912f0adbc" -->
### 2. Platform-Specific Setup
Refer to [Platform-Specific Guides](./platform-specific-guides.md) for detailed setup instructions for your chosen database platform.

<!-- section_id: "591a5a38-80a7-4241-916d-b51c8b0048c2" -->
### 3. Choosing Tools
Review [Migration Tools Comparison](./migration-tools-comparison.md) to select the right tools for your project.

<!-- section_id: "7f87543d-de20-43a7-93f4-8bed9f493ea8" -->
### 4. Structuring Your Repo
Follow [Repository Structure Templates](./repo-structure-templates.md) to organize your database files.

<!-- section_id: "9739ba5a-dfaf-4827-812a-dc1366e9694d" -->
### 5. Automating Deployment
Use [CI/CD Integration Guide](./ci-cd-integration-guide.md) to automate database deployments.

<!-- section_id: "2766c5df-52eb-4af7-ae6a-262462873728" -->
### 6. Handling Issues
Consult [Troubleshooting Guide](./troubleshooting-guide.md) when encountering problems.

<!-- section_id: "bb5bea54-2247-4fda-a31f-35648642d78b" -->
## Core Concepts

<!-- section_id: "d5c9cb8e-e764-4c61-af18-97a52129a932" -->
### Migration-Based Approach
Every change to database schema is captured as a migration file that can be:
- Applied to databases
- Version controlled in Git
- Reviewed through PRs
- Rolled back if needed

<!-- section_id: "30688daf-c291-4358-9bff-2277161f9185" -->
### Schema vs Data Versioning
- **Schema Versioning**: Track structural changes (tables, columns, indexes, etc.)
- **Data Versioning**: Track data changes (seed data, backups, snapshots)

<!-- section_id: "52c62661-4770-4bb4-a1a9-e1bbacdaced1" -->
### State-Based vs Migration-Based
- **Migration-Based**: Each change is a migration that builds on previous migrations
- **State-Based**: Maintain the desired final state, tool generates migrations

<!-- section_id: "f408a505-124e-4b3b-8329-761878d2ff20" -->
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

<!-- section_id: "481a2746-149d-453f-88e0-848c34d29ec4" -->
## Platform Selection Guide

<!-- section_id: "bd5d613b-702d-4539-8577-765db7e2f07a" -->
### Choose Supabase If:
- You need PostgreSQL database
- You want built-in migration support
- You need real-time features
- You prefer Git-based workflows

<!-- section_id: "e7b8afce-3325-436a-85e3-2de5232edfc4" -->
### Choose Firebase/Firestore If:
- You need NoSQL database
- You want real-time synchronization
- You're building mobile/web apps
- You need serverless scaling

<!-- section_id: "5e95cc5d-d898-4bb5-9ab1-9ec5d5fd0fb1" -->
### Choose Cloud SQL If:
- You need managed MySQL/PostgreSQL
- You want enterprise features
- You're on Google Cloud Platform
- You need SQL compatibility

<!-- section_id: "bcb032ae-1a93-48bc-a510-c3178e3e5a0b" -->
### Choose BigQuery If:
- You're building data warehouses
- You need analytics and ML
- You handle large datasets
- You want SQL on NoSQL data

<!-- section_id: "fade4936-2947-4b4f-9adb-03715cc6a738" -->
### Choose Vertex AI If:
- You're building ML/AI systems
- You need model versioning
- You want pipeline automation
- You're doing research/development

<!-- section_id: "6d102270-c665-4ec4-a797-d413401f2f81" -->
### Choose instant.db If:
- You need rapid prototyping
- You want simple NoSQL setup
- You're building small projects
- You need quick iterations

<!-- section_id: "fdcf5fab-1523-46fa-91a3-65dae83c6673" -->
## Best Practices

<!-- section_id: "d2b83973-70e0-446f-8335-156ad23f8403" -->
### 1. Schema Versioning
- ✅ Keep all schema changes as migration files
- ✅ Use descriptive migration names
- ✅ Include both up and down migrations when possible
- ✅ Review migrations through pull requests
- ✅ Test migrations in development first

<!-- section_id: "98ac0d98-96c0-4b64-9be2-3be22e8bef43" -->
### 2. Data Management
- ✅ Separate seed data from migrations
- ✅ Use exports for backup and restore
- ✅ Keep snapshots in versioned storage (not Git)
- ✅ Document data dependencies

<!-- section_id: "3ea45b14-b88f-45f4-ad0b-7b395146c653" -->
### 3. CI/CD Integration
- ✅ Run migrations automatically on deployment
- ✅ Apply migrations to staging before production
- ✅ Have rollback procedures ready
- ✅ Monitor migration execution
- ✅ Alert on migration failures

<!-- section_id: "52048af2-23e8-491f-9835-0444bc6ba366" -->
### 4. Team Collaboration
- ✅ One migration per PR
- ✅ Review migration syntax and logic
- ✅ Discuss breaking changes in advance
- ✅ Document database changes
- ✅ Coordinate with other developers

<!-- section_id: "5968d20c-db53-4683-84ba-8183088095ad" -->
## Tools Comparison

<!-- section_id: "9c6fc572-0bfb-4653-a2a8-3edd0cf0538b" -->
### Migration Tools

| Tool | Platform Support | Features | Use Case |
|------|------------------|----------|----------|
| **Liquibase** | SQL, MongoDB | Diff, rollback, branching | Enterprise databases |
| **Flyway** | SQL databases | Simplicity, CI/CD integration | Java/Spring projects |
| **Supabase CLI** | PostgreSQL (Supabase) | Built-in, Git integration | Supabase projects |
| **Firebase CLI** | Firebase, Firestore | Config versioning | Firebase projects |
| **Bytebase** | All SQL databases | GUI, collaboration | Teams, visual management |

See [Migration Tools Comparison](./migration-tools-comparison.md) for detailed analysis.

<!-- section_id: "3cd66c9a-5686-43d7-907a-40e4e8aae45c" -->
## Repository Structure

<!-- section_id: "80f0fec7-7e87-407b-9d6f-0ef8bdaae543" -->
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

<!-- section_id: "461b2dc2-544a-477f-8cef-69cb52a8aed1" -->
## CI/CD Integration

<!-- section_id: "1d3eaf76-cda7-4055-a79e-07851ddcf741" -->
### GitHub Actions Example
```yaml
- name: Run migrations
  run: supabase db push
```

<!-- section_id: "1471258c-1509-49d3-92e5-11150d65a31e" -->
### GitLab CI/CD Example
```yaml
migrate:
  script:
    - firebase deploy --only database
```

See [CI/CD Integration Guide](./ci-cd-integration-guide.md) for complete examples.

<!-- section_id: "ce097e7a-37b3-4204-9a7a-6df06549a97a" -->
## Common Issues

<!-- section_id: "8204f0f0-fb3b-495f-8f57-ac3bc352acf6" -->
### Migration Conflicts
**Problem**: Multiple developers create conflicting migrations
**Solution**: Communicate schema changes, use feature branches, review PRs

<!-- section_id: "b58d0d6f-fbeb-40ec-bf3b-29bc051a3142" -->
### Failed Migrations
**Problem**: Migration fails in production
**Solution**: Always test first, have rollback ready, monitor carefully

<!-- section_id: "8ee0fca0-6756-4608-b9d0-e187100c7d1d" -->
### Data Inconsistency
**Problem**: Schema and data become out of sync
**Solution**: Enforce migrations, regular backups, validation scripts

See [Troubleshooting Guide](./troubleshooting-guide.md) for more issues and solutions.

<!-- section_id: "0ea15245-3b0a-4b99-82fa-037185558fe4" -->
## Quick Reference

<!-- section_id: "9e7bc2b7-7f7d-4a06-9171-563ab559d82a" -->
### Supabase
```bash
supabase migration new <name>
supabase db push
supabase db reset
```

<!-- section_id: "83479c97-e0aa-4d96-bac0-fb5445bbcd11" -->
### Firebase
```bash
firebase deploy --only database
firebase deploy --only firestore:rules
```

<!-- section_id: "46d8fbff-11a1-4152-a9cd-fa6d6b1fc328" -->
### Cloud SQL
```bash
flyway migrate
flyway undo
```

<!-- section_id: "10f3e6f5-0329-4404-b7d1-7d4abffc2f1b" -->
### BigQuery
```bash
bq query --use_legacy_sql=false < schema.sql
```

See [Platform-Specific Guides](./platform-specific-guides.md) for all commands.

<!-- section_id: "9e31fb94-9182-457d-a35c-3f6fc499af24" -->
## Resources

<!-- section_id: "c60e9452-1ffc-4980-887a-4fc5363bb324" -->
### Official Documentation
- Supabase: https://supabase.com/docs/guides/migrations
- Firebase: https://firebase.google.com/docs/cli
- Flyway: https://flywaydb.org/documentation
- Liquibase: https://www.liquibase.org/documentation
- Bytebase: https://www.bytebase.com/docs

<!-- section_id: "d5ff9ee6-3305-4d55-9b18-ef6237391181" -->
### Community
- GitHub Issues for each tool
- Stack Overflow tags
- Platform-specific forums

<!-- section_id: "752d42ba-146d-4a21-bd93-f07e1f6c0b01" -->
## Getting Help

<!-- section_id: "6aea77fc-7f82-4476-8863-47b18ec138ae" -->
### Finding Answers
1. Check [Troubleshooting Guide](./troubleshooting-guide.md)
2. Review platform-specific documentation
3. Search GitHub issues
4. Ask on relevant forums

<!-- section_id: "e1a10896-9c9a-4ab1-bdb1-ac5ab4d121d6" -->
### Contributing
If you have improvements or find issues:
- Document new patterns
- Share successful workflows
- Report tool issues
- Improve documentation

---

**Remember**: Database version control is about treating database changes like code - version them, review them, test them, and deploy them safely.

