---
resource_id: "187d0940-74d8-46bf-ab30-fb1176245f8a"
resource_type: "document"
resource_name: "ci-cd-integration-guide"
---
# CI/CD Integration Guide
*Automating Database Migrations in Your Deployment Pipeline*

<!-- section_id: "eb4f068d-5914-4b18-9125-2bd5111dcd16" -->
## Overview

This guide shows you how to integrate database migrations into your CI/CD pipeline, ensuring automatic and safe deployment of database changes across environments.

<!-- section_id: "04afc83b-c8c6-4e32-818c-4da9bbe59aa0" -->
## CI/CD Platform Examples

<!-- section_id: "a07002d0-ffc4-46e3-85f0-88ab02192852" -->
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

<!-- section_id: "43aba568-ff3d-43ef-8ae2-5c498ce00e99" -->
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

<!-- section_id: "dc6b9246-f379-482e-86f6-b87220f187e7" -->
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

<!-- section_id: "3f1da975-22a8-4f9e-a83a-02276a5519a1" -->
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

<!-- section_id: "70dd119c-d20b-4eda-a733-e1d814220154" -->
## Environment-Specific Strategies

<!-- section_id: "44369ccf-bdf1-497b-9556-3c8c79e418ec" -->
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

<!-- section_id: "3ca8b76d-c266-4742-a13d-610853a13f80" -->
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

<!-- section_id: "09120691-ce2b-488b-9268-161bc3c3d5c9" -->
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

<!-- section_id: "604e0df2-4eec-4bb3-9edb-5800efcae3d1" -->
## Rollback Strategies

<!-- section_id: "d0291a30-1250-4aaf-962f-1c65b184dfb3" -->
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

<!-- section_id: "cdf94d0c-2e4d-44cd-8c79-b0c02c4d1676" -->
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

<!-- section_id: "2424e88c-cb86-47d2-a2da-2a55b18a59dd" -->
## Safety Measures

<!-- section_id: "a8cb4f08-a59c-40c2-b5ff-e89f1b067305" -->
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

<!-- section_id: "8d8869e4-2d55-4044-ac77-76dc7d5e2726" -->
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

<!-- section_id: "925b11ec-a3ae-42d0-bcf3-a50ca7788cf0" -->
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

<!-- section_id: "06251ab5-1a62-40f7-95a4-d0188c29f5c4" -->
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

<!-- section_id: "3a15ab12-43f1-47b3-9afb-49820626a67e" -->
## Best Practices

<!-- section_id: "3e204d7e-bf5d-49c6-97ae-4125b8e684ea" -->
### 1. Environment Parity
Keep development, staging, and production databases in sync.

<!-- section_id: "a9311d0a-bd60-4284-9416-4f8cd607f40d" -->
### 2. Migration Testing
Test migrations in staging before production.

<!-- section_id: "08f8a172-ee23-4083-928d-0eebdf651d78" -->
### 3. Backup Strategy
Always backup before running production migrations.

<!-- section_id: "5acf6cb7-9972-4a26-97ce-b29f521c397c" -->
### 4. Monitoring
Monitor migration execution and database health.

<!-- section_id: "3d8673b1-5bef-4515-bbe2-5e7cadce4b5b" -->
### 5. Rollback Plans
Have rollback procedures ready and tested.

<!-- section_id: "b2219af0-dd3e-4d8c-be4a-126f82e28c0e" -->
### 6. Communication
Notify team of migration status and failures.

<!-- section_id: "9a028b98-655d-4094-945d-fef464cdd047" -->
### 7. Audit Trail
Log all migration executions.

<!-- section_id: "a69d7f3a-302c-46b5-9103-d8b4ed14c0eb" -->
### 8. Security
Use secrets management for database credentials.

---

<!-- section_id: "dc450852-546c-4924-9e06-e63bfe4af926" -->
## Common Patterns

<!-- section_id: "c425f1c5-61b8-4b00-a24c-214c1d47f686" -->
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

<!-- section_id: "107ede12-5b44-4729-812e-5b11d78ccc1c" -->
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

<!-- section_id: "4f1d5cff-3eb8-4e34-b5e2-ba55a3243709" -->
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

<!-- section_id: "49bc2042-6249-41e4-9b8c-f74a72895dfd" -->
## Troubleshooting

<!-- section_id: "8626c8d8-7d6b-435f-a6e3-0d8a293162bb" -->
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

<!-- section_id: "32264a0b-3643-46f8-8a29-bde4f1f36568" -->
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

