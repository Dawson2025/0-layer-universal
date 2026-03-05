---
resource_id: "50d6cd06-9e6c-494b-b383-f53b75b607f1"
resource_type: "document"
resource_name: "ci-cd-integration-guide"
---
# CI/CD Integration Guide
*Automating Database Migrations in Your Deployment Pipeline*

<!-- section_id: "2ccf1d17-a36f-42f4-8b75-cde81dfbfb62" -->
## Overview

This guide shows you how to integrate database migrations into your CI/CD pipeline, ensuring automatic and safe deployment of database changes across environments.

<!-- section_id: "df7de02f-e537-4a7f-86b6-7e8f2c73d4c4" -->
## CI/CD Platform Examples

<!-- section_id: "7ae42425-43a5-4101-92bf-38fed5530680" -->
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

<!-- section_id: "e1d60d40-6fdc-4ed4-83d9-7ed9fc7bc512" -->
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

<!-- section_id: "1b6aa09f-5948-4697-b81a-9a9f8fd2ba2f" -->
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

<!-- section_id: "f1dfde77-93f5-47ef-808c-6cf52cd59423" -->
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

<!-- section_id: "53bfda4a-92c2-4e4a-bd54-09bed342a5e8" -->
## Environment-Specific Strategies

<!-- section_id: "6a74dc21-2e55-4a57-8594-2ec0633a26f7" -->
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

<!-- section_id: "4a14d473-88cd-4359-b4f2-c7cb4e3c8c17" -->
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

<!-- section_id: "537b20be-f7ba-4a55-ab20-6a4c5469156f" -->
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

<!-- section_id: "347fe534-3b2b-4b7d-aa42-73ae827dc7a5" -->
## Rollback Strategies

<!-- section_id: "59010f51-c556-4497-9da0-73bbf6db73ad" -->
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

<!-- section_id: "348ca616-28a4-4a50-9a1a-fbbf537bc768" -->
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

<!-- section_id: "9c1467bd-a108-45f1-8979-bb255fc987ec" -->
## Safety Measures

<!-- section_id: "dddf8f53-2c06-4b3c-904d-7f4b458b043c" -->
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

<!-- section_id: "4311fd0c-e16b-483f-9721-5db8a9c07927" -->
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

<!-- section_id: "bd107aac-a757-4d0e-9aa4-648cb38313db" -->
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

<!-- section_id: "7a0d243a-4f6c-4c62-b049-1894e7e6600d" -->
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

<!-- section_id: "f7639efc-e1a2-4e03-8f1d-2ecc5e942b6e" -->
## Best Practices

<!-- section_id: "73ca66ae-f44a-45eb-a0f8-d3b3f838cc8c" -->
### 1. Environment Parity
Keep development, staging, and production databases in sync.

<!-- section_id: "91b4d0bf-29fd-4bbb-9a45-75c14a9ff390" -->
### 2. Migration Testing
Test migrations in staging before production.

<!-- section_id: "19b12bea-9744-4e18-bc8a-e9d376de0d7d" -->
### 3. Backup Strategy
Always backup before running production migrations.

<!-- section_id: "5f284afd-45d0-473a-8ddd-c6919e502ce9" -->
### 4. Monitoring
Monitor migration execution and database health.

<!-- section_id: "dd7ca6f9-0bc3-4a5a-b4a0-9bfe2f73a703" -->
### 5. Rollback Plans
Have rollback procedures ready and tested.

<!-- section_id: "9ad624f6-d2b1-4554-929e-c0c28584ac59" -->
### 6. Communication
Notify team of migration status and failures.

<!-- section_id: "89f159a5-84ad-4336-8be1-d3f7c75c4272" -->
### 7. Audit Trail
Log all migration executions.

<!-- section_id: "c97cf730-c75f-47ec-b7f3-48d7688cbcb5" -->
### 8. Security
Use secrets management for database credentials.

---

<!-- section_id: "d57c814b-319a-427c-beeb-9529626d1805" -->
## Common Patterns

<!-- section_id: "c1aa26ae-fa07-41d0-b0ce-117f256eafe3" -->
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

<!-- section_id: "459a6bd0-8845-40d3-86ef-14206c24f802" -->
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

<!-- section_id: "9995eb59-0074-4e3a-86d2-cd089b84cd9e" -->
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

<!-- section_id: "04955b7c-16c9-4fc4-9220-0ed982cf2002" -->
## Troubleshooting

<!-- section_id: "2d9e7c9f-0b49-4cbc-80f2-04cea28a4d98" -->
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

<!-- section_id: "4297d0f8-1bbd-4c8a-b2bc-14feba1d000e" -->
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

