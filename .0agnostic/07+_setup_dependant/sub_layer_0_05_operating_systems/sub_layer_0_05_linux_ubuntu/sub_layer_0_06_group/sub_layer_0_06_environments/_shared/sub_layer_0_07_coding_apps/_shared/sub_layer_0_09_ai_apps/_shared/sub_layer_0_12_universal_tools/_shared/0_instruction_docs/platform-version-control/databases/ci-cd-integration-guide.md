---
resource_id: "8caa84ba-f50e-4da4-a283-b8494e8a2690"
resource_type: "document"
resource_name: "ci-cd-integration-guide"
---
# CI/CD Integration Guide
*Automating Database Migrations in Your Deployment Pipeline*

<!-- section_id: "1087debd-2b21-4877-b977-138026871f54" -->
## Overview

This guide shows you how to integrate database migrations into your CI/CD pipeline, ensuring automatic and safe deployment of database changes across environments.

<!-- section_id: "0bb1a8f4-c8ad-4466-9d7d-4510b371c0b7" -->
## CI/CD Platform Examples

<!-- section_id: "7b578bbd-f8ba-4337-9ff4-c02d7d1877eb" -->
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

<!-- section_id: "e60f5480-2691-43b0-b7fc-eedc83b28a3a" -->
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

<!-- section_id: "bcfaf74d-3a1b-49ab-9290-6d9cb035870b" -->
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

<!-- section_id: "748df528-0f2e-4816-ace4-179163ad7727" -->
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

<!-- section_id: "22f46ad4-640f-4143-a275-8afdc0f919e7" -->
## Environment-Specific Strategies

<!-- section_id: "b1f2112a-3656-4bee-a6c1-fdf6ad655f9a" -->
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

<!-- section_id: "e9554640-3bd1-450e-ad81-17d834a201df" -->
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

<!-- section_id: "f7f9b981-51b7-4096-9cc9-756bebb5377b" -->
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

<!-- section_id: "4f14e8be-e9bb-4691-aa2b-91dd918f2a16" -->
## Rollback Strategies

<!-- section_id: "850d26c5-fc44-4b1a-a81a-1b2345265231" -->
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

<!-- section_id: "3985c9f6-9ae9-422f-9c34-00a45c34d11c" -->
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

<!-- section_id: "aa87cb85-8725-419d-a491-3460c303de12" -->
## Safety Measures

<!-- section_id: "e05b02e6-1406-4e12-b1ad-976ba2e1f030" -->
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

<!-- section_id: "adcb129f-a469-4f71-99d5-ba40ee571617" -->
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

<!-- section_id: "d0704b90-b2ac-4cda-8860-fd930f2eb5e5" -->
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

<!-- section_id: "ef39a28c-a1a2-44c2-a479-3bba25b1b57f" -->
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

<!-- section_id: "d7ff816e-de99-40d3-84f3-6baf767ed718" -->
## Best Practices

<!-- section_id: "24d41473-31a0-4a20-ac34-f777c1fedd76" -->
### 1. Environment Parity
Keep development, staging, and production databases in sync.

<!-- section_id: "5a79732d-4f88-41e7-bed7-002bcd17d12c" -->
### 2. Migration Testing
Test migrations in staging before production.

<!-- section_id: "44e82e91-2a31-4598-92da-6d7ab1c442f9" -->
### 3. Backup Strategy
Always backup before running production migrations.

<!-- section_id: "8c103b7e-371c-4c33-9f1b-36465f939860" -->
### 4. Monitoring
Monitor migration execution and database health.

<!-- section_id: "4776bd84-d316-4fd0-b8ae-a7026bb8666e" -->
### 5. Rollback Plans
Have rollback procedures ready and tested.

<!-- section_id: "f24262dd-accb-45c4-924d-b14a85c66ce8" -->
### 6. Communication
Notify team of migration status and failures.

<!-- section_id: "d2502a4f-4fab-46f8-aadb-7e9c91896b53" -->
### 7. Audit Trail
Log all migration executions.

<!-- section_id: "3fa2cf1d-3dd7-4ca9-8155-59e97f59273b" -->
### 8. Security
Use secrets management for database credentials.

---

<!-- section_id: "a374788a-d5f5-48fb-8d3f-ef00e5b3a488" -->
## Common Patterns

<!-- section_id: "cae67b79-5ae5-4e88-a48a-7fc6559b7af4" -->
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

<!-- section_id: "c63308a6-1e04-42ca-b6f3-d103aebaa04e" -->
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

<!-- section_id: "5a418b86-41f7-4af7-8f70-269f469055e0" -->
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

<!-- section_id: "903e21a7-4666-4c75-ab95-35eebcafd2da" -->
## Troubleshooting

<!-- section_id: "635ebf1d-0d9c-49c6-a84a-801e5dfaff90" -->
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

<!-- section_id: "1098b239-dc58-4e76-b296-3218ae413cb3" -->
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

