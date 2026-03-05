---
resource_id: "67e8f2d0-ccf5-4c1d-80d5-41a6d49df1b6"
resource_type: "document"
resource_name: "troubleshooting-guide"
---
# Troubleshooting Guide
*Common Issues and Solutions for Database Version Control*

<!-- section_id: "b8476092-d697-4851-b711-fedcfa216255" -->
## Overview

This guide helps you troubleshoot common issues encountered when using database version control tools and migration systems. Each issue includes symptoms, causes, and step-by-step solutions.

<!-- section_id: "6176ed51-cf3a-4ab1-b97a-e5f13d9afb0f" -->
## Common Issues

<!-- section_id: "34a75ac5-01e9-4594-8dec-41e6df207f12" -->
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

<!-- section_id: "35da1d82-03d4-461d-b2d8-bb60d0357852" -->
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

<!-- section_id: "1e8985fc-7d74-4e1b-b4c8-c853915b5860" -->
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

<!-- section_id: "86023d06-eb97-4af1-8b05-fa813219aa70" -->
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

<!-- section_id: "f55d260f-44d3-4885-b009-041891a6c924" -->
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

<!-- section_id: "24d76b4e-e535-4ce3-8917-cf2d748fa74c" -->
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

<!-- section_id: "372090df-d2e5-4eb2-9701-a7a7307cdf26" -->
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

<!-- section_id: "43c708f9-a807-4b66-a211-1fa3d26406b0" -->
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

<!-- section_id: "a5d8ccd9-2b22-4ba1-9e8c-1860a3938dd2" -->
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

<!-- section_id: "5163b632-67ea-4126-98a0-20701f5ece13" -->
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

<!-- section_id: "cd41cb6c-29e7-40e7-9109-8780af97bf30" -->
## Debugging Tips

<!-- section_id: "37a92a11-2047-4320-8d4d-6a411ff53f02" -->
### 1. Enable Verbose Logging

```bash
# Flyway
flyway migrate -X

# Liquibase
liquibase update --logLevel=DEBUG
```

<!-- section_id: "077014e1-c30e-4709-8e87-21d0ee040690" -->
### 2. Check Migration Status

```bash
# Flyway info
flyway info

# Liquibase status
liquibase status

# Supabase status
supabase migration list
```

<!-- section_id: "5e87558c-cef6-4a7b-a4aa-db6638c44878" -->
### 3. Dry Run Migrations

```bash
# Flyway dry run
flyway migrate -dryRun

# Liquibase mark next changeset as ran
liquibase markNextChangesetRan
```

<!-- section_id: "e27e9c80-6efe-48a2-b56b-a026bf8973d0" -->
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

<!-- section_id: "cdd8df61-fd0b-4e82-845d-35d0b9b5ff63" -->
## Getting Help

<!-- section_id: "48ef9f79-f9e9-43ab-bad9-bcf12d06bcf8" -->
### 1. Check Logs
```bash
# Application logs
tail -f logs/application.log

# Database logs
tail -f /var/log/postgresql/postgresql.log

# CI/CD logs
gh run view --log
```

<!-- section_id: "73606bb2-1c85-43a4-9808-b2d21da4b466" -->
### 2. Reproduce Locally
```bash
# Clone the issue
git checkout <branch-with-issue>

# Set up same database version
docker run -d -e POSTGRES_PASSWORD=postgres postgres:15

# Run migration locally
flyway migrate
```

<!-- section_id: "1c6906ec-9fa3-4ea1-8ec6-12714a9d842b" -->
### 3. Community Resources
- Tool-specific GitHub issues
- Stack Overflow
- Tool documentation
- Community forums

---

<!-- section_id: "c5f40270-2315-4048-b193-9fea39aff900" -->
## Prevention Strategies

<!-- section_id: "5c885e5e-260a-4216-b197-8de2993423fb" -->
### 1. Pre-Migration Checks
```yaml
steps:
  - name: Validate SQL syntax
    run: |
      for file in database/migrations/*.sql; do
        psql --dry-run < "$file"
      done
```

<!-- section_id: "471d61bb-af4d-4f78-bbdf-0eaf877a52e8" -->
### 2. Test Migrations
```yaml
steps:
  - name: Test migrations
    run: |
      # Run on test database first
      flyway migrate -url=jdbc:postgresql://localhost/test_db
```

<!-- section_id: "95d531cc-f094-4558-9c2b-2eb80c26c8e3" -->
### 3. Backup Before Migration
```bash
# Always backup
pg_dump $DATABASE_URL > backup.sql

# Test restore
psql $DATABASE_URL < backup.sql
```

<!-- section_id: "914d3e16-3e0d-43fb-aeb2-1f7e89ee16c8" -->
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

<!-- section_id: "9dd11bf9-26fc-4c54-a72d-07d703dc69be" -->
## Quick Reference

<!-- section_id: "1517caf6-b92f-44f3-8293-d1721ed10652" -->
### Common Commands

| Task | Flyway | Liquibase |
|------|--------|-----------|
| Check status | `flyway info` | `liquibase status` |
| Migrate | `flyway migrate` | `liquibase update` |
| Validate | `flyway validate` | `liquibase validate` |
| Repair | `flyway repair` | `liquibase clearCheckSums` |
| Rollback | `flyway undo` (Pro) | `liquibase rollback` |
| History | `flyway info` | `liquibase history` |

<!-- section_id: "a97f5962-9fec-4cc1-84fc-38f33cd14dd3" -->
### Error Codes

| Error | Cause | Solution |
|-------|-------|----------|
| Checksum mismatch | Migration modified | Clear checksums or repair |
| Schema locked | Migration running | Wait or clear lock |
| Duplicate migration | Same filename | Rename migration |
| SQL syntax error | Invalid SQL | Fix SQL syntax |
| Permission denied | Insufficient rights | Grant permissions |

---

<!-- section_id: "63745d29-294f-4def-a0ec-c593ce1395d7" -->
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

