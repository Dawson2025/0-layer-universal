---
resource_id: "14ad92e7-3349-455d-84dd-ed83e04e77e7"
resource_type: "document"
resource_name: "universal-db-version-control-guide"
---
# Universal Database Version Control Guide
*Core Concepts and Practices for All Database Platforms*

## Overview

This guide covers universal concepts and practices for database version control that apply to all platforms. Whether you're working with PostgreSQL, NoSQL, data warehouses, or ML pipelines, these principles will help you manage database changes effectively.

## Core Concepts

### What is Database Version Control?

Database version control is the practice of managing database schema changes, configuration, and data migrations using version control systems (like Git) and automated migration tools. It treats database changes as code, making them:
- **Reviewable**: Changes go through pull requests
- **Testable**: Changes can be tested in isolation
- **Reversible**: Changes can be rolled back
- **Traceable**: History of all changes is maintained

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

## Approaches to Database Version Control

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

## Version Control Strategies

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

## Migration Workflows

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

## Database Change Patterns

### 1. Safe Changes (No Downtime)

These changes can be made without application downtime:
- Adding new tables
- Adding new columns (nullable)
- Adding new indexes (create concurrently)
- Adding new views
- Adding new functions
- Decreasing constraints

### 2. Breaking Changes (Require Coordination)

These changes require application coordination:
- Dropping columns (deprecate first)
- Renaming columns (add new, migrate, drop old)
- Changing column types (gradual migration)
- Adding NOT NULL constraints (make nullable first)
- Dropping tables (prevent access first)

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

## Best Practices

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

## Universal Principles

### 1. Immutability

Once a migration is applied, it should never be changed. Instead:
- Create a new migration to fix issues
- Document the fix clearly
- Add test coverage

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

### 3. Atomicity

Migrations should be atomic:
- Success: All changes applied
- Failure: No changes applied
- Use transactions when possible

### 4. Reviewability

Migrations should be reviewable:
- Clear, descriptive names
- Comments explaining why
- Links to related issues
- Examples of usage

### 5. Traceability

Track relationships:
- Migration to feature
- Migration to issue
- Migration to deployment
- Migration to rollback

## Common Patterns

### 1. Add New Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

### 2. Add Column to Existing Table
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add index if needed
CREATE INDEX idx_users_phone ON users(phone);
```

### 3. Modify Column
```sql
-- Add NOT NULL constraint (two-step)
ALTER TABLE users ADD COLUMN status_temp VARCHAR(50);
UPDATE users SET status_temp = 'active' WHERE status_temp IS NULL;
ALTER TABLE users ALTER COLUMN status_temp SET NOT NULL;
ALTER TABLE users DROP COLUMN status;
ALTER TABLE users RENAME COLUMN status_temp TO status;
```

### 4. Add Foreign Key
```sql
ALTER TABLE orders 
  ADD COLUMN user_id UUID REFERENCES users(id);
  
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

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

## Platform-Agnostic Guidelines

### 1. Always Use Version Control
Store all database changes in Git or similar VCS.

### 2. One Change Per Migration
Keep migrations focused and atomic.

### 3. Include Rollback Procedures
Always have a way to undo changes.

### 4. Test Before Deploy
Never deploy untested migrations.

### 5. Monitor Execution
Watch for errors, performance issues, locks.

### 6. Document Decisions
Explain why changes are made.

### 7. Review Together
Get team input on database changes.

### 8. Automate Deployment
Use CI/CD for consistent application.

### 9. Backup Regularly
Keep backups before significant changes.

### 10. Plan for Rollback
Have rollback procedures ready.

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
