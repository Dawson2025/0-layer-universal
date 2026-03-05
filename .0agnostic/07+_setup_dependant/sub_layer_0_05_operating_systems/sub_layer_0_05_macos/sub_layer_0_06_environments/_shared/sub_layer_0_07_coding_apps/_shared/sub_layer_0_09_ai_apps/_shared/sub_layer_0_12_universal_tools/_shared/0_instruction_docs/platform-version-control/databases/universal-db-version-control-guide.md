---
resource_id: "0b47bfd8-5bb8-40cd-a1d6-1c7591581ada"
resource_type: "document"
resource_name: "universal-db-version-control-guide"
---
# Universal Database Version Control Guide
*Core Concepts and Practices for All Database Platforms*

<!-- section_id: "a86222a1-2fdf-4ba6-a49a-3840c1d3d7b3" -->
## Overview

This guide covers universal concepts and practices for database version control that apply to all platforms. Whether you're working with PostgreSQL, NoSQL, data warehouses, or ML pipelines, these principles will help you manage database changes effectively.

<!-- section_id: "cf16511f-f609-4aeb-b2a2-5e9f8d9c2435" -->
## Core Concepts

<!-- section_id: "ea2ccb04-3272-469c-b887-064a4bc5fb47" -->
### What is Database Version Control?

Database version control is the practice of managing database schema changes, configuration, and data migrations using version control systems (like Git) and automated migration tools. It treats database changes as code, making them:
- **Reviewable**: Changes go through pull requests
- **Testable**: Changes can be tested in isolation
- **Reversible**: Changes can be rolled back
- **Traceable**: History of all changes is maintained

<!-- section_id: "6500347a-0295-40cc-b843-d681ae102c2a" -->
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

<!-- section_id: "03bca295-2411-4801-9359-14f2ff080cb1" -->
## Approaches to Database Version Control

<!-- section_id: "2a868c0e-0150-4094-bd32-deb1b4be60b5" -->
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

<!-- section_id: "a0dbd584-0d12-4c7e-a8c8-be1258b976e3" -->
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

<!-- section_id: "f089e983-d4ca-4ed7-b832-78540554ea2c" -->
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

<!-- section_id: "2959e3ab-ca96-4a31-83af-061f33ffbce9" -->
## Version Control Strategies

<!-- section_id: "8464b4c3-0633-4905-960d-0d8400be3a8c" -->
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

<!-- section_id: "fff30dab-aa50-4d29-8a13-f383f13e6ff9" -->
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

<!-- section_id: "e33028f9-c005-4313-b2e1-b573c2914d0c" -->
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

<!-- section_id: "0ddfc5b2-121d-421f-bc84-a4ce0d655d56" -->
## Migration Workflows

<!-- section_id: "68cc8af9-dc58-47ae-a9f1-635a657e4d58" -->
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

<!-- section_id: "a6701301-2f88-4d1c-a642-80c25d84d3e0" -->
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

<!-- section_id: "1ddab5d2-6546-4ed0-9cbd-c4768f21342d" -->
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

<!-- section_id: "99d97050-77b5-45f8-8337-4a3d474c7585" -->
## Database Change Patterns

<!-- section_id: "68a1bd54-4420-475a-bdc5-f34e09e474ce" -->
### 1. Safe Changes (No Downtime)

These changes can be made without application downtime:
- Adding new tables
- Adding new columns (nullable)
- Adding new indexes (create concurrently)
- Adding new views
- Adding new functions
- Decreasing constraints

<!-- section_id: "104fb2a5-1e68-4e2e-b91b-438a77232e45" -->
### 2. Breaking Changes (Require Coordination)

These changes require application coordination:
- Dropping columns (deprecate first)
- Renaming columns (add new, migrate, drop old)
- Changing column types (gradual migration)
- Adding NOT NULL constraints (make nullable first)
- Dropping tables (prevent access first)

<!-- section_id: "f501cc5a-d2a4-42b1-98ec-61e81522494d" -->
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

<!-- section_id: "f0eb3418-0faa-4e60-93fe-85c2e196ef63" -->
## Best Practices

<!-- section_id: "5bcc4e95-dd2f-4b58-a32b-e7f2d33c9f85" -->
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

<!-- section_id: "3283852e-3db2-41b8-8dcb-8b4a89dc7acb" -->
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

<!-- section_id: "1de5e96e-82e5-4070-8bbb-79fff1ec71c2" -->
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

<!-- section_id: "ecfdbc47-d1ef-4588-90c8-7e42f96099f0" -->
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

<!-- section_id: "8810644b-e41d-4f64-92be-c7e4a3a657e2" -->
## Universal Principles

<!-- section_id: "d4f19a29-e5a2-413a-b0a2-df02848e2bea" -->
### 1. Immutability

Once a migration is applied, it should never be changed. Instead:
- Create a new migration to fix issues
- Document the fix clearly
- Add test coverage

<!-- section_id: "2886e4dc-b396-4cb0-9baf-cba8e5801dcf" -->
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

<!-- section_id: "30f23174-fac4-4423-a300-8749ccc738e2" -->
### 3. Atomicity

Migrations should be atomic:
- Success: All changes applied
- Failure: No changes applied
- Use transactions when possible

<!-- section_id: "557bf044-cdfc-4306-b4ab-20e7b81328b0" -->
### 4. Reviewability

Migrations should be reviewable:
- Clear, descriptive names
- Comments explaining why
- Links to related issues
- Examples of usage

<!-- section_id: "cf33a09e-4e07-43f5-91c3-a929c784a02f" -->
### 5. Traceability

Track relationships:
- Migration to feature
- Migration to issue
- Migration to deployment
- Migration to rollback

<!-- section_id: "2807de03-9c45-41df-9927-297e349cd9b4" -->
## Common Patterns

<!-- section_id: "5e6e512e-891e-4f3f-9e0c-7442c6812e91" -->
### 1. Add New Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

<!-- section_id: "820d96b7-5b84-4f1c-9da2-29a5d5778005" -->
### 2. Add Column to Existing Table
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add index if needed
CREATE INDEX idx_users_phone ON users(phone);
```

<!-- section_id: "ae9a9514-4b16-4170-9f83-9d7c2b6ba1dd" -->
### 3. Modify Column
```sql
-- Add NOT NULL constraint (two-step)
ALTER TABLE users ADD COLUMN status_temp VARCHAR(50);
UPDATE users SET status_temp = 'active' WHERE status_temp IS NULL;
ALTER TABLE users ALTER COLUMN status_temp SET NOT NULL;
ALTER TABLE users DROP COLUMN status;
ALTER TABLE users RENAME COLUMN status_temp TO status;
```

<!-- section_id: "81a3db15-522d-467e-8a6f-562ac95e1761" -->
### 4. Add Foreign Key
```sql
ALTER TABLE orders 
  ADD COLUMN user_id UUID REFERENCES users(id);
  
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

<!-- section_id: "ecd9a6c6-9d2e-401d-9647-cfd7164cc8c8" -->
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

<!-- section_id: "834bb790-c8e1-4940-b392-670e8dbde0d6" -->
## Platform-Agnostic Guidelines

<!-- section_id: "1220c0cc-442d-43d8-9c93-97944d9d50d8" -->
### 1. Always Use Version Control
Store all database changes in Git or similar VCS.

<!-- section_id: "e9fe59cf-19a2-4bdf-8dc4-480c257cc201" -->
### 2. One Change Per Migration
Keep migrations focused and atomic.

<!-- section_id: "0bef10ad-d2a9-486a-8bca-f682fc8cd66e" -->
### 3. Include Rollback Procedures
Always have a way to undo changes.

<!-- section_id: "d48fd638-d0ac-4266-9599-29aaad02e2e3" -->
### 4. Test Before Deploy
Never deploy untested migrations.

<!-- section_id: "be14d7e1-66d4-4bd6-b994-6bd78adc0dd0" -->
### 5. Monitor Execution
Watch for errors, performance issues, locks.

<!-- section_id: "e47820dd-e095-45f2-8f41-7ddc0565f31c" -->
### 6. Document Decisions
Explain why changes are made.

<!-- section_id: "d076f62e-4704-4d97-859f-46a9ecc87b8d" -->
### 7. Review Together
Get team input on database changes.

<!-- section_id: "59fc463e-e33c-4396-b0e7-abdc0f6c4b68" -->
### 8. Automate Deployment
Use CI/CD for consistent application.

<!-- section_id: "dee27f8d-f475-4167-a597-7b6667157376" -->
### 9. Backup Regularly
Keep backups before significant changes.

<!-- section_id: "f1a95289-f459-47a6-bd80-a819a671ac86" -->
### 10. Plan for Rollback
Have rollback procedures ready.

<!-- section_id: "72d4f621-5ca0-429b-aff1-21ec6b4e53d2" -->
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
