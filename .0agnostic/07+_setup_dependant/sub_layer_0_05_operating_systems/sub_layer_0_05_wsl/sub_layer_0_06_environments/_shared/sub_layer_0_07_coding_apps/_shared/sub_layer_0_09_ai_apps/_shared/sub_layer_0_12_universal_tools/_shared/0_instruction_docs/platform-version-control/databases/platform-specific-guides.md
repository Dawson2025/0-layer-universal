---
resource_id: "9bb9f244-51b7-46ce-adcd-35810122ea48"
resource_type: "document"
resource_name: "platform-specific-guides"
---
# Platform-Specific Guides
*Detailed Database Version Control Workflows for Each Platform*

<!-- section_id: "b683a50a-ec62-4674-b4ed-10c0c1ea1412" -->
## Overview

This guide provides detailed, platform-specific instructions for version controlling databases across different platforms. Each section includes installation, configuration, common workflows, and examples.

<!-- section_id: "9cc655a3-1c71-436d-af06-127f878764d7" -->
## Table of Contents

1. [Supabase](#supabase)
2. [Firebase Realtime Database](#firebase-realtime-database)
3. [Firestore](#firestore)
4. [Google Cloud SQL](#google-cloud-sql)
5. [BigQuery](#bigquery)
6. [Vertex AI](#vertex-ai)
7. [instant.db](#instantdb)

---

<!-- section_id: "33ac5303-98c0-4399-83b2-9332a2e102bd" -->
## Supabase

<!-- section_id: "e00e5e32-4be3-40ca-83c9-3b6e5890dda9" -->
### Overview

Supabase is a PostgreSQL-based platform with built-in migration support through the Supabase CLI. It provides excellent version control capabilities with native Git integration.

<!-- section_id: "9a618fa0-228b-4b85-8fe2-d231c48a4e12" -->
### Prerequisites

- Supabase account
- Supabase CLI installed
- Node.js 18+ or Python 3.8+

<!-- section_id: "3680eaa7-7092-4e25-80e2-bc10390fbb3c" -->
### Installation

```bash
# Install Supabase CLI
npm install -g supabase

# Or via Homebrew (macOS)
brew install supabase/tap/supabase

# Login
supabase login
```

<!-- section_id: "61055205-9b76-496c-88ca-6bd13d58eb25" -->
### Initialization

```bash
# Initialize a new project
supabase init

# Link to existing project
supabase link --project-ref your-project-ref
```

<!-- section_id: "2894d759-67a3-46cd-9b8e-4e3dc9626bb1" -->
### Migration Workflow

#### 1. Create Migration

```bash
# Create a new migration
supabase migration new create-users-table

# This creates: supabase/migrations/20251027143022_create_users_table.sql
```

#### 2. Write Migration

```sql
-- File: supabase/migrations/20251027143022_create_users_table.sql
CREATE TABLE public.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON public.users(email);

-- Add RLS (Row Level Security)
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own data"
  ON public.users
  FOR SELECT
  USING (auth.uid() = id);
```

#### 3. Apply Migration

```bash
# Apply migrations to local database
supabase db reset

# Apply migrations to linked project
supabase db push

# Check migration status
supabase migration list
```

#### 4. Rollback

```bash
# Reset local database (drops all tables)
supabase db reset

# For remote, create down migration
# Or use Supabase dashboard to manage
```

<!-- section_id: "27cef379-d76a-404f-80c9-d649c8bfbfdc" -->
### Common Commands

```bash
# Start local development
supabase start

# Stop local development
supabase stop

# Generate TypeScript types
supabase gen types typescript --local > types/supabase.ts

# Diff local and remote
supabase db diff

# Open Supabase Studio
supabase studio
```

<!-- section_id: "4a983585-f6d7-4d31-91e4-75cc750057e0" -->
### Repository Structure

```
project/
├── supabase/
│   ├── config.toml           # Supabase config
│   ├── seed.sql              # Seed data
│   ├── migrations/
│   │   ├── 20251027000001_create_users_table.sql
│   │   ├── 20251027000002_add_user_profiles.sql
│   │   └── 20251027000003_add_indices.sql
│   └── functions/            # Edge functions
├── supabase/
│   ├── .env.local
└── package.json
```

<!-- section_id: "bdf656fd-eb20-48fb-856d-8bfbe2229e45" -->
### CI/CD Integration

```yaml
# .github/workflows/deploy.yml
name: Deploy Migrations

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: supabase/setup-cli@v1
      
      - run: supabase db push
        env:
          SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
          SUPABASE_DB_PASSWORD: ${{ secrets.SUPABASE_DB_PASSWORD }}
          SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}
```

<!-- section_id: "dcee95ed-9fa5-4dd1-afa2-7e99f4762a17" -->
### Best Practices

- ✅ Use timestamped migration names
- ✅ Include up and down migrations when possible
- ✅ Test locally before pushing
- ✅ Review migrations in PRs
- ✅ Use Supabase RLS for security
- ✅ Keep migrations small and focused

---

<!-- section_id: "5cefc074-6796-4129-958d-27bac3dc1919" -->
## Firebase Realtime Database

<!-- section_id: "41eec0ab-2959-4e64-a0d1-dde529d6190b" -->
### Overview

Firebase Realtime Database uses JSON and requires manual export/import for version control. The Firebase CLI manages configuration and deployments.

<!-- section_id: "a0162bb4-f0a6-475c-9b55-9d0957a83dfc" -->
### Prerequisites

- Firebase account
- Firebase CLI installed
- Node.js 8.0+

<!-- section_id: "9d4f8afa-19da-4a07-bcec-e72174c57d9c" -->
### Installation

```bash
npm install -g firebase-tools

# Login
firebase login
```

<!-- section_id: "5ec10c10-0a88-432b-ae93-cfc54becc12d" -->
### Initialization

```bash
# Initialize Firebase project
firebase init

# Select:
# - Realtime Database
# - Configure security rules
```

<!-- section_id: "59a70db1-8d93-4b78-a870-67e2bf123e02" -->
### Configuration Files

#### Database Rules

```javascript
// database.rules.json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null",
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```

#### Project Configuration

```json
// firebase.json
{
  "database": {
    "rules": "database.rules.json"
  },
  "hosting": {
    "public": "public",
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

<!-- section_id: "1d57b8d7-0d80-42ed-9eeb-75ea77044b63" -->
### Deployment Workflow

#### 1. Modify Rules

```javascript
// database.rules.json - Update security rules
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "auth != null",
        ".write": "$uid === auth.uid",
        ".validate": "newData.hasChildren(['email', 'displayName'])"
      }
    }
  }
}
```

#### 2. Deploy Rules

```bash
# Deploy database rules
firebase deploy --only database

# Deploy specific rules file
firebase deploy --only database:database
```

#### 3. Data Export/Import

```bash
# Export database data
firebase database:get /users > backup/users.json

# Import database data
firebase database:set /users backup/users.json
```

<!-- section_id: "d03752d6-1e4d-4ff0-ab4f-0fbe6ac376ad" -->
### Data Versioning Strategy

Since Firebase doesn't support migrations natively:

#### 1. Configuration Versioning
Store rules in Git:
```
database/
├── database.rules.json
├── database.development.rules.json
└── database.production.rules.json
```

#### 2. Data Snapshots
Regularly export data:
```bash
#!/bin/bash
# backup-firebase.sh
DATE=$(date +%Y%m%d_%H%M%S)
firebase database:get /users > backup/users_$DATE.json
```

#### 3. Structure Documentation
Document data structure in code:
```typescript
// types/database.ts
interface User {
  uid: string;
  email: string;
  displayName: string;
  createdAt: string;
  updatedAt: string;
}
```

<!-- section_id: "6e127b82-f3c7-4fb8-bed8-509424dc83a6" -->
### Repository Structure

```
project/
├── database/
│   ├── database.rules.json
│   ├── database.development.rules.json
│   └── database.production.rules.json
├── backup/
│   ├── users_20251027.json
│   └── users_20251026.json
├── scripts/
│   └── backup.sh
└── firebase.json
```

<!-- section_id: "0b82c8bd-fd77-43a7-a3ed-ee74a6222fda" -->
### CI/CD Integration

```yaml
# .github/workflows/deploy.yml
name: Deploy Firebase

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: node:16
        with:
          node-version: 16
      
      - run: npm install -g firebase-tools
      
      - run: firebase deploy --only database
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

<!-- section_id: "cc7136a8-92ab-4392-83b3-d4422bc902b0" -->
### Best Practices

- ✅ Store rules in Git
- ✅ Use different rules for environments
- ✅ Regularly export data for backup
- ✅ Document data structures
- ✅ Use TypeScript for type safety
- ✅ Test rules with Firebase emulator

---

<!-- section_id: "c6c25f8d-d5dc-4910-8de2-1ae3a2217618" -->
## Firestore

<!-- section_id: "757b4eac-deaf-4c1b-84f3-9317685ba4c1" -->
### Overview

Firestore is a NoSQL document database. Like Firebase Realtime Database, it requires configuration versioning and manual data management.

<!-- section_id: "df64a261-42b1-44b1-a33d-845377771e2b" -->
### Prerequisites

- Firebase account
- Firebase CLI installed

<!-- section_id: "319b2c0a-6cec-458f-ada7-f54fcebbaae3" -->
### Installation and Setup

Same as Firebase Realtime Database installation.

<!-- section_id: "0e43e756-d982-46cd-9b2e-1e4924f3aac4" -->
### Firestore-Specific Files

#### Security Rules

```javascript
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users collection
    match /users/{userId} {
      allow read: if request.auth != null;
      allow write: if request.auth.uid == userId;
      allow create: if request.auth != null;
      
      match /posts/{postId} {
        allow read: if true;
        allow write: if request.auth.uid == resource.data.authorId;
      }
    }
  }
}
```

#### Indexes

```javascript
// firestore.indexes.json
{
  "indexes": [
    {
      "collectionGroup": "posts",
      "queryScope": "COLLECTION",
      "fields": [
        {
          "fieldPath": "authorId",
          "order": "ASCENDING"
        },
        {
          "fieldPath": "createdAt",
          "order": "DESCENDING"
        }
      ]
    }
  ],
  "fieldOverrides": []
}
```

<!-- section_id: "55ecb065-589b-4edc-8b0a-5488a6ade2ca" -->
### Deployment Workflow

```bash
# Deploy rules and indexes
firebase deploy --only firestore

# Deploy only rules
firebase deploy --only firestore:rules

# Deploy only indexes
firebase deploy --only firestore:indexes
```

<!-- section_id: "a6f349e1-2270-4b70-ab29-7729749c2bb0" -->
### Data Export/Import

```bash
# Export Firestore data
gcloud firestore export gs://your-bucket/export

# Import Firestore data
gcloud firestore import gs://your-bucket/export
```

<!-- section_id: "8b38701b-2fb8-46af-b405-37e0ade506e8" -->
### Repository Structure

```
project/
├── firestore/
│   ├── firestore.rules
│   ├── firestore.indexes.json
│   └── firestore.indexes.dev.json
├── backup/
│   └── firestore-backups/
└── firebase.json
```

<!-- section_id: "787ced82-04e0-4018-90a2-de1190255a71" -->
### Data Migration Example

```javascript
// scripts/migrate-users.js
const admin = require('firebase-admin');
const serviceAccount = require('./serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

async function migrateUsers() {
  const snapshot = await db.collection('users').get();
  
  const batch = db.batch();
  snapshot.docs.forEach(doc => {
    const data = doc.data();
    if (!data.createdAt) {
      batch.update(doc.ref, {
        createdAt: admin.firestore.FieldValue.serverTimestamp()
      });
    }
  });
  
  await batch.commit();
  console.log('Migration complete');
}

migrateUsers().catch(console.error);
```

<!-- section_id: "be28df91-656c-4127-a498-b6b0c4a4d727" -->
### Best Practices

- ✅ Version control rules and indexes
- ✅ Use emulator for testing
- ✅ Regularly backup data
- ✅ Use batch operations
- ✅ Monitor index creation
- ✅ Document data models

---

<!-- section_id: "74e3075a-6ce3-40dc-9c71-701e97f83cf8" -->
## Google Cloud SQL

<!-- section_id: "428f6edd-70aa-4895-884d-7aae7fd99c5a" -->
### Overview

Cloud SQL provides managed MySQL, PostgreSQL, and SQL Server databases. Use migration tools like Flyway or Liquibase for version control.

<!-- section_id: "084cf281-3f88-45e8-9fcc-ea0efb2a3474" -->
### Prerequisites

- Google Cloud account
- gcloud CLI installed
- Migration tool (Flyway or Liquibase)

<!-- section_id: "442e64e4-3e94-426d-8c7e-2943c5442b6d" -->
### Installation

```bash
# Install gcloud CLI
curl https://sdk.cloud.google.com | bash

# Install Flyway
# Download from https://flywaydb.org/download/

# Or use via Docker
docker pull flyway/flyway
```

<!-- section_id: "9cf32ac4-5136-49d7-adb4-990e22a02e6b" -->
### Flyway Setup

#### Directory Structure

```
project/
├── db/
│   ├── flyway.conf
│   └── migrations/
│       ├── V1__Create_users_table.sql
│       ├── V2__Add_indexes.sql
│       └── V3__Add_foreign_keys.sql
└── pom.xml (if using Maven)
```

#### Configuration

```properties
# flyway.conf
flyway.url=jdbc:postgresql://localhost:5432/mydb
flyway.user=myuser
flyway.password=mypass
flyway.locations=filesystem:db/migrations
flyway.baselineDescription=Initial schema
```

#### Migration Example

```sql
-- V1__Create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
```

<!-- section_id: "f23f16ae-7ac8-46aa-b3d3-9ac4e8bc5cb8" -->
### Flyway Commands

```bash
# Check current version
flyway info

# Apply migrations
flyway migrate

# Clean database (dev only)
flyway clean

# Validate migrations
flyway validate

# Repair failed migration
flyway repair
```

<!-- section_id: "01f2e51f-e36b-4733-a9e6-9534fd09f9f9" -->
### CI/CD Integration

```yaml
# .github/workflows/deploy.yml
name: Deploy Migrations

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: flyway/flyway-docker-action@v1
        with:
          flyway-cli-args: |
            -url=jdbc:postgresql://${{ secrets.DB_HOST }}/${{ secrets.DB_NAME }}
            -user=${{ secrets.DB_USER }}
            -password=${{ secrets.DB_PASSWORD }}
            migrate
```

<!-- section_id: "095a266a-86c7-40c4-b90e-34ecdaa1e0a3" -->
### Liquibase Alternative

```xml
<!-- liquibase.xml -->
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

  <changeSet id="1" author="jdoe">
    <createTable tableName="users">
      <column name="id" type="bigserial" autoIncrement="true">
        <constraints primaryKey="true" nullable="false"/>
      </column>
      <column name="email" type="varchar(255)">
        <constraints nullable="false" unique="true"/>
      </column>
      <column name="created_at" type="timestamp" defaultValueComputed="CURRENT_TIMESTAMP"/>
    </createTable>
  </changeSet>

</databaseChangeLog>
```

<!-- section_id: "93202e62-efab-49a4-b26b-49a3a790e627" -->
### Best Practices

- ✅ Use Flyway or Liquibase for migrations
- ✅ Version control all migration files
- ✅ Test on staging before production
- ✅ Use cloud proxy for security
- ✅ Monitor migration execution
- ✅ Keep backups before migrations

---

<!-- section_id: "00dd9731-352c-48ac-9351-c85548d5bd5f" -->
## BigQuery

<!-- section_id: "927c3bcd-f945-43f6-ba34-3f86af084cc6" -->
### Overview

BigQuery is a serverless data warehouse. Version control SQL queries, views, routines, and datasets through SQL files in Git.

<!-- section_id: "71c7afd1-102d-4002-a43a-b19d95ba611c" -->
### Prerequisites

- Google Cloud account
- bq CLI installed
- gcloud authenticated

<!-- section_id: "39e3fb61-d42b-48d6-a2e4-1b3ea359721f" -->
### Installation

```bash
# Install gcloud CLI
# Then install bq component
gcloud components install bq
```

<!-- section_id: "e75ecf3d-b654-4784-a27a-d9954b14aada" -->
### Version Control Strategy

#### 1. SQL Queries and Views

```sql
-- db/bigquery/views/v_user_stats.sql
CREATE OR REPLACE VIEW `project.dataset.v_user_stats` AS
SELECT
  DATE(created_at) as date,
  COUNT(DISTINCT user_id) as active_users,
  SUM(orders) as total_orders
FROM `project.dataset.events`
WHERE event_type = 'purchase'
GROUP BY date
ORDER BY date DESC;
```

#### 2. Routine Versioning

```sql
-- db/bigquery/routines/f_calculate_revenue.sql
CREATE OR REPLACE FUNCTION `project.dataset.f_calculate_revenue`(
  order_amount FLOAT64
) AS (
  SELECT order_amount * 0.08 as tax
);
```

#### 3. Dataset Configuration

```yaml
# db/bigquery/datasets/sales.yaml
name: sales
location: US
description: Sales data warehouse
defaultTableExpiration: 2592000  # 30 days
```

<!-- section_id: "1431fe06-5261-4e2e-aec3-329ce151ded7" -->
### Deployment Workflow

```bash
# Deploy view
bq query --use_legacy_sql=false < db/bigquery/views/v_user_stats.sql

# Deploy function
bq query --use_legacy_sql=false < db/bigquery/routines/f_calculate_revenue.sql

# Create dataset (if needed)
bq mk --dataset --location=US project:dataset
```

<!-- section_id: "8fcfdb05-d342-4cc7-be69-5c3c6b22833e" -->
### Repository Structure

```
project/
├── db/
│   └── bigquery/
│       ├── datasets/
│       │   └── sales.yaml
│       ├── views/
│       │   └── v_user_stats.sql
│       ├── routines/
│       │   └── f_calculate_revenue.sql
│       └── schedules/
│           └── hourly_etl.yaml
└── scripts/
    └── deploy-bigquery.sh
```

<!-- section_id: "4aff1f97-d224-4c45-b00a-06674f2112a0" -->
### CI/CD Integration

```yaml
# .github/workflows/deploy.yml
name: Deploy BigQuery

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}
      
      - name: Deploy views
        run: |
          bq query --use_legacy_sql=false < db/bigquery/views/v_user_stats.sql
```

<!-- section_id: "fed95ae4-aa32-4805-b3b7-8518a7ad75e8" -->
### Best Practices

- ✅ Store all SQL in Git
- ✅ Use views instead of direct queries
- ✅ Version control routine definitions
- ✅ Document data schemas
- ✅ Keep test and production separate
- ✅ Use Dataform for complex pipelines

---

<!-- section_id: "3596b77f-48be-490d-a0b4-0bb20ae548cc" -->
## Vertex AI

<!-- section_id: "792f2f05-826e-4771-b4b0-822cd5c2e816" -->
### Overview

Vertex AI manages ML models and pipelines. Version control model definitions, pipeline configurations, and training code.

<!-- section_id: "630fe43a-bc56-4302-8446-60c98de95048" -->
### Prerequisites

- Google Cloud account
- Vertex AI enabled
- Python 3.8+ with Vertex AI SDK

<!-- section_id: "88bf8c2c-e603-445f-b299-5a17e92a19e3" -->
### Installation

```bash
pip install google-cloud-aiplatform
```

<!-- section_id: "7cf7734f-682e-45b2-9426-6119d946115c" -->
### Version Control Strategy

#### 1. Model Definitions

```python
# models/user_classifier.py
from google.cloud import aiplatform

class UserClassifier:
    def __init__(self):
        self.model = aiplatform.Model.load('user-classifier-v1')
    
    def predict(self, features):
        return self.model.predict(features)
```

#### 2. Pipeline Configurations

```yaml
# pipelines/training_pipeline.yaml
display_name: user_classifier_training
description: Train user classification model

pipeline_steps:
  - name: data_preprocessing
    component: DataProcessingComponent
  - name: model_training
    component: ModelTrainingComponent
    depends_on: [data_preprocessing]
  - name: model_evaluation
    component: ModelEvaluationComponent
    depends_on: [model_training]
```

#### 3. Dataset Schemas

```json
{
  "dataset_id": "users_v1",
  "schema": {
    "features": [
      {"name": "age", "type": "INTEGER"},
      {"name": "email_domain", "type": "STRING"},
      {"name": "purchase_history", "type": "ARRAY<FLOAT64>"}
    ],
    "label": {
      "name": "user_type",
      "type": "STRING",
      "values": ["premium", "standard", "trial"]
    }
  }
}
```

<!-- section_id: "e1620783-6f82-45cc-b75c-cc3132f748f5" -->
### Deployment Workflow

```bash
# Deploy pipeline
python scripts/deploy_pipeline.py

# Submit training job
python scripts/submit_training.py --version v1.0
```

<!-- section_id: "b46db029-8001-4a14-a249-53ddc93c8aac" -->
### Repository Structure

```
project/
├── models/
│   ├── user_classifier.py
│   └── product_recommender.py
├── pipelines/
│   ├── training_pipeline.yaml
│   └── inference_pipeline.yaml
├── datasets/
│   └── users_schema.json
└── scripts/
    ├── deploy_pipeline.py
    └── submit_training.py
```

<!-- section_id: "967af6b5-5ea6-4f2e-8a7c-14b2a77fa5fc" -->
### CI/CD Integration

```yaml
# .github/workflows/deploy.yml
name: Deploy Model

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}
      
      - name: Deploy model
        run: python scripts/deploy_pipeline.py
```

<!-- section_id: "d3dc3428-b66b-488f-829a-f991f90d0b61" -->
### Best Practices

- ✅ Version control model definitions
- ✅ Use semantic versioning for models
- ✅ Track training hyperparameters
- ✅ Monitor model performance
- ✅ A/B test new models
- ✅ Document model architecture

---

<!-- section_id: "0fedfa53-6194-46d4-b516-842f6971499f" -->
## instant.db

<!-- section_id: "596d116f-d705-4707-9671-fdf96dd3ae62" -->
### Overview

instant.db is a developer-friendly NoSQL database with instant setup. Version control schema definitions and use CLI tools for schema management.

<!-- section_id: "6be2001c-160f-447c-b985-e5594e16f858" -->
### Prerequisites

- Node.js 18+
- npm or yarn

<!-- section_id: "189c7df8-6282-41c6-ae9f-df7ab55702f3" -->
### Installation

```bash
# Install instant.db CLI
npm install -g instant.db

# Or use locally in project
npm install instant.db
```

<!-- section_id: "ea703a31-259e-4291-b23a-6a56b0d22ff8" -->
### Configuration

```javascript
// db/schema.js
module.exports = {
  users: {
    schema: {
      id: 'string',
      email: 'string',
      name: 'string',
      createdAt: 'date'
    },
    indexes: ['email']
  },
  posts: {
    schema: {
      id: 'string',
      userId: 'string',
      title: 'string',
      content: 'text',
      createdAt: 'date'
    },
    indexes: ['userId', 'createdAt']
  }
};
```

<!-- section_id: "c820148f-369c-4ad3-b006-45f082fb506c" -->
### Deployment Workflow

```bash
# Apply schema
instant.db schema apply schema.js

# Export current data
instant.db export > backup.json

# Import data
instant.db import < backup.json
```

<!-- section_id: "1c01b4d4-9d22-4781-873f-be1d5eb2ec3c" -->
### Repository Structure

```
project/
├── db/
│   ├── schema.js
│   ├── migrations/
│   │   ├── 001_add_users.js
│   │   └── 002_add_posts.js
│   └── seed/
│       └── initial_data.js
└── instant.config.js
```

<!-- section_id: "ec2f2d76-869f-444c-8d38-367a154086e4" -->
### Best Practices

- ✅ Define schema in code
- ✅ Version control schema files
- ✅ Use migrations for changes
- ✅ Export data regularly
- ✅ Test schema changes locally
- ✅ Document field types

---

<!-- section_id: "26b46267-84e5-4b41-bc51-bcac8dc4ee94" -->
## Summary

Each platform has unique characteristics:

| Platform | Primary Method | Key Tool | Best For |
|----------|----------------|----------|----------|
| Supabase | SQL Migrations | Supabase CLI | Postgres projects |
| Firebase | Rules Versioning | Firebase CLI | Real-time apps |
| Firestore | Rules + Indexes | Firebase CLI | NoSQL apps |
| Cloud SQL | SQL Migrations | Flyway/Liquibase | Managed SQL |
| BigQuery | SQL Versioning | bq CLI | Data warehousing |
| Vertex AI | YAML/Python | Vertex SDK | ML pipelines |
| instant.db | JSON Schema | instant CLI | Quick prototypes |

---

*For migration tools comparison, see [Migration Tools Comparison](./migration-tools-comparison.md). For troubleshooting, see [Troubleshooting Guide](./troubleshooting-guide.md).*

