---
resource_id: "d8d59298-f4a2-4d04-bfec-8c9bded3bb4c"
resource_type: "document"
resource_name: "universal-db-version-control-guide"
---
# Universal Database Version Control Guide
*Core Concepts and Practices for All Database Platforms*

<!-- section_id: "ba073a35-5bec-4f1f-ba9f-8731739e98e0" -->
## Overview

This guide covers universal concepts and practices for database version control that apply to all platforms. Whether you're working with PostgreSQL, NoSQL, data warehouses, or ML pipelines, these principles will help you manage database changes effectively.

<!-- section_id: "5ea7317c-24f4-489c-8ceb-69435e738df7" -->
## Core Concepts

<!-- section_id: "68a59538-5ad3-4da0-83de-11d53a4947cf" -->
### What is Database Version Control?

Database version control is the practice of managing database schema changes, configuration, and data migrations using version control systems (like Git) and automated migration tools. It treats database changes as code, making them:
- **Reviewable**: Changes go through pull requests
- **Testable**: Changes can be tested in isolation
- **Reversible**: Changes can be rolled back
- **Traceable**: History of all changes is maintained

<!-- section_id: "e4627e96-117f-4fbe-9d4d-13050234ec7f" -->
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

<!-- section_id: "ddf3b4a8-27ac-4a59-b3c1-d8315b44886b" -->
## Approaches to Database Version Control

<!-- section_id: "5eb49419-5e0b-4a36-9d40-501cc1f051fb" -->
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

<!-- section_id: "d0d7330e-fcff-4ecb-a88c-eacd3b85f739" -->
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

<!-- section_id: "c7ee495f-6adb-4e91-9458-04e3c2593816" -->
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

<!-- section_id: "c9a1e2ec-79fe-4aee-a51f-818c5344b469" -->
## Version Control Strategies

<!-- section_id: "7102179e-ce25-4baf-b7ff-17ff96dd303f" -->
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

<!-- section_id: "c4dade59-5b62-4e2b-9434-8f2ea3711fda" -->
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

<!-- section_id: "d3d8db61-2323-4461-a995-59563893ead5" -->
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

<!-- section_id: "b7e70aee-70f1-455f-a6e5-a0176f4cc111" -->
## Migration Workflows

<!-- section_id: "3f33006d-2370-4c04-a7e3-eb6fee1b6284" -->
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

<!-- section_id: "ae2c67da-d870-4573-b03b-6738837c3fd0" -->
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

<!-- section_id: "ed2b6d62-bebe-42d0-bd64-936963eeecac" -->
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

<!-- section_id: "fdb04121-3c10-44b7-a0ca-c61e9fb094d9" -->
## Database Change Patterns

<!-- section_id: "6bd832d2-f0ff-459c-9c62-43650cec6458" -->
### 1. Safe Changes (No Downtime)

These changes can be made without application downtime:
- Adding new tables
- Adding new columns (nullable)
- Adding new indexes (create concurrently)
- Adding new views
- Adding new functions
- Decreasing constraints

<!-- section_id: "9a750d7e-6c67-4068-9aa9-9caf75465773" -->
### 2. Breaking Changes (Require Coordination)

These changes require application coordination:
- Dropping columns (deprecate first)
- Renaming columns (add new, migrate, drop old)
- Changing column types (gradual migration)
- Adding NOT NULL constraints (make nullable first)
- Dropping tables (prevent access first)

<!-- section_id: "7a3b8310-b4f0-4cad-a250-ee38e444ffd3" -->
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

<!-- section_id: "5ce0fa2c-3bfe-4a03-8a5a-7c402fcc1853" -->
## Best Practices

<!-- section_id: "e3d160f9-0040-49ce-9a73-250ad68317f9" -->
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

<!-- section_id: "cda0e735-9445-469f-b3ca-c16d81ecd2f3" -->
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

<!-- section_id: "676129fc-cc0a-429c-98a3-7979ef15a06a" -->
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

<!-- section_id: "12d664ae-7856-4f28-a2e7-924522e33ee2" -->
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

<!-- section_id: "4241bdce-4ec6-482c-907c-e5790b45e342" -->
## Universal Principles

<!-- section_id: "6069e14f-8034-4f41-9a94-eb8763e73c5e" -->
### 1. Immutability

Once a migration is applied, it should never be changed. Instead:
- Create a new migration to fix issues
- Document the fix clearly
- Add test coverage

<!-- section_id: "a390db8f-080c-41d4-babd-a50124d8ed07" -->
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

<!-- section_id: "2bbd86cf-4208-434d-9fce-e6166dac69fb" -->
### 3. Atomicity

Migrations should be atomic:
- Success: All changes applied
- Failure: No changes applied
- Use transactions when possible

<!-- section_id: "90278c44-0c05-4d8b-b26d-b50a8a3fe290" -->
### 4. Reviewability

Migrations should be reviewable:
- Clear, descriptive names
- Comments explaining why
- Links to related issues
- Examples of usage

<!-- section_id: "74da180b-b4c0-4ff2-8cca-3083b9911dc2" -->
### 5. Traceability

Track relationships:
- Migration to feature
- Migration to issue
- Migration to deployment
- Migration to rollback

<!-- section_id: "78219bdf-0009-452d-9e73-dc9097752c0d" -->
## Common Patterns

<!-- section_id: "a99b76cb-4b37-407f-9a22-d802b35e1b53" -->
### 1. Add New Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

<!-- section_id: "ed950165-99bf-4489-9684-9274a60b86c0" -->
### 2. Add Column to Existing Table
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add index if needed
CREATE INDEX idx_users_phone ON users(phone);
```

<!-- section_id: "423bdae4-7de8-48e4-9a3e-78ad11759a19" -->
### 3. Modify Column
```sql
-- Add NOT NULL constraint (two-step)
ALTER TABLE users ADD COLUMN status_temp VARCHAR(50);
UPDATE users SET status_temp = 'active' WHERE status_temp IS NULL;
ALTER TABLE users ALTER COLUMN status_temp SET NOT NULL;
ALTER TABLE users DROP COLUMN status;
ALTER TABLE users RENAME COLUMN status_temp TO status;
```

<!-- section_id: "2d42fb17-8cad-46fb-83c4-4780cc5b6178" -->
### 4. Add Foreign Key
```sql
ALTER TABLE orders 
  ADD COLUMN user_id UUID REFERENCES users(id);
  
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

<!-- section_id: "295d6b04-6310-4112-bd0d-604dbfde7b73" -->
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

<!-- section_id: "c67d5ba6-fb99-4d37-8605-8773c2d035a8" -->
## Platform-Agnostic Guidelines

<!-- section_id: "876356d5-82a2-4c57-be8e-b877df6d316d" -->
### 1. Always Use Version Control
Store all database changes in Git or similar VCS.

<!-- section_id: "7a8ac3b3-5cc2-405e-b7cd-d6599d717fe3" -->
### 2. One Change Per Migration
Keep migrations focused and atomic.

<!-- section_id: "ab7f0cf3-20bf-4c2a-baaf-8d9b3d283790" -->
### 3. Include Rollback Procedures
Always have a way to undo changes.

<!-- section_id: "49e89a37-530f-40e7-b0c5-193b9c94f13d" -->
### 4. Test Before Deploy
Never deploy untested migrations.

<!-- section_id: "9a2890c0-1f29-4ba9-99d4-cf28f1e48432" -->
### 5. Monitor Execution
Watch for errors, performance issues, locks.

<!-- section_id: "501474ba-f368-41a1-827e-6dab86283767" -->
### 6. Document Decisions
Explain why changes are made.

<!-- section_id: "cfe6ed99-9384-4f58-80bb-f1e3505e15fb" -->
### 7. Review Together
Get team input on database changes.

<!-- section_id: "b0dca2b2-92ab-47f3-8758-b65f4c70b7c1" -->
### 8. Automate Deployment
Use CI/CD for consistent application.

<!-- section_id: "800374bc-e3e5-4ed3-bdf7-caecce38d263" -->
### 9. Backup Regularly
Keep backups before significant changes.

<!-- section_id: "c29cc6cc-3eb0-4df0-9a1d-fedb05830b94" -->
### 10. Plan for Rollback
Have rollback procedures ready.

<!-- section_id: "1d159a3f-55d1-4aea-a9a2-6bb43bc4c197" -->
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
