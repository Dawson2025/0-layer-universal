---
resource_id: "06765219-ffe2-46a1-8e8f-d44d9bfadfb4"
resource_type: "document"
resource_name: "universal-db-version-control-guide"
---
# Universal Database Version Control Guide
*Core Concepts and Practices for All Database Platforms*

<!-- section_id: "b7fcffeb-9698-41bf-b309-276ccaff84a6" -->
## Overview

This guide covers universal concepts and practices for database version control that apply to all platforms. Whether you're working with PostgreSQL, NoSQL, data warehouses, or ML pipelines, these principles will help you manage database changes effectively.

<!-- section_id: "15063781-3d16-4e0e-a9a3-8b2f511083bc" -->
## Core Concepts

<!-- section_id: "4ba4968a-afac-4c3c-9021-62e876992760" -->
### What is Database Version Control?

Database version control is the practice of managing database schema changes, configuration, and data migrations using version control systems (like Git) and automated migration tools. It treats database changes as code, making them:
- **Reviewable**: Changes go through pull requests
- **Testable**: Changes can be tested in isolation
- **Reversible**: Changes can be rolled back
- **Traceable**: History of all changes is maintained

<!-- section_id: "56c9ade6-49cc-4667-9a04-6fa18e0758d9" -->
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

<!-- section_id: "e402cfb6-4d7b-4aaf-ae00-99219befeb62" -->
## Approaches to Database Version Control

<!-- section_id: "29de9535-7256-4f08-becf-517d0cfddf4b" -->
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

<!-- section_id: "2e29daa9-ece7-4322-9dbf-29aee92be831" -->
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

<!-- section_id: "793d08a1-61a5-4a1e-8803-88229af861ba" -->
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

<!-- section_id: "eef1f99e-013a-4194-b2d1-f7c9c77e727e" -->
## Version Control Strategies

<!-- section_id: "552c9f7b-1a42-4f51-8817-70a8f6e6d170" -->
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

<!-- section_id: "36740cbb-4ef9-4a4e-9197-bf8fb2b8c6f0" -->
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

<!-- section_id: "ecf6aae4-cd5b-42d1-ad7d-ffc9c5d8917d" -->
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

<!-- section_id: "522dd872-2a7d-4961-b35d-2f5dd95fd2bb" -->
## Migration Workflows

<!-- section_id: "d66f7cbe-021a-4013-a6b9-c13077ba6e50" -->
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

<!-- section_id: "3458f0c5-3b4a-48d5-9e1d-795cb78a79a2" -->
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

<!-- section_id: "638ca1b7-5c72-435b-91c7-15c00e16c96e" -->
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

<!-- section_id: "0b2ff2c8-12fc-42a8-9603-ae2a2efeb7ba" -->
## Database Change Patterns

<!-- section_id: "d6edd4a3-d0c3-49d3-a970-f14f99f70655" -->
### 1. Safe Changes (No Downtime)

These changes can be made without application downtime:
- Adding new tables
- Adding new columns (nullable)
- Adding new indexes (create concurrently)
- Adding new views
- Adding new functions
- Decreasing constraints

<!-- section_id: "719e4bdc-77b9-4b95-ad88-92f204ec2e45" -->
### 2. Breaking Changes (Require Coordination)

These changes require application coordination:
- Dropping columns (deprecate first)
- Renaming columns (add new, migrate, drop old)
- Changing column types (gradual migration)
- Adding NOT NULL constraints (make nullable first)
- Dropping tables (prevent access first)

<!-- section_id: "b6d2485d-b842-4a64-86f0-39edada1f6e8" -->
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

<!-- section_id: "95fb7463-78a1-4f9f-8713-671b41bcb72c" -->
## Best Practices

<!-- section_id: "4926e9ad-2465-4557-bca3-8d62a66227a9" -->
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

<!-- section_id: "46e5a074-0194-42bc-8f75-ca1eff315a8f" -->
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

<!-- section_id: "611ef57e-61d3-4e44-bb77-447b71bd007a" -->
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

<!-- section_id: "fe5fd1b1-9e82-4810-93b2-19a3c6007c75" -->
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

<!-- section_id: "9e03ec50-5142-47cb-8404-420b9fcad716" -->
## Universal Principles

<!-- section_id: "09239912-550d-4bf6-b0ce-2ba4f0ccb6eb" -->
### 1. Immutability

Once a migration is applied, it should never be changed. Instead:
- Create a new migration to fix issues
- Document the fix clearly
- Add test coverage

<!-- section_id: "925f3d08-b27f-46de-b2cc-f085fa7daab1" -->
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

<!-- section_id: "fef863d2-2c41-40cf-a31c-35c1c0321618" -->
### 3. Atomicity

Migrations should be atomic:
- Success: All changes applied
- Failure: No changes applied
- Use transactions when possible

<!-- section_id: "7d3c887b-f868-4b39-830a-47fabab52498" -->
### 4. Reviewability

Migrations should be reviewable:
- Clear, descriptive names
- Comments explaining why
- Links to related issues
- Examples of usage

<!-- section_id: "c6fb1c9d-a2dd-4a96-8066-b61f50bca6a3" -->
### 5. Traceability

Track relationships:
- Migration to feature
- Migration to issue
- Migration to deployment
- Migration to rollback

<!-- section_id: "2ec56304-38cd-4852-b295-d8914d85a48f" -->
## Common Patterns

<!-- section_id: "739e49cc-9655-48ad-9130-1793378959c3" -->
### 1. Add New Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

<!-- section_id: "714c161b-2351-4073-a0c7-7986346bfeee" -->
### 2. Add Column to Existing Table
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add index if needed
CREATE INDEX idx_users_phone ON users(phone);
```

<!-- section_id: "598a4511-a7bf-4c73-bf6f-7e2d8b50537e" -->
### 3. Modify Column
```sql
-- Add NOT NULL constraint (two-step)
ALTER TABLE users ADD COLUMN status_temp VARCHAR(50);
UPDATE users SET status_temp = 'active' WHERE status_temp IS NULL;
ALTER TABLE users ALTER COLUMN status_temp SET NOT NULL;
ALTER TABLE users DROP COLUMN status;
ALTER TABLE users RENAME COLUMN status_temp TO status;
```

<!-- section_id: "2231f1df-8727-4a97-ba51-a8abfa4ed578" -->
### 4. Add Foreign Key
```sql
ALTER TABLE orders 
  ADD COLUMN user_id UUID REFERENCES users(id);
  
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

<!-- section_id: "ffeab042-038d-4c07-9614-d08463610e60" -->
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

<!-- section_id: "4769cfbd-3c09-413a-badd-ac5d7f1eb863" -->
## Platform-Agnostic Guidelines

<!-- section_id: "5b178f0b-00f2-4571-9263-989e545b0999" -->
### 1. Always Use Version Control
Store all database changes in Git or similar VCS.

<!-- section_id: "95042840-38e0-494f-8d56-b33243ef2375" -->
### 2. One Change Per Migration
Keep migrations focused and atomic.

<!-- section_id: "122ac4a4-0609-4b43-9b03-137837577bf1" -->
### 3. Include Rollback Procedures
Always have a way to undo changes.

<!-- section_id: "34149ef0-93c5-4c82-a1d6-fdb146b231f6" -->
### 4. Test Before Deploy
Never deploy untested migrations.

<!-- section_id: "e1bf41e1-ad39-4967-ba43-02b28cb17a2b" -->
### 5. Monitor Execution
Watch for errors, performance issues, locks.

<!-- section_id: "2705bcb9-ab3c-4b5f-ba83-c205128d003d" -->
### 6. Document Decisions
Explain why changes are made.

<!-- section_id: "21508a12-fcc6-4397-8102-71881dfdd310" -->
### 7. Review Together
Get team input on database changes.

<!-- section_id: "2059baf1-9c4d-4ea7-9eaa-90b992e469b2" -->
### 8. Automate Deployment
Use CI/CD for consistent application.

<!-- section_id: "66c4f962-d7eb-4718-80ea-24a31d684a59" -->
### 9. Backup Regularly
Keep backups before significant changes.

<!-- section_id: "f9f9013f-6942-4c8c-9a9f-2ef597e0eb5f" -->
### 10. Plan for Rollback
Have rollback procedures ready.

<!-- section_id: "f7fbbbf5-889a-4351-867e-cd324be5b085" -->
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
