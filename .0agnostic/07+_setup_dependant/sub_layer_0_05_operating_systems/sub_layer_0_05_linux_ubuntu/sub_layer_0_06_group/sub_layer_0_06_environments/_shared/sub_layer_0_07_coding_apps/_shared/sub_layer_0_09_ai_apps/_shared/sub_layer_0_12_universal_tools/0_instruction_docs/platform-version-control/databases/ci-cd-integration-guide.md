---
resource_id: "fdc94a4f-1d09-4ba7-aad1-450e159e6dfd"
resource_type: "document"
resource_name: "ci-cd-integration-guide"
---
# CI/CD Integration Guide
*Automating Database Migrations in Your Deployment Pipeline*

<!-- section_id: "5d763710-66a1-4485-b80a-3cf0fd63d3be" -->
## Overview

This guide shows you how to integrate database migrations into your CI/CD pipeline, ensuring automatic and safe deployment of database changes across environments.

<!-- section_id: "c2b314f0-f3b4-4305-afe5-364fdcec6c9f" -->
## CI/CD Platform Examples

<!-- section_id: "197d5e5a-99ea-47f8-9916-8dbf8239ed21" -->
### GitHub Actions

#### Basic Workflow

```yaml
# .github/workflows/migrate.yml
name: Database Migration

on:
  push:
    branches: [main]
    paths:
      - 'database/migrations/**'

jobs:
  migrate:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup database
        run: |
          # Start database (example)
          docker run -d \
            -e POSTGRES_PASSWORD=postgres \
            -p 5432:5432 \
            postgres:15
      
      - name: Wait for database
        run: |
          until pg_isready -h localhost -p 5432; do
            sleep 1
          done
      
      - name: Run migrations
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
        run: |
          # Example: Using flyway
          ./migrate.sh
      
      - name: Run tests
        run: |
          npm test
```

#### Flyway with PostgreSQL

```yaml
name: Deploy Database Changes

on:
  push:
    branches: [main]

jobs:
  migrate-staging:
    runs-on: ubuntu-latest
    environment: staging
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup JDK
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      
      - name: Download Flyway
        run: |
          wget -qO- https://download.red-gate.com/maven/release/org/flywaydb/flyway-commandline/10.0.0/flyway-commandline-10.0.0-linux-x64.tar.gz | tar xvz
          sudo mv flyway-*/flyway /usr/local/bin
      
      - name: Run migrations
        env:
          FLYWAY_URL: jdbc:postgresql://${{ secrets.STAGING_DB_HOST }}/${{ secrets.STAGING_DB_NAME }}
          FLYWAY_USER: ${{ secrets.STAGING_DB_USER }}
          FLYWAY_PASSWORD: ${{ secrets.STAGING_DB_PASSWORD }}
          FLYWAY_LOCATIONS: filesystem:database/migrations
        run: flyway migrate
      
      - name: Validate migrations
        env:
          FLYWAY_URL: jdbc:postgresql://${{ secrets.STAGING_DB_HOST }}/${{ secrets.STAGING_DB_NAME }}
          FLYWAY_USER: ${{ secrets.STAGING_DB_USER }}
          FLYWAY_PASSWORD: ${{ secrets.STAGING_DB_PASSWORD }}
          FLYWAY_LOCATIONS: filesystem:database/migrations
        run: flyway validate
```

#### Supabase Migration

```yaml
name: Supabase Migration

on:
  push:
    branches: [main]

jobs:
  migrate:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: supabase/setup-cli@v1
      
      - name: Deploy migrations
        run: supabase db push
        env:
          SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
          SUPABASE_DB_PASSWORD: ${{ secrets.SUPABASE_DB_PASSWORD }}
          SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}
```

#### Firebase Deployment

```yaml
name: Deploy Firebase Database

on:
  push:
    branches: [main]
    paths:
      - 'database/**'

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: node:16
        with:
          node-version: 16
      
      - name: Install dependencies
        run: npm install -g firebase-tools
      
      - name: Deploy rules
        run: firebase deploy --only database
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
          GCP_SA_KEY: ${{ secrets.GCP_SA_KEY }}
```

---

<!-- section_id: "a72c24be-50f5-40e6-a168-409038b6432d" -->
### GitLab CI/CD

#### Basic Pipeline

```yaml
# .gitlab-ci.yml
stages:
  - migrate
  - test

migrate-staging:
  stage: migrate
  image: postgres:15
  services:
    - postgres:15
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres
  script:
    - apt-get update && apt-get install -y flyway
    - flyway -url=jdbc:postgresql://postgres:5432/test_db \
            -user=postgres \
            -password=postgres \
            -locations=filesystem:database/migrations \
            migrate
  only:
    changes:
      - database/migrations/**/*

migrate-production:
  stage: migrate
  image: alpine:latest
  before_script:
    - apk add --no-cache postgresql-client flyway
  script:
    - flyway migrate
        -url=jdbc:postgresql://$PROD_DB_HOST/$PROD_DB_NAME
        -user=$PROD_DB_USER
        -password=$PROD_DB_PASSWORD
        -locations=filesystem:database/migrations
  environment:
    name: production
  when: manual
  only:
    - main
```

#### Multi-Environment

```yaml
stages:
  - migrate
  - deploy

.migrate_template:
  image: flyway/flyway:latest
  script:
    - flyway migrate
        -url=$DATABASE_URL
        -user=$DATABASE_USER
        -password=$DATABASE_PASSWORD
        -locations=filesystem:database/migrations

migrate-dev:
  extends: .migrate_template
  stage: migrate
  environment:
    name: development
  variables:
    DATABASE_URL: $DEV_DATABASE_URL
    DATABASE_USER: $DEV_DATABASE_USER
    DATABASE_PASSWORD: $DEV_DATABASE_PASSWORD

migrate-staging:
  extends: .migrate_template
  stage: migrate
  environment:
    name: staging
  variables:
    DATABASE_URL: $STAGING_DATABASE_URL
    DATABASE_USER: $STAGING_DATABASE_USER
    DATABASE_PASSWORD: $STAGING_DATABASE_PASSWORD

migrate-production:
  extends: .migrate_template
  stage: migrate
  environment:
    name: production
  when: manual
  variables:
    DATABASE_URL: $PROD_DATABASE_URL
    DATABASE_USER: $PROD_DATABASE_USER
    DATABASE_PASSWORD: $PROD_DATABASE_PASSWORD
```

---

<!-- section_id: "a609c552-6e44-462c-8ef1-6eeca67c2bfa" -->
### Jenkins

#### Pipeline Definition

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        DATABASE_HOST = credentials('database-host')
        DATABASE_NAME = credentials('database-name')
        DATABASE_USER = credentials('database-user')
        DATABASE_PASSWORD = credentials('database-password')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                sh '''
                    # Install Flyway
                    wget -qO- https://download.red-gate.com/maven/release/org/flywaydb/flyway-commandline/10.0.0/flyway-commandline-10.0.0-linux-x64.tar.gz | tar xvz
                    mv flyway-*/flyway /usr/local/bin
                '''
            }
        }
        
        stage('Migrate') {
            steps {
                sh '''
                    flyway migrate \
                        -url=jdbc:postgresql://${DATABASE_HOST}/${DATABASE_NAME} \
                        -user=${DATABASE_USER} \
                        -password=${DATABASE_PASSWORD} \
                        -locations=filesystem:database/migrations
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
    
    post {
        success {
            echo 'Migrations applied successfully'
        }
        failure {
            echo 'Migration failed'
        }
    }
}
```

---

<!-- section_id: "73bb7124-b7f3-4320-a23a-a0b6612d6bc2" -->
### Cloud Build (Google Cloud Platform)

#### Basic Configuration

```yaml
# cloudbuild.yaml
steps:
  # Install Flyway
  - name: 'gcr.io/cloud-builders/docker'
    args: ['run', '--rm',
           '-v', '/workspace:/data',
           'flyway/flyway:latest',
           'migrate',
           '-url=jdbc:postgresql://$DB_HOST/$DB_NAME',
           '-user=$DB_USER',
           '-password=$DB_PASSWORD',
           '-locations=filesystem:/data/database/migrations']

  # Run tests
  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']

options:
  machineType: 'E2_HIGHCPU_8'

substitutions:
  DB_HOST: 'localhost'
  DB_NAME: 'myapp'
  DB_USER: 'postgres'
  DB_PASSWORD: 'secret'
```

#### Using Build Triggers

```yaml
steps:
  # Pull migrations from source
  - name: 'gcr.io/cloud-builders/git'
    args: ['clone', 'https://github.com/user/repo.git']
  
  # Run migrations
  - name: 'flyway/flyway'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        wget https://download.red-gate.com/maven/release/org/flywaydb/flyway-commandline/10.0.0/flyway-commandline-10.0.0-linux-x64.tar.gz
        tar xzf flyway-commandline-10.0.0-linux-x64.tar.gz
        flyway-*/flyway migrate \
          -url=jdbc:postgresql://$$DB_HOST/$$DB_NAME \
          -user=$$DB_USER \
          -password=$$DB_PASSWORD \
          -locations=filesystem:database/migrations
```

---

<!-- section_id: "5cfc3046-f0c3-4c2a-b3ad-a777bee2a80f" -->
## Environment-Specific Strategies

<!-- section_id: "f57f6775-c623-4ace-a303-4c237b8e196d" -->
### 1. Development Environment

**Automatic on merge**:

```yaml
# Auto-migrate on merge to main
on:
  push:
    branches:
      - main

jobs:
  migrate-dev:
    runs-on: ubuntu-latest
    steps:
      - run: ./migrate.sh --env development
```

**Local-first workflow**:
- Developers run migrations locally
- Migrations tested before pushing
- No CI/CD migration for dev

<!-- section_id: "7ce0aee2-0896-4398-8c2c-4c1c0021f892" -->
### 2. Staging Environment

**Automated but monitored**:

```yaml
migrate-staging:
  runs-on: ubuntu-latest
  environment:
    name: staging
  steps:
    - name: Run migrations
      run: ./migrate.sh --env staging
    
    - name: Notify team
      if: failure()
      run: |
        curl -X POST $SLACK_WEBHOOK_URL \
          -d '{"text":"Migration to staging failed"}'
```

<!-- section_id: "310973ed-4fd6-436a-88a7-f29ed7dbfdda" -->
### 3. Production Environment

**Manual approval required**:

```yaml
migrate-production:
  runs-on: ubuntu-latest
  environment:
    name: production
  steps:
    - name: Backup database
      run: ./backup.sh
    
    - name: Run migrations
      run: ./migrate.sh --env production
    
    - name: Verify migration
      run: ./verify.sh
    
  # Requires manual approval in GitHub
  # Set in repository settings → Environments
```

**Approval Configuration**:
1. Go to repository settings
2. Environments
3. Create production environment
4. Add protection rules:
   - Required reviewers
   - Wait timer
   - Deployment branches only

---

<!-- section_id: "c23383e0-b82b-4e15-9d67-ea2b4c59dce5" -->
## Rollback Strategies

<!-- section_id: "a88f8834-29bf-413b-900d-518086d19e9f" -->
### Automatic Rollback

```yaml
migrate-production:
  runs-on: ubuntu-latest
  steps:
    - name: Run migrations
      id: migrate
      continue-on-error: true
      run: ./migrate.sh
    
    - name: Rollback on failure
      if: steps.migrate.outcome == 'failure'
      run: |
        echo "Migration failed, rolling back..."
        ./rollback.sh
    
    - name: Alert team
      if: steps.migrate.outcome == 'failure'
      run: |
        curl -X POST $WEBHOOK_URL \
          -d '{"text":"Migration failed and rollback initiated"}'
```

<!-- section_id: "428b464a-158d-4f66-a198-f86ccb5a9118" -->
### Manual Rollback

```yaml
rollback-production:
  runs-on: ubuntu-latest
  environment: production
  workflow_dispatch:
    inputs:
      migration_count:
        description: 'Number of migrations to rollback'
        required: true
        type: number
  steps:
    - name: Confirm rollback
      run: |
        read -p "Confirm rollback? (yes/no): " confirm
        [ "$confirm" = "yes" ] || exit 1
    
    - name: Execute rollback
      run: ./rollback.sh --count ${{ inputs.migration_count }}
```

---

<!-- section_id: "094ee5fb-ab8c-45a4-b871-30dcbba0ce71" -->
## Safety Measures

<!-- section_id: "f9144080-2f34-4d6e-bb7a-2ab9b3241cd6" -->
### 1. Pre-Migration Checks

```yaml
steps:
  - name: Validate migrations
    run: |
      # Check syntax
      flyway validate
      
      # Dry run
      flyway migrate -dryRun
      
      # Check for locks
      flyway info
```

<!-- section_id: "e582053e-9501-45ca-81ad-5600e4fcf170" -->
### 2. Backup Before Migration

```yaml
steps:
  - name: Backup database
    run: |
      pg_dump $DATABASE_URL > backup.sql
      gzip backup.sql
      aws s3 cp backup.sql.gz s3://backups/$(date +%Y%m%d_%H%M%S).sql.gz
  
  - name: Run migrations
    run: flyway migrate
```

<!-- section_id: "f9078c8e-cba5-49b5-bc93-1bd1efcdd930" -->
### 3. Verification After Migration

```yaml
steps:
  - name: Run migrations
    run: flyway migrate
  
  - name: Verify database state
    run: |
      psql $DATABASE_URL -c "SELECT COUNT(*) FROM schema_migrations;"
      psql $DATABASE_URL -c "SELECT version FROM schema_migrations ORDER BY version DESC LIMIT 1;"
  
  - name: Run integration tests
    run: npm run test:integration
```

<!-- section_id: "a2be70eb-67e8-468c-bb2f-7c72b38c35a1" -->
### 4. Notifications

```yaml
steps:
  - name: Run migrations
    id: migrate
    continue-on-error: true
    run: flyway migrate
  
  - name: Notify on success
    if: success()
    run: |
      curl -X POST $WEBHOOK_URL \
        -d '{"text":"✅ Migrations applied successfully"}'
  
  - name: Notify on failure
    if: failure()
    run: |
      curl -X POST $WEBHOOK_URL \
        -d '{"text":"❌ Migrations failed - immediate attention required"}'
```

---

<!-- section_id: "d1008970-f062-4ab3-ab99-f65510010224" -->
## Best Practices

<!-- section_id: "1c3bac9c-2499-40ec-9d59-4d3c99109533" -->
### 1. Environment Parity
Keep development, staging, and production databases in sync.

<!-- section_id: "2f409a4b-2311-4054-a84f-b0a5cab68754" -->
### 2. Migration Testing
Test migrations in staging before production.

<!-- section_id: "f6872263-1e1f-4eac-b07d-ac152f4713c5" -->
### 3. Backup Strategy
Always backup before running production migrations.

<!-- section_id: "6ff36489-7711-412a-9f5b-8edba9ed3541" -->
### 4. Monitoring
Monitor migration execution and database health.

<!-- section_id: "5e7ed330-b4ba-467d-875b-0ea96500625e" -->
### 5. Rollback Plans
Have rollback procedures ready and tested.

<!-- section_id: "60346cae-c7b7-48ad-9411-ec5e84e492d1" -->
### 6. Communication
Notify team of migration status and failures.

<!-- section_id: "43902b24-1110-45f0-bbe1-7d56668b5aee" -->
### 7. Audit Trail
Log all migration executions.

<!-- section_id: "0a77a34b-2ed1-41a7-924e-934a05a6f823" -->
### 8. Security
Use secrets management for database credentials.

---

<!-- section_id: "4214a0f9-c4b6-486b-a687-3a88a047219f" -->
## Common Patterns

<!-- section_id: "6f61bd93-455b-4f4c-9736-d2ca7be98f81" -->
### Sequential Deployments

```yaml
# Migrate staging first
migrate-staging:
  runs-on: ubuntu-latest
  environment: staging

# Then migrate production
migrate-production:
  runs-on: ubuntu-latest
  needs: [migrate-staging]
  environment: production
```

<!-- section_id: "879f150a-a722-48ad-99eb-21b5974cfc0f" -->
### Parallel Testing

```yaml
jobs:
  migrate-staging:
    runs-on: ubuntu-latest
  
  run-tests:
    runs-on: ubuntu-latest
    needs: [migrate-staging]
    strategy:
      matrix:
        test-suite: [unit, integration, e2e]
```

<!-- section_id: "c21ad4e9-0e20-4589-b92b-58032ed708c4" -->
### Feature Flags

```yaml
steps:
  - name: Run migrations
    run: flyway migrate
  
  - name: Enable feature flag
    run: |
      # Migration enables new feature
      psql $DATABASE_URL -c "INSERT INTO feature_flags (name, enabled) VALUES ('new_feature', false);"
```

---

<!-- section_id: "efb125ef-d790-4b59-8064-13876d4c083e" -->
## Troubleshooting

<!-- section_id: "5cbdc15d-1167-4f69-b60a-065b6c740a22" -->
### Common Issues

**Issue**: Migration fails in CI/CD but works locally
- Check environment differences
- Verify database connection
- Check for locks

**Issue**: Migrations run out of order
- Use timestamped migrations
- Verify migration tools configuration

**Issue**: Rollback not working
- Check down migrations exist
- Verify rollback permissions
- Test rollback procedures

See [Troubleshooting Guide](./troubleshooting-guide.md) for more.

---

<!-- section_id: "e461c0a3-cc57-4a0d-9f9d-eaa9eb4cbe05" -->
## Summary

CI/CD integration for database migrations provides:
- ✅ Automated deployment
- ✅ Consistent environments
- ✅ Safety through testing
- ✅ Audit trail
- ✅ Quick rollback capability

**Key Components**:
- Migration tools (Flyway, Liquibase, etc.)
- CI/CD platform (GitHub Actions, GitLab CI, etc.)
- Environment configuration
- Safety measures (backup, testing, rollback)
- Monitoring and notifications

---

*For troubleshooting issues, see [Troubleshooting Guide](./troubleshooting-guide.md). For repo structures, see [Repository Structure Templates](./repo-structure-templates.md).*

