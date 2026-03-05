---
resource_id: "d69e7d70-22fc-42ad-8e9a-7b7c28b88e47"
resource_type: "document"
resource_name: "troubleshooting-guide"
---
# Troubleshooting Guide
*Common Issues and Solutions for Database Version Control*

<!-- section_id: "782548b8-f4e3-4dcc-9e26-70c5b4421cbc" -->
## Overview

This guide helps you troubleshoot common issues encountered when using database version control tools and migration systems. Each issue includes symptoms, causes, and step-by-step solutions.

<!-- section_id: "67bc7e67-e358-406d-b0a4-9b3e60737047" -->
## Common Issues

<!-- section_id: "214ec65e-c82a-4064-9b5f-5429b9dbe256" -->
### 1. Migration Conflicts

**Symptoms**:
- Multiple developers create migrations with same timestamp
- Migration files conflict on merge
- Out-of-order migration application

**Diagnosis**:
```bash
# Check migration status
flyway info

# Check for conflicts
git diff database/migrations/
```

**Solutions**:

#### Timestamp Conflicts
```bash
# Rename conflicting migration
mv database/migrations/20251027-143022_old.sql \
   database/migrations/20251027-143023_update.sql

# Or merge migrations
cat >> database/migrations/20251027-143022.sql <<EOF
# John's changes
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
EOF
```

#### Prevention
- Use centralized migration creation
- Use pre-commit hooks
- Communicate schema changes
- Review PRs before merging

---

<!-- section_id: "f7ce2e92-4602-46bf-8408-952f77abbd66" -->
### 2. Failed Migrations

**Symptoms**:
- Migration execution fails
- Database in inconsistent state
- Cannot apply remaining migrations

**Diagnosis**:
```bash
# Check migration status
flyway info

# Check specific migration
flyway migrate -target=20251027-143022

# View error logs
tail -f logs/migration.log
```

**Solutions**:

#### SQL Syntax Error
```sql
-- ❌ Bad: Syntax error
CREATE TABLE users (
  id INT PRIMARY KEY
  email VARCHAR(255)  -- Missing comma
);

-- ✅ Good: Correct syntax
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255)
);
```

#### Rollback Failed Migration
```bash
# For Liquibase
liquibase rollback-count 1

# For Flyway
flyway undo  # Pro version only

# Manual rollback
psql $DATABASE_URL < database/migrations/rollback/20251027-143022_down.sql
```

#### Repair Schema History
```bash
# Flyway repair
flyway repair

# Liquibase clear checksums
liquibase clear-check-sums
```

---

<!-- section_id: "cd80cff1-396d-460f-907c-7086f338be41" -->
### 3. Migration Lock Issues

**Symptoms**:
- "Schema is locked" errors
- Multiple processes trying to migrate simultaneously
- Stale lock files

**Diagnosis**:
```sql
-- Check for locks (Flyway)
SELECT * FROM flyway_schema_history;

-- Check for locks (Liquibase)
SELECT * FROM DATABASECHANGELOGLOCK;
```

**Solutions**:

#### Clear Stale Locks
```sql
-- Flyway
DELETE FROM flyway_schema_history WHERE success = false;

-- Liquibase
UPDATE DATABASECHANGELOGLOCK SET LOCKED = false, LOCKGRANTED = null, LOCKEDBY = null;
```

#### Lock Prevention
```yaml
# Ensure only one migration job runs
jobs:
  migrate:
    runs-on: ubuntu-latest
    # Single instance
    concurrency:
      group: migration
      cancel-in-progress: false
```

---

<!-- section_id: "5e11195a-671c-4575-8cb0-e780336f8465" -->
### 4. Data Consistency Issues

**Symptoms**:
- Schema and data out of sync
- Foreign key violations
- Missing data after migration
- Orphaned records

**Diagnosis**:
```sql
-- Check for orphaned records
SELECT * FROM orders
WHERE user_id NOT IN (SELECT id FROM users);

-- Check foreign key violations
SELECT * FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';
```

**Solutions**:

#### Fix Orphaned Data
```sql
-- Option 1: Delete orphaned records
DELETE FROM orders
WHERE user_id NOT IN (SELECT id FROM users);

-- Option 2: Set to default
UPDATE orders
SET user_id = NULL
WHERE user_id NOT IN (SELECT id FROM users);

-- Option 3: Restore data
INSERT INTO users (id, email)
VALUES ('orphaned-user-id', 'temp@example.com')
ON CONFLICT DO NOTHING;
```

#### Data Migration Best Practice
```sql
-- ✅ Good: Transactional data migration
BEGIN;
  -- Migrate data
  UPDATE users SET status = 'active' WHERE status IS NULL;
  
  -- Verify
  SELECT COUNT(*) FROM users WHERE status IS NULL;  -- Should be 0
  
  -- Add constraint only if verification succeeds
  ALTER TABLE users ALTER COLUMN status SET NOT NULL;
COMMIT;
```

---

<!-- section_id: "25b0e752-08ff-48ce-befa-47e7860ef01d" -->
### 5. Performance Issues

**Symptoms**:
- Slow migration execution
- Database locks during migration
- Timeout errors
- Out of memory errors

**Diagnosis**:
```sql
-- Check active locks
SELECT * FROM pg_locks WHERE granted = true;

-- Check long-running queries
SELECT * FROM pg_stat_activity
WHERE state = 'active' AND query_start < now() - interval '5 minutes';

-- Check table sizes
SELECT schemaname, tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

**Solutions**:

#### Optimize Migrations
```sql
-- ❌ Bad: Slow migration
UPDATE users SET updated_at = NOW();
-- Updates all rows at once

-- ✅ Good: Batched migration
DO $$
DECLARE
  batch_size CONSTANT INTEGER := 1000;
  updated_count INTEGER;
BEGIN
  LOOP
    UPDATE users
    SET updated_at = NOW()
    WHERE updated_at IS NULL
    AND id IN (
      SELECT id FROM users
      WHERE updated_at IS NULL
      LIMIT batch_size
    );
    
    GET DIAGNOSTICS updated_count = ROW_COUNT;
    EXIT WHEN updated_count = 0;
    
    COMMIT;
  END LOOP;
END $$;
```

#### Add Indexes Concurrently
```sql
-- ❌ Bad: Locks table
CREATE INDEX idx_users_email ON users(email);

-- ✅ Good: Non-blocking index
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```

#### Use Online Schema Changes
```bash
# Use pt-online-schema-change for MySQL
pt-online-schema-change \
  --alter "ADD COLUMN email VARCHAR(255)" \
  --execute \
  D=mydb,t=users
```

---

<!-- section_id: "10ab6b91-2fdc-4752-85b6-4c3c1409407a" -->
### 6. Environment-Specific Issues

**Symptoms**:
- Migration works locally but fails in production
- Different database versions
- Missing permissions

**Diagnosis**:
```bash
# Check database versions
psql --version
mysql --version

# Check user permissions
psql $DATABASE_URL -c "\du"
mysql -e "SHOW GRANTS;"
```

**Solutions**:

#### Version Compatibility
```yaml
# .github/workflows/migrate.yml
steps:
  - name: Use specific database version
    run: |
      docker run -d \
        -e POSTGRES_PASSWORD=postgres \
        postgres:15  # Match production version
```

#### Permission Issues
```sql
-- Grant necessary permissions
GRANT ALL ON DATABASE myapp TO myuser;
GRANT ALL ON SCHEMA public TO myuser;
GRANT ALL ON ALL TABLES IN SCHEMA public TO myuser;
```

#### Environment Variables
```bash
# Different URLs per environment
export DATABASE_URL="postgresql://user:pass@localhost:5432/dev_db"
export STAGING_DATABASE_URL="postgresql://user:pass@staging:5432/staging_db"
export PROD_DATABASE_URL="postgresql://user:pass@prod:5432/prod_db"
```

---

<!-- section_id: "46c3fb04-d52e-4498-be2b-cdf9ed665bcc" -->
### 7. Git Integration Issues

**Symptoms**:
- Migrations not tracked in Git
- Binary migration files
- Large migration files

**Diagnosis**:
```bash
# Check Git status
git status database/migrations/

# Check file sizes
du -sh database/migrations/*

# Check binary files
git diff --check
```

**Solutions**:

#### Add to Git
```bash
# Track migration files
git add database/migrations/
git commit -m "Add database migrations"
```

#### Configure .gitignore
```gitignore
# database/
*.dump
*.sql.gz
backup/
*.pgdump

# But allow migrations
!database/migrations/
!database/schema/
```

#### Compress Large Migrations
```bash
# Use gzip for large files
gzip database/migrations/20251027-large-data.sql

# In migration script
if [[ -f "database/migrations/20251027-large-data.sql.gz" ]]; then
  gunzip database/migrations/20251027-large-data.sql.gz
fi
```

---

<!-- section_id: "d3ec2f28-1bdf-4385-b7d2-63e117fabbe0" -->
### 8. Supabase-Specific Issues

**Symptoms**:
- Supabase migrations failing
- RLS policies not applying
- Type generation errors

**Solutions**:

#### Migration Failures
```bash
# Check Supabase status
supabase status

# Reset local database
supabase db reset

# Push with force
supabase db push --include-all
```

#### RLS Policy Issues
```sql
-- Verify RLS is enabled
SELECT tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public';

-- Re-enable RLS if needed
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
```

#### Type Generation
```bash
# Regenerate types
supabase gen types typescript --local > types/supabase.ts

# Use specific schema
supabase gen types typescript --schema public > types/database.ts
```

---

<!-- section_id: "9c2139e8-2713-417e-95bd-e4932cf57e99" -->
### 9. Firebase-Specific Issues

**Symptoms**:
- Rules deployment failing
- Index creation errors
- Emulator connection issues

**Solutions**:

#### Rules Deployment
```bash
# Check rules syntax
firebase deploy --only firestore:rules --debug

# Validate rules locally
firebase emulators:start
curl http://localhost:8080/v1/projects/my-project/databases/(default)/documents/users/test-user
```

#### Index Errors
```bash
# Wait for index creation
firebase deploy --only firestore:indexes

# Check index status
gcloud firestore indexes list
```

#### Emulator Issues
```bash
# Clear emulator data
firebase emulators:exec "echo 'Reset complete'" --inspect-functions

# Use different port
firebase emulators:start --only firestore --port 8080
```

---

<!-- section_id: "5e54c073-8361-4faa-88ea-d8362c0c3829" -->
### 10. Liquibase-Specific Issues

**Symptoms**:
- Checksum validation errors
- Changelog lock errors
- Duplicate changeSet IDs

**Solutions**:

#### Checksum Errors
```bash
# Clear checksums
liquibase clearCheckSums

# Update checksums
liquibase update
```

#### Changelog Lock
```sql
-- Clear locks manually
UPDATE DATABASECHANGELOGLOCK
SET LOCKED = false,
    LOCKGRANTED = null,
    LOCKEDBY = null;
```

#### Duplicate IDs
```xml
<!-- ❌ Bad: Duplicate ID -->
<changeSet id="1" author="john">
<changeSet id="1" author="jane">

<!-- ✅ Good: Unique IDs -->
<changeSet id="1" author="john">
<changeSet id="2" author="jane">
```

---

<!-- section_id: "3c806940-92ca-42b2-8eda-994d2e4430d2" -->
## Debugging Tips

<!-- section_id: "fe99a849-adba-4241-a961-5918e4ce28cf" -->
### 1. Enable Verbose Logging

```bash
# Flyway
flyway migrate -X

# Liquibase
liquibase update --logLevel=DEBUG
```

<!-- section_id: "0ec93731-1416-4388-8765-6b6e59e22bc8" -->
### 2. Check Migration Status

```bash
# Flyway info
flyway info

# Liquibase status
liquibase status

# Supabase status
supabase migration list
```

<!-- section_id: "382fd6b1-0eae-4ad4-8d45-3c23672e9733" -->
### 3. Dry Run Migrations

```bash
# Flyway dry run
flyway migrate -dryRun

# Liquibase mark next changeset as ran
liquibase markNextChangesetRan
```

<!-- section_id: "b52108e3-d702-40c6-9e49-f158fad0a713" -->
### 4. Verify Database State

```sql
-- Check current schema version
SELECT * FROM flyway_schema_history ORDER BY installed_rank DESC LIMIT 1;

-- Check table existence
SELECT tablename FROM pg_tables WHERE schemaname = 'public';

-- Check data integrity
SELECT COUNT(*), MIN(created_at), MAX(created_at) FROM users;
```

---

<!-- section_id: "ebb21ddf-5810-4f48-a090-70f8e07b2177" -->
## Getting Help

<!-- section_id: "0a7294b4-6a4a-4271-baa0-32032c5f1318" -->
### 1. Check Logs
```bash
# Application logs
tail -f logs/application.log

# Database logs
tail -f /var/log/postgresql/postgresql.log

# CI/CD logs
gh run view --log
```

<!-- section_id: "9d8cade4-0094-4a74-901b-4ed31fc40a1b" -->
### 2. Reproduce Locally
```bash
# Clone the issue
git checkout <branch-with-issue>

# Set up same database version
docker run -d -e POSTGRES_PASSWORD=postgres postgres:15

# Run migration locally
flyway migrate
```

<!-- section_id: "6c5edfdc-e430-4435-8a32-57ec762184f9" -->
### 3. Community Resources
- Tool-specific GitHub issues
- Stack Overflow
- Tool documentation
- Community forums

---

<!-- section_id: "58ba60d1-71ef-4a4b-a619-c489867f22a8" -->
## Prevention Strategies

<!-- section_id: "5374bf27-5e11-4bf3-96b8-e7684a10678d" -->
### 1. Pre-Migration Checks
```yaml
steps:
  - name: Validate SQL syntax
    run: |
      for file in database/migrations/*.sql; do
        psql --dry-run < "$file"
      done
```

<!-- section_id: "0173f766-8b90-4ed7-9360-c657a9f4c1f5" -->
### 2. Test Migrations
```yaml
steps:
  - name: Test migrations
    run: |
      # Run on test database first
      flyway migrate -url=jdbc:postgresql://localhost/test_db
```

<!-- section_id: "3501867b-2c69-4c8b-8c25-1bf3514992b9" -->
### 3. Backup Before Migration
```bash
# Always backup
pg_dump $DATABASE_URL > backup.sql

# Test restore
psql $DATABASE_URL < backup.sql
```

<!-- section_id: "52a1a80d-af1d-40a1-8a13-3e9280bdc184" -->
### 4. Monitor Migrations
```bash
# Log migration execution
flyway migrate -X | tee migration.log

# Alert on failure
if [ $? -ne 0 ]; then
  echo "Migration failed" | mail -s "Alert" admin@example.com
fi
```

---

<!-- section_id: "d9a59ab8-bbff-497f-af22-ec260438cecd" -->
## Quick Reference

<!-- section_id: "b25b7649-a180-4641-9e0e-f0c52b150072" -->
### Common Commands

| Task | Flyway | Liquibase |
|------|--------|-----------|
| Check status | `flyway info` | `liquibase status` |
| Migrate | `flyway migrate` | `liquibase update` |
| Validate | `flyway validate` | `liquibase validate` |
| Repair | `flyway repair` | `liquibase clearCheckSums` |
| Rollback | `flyway undo` (Pro) | `liquibase rollback` |
| History | `flyway info` | `liquibase history` |

<!-- section_id: "b840a67a-5207-4fa6-a71b-d0f57df1d385" -->
### Error Codes

| Error | Cause | Solution |
|-------|-------|----------|
| Checksum mismatch | Migration modified | Clear checksums or repair |
| Schema locked | Migration running | Wait or clear lock |
| Duplicate migration | Same filename | Rename migration |
| SQL syntax error | Invalid SQL | Fix SQL syntax |
| Permission denied | Insufficient rights | Grant permissions |

---

<!-- section_id: "c69fd7e3-57de-4648-b230-acda0d36c5d0" -->
## Summary

Common issues include:
- ✅ Migration conflicts → Use unique timestamps
- ✅ Failed migrations → Test locally first
- ✅ Lock issues → Clear stale locks
- ✅ Data consistency → Verify before/after
- ✅ Performance → Optimize queries
- ✅ Environment issues → Match versions
- ✅ Git issues → Proper .gitignore
- ✅ Platform-specific → Check tool docs

**Key Takeaways**:
- Always test migrations locally
- Backup before production migrations
- Monitor migration execution
- Have rollback procedures ready
- Document troubleshooting steps
- Ask for help when stuck

---

*For platform-specific guides, see [Platform-Specific Guides](./platform-specific-guides.md). For CI/CD integration, see [CI/CD Integration Guide](./ci-cd-integration-guide.md).*

