---
resource_id: "e6008df7-9079-4f17-bb2e-de25a953d6fc"
resource_type: "document"
resource_name: "troubleshooting-guide"
---
# Troubleshooting Guide
*Common Issues and Solutions for Database Version Control*

<!-- section_id: "a2fe1cde-1873-45e7-be22-b5831d3a344e" -->
## Overview

This guide helps you troubleshoot common issues encountered when using database version control tools and migration systems. Each issue includes symptoms, causes, and step-by-step solutions.

<!-- section_id: "5b303c3a-9e02-484f-8d98-b018926f0d9d" -->
## Common Issues

<!-- section_id: "94c99519-94c8-4439-adfa-b83def91263e" -->
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

<!-- section_id: "3a07edc0-1116-4a40-9587-bc6fcab4bba7" -->
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

<!-- section_id: "4881d96b-7e39-4e1a-a84b-331659f27fe9" -->
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

<!-- section_id: "8a06d384-87dd-408b-8c2c-50ec2315b804" -->
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

<!-- section_id: "03683ec6-4d94-4d7b-b69a-c4ff16b6dca3" -->
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

<!-- section_id: "12280733-37ae-4c47-a315-e73b1a70f468" -->
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

<!-- section_id: "74a3b0c3-0007-42f4-aa5c-2abffc4bb467" -->
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

<!-- section_id: "fa0d6147-3899-4fe4-8672-a5f64c79f82b" -->
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

<!-- section_id: "7a10e22e-962b-4819-b989-ad1a60ed2a26" -->
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

<!-- section_id: "246f1f74-bc20-46a1-bcb2-63d0be583540" -->
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

<!-- section_id: "18c0b2eb-35b3-4c2a-a8ab-653e226bd622" -->
## Debugging Tips

<!-- section_id: "1d8d69a3-6baa-4cda-a8b9-bc21de8b3599" -->
### 1. Enable Verbose Logging

```bash
# Flyway
flyway migrate -X

# Liquibase
liquibase update --logLevel=DEBUG
```

<!-- section_id: "2e92e236-f997-4d7b-9ba8-ab8eab6755d0" -->
### 2. Check Migration Status

```bash
# Flyway info
flyway info

# Liquibase status
liquibase status

# Supabase status
supabase migration list
```

<!-- section_id: "0850e965-ac79-41aa-9cf1-7de66b028fdb" -->
### 3. Dry Run Migrations

```bash
# Flyway dry run
flyway migrate -dryRun

# Liquibase mark next changeset as ran
liquibase markNextChangesetRan
```

<!-- section_id: "3b78dbdb-6f86-402b-b964-68090b2332da" -->
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

<!-- section_id: "100bc6cb-cc54-4f0e-9559-ca1ecb91beec" -->
## Getting Help

<!-- section_id: "b3a88660-2eb5-45cf-8215-6e469cb799c0" -->
### 1. Check Logs
```bash
# Application logs
tail -f logs/application.log

# Database logs
tail -f /var/log/postgresql/postgresql.log

# CI/CD logs
gh run view --log
```

<!-- section_id: "759b8f4f-c734-493a-ab9e-426783be477a" -->
### 2. Reproduce Locally
```bash
# Clone the issue
git checkout <branch-with-issue>

# Set up same database version
docker run -d -e POSTGRES_PASSWORD=postgres postgres:15

# Run migration locally
flyway migrate
```

<!-- section_id: "01b9d07f-e27c-42e8-adef-dc1ae08ad021" -->
### 3. Community Resources
- Tool-specific GitHub issues
- Stack Overflow
- Tool documentation
- Community forums

---

<!-- section_id: "6d469133-52e8-495a-8ae1-718b98074674" -->
## Prevention Strategies

<!-- section_id: "bbb79730-789e-4416-8fae-10c3171e0227" -->
### 1. Pre-Migration Checks
```yaml
steps:
  - name: Validate SQL syntax
    run: |
      for file in database/migrations/*.sql; do
        psql --dry-run < "$file"
      done
```

<!-- section_id: "92e62944-eeeb-4626-8414-153c20ba740e" -->
### 2. Test Migrations
```yaml
steps:
  - name: Test migrations
    run: |
      # Run on test database first
      flyway migrate -url=jdbc:postgresql://localhost/test_db
```

<!-- section_id: "57848b80-1c8f-48c2-a074-b91d488df1e5" -->
### 3. Backup Before Migration
```bash
# Always backup
pg_dump $DATABASE_URL > backup.sql

# Test restore
psql $DATABASE_URL < backup.sql
```

<!-- section_id: "9f08a8bb-6a76-4177-beea-81c458a771dd" -->
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

<!-- section_id: "f4d54069-c7f2-4398-bab3-375c046b18b5" -->
## Quick Reference

<!-- section_id: "a8390596-4de1-46dc-a37a-3870424e7a4b" -->
### Common Commands

| Task | Flyway | Liquibase |
|------|--------|-----------|
| Check status | `flyway info` | `liquibase status` |
| Migrate | `flyway migrate` | `liquibase update` |
| Validate | `flyway validate` | `liquibase validate` |
| Repair | `flyway repair` | `liquibase clearCheckSums` |
| Rollback | `flyway undo` (Pro) | `liquibase rollback` |
| History | `flyway info` | `liquibase history` |

<!-- section_id: "f879c21b-3cd9-43b2-a872-1a661b054499" -->
### Error Codes

| Error | Cause | Solution |
|-------|-------|----------|
| Checksum mismatch | Migration modified | Clear checksums or repair |
| Schema locked | Migration running | Wait or clear lock |
| Duplicate migration | Same filename | Rename migration |
| SQL syntax error | Invalid SQL | Fix SQL syntax |
| Permission denied | Insufficient rights | Grant permissions |

---

<!-- section_id: "a36616fa-ed11-4375-947b-241cf6c3d829" -->
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

