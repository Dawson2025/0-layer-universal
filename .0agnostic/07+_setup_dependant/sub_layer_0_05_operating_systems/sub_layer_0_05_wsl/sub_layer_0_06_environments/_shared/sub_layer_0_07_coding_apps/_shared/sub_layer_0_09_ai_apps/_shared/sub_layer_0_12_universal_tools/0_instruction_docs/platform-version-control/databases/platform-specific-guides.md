---
resource_id: "29191e55-ab0e-40d0-8952-a6a14fa10f5a"
resource_type: "document"
resource_name: "platform-specific-guides"
---
# Platform-Specific Guides
*Detailed Database Version Control Workflows for Each Platform*

<!-- section_id: "0656feb3-a6a9-4d53-9353-c868af0e27c8" -->
## Overview

This guide provides detailed, platform-specific instructions for version controlling databases across different platforms. Each section includes installation, configuration, common workflows, and examples.

<!-- section_id: "5fa0f118-5b92-4a20-a548-6c5c4d17fe8a" -->
## Table of Contents

1. [Supabase](#supabase)
2. [Firebase Realtime Database](#firebase-realtime-database)
3. [Firestore](#firestore)
4. [Google Cloud SQL](#google-cloud-sql)
5. [BigQuery](#bigquery)
6. [Vertex AI](#vertex-ai)
7. [instant.db](#instantdb)

---

<!-- section_id: "f78c6862-d937-45f3-b83c-3ff571da14ff" -->
## Supabase

<!-- section_id: "2de5bfb4-709f-4f12-9112-d0a43b485553" -->
### Overview

Supabase is a PostgreSQL-based platform with built-in migration support through the Supabase CLI. It provides excellent version control capabilities with native Git integration.

<!-- section_id: "8e0cf818-db00-40ad-8e92-c043ddee6b38" -->
### Prerequisites

- Supabase account
- Supabase CLI installed
- Node.js 18+ or Python 3.8+

<!-- section_id: "506bdeab-7d9e-45b8-898f-a6a2af510d07" -->
### Installation

```bash
# Install Supabase CLI
npm install -g supabase

# Or via Homebrew (macOS)
brew install supabase/tap/supabase

# Login
supabase login
```

<!-- section_id: "39097631-7d93-4666-8020-949dc9ebbadb" -->
### Initialization

```bash
# Initialize a new project
supabase init

# Link to existing project
supabase link --project-ref your-project-ref
```

<!-- section_id: "1dcdb7e7-4a4f-49d7-ba4c-8bc022058722" -->
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

<!-- section_id: "c23cfca5-d164-4381-b127-04a59c962b48" -->
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

<!-- section_id: "4514236a-12be-4634-9c84-f61b7c128c48" -->
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

<!-- section_id: "234ed73c-31c8-4338-a8d1-f2d43819dc26" -->
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

<!-- section_id: "8d544a4f-795c-4f57-9fe6-1b7247e4509f" -->
### Best Practices

- ✅ Use timestamped migration names
- ✅ Include up and down migrations when possible
- ✅ Test locally before pushing
- ✅ Review migrations in PRs
- ✅ Use Supabase RLS for security
- ✅ Keep migrations small and focused

---

<!-- section_id: "bb438121-d0a8-4906-92b8-d8aa8eaddd66" -->
## Firebase Realtime Database

<!-- section_id: "1e3737eb-1572-48c9-9c31-5197d2cd2638" -->
### Overview

Firebase Realtime Database uses JSON and requires manual export/import for version control. The Firebase CLI manages configuration and deployments.

<!-- section_id: "28d0b90d-5d84-4691-afac-76d882d60a26" -->
### Prerequisites

- Firebase account
- Firebase CLI installed
- Node.js 8.0+

<!-- section_id: "57a1a27d-7986-4dc4-a560-516fed390312" -->
### Installation

```bash
npm install -g firebase-tools

# Login
firebase login
```

<!-- section_id: "315749f3-03ca-42dc-9920-ecfb6219575f" -->
### Initialization

```bash
# Initialize Firebase project
firebase init

# Select:
# - Realtime Database
# - Configure security rules
```

<!-- section_id: "bf687e28-b534-412d-88c9-cbc577d92752" -->
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

<!-- section_id: "61259b87-de14-4572-801e-f47694c723af" -->
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

<!-- section_id: "545473b3-1730-47c8-acce-669444ec8cc9" -->
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

<!-- section_id: "9f17698e-125a-4267-bcae-ef18ccc80f75" -->
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

<!-- section_id: "c6cfdf79-7f3e-4fd5-abc9-fd98ab8c755f" -->
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

<!-- section_id: "444e3c88-e6d9-4d92-9cb4-8fed8bacf0ff" -->
### Best Practices

- ✅ Store rules in Git
- ✅ Use different rules for environments
- ✅ Regularly export data for backup
- ✅ Document data structures
- ✅ Use TypeScript for type safety
- ✅ Test rules with Firebase emulator

---

<!-- section_id: "d0eaaafd-0049-4def-ad1c-533ee204d9cf" -->
## Firestore

<!-- section_id: "bd6c2770-e895-4096-94c7-c89ded22bf9f" -->
### Overview

Firestore is a NoSQL document database. Like Firebase Realtime Database, it requires configuration versioning and manual data management.

<!-- section_id: "43c4a85c-3bec-436a-a3e4-61968f8c058b" -->
### Prerequisites

- Firebase account
- Firebase CLI installed

<!-- section_id: "21242c16-d318-4961-8125-2fa7d9916f5d" -->
### Installation and Setup

Same as Firebase Realtime Database installation.

<!-- section_id: "e50fcf99-4d02-440e-ba6c-9173573a65cc" -->
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

<!-- section_id: "2854035f-60f1-4b32-84e3-7a1a2a5ee16c" -->
### Deployment Workflow

```bash
# Deploy rules and indexes
firebase deploy --only firestore

# Deploy only rules
firebase deploy --only firestore:rules

# Deploy only indexes
firebase deploy --only firestore:indexes
```

<!-- section_id: "282685ef-da49-44e8-8f2d-9ad8fa502fbc" -->
### Data Export/Import

```bash
# Export Firestore data
gcloud firestore export gs://your-bucket/export

# Import Firestore data
gcloud firestore import gs://your-bucket/export
```

<!-- section_id: "be6ac0de-4561-4a7b-87d5-09b23b77268b" -->
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

<!-- section_id: "488da7fe-3318-451c-ad2b-2cc176c687f8" -->
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

<!-- section_id: "888da1ac-3c3e-4b46-aff8-e2946b690c29" -->
### Best Practices

- ✅ Version control rules and indexes
- ✅ Use emulator for testing
- ✅ Regularly backup data
- ✅ Use batch operations
- ✅ Monitor index creation
- ✅ Document data models

---

<!-- section_id: "4c78f21a-1f5d-4dd5-b060-12eb374fbb73" -->
## Google Cloud SQL

<!-- section_id: "90a3ff6f-7547-4e74-b5d1-9d582708ce75" -->
### Overview

Cloud SQL provides managed MySQL, PostgreSQL, and SQL Server databases. Use migration tools like Flyway or Liquibase for version control.

<!-- section_id: "87722ee8-9335-4bc5-acbd-b0663d2b8a83" -->
### Prerequisites

- Google Cloud account
- gcloud CLI installed
- Migration tool (Flyway or Liquibase)

<!-- section_id: "289f84dc-d740-49ae-8fb4-79502e661821" -->
### Installation

```bash
# Install gcloud CLI
curl https://sdk.cloud.google.com | bash

# Install Flyway
# Download from https://flywaydb.org/download/

# Or use via Docker
docker pull flyway/flyway
```

<!-- section_id: "00e31cee-3c0f-43a6-8c0e-3825f088d9a9" -->
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

<!-- section_id: "f612d1ec-94fa-419e-8500-2de5d74c8732" -->
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

<!-- section_id: "cc2640b0-4b1f-4514-b759-528158b42190" -->
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

<!-- section_id: "17d1cfd3-1370-448c-8296-73b59bbd0406" -->
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

<!-- section_id: "8da46fcf-2dad-47d0-b2bb-2fa7d11c575c" -->
### Best Practices

- ✅ Use Flyway or Liquibase for migrations
- ✅ Version control all migration files
- ✅ Test on staging before production
- ✅ Use cloud proxy for security
- ✅ Monitor migration execution
- ✅ Keep backups before migrations

---

<!-- section_id: "1a807117-a327-4997-8709-4f2693fec2f2" -->
## BigQuery

<!-- section_id: "413654d5-2c6a-41a3-93ef-521bb2167ab1" -->
### Overview

BigQuery is a serverless data warehouse. Version control SQL queries, views, routines, and datasets through SQL files in Git.

<!-- section_id: "b7b07abd-af10-4741-97d8-4341dbc5a0bd" -->
### Prerequisites

- Google Cloud account
- bq CLI installed
- gcloud authenticated

<!-- section_id: "9d23356d-d069-40b7-8fa8-30dcf4e6d10a" -->
### Installation

```bash
# Install gcloud CLI
# Then install bq component
gcloud components install bq
```

<!-- section_id: "6023e3fa-b594-49b8-93bd-0788c387fdb9" -->
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

<!-- section_id: "cb477f00-4dcc-4c8e-8ce0-d35986596cf2" -->
### Deployment Workflow

```bash
# Deploy view
bq query --use_legacy_sql=false < db/bigquery/views/v_user_stats.sql

# Deploy function
bq query --use_legacy_sql=false < db/bigquery/routines/f_calculate_revenue.sql

# Create dataset (if needed)
bq mk --dataset --location=US project:dataset
```

<!-- section_id: "801451ee-c6de-4f92-b101-6a0544cd57e1" -->
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

<!-- section_id: "d05faed4-7757-4e17-9fd5-ff3c6a38e964" -->
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

<!-- section_id: "8ab21aa5-e11d-41c9-b906-4b61d68925d3" -->
### Best Practices

- ✅ Store all SQL in Git
- ✅ Use views instead of direct queries
- ✅ Version control routine definitions
- ✅ Document data schemas
- ✅ Keep test and production separate
- ✅ Use Dataform for complex pipelines

---

<!-- section_id: "a623ef38-6920-4aa2-814f-b7234335644f" -->
## Vertex AI

<!-- section_id: "6037cad9-2629-4aac-b34a-67c6a1f41bc8" -->
### Overview

Vertex AI manages ML models and pipelines. Version control model definitions, pipeline configurations, and training code.

<!-- section_id: "18b17e04-0309-4520-a28e-e28fbbec170e" -->
### Prerequisites

- Google Cloud account
- Vertex AI enabled
- Python 3.8+ with Vertex AI SDK

<!-- section_id: "56944a10-4a4b-40c1-a7e5-996a4d5c2651" -->
### Installation

```bash
pip install google-cloud-aiplatform
```

<!-- section_id: "363f3914-2130-4d6c-97ab-142a69500b13" -->
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

<!-- section_id: "e7345609-a6fc-4f94-a4f8-f311eb082c44" -->
### Deployment Workflow

```bash
# Deploy pipeline
python scripts/deploy_pipeline.py

# Submit training job
python scripts/submit_training.py --version v1.0
```

<!-- section_id: "ddeba5dc-99d8-4e4e-b920-70e4c6ec87a4" -->
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

<!-- section_id: "81a63969-e0e0-4b09-b8dc-6939548c3366" -->
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

<!-- section_id: "e2900090-9f47-45dc-97f2-890573743988" -->
### Best Practices

- ✅ Version control model definitions
- ✅ Use semantic versioning for models
- ✅ Track training hyperparameters
- ✅ Monitor model performance
- ✅ A/B test new models
- ✅ Document model architecture

---

<!-- section_id: "dde83da0-5287-4742-95cf-db9cfbd37c9c" -->
## instant.db

<!-- section_id: "39a70501-b29e-4169-ae4f-c897950f2444" -->
### Overview

instant.db is a developer-friendly NoSQL database with instant setup. Version control schema definitions and use CLI tools for schema management.

<!-- section_id: "e0ddb707-7704-4a9a-835a-246afb644e2a" -->
### Prerequisites

- Node.js 18+
- npm or yarn

<!-- section_id: "bc2e1e3a-c478-4fc6-997a-944872d51d2a" -->
### Installation

```bash
# Install instant.db CLI
npm install -g instant.db

# Or use locally in project
npm install instant.db
```

<!-- section_id: "fda1e29f-9e24-4db4-9674-738fdbadceae" -->
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

<!-- section_id: "c8e14cce-bcda-44f0-89c9-88c0847d3120" -->
### Deployment Workflow

```bash
# Apply schema
instant.db schema apply schema.js

# Export current data
instant.db export > backup.json

# Import data
instant.db import < backup.json
```

<!-- section_id: "2ffb1940-f021-4828-86e8-b7cf6bc5e87a" -->
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

<!-- section_id: "da9fee13-d439-468f-9e77-e7dac0299ba9" -->
### Best Practices

- ✅ Define schema in code
- ✅ Version control schema files
- ✅ Use migrations for changes
- ✅ Export data regularly
- ✅ Test schema changes locally
- ✅ Document field types

---

<!-- section_id: "c99c4be4-826c-422c-8525-110fcee9b1ad" -->
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

