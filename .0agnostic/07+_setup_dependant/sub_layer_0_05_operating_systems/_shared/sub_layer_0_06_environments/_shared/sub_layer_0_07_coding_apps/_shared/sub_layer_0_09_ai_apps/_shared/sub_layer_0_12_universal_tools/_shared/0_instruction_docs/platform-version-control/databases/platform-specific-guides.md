---
resource_id: "3392b5df-1ec4-4ffc-9c92-a4bc0c24466c"
resource_type: "document"
resource_name: "platform-specific-guides"
---
# Platform-Specific Guides
*Detailed Database Version Control Workflows for Each Platform*

<!-- section_id: "a2cb26d0-6229-4744-81ad-f71c4eb98ed6" -->
## Overview

This guide provides detailed, platform-specific instructions for version controlling databases across different platforms. Each section includes installation, configuration, common workflows, and examples.

<!-- section_id: "97825c36-f967-4e2d-99b4-0cb0b31fd4d8" -->
## Table of Contents

1. [Supabase](#supabase)
2. [Firebase Realtime Database](#firebase-realtime-database)
3. [Firestore](#firestore)
4. [Google Cloud SQL](#google-cloud-sql)
5. [BigQuery](#bigquery)
6. [Vertex AI](#vertex-ai)
7. [instant.db](#instantdb)

---

<!-- section_id: "daae30e2-70f7-4587-ba06-a2cf16245629" -->
## Supabase

<!-- section_id: "fd769acd-2c9b-4fb2-a3e3-8c011a5810c4" -->
### Overview

Supabase is a PostgreSQL-based platform with built-in migration support through the Supabase CLI. It provides excellent version control capabilities with native Git integration.

<!-- section_id: "dc1b8c8d-47c5-4eac-875b-30ee72a7d745" -->
### Prerequisites

- Supabase account
- Supabase CLI installed
- Node.js 18+ or Python 3.8+

<!-- section_id: "6788169f-04bd-4b24-a0c7-f5bb624af8ed" -->
### Installation

```bash
# Install Supabase CLI
npm install -g supabase

# Or via Homebrew (macOS)
brew install supabase/tap/supabase

# Login
supabase login
```

<!-- section_id: "1716b948-f197-4bd4-b6aa-65d68fdf5b11" -->
### Initialization

```bash
# Initialize a new project
supabase init

# Link to existing project
supabase link --project-ref your-project-ref
```

<!-- section_id: "6e20c5c4-36c3-4c85-a4d6-305d86683543" -->
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

<!-- section_id: "6bf66a91-f9a9-4379-a5bf-b5bbf2ff1463" -->
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

<!-- section_id: "a019efb4-d06b-489a-a939-3d772ba15326" -->
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

<!-- section_id: "bf8f67f2-f9fc-4970-a3b3-d23fb0e1945b" -->
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

<!-- section_id: "24fa8689-dbed-4630-b5a4-ba13687cee71" -->
### Best Practices

- ✅ Use timestamped migration names
- ✅ Include up and down migrations when possible
- ✅ Test locally before pushing
- ✅ Review migrations in PRs
- ✅ Use Supabase RLS for security
- ✅ Keep migrations small and focused

---

<!-- section_id: "53db1c69-3792-4a72-8ac5-684130d4ea37" -->
## Firebase Realtime Database

<!-- section_id: "6138b0c0-45b0-41d0-9fad-6710205b2d64" -->
### Overview

Firebase Realtime Database uses JSON and requires manual export/import for version control. The Firebase CLI manages configuration and deployments.

<!-- section_id: "354ce8c2-a82e-40f4-b82c-e6c5becd9041" -->
### Prerequisites

- Firebase account
- Firebase CLI installed
- Node.js 8.0+

<!-- section_id: "27f1f814-54c6-4cbd-85fc-33eb3656f2ad" -->
### Installation

```bash
npm install -g firebase-tools

# Login
firebase login
```

<!-- section_id: "c4fa6053-b39c-4112-b552-895f14022390" -->
### Initialization

```bash
# Initialize Firebase project
firebase init

# Select:
# - Realtime Database
# - Configure security rules
```

<!-- section_id: "4fe46bf7-b099-4ba1-bea9-bf1f7a74a94b" -->
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

<!-- section_id: "f7596cc6-b981-4e3f-aa01-d6f0721e1d30" -->
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

<!-- section_id: "3c80b15f-87a6-419b-8d55-46cca47af1d9" -->
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

<!-- section_id: "a01f0f33-6dcd-4a7a-8c0a-656655909377" -->
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

<!-- section_id: "8c6fd59b-8cfe-4045-9659-405ca8fdcfe2" -->
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

<!-- section_id: "988da7c8-3591-4892-bfb6-fbe9d3a832f8" -->
### Best Practices

- ✅ Store rules in Git
- ✅ Use different rules for environments
- ✅ Regularly export data for backup
- ✅ Document data structures
- ✅ Use TypeScript for type safety
- ✅ Test rules with Firebase emulator

---

<!-- section_id: "0c383ca8-6fba-4887-84f3-e7af12553709" -->
## Firestore

<!-- section_id: "cebe9251-697a-494e-b66f-d7c4bf6a16c3" -->
### Overview

Firestore is a NoSQL document database. Like Firebase Realtime Database, it requires configuration versioning and manual data management.

<!-- section_id: "f10fd769-d54d-4649-a2e5-891eb7d106cf" -->
### Prerequisites

- Firebase account
- Firebase CLI installed

<!-- section_id: "5a1dc930-8489-4680-81c5-c820bb928d99" -->
### Installation and Setup

Same as Firebase Realtime Database installation.

<!-- section_id: "66b0dc32-6c3a-40a9-a0ae-031c69215ec8" -->
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

<!-- section_id: "f3b788e5-02c8-456e-bfde-1ff8e748c1eb" -->
### Deployment Workflow

```bash
# Deploy rules and indexes
firebase deploy --only firestore

# Deploy only rules
firebase deploy --only firestore:rules

# Deploy only indexes
firebase deploy --only firestore:indexes
```

<!-- section_id: "569a8648-ad85-42f9-8513-92d2b225b5dd" -->
### Data Export/Import

```bash
# Export Firestore data
gcloud firestore export gs://your-bucket/export

# Import Firestore data
gcloud firestore import gs://your-bucket/export
```

<!-- section_id: "f278a71f-0dde-4a4b-87a7-97736ca7812d" -->
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

<!-- section_id: "66716792-8bb0-4cb3-bd8e-4cb7331e40dd" -->
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

<!-- section_id: "c5889be1-aaae-4137-8a2d-0f56e36e10a1" -->
### Best Practices

- ✅ Version control rules and indexes
- ✅ Use emulator for testing
- ✅ Regularly backup data
- ✅ Use batch operations
- ✅ Monitor index creation
- ✅ Document data models

---

<!-- section_id: "284de466-b602-4f2a-ad69-57aa75ed612e" -->
## Google Cloud SQL

<!-- section_id: "7a23404b-ab1a-4f86-b90d-a872618ef246" -->
### Overview

Cloud SQL provides managed MySQL, PostgreSQL, and SQL Server databases. Use migration tools like Flyway or Liquibase for version control.

<!-- section_id: "c3c51a3d-30d3-41f4-a8da-2953ec06517e" -->
### Prerequisites

- Google Cloud account
- gcloud CLI installed
- Migration tool (Flyway or Liquibase)

<!-- section_id: "0682fe67-c21a-4332-8dea-d861f5951979" -->
### Installation

```bash
# Install gcloud CLI
curl https://sdk.cloud.google.com | bash

# Install Flyway
# Download from https://flywaydb.org/download/

# Or use via Docker
docker pull flyway/flyway
```

<!-- section_id: "8b1bcf6c-936b-491b-87d4-f223605d6ad4" -->
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

<!-- section_id: "f0a4656e-0746-4dcd-bb3c-5174d4f04e83" -->
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

<!-- section_id: "6f09fc0f-1061-4ec8-b691-826ea77ca888" -->
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

<!-- section_id: "810a7922-4500-444d-ba8f-e42efedee024" -->
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

<!-- section_id: "165c0fc3-0b4d-4f34-8018-b23ef5834beb" -->
### Best Practices

- ✅ Use Flyway or Liquibase for migrations
- ✅ Version control all migration files
- ✅ Test on staging before production
- ✅ Use cloud proxy for security
- ✅ Monitor migration execution
- ✅ Keep backups before migrations

---

<!-- section_id: "94c41e8f-430c-4e6d-b257-1b8d4cbe582f" -->
## BigQuery

<!-- section_id: "7a25a3f4-47c4-4c39-9bd5-1dbc07c393b4" -->
### Overview

BigQuery is a serverless data warehouse. Version control SQL queries, views, routines, and datasets through SQL files in Git.

<!-- section_id: "ef621848-8568-49c3-a4ca-eadedad40924" -->
### Prerequisites

- Google Cloud account
- bq CLI installed
- gcloud authenticated

<!-- section_id: "1a8b3a4c-0ef3-4ea9-b48e-ab86fba543e6" -->
### Installation

```bash
# Install gcloud CLI
# Then install bq component
gcloud components install bq
```

<!-- section_id: "66bbe180-e411-4ac0-93cc-0262c38dfce7" -->
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

<!-- section_id: "adbe8088-2085-4eaf-b074-135f420f9fdb" -->
### Deployment Workflow

```bash
# Deploy view
bq query --use_legacy_sql=false < db/bigquery/views/v_user_stats.sql

# Deploy function
bq query --use_legacy_sql=false < db/bigquery/routines/f_calculate_revenue.sql

# Create dataset (if needed)
bq mk --dataset --location=US project:dataset
```

<!-- section_id: "8d35d69c-6940-4c24-b583-1fb838892f26" -->
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

<!-- section_id: "461c26d9-aef1-4f75-9be1-577b4d406243" -->
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

<!-- section_id: "9d9875b8-7f63-452d-b5e0-85695c795525" -->
### Best Practices

- ✅ Store all SQL in Git
- ✅ Use views instead of direct queries
- ✅ Version control routine definitions
- ✅ Document data schemas
- ✅ Keep test and production separate
- ✅ Use Dataform for complex pipelines

---

<!-- section_id: "b8f8647b-9537-4b6f-b0ce-7f95828bf71d" -->
## Vertex AI

<!-- section_id: "a0f405bb-5e5a-45b2-ada0-6640ea46c0c1" -->
### Overview

Vertex AI manages ML models and pipelines. Version control model definitions, pipeline configurations, and training code.

<!-- section_id: "43ab4558-e07a-4e04-a5f9-102d3547e3e1" -->
### Prerequisites

- Google Cloud account
- Vertex AI enabled
- Python 3.8+ with Vertex AI SDK

<!-- section_id: "462a2708-da3b-4fba-830f-5c1aaf5ad118" -->
### Installation

```bash
pip install google-cloud-aiplatform
```

<!-- section_id: "7770af9f-f758-4b8b-80f9-cab79d8c6b08" -->
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

<!-- section_id: "5c58172c-d0b5-42cf-a04e-ca1461aca05b" -->
### Deployment Workflow

```bash
# Deploy pipeline
python scripts/deploy_pipeline.py

# Submit training job
python scripts/submit_training.py --version v1.0
```

<!-- section_id: "a61f3f33-2908-4466-9fe2-e4cc15683b5f" -->
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

<!-- section_id: "4cb4f362-0c46-4c78-b6ab-71fcf03c6ebc" -->
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

<!-- section_id: "5e236c14-c3b6-4aae-8180-4bbfa6699efe" -->
### Best Practices

- ✅ Version control model definitions
- ✅ Use semantic versioning for models
- ✅ Track training hyperparameters
- ✅ Monitor model performance
- ✅ A/B test new models
- ✅ Document model architecture

---

<!-- section_id: "13cf9dfd-e9a3-4b81-9444-da650bdb4fc7" -->
## instant.db

<!-- section_id: "beeafb0f-e074-4809-a68c-07cb4d13fbc3" -->
### Overview

instant.db is a developer-friendly NoSQL database with instant setup. Version control schema definitions and use CLI tools for schema management.

<!-- section_id: "d443d076-100c-43c2-98ab-8f08ad0be92c" -->
### Prerequisites

- Node.js 18+
- npm or yarn

<!-- section_id: "e60deb03-140c-4877-be03-2af237e17c30" -->
### Installation

```bash
# Install instant.db CLI
npm install -g instant.db

# Or use locally in project
npm install instant.db
```

<!-- section_id: "20ef6153-f623-45f2-a621-4e4497b31875" -->
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

<!-- section_id: "4b07521e-c0cc-4c53-a062-f88838fc6981" -->
### Deployment Workflow

```bash
# Apply schema
instant.db schema apply schema.js

# Export current data
instant.db export > backup.json

# Import data
instant.db import < backup.json
```

<!-- section_id: "30c88591-d9f5-41c6-bd96-785033700ffa" -->
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

<!-- section_id: "ee8b9ff9-a350-465a-9f39-ac71562b0121" -->
### Best Practices

- ✅ Define schema in code
- ✅ Version control schema files
- ✅ Use migrations for changes
- ✅ Export data regularly
- ✅ Test schema changes locally
- ✅ Document field types

---

<!-- section_id: "d3a2f704-a13a-43ac-ac33-0d960f5ff89c" -->
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

