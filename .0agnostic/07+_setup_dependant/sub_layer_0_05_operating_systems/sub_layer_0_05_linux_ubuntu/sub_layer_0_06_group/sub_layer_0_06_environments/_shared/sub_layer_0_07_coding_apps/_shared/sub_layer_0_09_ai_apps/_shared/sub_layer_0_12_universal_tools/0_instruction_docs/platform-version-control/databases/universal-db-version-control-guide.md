---
resource_id: "4737ece0-80a7-45b2-a07c-8b02fa7811d8"
resource_type: "document"
resource_name: "universal-db-version-control-guide"
---
# Universal Database Version Control Guide
*Core Concepts and Practices for All Database Platforms*

<!-- section_id: "84be4423-cdcf-4399-b00f-ec4c11687f40" -->
## Overview

This guide covers universal concepts and practices for database version control that apply to all platforms. Whether you're working with PostgreSQL, NoSQL, data warehouses, or ML pipelines, these principles will help you manage database changes effectively.

<!-- section_id: "600313ff-2172-42ad-bcf1-744f959b5b22" -->
## Core Concepts

<!-- section_id: "f634cc45-eeb7-4e75-acfe-e6b5f431f422" -->
### What is Database Version Control?

Database version control is the practice of managing database schema changes, configuration, and data migrations using version control systems (like Git) and automated migration tools. It treats database changes as code, making them:
- **Reviewable**: Changes go through pull requests
- **Testable**: Changes can be tested in isolation
- **Reversible**: Changes can be rolled back
- **Traceable**: History of all changes is maintained

<!-- section_id: "9e0d8534-71a9-463e-a66f-823be89955b0" -->
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

<!-- section_id: "bdfebebf-d12d-4d54-90b0-2159c25f13e8" -->
## Approaches to Database Version Control

<!-- section_id: "0a26f1b5-0e6e-42a5-9c98-e482bc036def" -->
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

<!-- section_id: "22d8425d-892d-4f83-814e-f8ee715ca51c" -->
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

<!-- section_id: "2020a7f6-3193-4855-9302-21e4b10a0080" -->
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

<!-- section_id: "1ef71928-bc70-4f9c-87bb-884408ae5697" -->
## Version Control Strategies

<!-- section_id: "1b692e6f-64f8-4dcc-9d9c-c3de6b6b88c0" -->
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

<!-- section_id: "0d510d31-280f-4c12-bdfc-f669de5841c0" -->
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

<!-- section_id: "bee1a9e9-6bdc-45d1-b11b-08bd24e3b70a" -->
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

<!-- section_id: "5e3cb682-3736-4edb-abfa-d8c8ec443962" -->
## Migration Workflows

<!-- section_id: "726aebf9-42a3-4a9b-89f5-26b851ddaf96" -->
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

<!-- section_id: "ec329988-2f25-4182-99f1-0bba50eb3a1a" -->
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

<!-- section_id: "a5d799f4-0b4a-4f3b-8d72-0e5e44dff4ac" -->
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

<!-- section_id: "c6f4e124-2d11-43de-948e-85fcc22b3b9b" -->
## Database Change Patterns

<!-- section_id: "4d9efd67-c476-4b11-9549-630d1b424325" -->
### 1. Safe Changes (No Downtime)

These changes can be made without application downtime:
- Adding new tables
- Adding new columns (nullable)
- Adding new indexes (create concurrently)
- Adding new views
- Adding new functions
- Decreasing constraints

<!-- section_id: "df842711-3ee5-4e5d-a71a-6f4a3bc90995" -->
### 2. Breaking Changes (Require Coordination)

These changes require application coordination:
- Dropping columns (deprecate first)
- Renaming columns (add new, migrate, drop old)
- Changing column types (gradual migration)
- Adding NOT NULL constraints (make nullable first)
- Dropping tables (prevent access first)

<!-- section_id: "e1dd183f-6ad3-491d-bd8c-b530f9cd0bf4" -->
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

<!-- section_id: "8f92d264-0bbf-4122-9579-e0eb206c495d" -->
## Best Practices

<!-- section_id: "bd47265e-6698-46b7-a0ff-f87055a8f5ad" -->
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

<!-- section_id: "c395f4dc-b7aa-495c-b160-f27690426894" -->
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

<!-- section_id: "62395ca4-ca4c-4799-8e23-7898d2643f86" -->
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

<!-- section_id: "0adcdf15-e692-4d60-b24c-f738cb450c54" -->
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

<!-- section_id: "12679eb5-89ac-43ac-8461-dcd816c1295f" -->
## Universal Principles

<!-- section_id: "65f0ba77-c3f7-4f04-8260-ac0b656b4fc3" -->
### 1. Immutability

Once a migration is applied, it should never be changed. Instead:
- Create a new migration to fix issues
- Document the fix clearly
- Add test coverage

<!-- section_id: "92edad41-1820-4f67-b3b3-f263dfa9200b" -->
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

<!-- section_id: "cd744032-c98e-44df-bf4e-6e57fb887d7c" -->
### 3. Atomicity

Migrations should be atomic:
- Success: All changes applied
- Failure: No changes applied
- Use transactions when possible

<!-- section_id: "4c9432ba-ee68-4d54-9bd2-f8fb40ae4ab5" -->
### 4. Reviewability

Migrations should be reviewable:
- Clear, descriptive names
- Comments explaining why
- Links to related issues
- Examples of usage

<!-- section_id: "f83d483c-15fc-4528-9f3e-b66a6fd3b2ac" -->
### 5. Traceability

Track relationships:
- Migration to feature
- Migration to issue
- Migration to deployment
- Migration to rollback

<!-- section_id: "8c3c987b-0363-4cbe-ab66-c5aac2393265" -->
## Common Patterns

<!-- section_id: "f3c258b1-2e9f-46f4-a09f-60bbe2ecb8f4" -->
### 1. Add New Table
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

<!-- section_id: "1082e2f4-6eaf-425e-abd5-f2a4b236afca" -->
### 2. Add Column to Existing Table
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add index if needed
CREATE INDEX idx_users_phone ON users(phone);
```

<!-- section_id: "41714aa8-c702-40ba-8e5b-3176a37ecdae" -->
### 3. Modify Column
```sql
-- Add NOT NULL constraint (two-step)
ALTER TABLE users ADD COLUMN status_temp VARCHAR(50);
UPDATE users SET status_temp = 'active' WHERE status_temp IS NULL;
ALTER TABLE users ALTER COLUMN status_temp SET NOT NULL;
ALTER TABLE users DROP COLUMN status;
ALTER TABLE users RENAME COLUMN status_temp TO status;
```

<!-- section_id: "cdc34496-8e47-4deb-bccc-a19bc9628aae" -->
### 4. Add Foreign Key
```sql
ALTER TABLE orders 
  ADD COLUMN user_id UUID REFERENCES users(id);
  
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

<!-- section_id: "f77a06e8-2a72-44e0-926b-07f8e621e208" -->
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

<!-- section_id: "4c809915-a7f5-4b25-a2e4-5089f8cc3955" -->
## Platform-Agnostic Guidelines

<!-- section_id: "dbdbd114-446d-412c-b3e7-3151b74abeed" -->
### 1. Always Use Version Control
Store all database changes in Git or similar VCS.

<!-- section_id: "37690a77-e0ec-4793-85a4-ba35edb4d8e6" -->
### 2. One Change Per Migration
Keep migrations focused and atomic.

<!-- section_id: "b263a896-6f4d-40d4-80e7-9f42108281da" -->
### 3. Include Rollback Procedures
Always have a way to undo changes.

<!-- section_id: "b7096888-18a0-4ec3-90c1-966d3ccd8c27" -->
### 4. Test Before Deploy
Never deploy untested migrations.

<!-- section_id: "9d99a1e7-6868-4219-817c-02ff3143cf90" -->
### 5. Monitor Execution
Watch for errors, performance issues, locks.

<!-- section_id: "035fca65-f793-4022-bd5d-1628780e6849" -->
### 6. Document Decisions
Explain why changes are made.

<!-- section_id: "e25286b3-e69e-4fa6-ba5a-22fe0aac1df5" -->
### 7. Review Together
Get team input on database changes.

<!-- section_id: "187570e6-153b-4898-8698-bb9b4351a7ad" -->
### 8. Automate Deployment
Use CI/CD for consistent application.

<!-- section_id: "6a24d169-e39e-4bce-a352-32867962050d" -->
### 9. Backup Regularly
Keep backups before significant changes.

<!-- section_id: "cba83a1a-26c4-4b01-a663-dcd131e656ae" -->
### 10. Plan for Rollback
Have rollback procedures ready.

<!-- section_id: "18433387-afe0-4986-807a-cc2215bdf420" -->
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
