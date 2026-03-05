---
resource_id: "14ad92e7-3349-455d-84dd-ed83e04e77e7"
resource_type: "document"
resource_name: "universal-db-version-control-guide"
---
# Universal Database Version Control Guide
*Core Concepts and Practices for All Database Platforms*

<!-- section_id: "f86c17f3-1ba7-4988-a12a-5aeee87750dc" -->
## Overview

This guide covers universal concepts and practices for database version control that apply to all platforms. Whether you're working with PostgreSQL, NoSQL, data warehouses, or ML pipelines, these principles will help you manage database changes effectively.

<!-- section_id: "3e5d0c45-2e46-4ec6-b23c-69be5b08102d" -->
## Core Concepts

<!-- section_id: "accd9922-1517-40ab-ba07-40fdde662b69" -->
### What is Database Version Control?

Database version control is the practice of managing database schema changes, configuration, and data migrations using version control systems (like Git) and automated migration tools. It treats database changes as code, making them:
- **Reviewable**: Changes go through pull requests
- **Testable**: Changes can be tested in isolation
- **Reversible**: Changes can be rolled back
- **Traceable**: History of all changes is maintained

<!-- section_id: "c26f4b4a-41f0-40aa-a960-de2f0a41ceb1" -->
### Why Version Control Databases?

#### Problems Without Version Control
- Manual, error-prone schema changes
- No audit trail of changes
- Difficult to roll back mistakes
- Hard to coordinate team changes
- Inconsistent database states across environments
- No way to test changes safely

#### Benefits With Version Control
- Automated, reproducible deployments
- Complete history of all changes
- Easy rollbacks when needed
- Team coordination through PRs
- Consistent database states
- Safe testing in isolation

<!-- section_id: "871eee38-2f0c-427c-bcbb-62f9ebb781ce" -->
## Approaches to Database Version Control

<!-- section_id: "f1d16ee1-6da3-4329-9f18-e5a433083d7b" -->
### 1. Migration-Based Approach

**How It Works**: Each database change is captured as a migration file that describes how to transform the database from one state to another.

**Characteristics**:
- Each migration has a unique identifier (usually timestamp)
- Migrations are applied sequentially
- Each migration is immutable once applied
- Migrations can include both schema and data changes

**Example**:
```sql
-- Migration: 20251027-001-add-users-table.sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

**Advantages**:
- Complete history of all changes
- Can reproduce exact database state
- Easy to understand what changed
- Works well with CI/CD
- Supports rollbacks

**Disadvantages**:
- Must maintain sequential order
- Difficult to modify after applying
- Can accumulate technical debt
- Requires discipline

<!-- section_id: "be87941a-09c2-443b-b5e1-a11d7e1823e2" -->
### 2. State-Based Approach

**How It Works**: Maintain a single source of truth (the desired final state) and generate migrations automatically by diffing current state vs desired state.

**Characteristics**:
- Define desired database state as a schema file
- Tool automatically generates migrations
- Each deployment compares current vs desired
- Creates migrations only for differences

**Example**:
```yaml
# desired-schema.yaml
tables:
  - name: users
    columns:
      - name: id
        type: UUID
        primary_key: true
      - name: email
        type: VARCHAR(255)
        unique: true
```

**Advantages**:
- Simpler mental model
- Less migration files to manage
- Automatically handles new vs existing
- Good for small teams

**Disadvantages**:
- Less control over specific migrations
- Harder to review generated migrations
- Can lose history of change intent
- May generate unexpected migrations

<!-- section_id: "e5bbed32-62f2-4fe6-8ddf-ef423622be0a" -->
### 3. Hybrid Approach

**How It Works**: Use state-based for schema definition but migration-based for complex or critical changes.

**Characteristics**:
- Maintain schema files for structure
- Create migrations for complex changes
- Combine both approaches as needed
- Best of both worlds

**Advantages**:
- Flexibility to choose approach
- Control when needed
- Simplicity for routine changes
- Safety for complex changes

<!-- section_id: "ca363d1e-8b5e-4a6f-8ce2-95271aea6184" -->
## Version Control Strategies

<!-- section_id: "0e6cffb1-df4c-4ef3-8b58-2a42eb76ff33" -->
### 1. Schema Versioning

Schema versioning tracks structural changes to your database:

#### What to Version
- Table creation and deletion
- Column additions, modifications, deletions
- Index creation and deletion
- Constraints (foreign keys, checks, etc.)
- Views, functions, procedures
- Triggers
- Sequences

#### Best Practices
```sql
-- ✅ Good: Descriptive migration
-- File: 20251027-001-create-users-table.sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);

-- ❌ Bad: Vague or combined changes
CREATE TABLE users (...); -- What does this do?
```

<!-- section_id: "554f75e5-0e14-4033-870c-0b0902311484" -->
### 2. Data Versioning

Data versioning tracks data changes:

#### What to Version
- Seed data for development
- Reference data
- Test fixtures
- Configuration data
- Lookup tables

#### Best Practices
```sql
-- ✅ Good: Organized seed data
-- File: seed/users.sql
INSERT INTO users (email, password_hash) VALUES
  ('test@example.com', '$2a$10$...'),
  ('admin@example.com', '$2a$10$...')
ON CONFLICT (email) DO NOTHING;

-- ❌ Bad: Inline seed data in migrations
-- Better: Separate seed files or dedicated seed commands
```

<!-- section_id: "826561ed-e48e-4e40-b81d-4bd2f7dbca91" -->
### 3. Configuration Versioning

Configuration versioning tracks non-schema, non-data changes:

#### What to Version
- Database connection settings
- Security rules (Firebase, Supabase RLS)
- Index definitions
- Replication settings
- Feature flags
- Environment-specific configs

#### Example: Firebase Rules
```javascript
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read: if request.auth != null;
      allow write: if request.auth.uid == userId;
    }
  }
}
```

<!-- section_id: "20f30a54-8520-4c26-bf53-3589fbe2dce1" -->
## Migration Workflows

<!-- section_id: "ccc0b9e6-3625-4995-b1bf-1d566bc69a77" -->
### Basic Migration Lifecycle

```
1. Create Migration File
   ↓
2. Write Migration SQL/Config
   ↓
3. Commit to Git
   ↓
4. Create Pull Request
   ↓
5. Review and Approve
   ↓
6. Merge to Main
   ↓
7. Apply to Environments
   ↓
8. Verify Success
```

<!-- section_id: "3f9296e5-9acc-4ee2-a0d3-268af5ae1523" -->
### Environment Promotion

Typical environment flow:
```
Development → Staging → Production
```

**Development**:
- Test new migrations
- Verify migrations work
- Check for conflicts
- Validate schema changes

**Staging**:
- Apply migrations automatically
- Test with production-like data
- Performance testing
- Security review

**Production**:
- Apply migrations carefully
- Monitor execution
- Verify results
- Have rollback ready

<!-- section_id: "64853374-40cb-4ddd-91ca-105117649ef5" -->
### Rollback Procedures

#### Preventive Measures
- Always test migrations first
- Keep backups before applying
- Use transactions when possible
- Test rollback procedures
- Document rollback steps

#### Rollback Strategies

**1. Down Migrations**
```sql
-- up migration: 20251027-001-add-created-at-column.sql
ALTER TABLE users ADD COLUMN created_at TIMESTAMP;

-- down migration: 20251027-001-add-created-at-column.sql
ALTER TABLE users DROP COLUMN created_at;
```

**2. Backup and Restore**
```bash
# Before applying migration
pg_dump database > backup.sql

# If migration fails
psql database < backup.sql
```

**3. Feature Flags**
```sql
-- Deploy code first, then data
ALTER TABLE users ADD COLUMN status VARCHAR(50);

-- In application code
SELECT * FROM users WHERE (status = 'active' OR status IS NULL);
```

<!-- section_id: "ff38cf44-b31c-4636-bba2-8004a8ec7ecd" -->
## Database Change Patterns

<!-- section_id: "2f276795-57a2-447a-b4f6-248715fab05b" -->
### 1. Safe Changes (No Downtime)

These changes can be made without application downtime:
- Adding new tables
- Adding new columns (nullable)
- Adding new indexes (create concurrently)
- Adding new views
- Adding new functions
- Decreasing constraints

<!-- section_id: "a4ed3a13-7ab7-40b8-a3de-abaca3ad79c6" -->
### 2. Breaking Changes (Require Coordination)

These changes require application coordination:
- Dropping columns (deprecate first)
- Renaming columns (add new, migrate, drop old)
- Changing column types (gradual migration)
- Adding NOT NULL constraints (make nullable first)
- Dropping tables (prevent access first)

<!-- section_id: "dd5854d8-ff6d-4540-93b3-e5277c63d653" -->
### 3. Data Migrations

Moving or transforming data:

#### Simple Data Migration
```sql
-- Update existing data
UPDATE users SET status = 'active' WHERE status IS NULL;
```

#### Complex Data Migration
```sql
-- Create new column
ALTER TABLE users ADD COLUMN status_new VARCHAR(50);

-- Migrate data
UPDATE users SET status_new = 
  CASE 
    WHEN is_active = true THEN 'active'
    WHEN is_active = false THEN 'inactive'
  END;

-- Verify migration
SELECT COUNT(*) FROM users WHERE status_new IS NULL;

-- Switch columns
ALTER TABLE users RENAME COLUMN status TO status_old;
ALTER TABLE users RENAME COLUMN status_new TO status;
ALTER TABLE users DROP COLUMN status_old;
```

<!-- section_id: "6623f2cd-332b-4ba0-88a2-4fc76567a52a" -->
## Best Practices

<!-- section_id: "cec767cc-ecad-486e-bf49-99fe45164f6a" -->
### 1. Naming Conventions

#### Migration Files
```
✅ Good: 20251027-143022-create-users-table.sql
✅ Good: 20251027-001-create-users-table.sql
✅ Good: 20251027_add_users_table.sql

❌ Bad: migration.sql
❌ Bad: users.sql
❌ Bad: change.sql
```

#### Commit Messages
```
✅ Good: "Add users table with email and password fields"
✅ Good: "Update users table to support OAuth"

❌ Bad: "Changes"
❌ Bad: "WIP"
❌ Bad: "Update db"
```

<!-- section_id: "dcbc7f55-89ec-4e1b-93ce-904ea9738497" -->
### 2. Review Process

#### What to Review
- SQL syntax and logic
- Performance implications
- Index usage
- Data integrity
- Breaking changes
- Rollback procedures

#### Review Checklist
- [ ] Migration has descriptive name
- [ ] Migration includes both up and down
- [ ] No hardcoded values
- [ ] Indexes are appropriate
- [ ] Foreign keys are correct
- [ ] Performance impact considered
- [ ] Documentation updated
- [ ] Rollback tested

<!-- section_id: "b997a308-836a-4dc1-a6f7-f3155b8f740d" -->
### 3. Testing Migrations

#### Unit Testing
- Test migration in isolation
- Verify SQL syntax
- Check constraints
- Validate indexes

#### Integration Testing
- Apply migration to test database
- Verify data integrity
- Check application compatibility
- Test rollback

#### Performance Testing
- Test on production-like data
- Measure execution time
- Monitor resource usage
- Check for locking issues

<!-- section_id: "c51afc8c-4fcd-41a6-ab1a-86085493e197" -->
### 4. Documentation

#### Migration Comments
```sql
-- Migration: Add user authentication fields
-- Date: 2025-10-27
-- Author: John Doe
-- Description: Adds email and password_hash fields to users table
-- Related: Issue #123

-- Add email field with unique constraint
ALTER TABLE users ADD COLUMN email VARCHAR(255) UNIQUE;
```

#### Change Log
```markdown
## Changelog

### [2025-10-27] Add user authentication
- Added email field to users table
- Added password_hash field to users table
- Added unique constraint on email
```

<!-- section_id: "709cbd80-b3d3-452a-9705-e203bc605e97" -->
## Universal Principles

<!-- section_id: "8769f27f-ed8b-459b-81a7-1380c88d10ca" -->
### 1. Immutability

Once a migration is applied, it should never be changed. Instead:
- Create a new migration to fix issues
- Document the fix clearly
- Add test coverage

<!-- section_id: "96ff1d41-9a9b-42dc-8750-64858f3217dc" -->
### 2. Idempotency

Migrations should be idempotent when possible:
```sql
-- ✅ Good: Safe to run multiple times
CREATE TABLE IF NOT EXISTS users (...);

-- ✅ Good: Idempotent
ALTER TABLE users ADD COLUMN IF NOT EXISTS email VARCHAR(255);

-- ❌ Bad: Will fail if run twice
CREATE TABLE users (...);
```

<!-- section_id: "5e91b1af-dd19-4c40-8236-a733ddd98321" -->
### 3. Atomicity

Migrations should be atomic:
- Success: All changes applied
- Failure: No changes applied
- Use transactions when possible

<!-- section_id: "ea47be7c-d534-407f-ac33-4820c686294e" -->
### 4. Reviewability

Migrations should be reviewable:
- Clear, descriptive names
- Comments explaining why
- Links to related issues
- Examples of usage

<!-- section_id: "3a0f032e-17b8-4ca7-be2d-dc7adafc8ff1" -->
### 5. Traceability

Track relationships:
- Migration to feature
- Migration to issue
- Migration to deployment
- Migration to rollback

<!-- section_id: "79393ed0-15a2-466d-ab21-71f13c9b45d1" -->
## Common Patterns

<!-- section_id: "7e580612-7163-4466-94a3-eca02d4d2094" -->
### 1. Add New Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

<!-- section_id: "123e2494-0cc6-45c7-9348-9a3fd2f4cc18" -->
### 2. Add Column to Existing Table
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add index if needed
CREATE INDEX idx_users_phone ON users(phone);
```

<!-- section_id: "a0b8ea20-d619-48b4-a514-bb9d209cf30b" -->
### 3. Modify Column
```sql
-- Add NOT NULL constraint (two-step)
ALTER TABLE users ADD COLUMN status_temp VARCHAR(50);
UPDATE users SET status_temp = 'active' WHERE status_temp IS NULL;
ALTER TABLE users ALTER COLUMN status_temp SET NOT NULL;
ALTER TABLE users DROP COLUMN status;
ALTER TABLE users RENAME COLUMN status_temp TO status;
```

<!-- section_id: "40f68411-da2e-4cda-88c4-975fe6437b75" -->
### 4. Add Foreign Key
```sql
ALTER TABLE orders 
  ADD COLUMN user_id UUID REFERENCES users(id);
  
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

<!-- section_id: "65c44210-0425-4b5d-80fa-175fb3324e3a" -->
### 5. Data Backfill
```sql
-- Add new column
ALTER TABLE users ADD COLUMN display_name VARCHAR(255);

-- Backfill data
UPDATE users SET display_name = 
  COALESCE(first_name || ' ' || last_name, email);

-- Add constraint
ALTER TABLE users ALTER COLUMN display_name SET NOT NULL;
```

<!-- section_id: "d2ec3c25-c60f-4835-82d3-f0756d98ab06" -->
## Platform-Agnostic Guidelines

<!-- section_id: "660ec13f-58c1-4721-a839-3fff73ef7333" -->
### 1. Always Use Version Control
Store all database changes in Git or similar VCS.

<!-- section_id: "b3b98efd-4327-45a3-881f-ba02462f70f7" -->
### 2. One Change Per Migration
Keep migrations focused and atomic.

<!-- section_id: "2822a981-7d44-43f0-aefb-5bdb818e16fb" -->
### 3. Include Rollback Procedures
Always have a way to undo changes.

<!-- section_id: "41323651-8e26-4058-91f3-c7b43a2dff06" -->
### 4. Test Before Deploy
Never deploy untested migrations.

<!-- section_id: "b580421e-7167-4f3b-9704-0e629facd0fc" -->
### 5. Monitor Execution
Watch for errors, performance issues, locks.

<!-- section_id: "b33cf547-c3a3-4406-be6d-1868f07bdbb1" -->
### 6. Document Decisions
Explain why changes are made.

<!-- section_id: "e86d19bc-1d20-4a3d-be80-b71eb61f8c6f" -->
### 7. Review Together
Get team input on database changes.

<!-- section_id: "1d7c518e-35e0-4ef1-b203-9e50f75d7fbf" -->
### 8. Automate Deployment
Use CI/CD for consistent application.

<!-- section_id: "3ae39cd2-be22-4ade-b2b9-166ba9ac6b49" -->
### 9. Backup Regularly
Keep backups before significant changes.

<!-- section_id: "d8aee450-8a4a-4daf-baf0-34385b927ab6" -->
### 10. Plan for Rollback
Have rollback procedures ready.

<!-- section_id: "4dcf32ae-c9fd-4817-86f4-f02a7f0bfbae" -->
## Conclusion

Database version control is essential for modern development. By following these universal principles, you can safely manage database changes across any platform or team size.

**Key Takeaways**:
- Treat database changes like code
- Use migrations for all schema changes
- Test migrations before deploying
- Review changes collaboratively
- Always have rollback plans
- Automate deployments
- Document everything

---

*For platform-specific implementations, see [Platform-Specific Guides](./platform-specific-guides.md). For tool selection, see [Migration Tools Comparison](./migration-tools-comparison.md).*
