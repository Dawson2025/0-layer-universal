---
resource_id: "fecabc9e-e1f4-4a4c-82e0-61b20713a1b7"
resource_type: "document"
resource_name: "platform-specific-guides"
---
# Platform-Specific Guides
*Detailed Database Version Control Workflows for Each Platform*

<!-- section_id: "4abf15ec-8771-412a-9773-1e1eed2c4ad8" -->
## Overview

This guide provides detailed, platform-specific instructions for version controlling databases across different platforms. Each section includes installation, configuration, common workflows, and examples.

<!-- section_id: "c96a0b0a-61ed-4a7e-ac87-f92a5126e413" -->
## Table of Contents

1. [Supabase](#supabase)
2. [Firebase Realtime Database](#firebase-realtime-database)
3. [Firestore](#firestore)
4. [Google Cloud SQL](#google-cloud-sql)
5. [BigQuery](#bigquery)
6. [Vertex AI](#vertex-ai)
7. [instant.db](#instantdb)

---

<!-- section_id: "18311799-5f7f-42c9-a379-ab157fb698e7" -->
## Supabase

<!-- section_id: "d14a1237-dde6-4bde-9825-6148340a7afc" -->
### Overview

Supabase is a PostgreSQL-based platform with built-in migration support through the Supabase CLI. It provides excellent version control capabilities with native Git integration.

<!-- section_id: "8800d607-19d6-4ecb-ab5d-650df477924b" -->
### Prerequisites

- Supabase account
- Supabase CLI installed
- Node.js 18+ or Python 3.8+

<!-- section_id: "fffbbe3a-6d3b-44a4-9b92-9a4f1133a7d2" -->
### Installation

```bash
# Install Supabase CLI
npm install -g supabase

# Or via Homebrew (macOS)
brew install supabase/tap/supabase

# Login
supabase login
```

<!-- section_id: "466b1042-93e7-4ea1-8004-ca51753f9ea0" -->
### Initialization

```bash
# Initialize a new project
supabase init

# Link to existing project
supabase link --project-ref your-project-ref
```

<!-- section_id: "7c87eb18-ca50-4c70-bad6-532a5b058131" -->
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

<!-- section_id: "61a654c3-eb67-4c05-9700-9e7f32fcdb14" -->
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

<!-- section_id: "5d5b32ee-9967-4cda-a21d-274c46f2df86" -->
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

<!-- section_id: "075a7b20-e8eb-4b83-83d8-021c8358931c" -->
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

<!-- section_id: "7c1a382e-64b8-431a-9df7-d2016eccbecf" -->
### Best Practices

- ✅ Use timestamped migration names
- ✅ Include up and down migrations when possible
- ✅ Test locally before pushing
- ✅ Review migrations in PRs
- ✅ Use Supabase RLS for security
- ✅ Keep migrations small and focused

---

<!-- section_id: "afd557a3-414f-4443-8e68-2dc3b1d097da" -->
## Firebase Realtime Database

<!-- section_id: "62d701f8-c0e2-463c-ae4c-94bef01e5d58" -->
### Overview

Firebase Realtime Database uses JSON and requires manual export/import for version control. The Firebase CLI manages configuration and deployments.

<!-- section_id: "8eb52f0f-d219-468d-b23f-d10a7cfa47e2" -->
### Prerequisites

- Firebase account
- Firebase CLI installed
- Node.js 8.0+

<!-- section_id: "b7e83ef9-db56-4459-89fe-dfaf9ace78f6" -->
### Installation

```bash
npm install -g firebase-tools

# Login
firebase login
```

<!-- section_id: "402a9158-328b-4f2b-b664-d45c6202435a" -->
### Initialization

```bash
# Initialize Firebase project
firebase init

# Select:
# - Realtime Database
# - Configure security rules
```

<!-- section_id: "dc58c71d-76ae-48df-b3bb-461bf19f786a" -->
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

<!-- section_id: "facb6e7b-5d49-4fff-93ce-6ce7f0dc587a" -->
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

<!-- section_id: "e63e0d10-1e03-45bf-ad5e-12e59c4543f3" -->
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

<!-- section_id: "e9273e27-ead3-49d4-8605-ea8f1ec04706" -->
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

<!-- section_id: "447ad3c8-8bc2-4568-8ead-5fac627e2403" -->
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

<!-- section_id: "992764e0-73a3-44e2-9c19-ccbdbba4e940" -->
### Best Practices

- ✅ Store rules in Git
- ✅ Use different rules for environments
- ✅ Regularly export data for backup
- ✅ Document data structures
- ✅ Use TypeScript for type safety
- ✅ Test rules with Firebase emulator

---

<!-- section_id: "aeaaa8d7-e97c-4413-9caf-59c637040e4d" -->
## Firestore

<!-- section_id: "73ffab69-6eec-4476-bbfa-cb871ff4a509" -->
### Overview

Firestore is a NoSQL document database. Like Firebase Realtime Database, it requires configuration versioning and manual data management.

<!-- section_id: "52511aa6-87e9-4125-a491-f9fe13e2a852" -->
### Prerequisites

- Firebase account
- Firebase CLI installed

<!-- section_id: "8afcaab2-a88f-42ba-8bc5-efdfa0020e8a" -->
### Installation and Setup

Same as Firebase Realtime Database installation.

<!-- section_id: "bca121b6-024d-46e1-b276-d97542695de0" -->
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

<!-- section_id: "216b608a-f788-4702-aaa8-b3ff97db6c39" -->
### Deployment Workflow

```bash
# Deploy rules and indexes
firebase deploy --only firestore

# Deploy only rules
firebase deploy --only firestore:rules

# Deploy only indexes
firebase deploy --only firestore:indexes
```

<!-- section_id: "62efec5d-2d86-4062-978f-412f878c017a" -->
### Data Export/Import

```bash
# Export Firestore data
gcloud firestore export gs://your-bucket/export

# Import Firestore data
gcloud firestore import gs://your-bucket/export
```

<!-- section_id: "133f2825-7a1b-46fc-8412-ce184d07bae4" -->
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

<!-- section_id: "1a10a3e2-7139-4846-96b9-5497c354b954" -->
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

<!-- section_id: "6bf52e03-7bdf-4e01-b9c5-527c009eaba3" -->
### Best Practices

- ✅ Version control rules and indexes
- ✅ Use emulator for testing
- ✅ Regularly backup data
- ✅ Use batch operations
- ✅ Monitor index creation
- ✅ Document data models

---

<!-- section_id: "1d60ad2d-7bd5-4041-9ae0-79f854888453" -->
## Google Cloud SQL

<!-- section_id: "fc440c32-1497-4310-82c4-b6a920612acb" -->
### Overview

Cloud SQL provides managed MySQL, PostgreSQL, and SQL Server databases. Use migration tools like Flyway or Liquibase for version control.

<!-- section_id: "116ec8a3-8b0f-42f6-a532-e5c2d952481f" -->
### Prerequisites

- Google Cloud account
- gcloud CLI installed
- Migration tool (Flyway or Liquibase)

<!-- section_id: "3ef890f8-9965-4468-a7bf-3ca3ef247337" -->
### Installation

```bash
# Install gcloud CLI
curl https://sdk.cloud.google.com | bash

# Install Flyway
# Download from https://flywaydb.org/download/

# Or use via Docker
docker pull flyway/flyway
```

<!-- section_id: "63b6e634-d2fe-40e2-bd42-2adaa8b4d1e8" -->
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

<!-- section_id: "c35aeb38-d0ae-4a1b-b3cc-3b5742e62cc6" -->
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

<!-- section_id: "24c3e3fb-65f1-451d-abab-86e1a2a70f4e" -->
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

<!-- section_id: "c9477110-b81a-4fed-ae71-a115cdc55908" -->
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

<!-- section_id: "dc0cf204-a19e-4148-ae17-5d704ab59f0a" -->
### Best Practices

- ✅ Use Flyway or Liquibase for migrations
- ✅ Version control all migration files
- ✅ Test on staging before production
- ✅ Use cloud proxy for security
- ✅ Monitor migration execution
- ✅ Keep backups before migrations

---

<!-- section_id: "87e7e62f-320b-4752-86ba-3c9b9decc659" -->
## BigQuery

<!-- section_id: "4e3ccc45-1322-4861-b2e3-60d08cf3cca2" -->
### Overview

BigQuery is a serverless data warehouse. Version control SQL queries, views, routines, and datasets through SQL files in Git.

<!-- section_id: "9ca97383-d925-4faa-a085-5b6123d316ba" -->
### Prerequisites

- Google Cloud account
- bq CLI installed
- gcloud authenticated

<!-- section_id: "98d7ed5e-e6c5-433e-8f90-95deedcf8ca5" -->
### Installation

```bash
# Install gcloud CLI
# Then install bq component
gcloud components install bq
```

<!-- section_id: "d831a055-7bec-4c88-9152-5a138469e78c" -->
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

<!-- section_id: "d30fb2ab-b016-4e34-99ff-db94d865b5a6" -->
### Deployment Workflow

```bash
# Deploy view
bq query --use_legacy_sql=false < db/bigquery/views/v_user_stats.sql

# Deploy function
bq query --use_legacy_sql=false < db/bigquery/routines/f_calculate_revenue.sql

# Create dataset (if needed)
bq mk --dataset --location=US project:dataset
```

<!-- section_id: "8fdd5a59-9ae7-4d12-a5b4-49c239a17827" -->
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

<!-- section_id: "80d70f63-2a5c-4cf7-bb78-49eb09589cd2" -->
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

<!-- section_id: "901f74d1-4de0-4568-b184-286087ed70bc" -->
### Best Practices

- ✅ Store all SQL in Git
- ✅ Use views instead of direct queries
- ✅ Version control routine definitions
- ✅ Document data schemas
- ✅ Keep test and production separate
- ✅ Use Dataform for complex pipelines

---

<!-- section_id: "713cf141-8ab7-4384-8029-643f2451f11b" -->
## Vertex AI

<!-- section_id: "1ccabb76-3a72-4361-b347-be7cb38459bd" -->
### Overview

Vertex AI manages ML models and pipelines. Version control model definitions, pipeline configurations, and training code.

<!-- section_id: "0e4fe1a6-59a8-40d5-93f4-cf838e2d0263" -->
### Prerequisites

- Google Cloud account
- Vertex AI enabled
- Python 3.8+ with Vertex AI SDK

<!-- section_id: "97297a8c-1c12-42d1-af27-0356cad2498c" -->
### Installation

```bash
pip install google-cloud-aiplatform
```

<!-- section_id: "a0c7ec82-e748-4ad5-8881-381458611af3" -->
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

<!-- section_id: "55b1d17c-0b87-41c5-b03f-594b73ffc117" -->
### Deployment Workflow

```bash
# Deploy pipeline
python scripts/deploy_pipeline.py

# Submit training job
python scripts/submit_training.py --version v1.0
```

<!-- section_id: "d748445b-1083-494e-8a79-439885b801f4" -->
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

<!-- section_id: "98643b49-7fd3-4726-8ddf-f953cc5309b5" -->
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

<!-- section_id: "1ed5c7f4-bbb9-43b9-a04b-e595f63ebcea" -->
### Best Practices

- ✅ Version control model definitions
- ✅ Use semantic versioning for models
- ✅ Track training hyperparameters
- ✅ Monitor model performance
- ✅ A/B test new models
- ✅ Document model architecture

---

<!-- section_id: "b216faab-30be-4ea4-b1ed-a908c15355f1" -->
## instant.db

<!-- section_id: "c83e1542-8ff3-4285-a15f-2ed11b92c7ea" -->
### Overview

instant.db is a developer-friendly NoSQL database with instant setup. Version control schema definitions and use CLI tools for schema management.

<!-- section_id: "cd610339-495a-41af-9f2d-a857a31ce8cc" -->
### Prerequisites

- Node.js 18+
- npm or yarn

<!-- section_id: "cb317ec6-3cfe-4a05-add4-dcc79eee2935" -->
### Installation

```bash
# Install instant.db CLI
npm install -g instant.db

# Or use locally in project
npm install instant.db
```

<!-- section_id: "98373bd1-da74-49f1-bc3c-498e7ca74cd9" -->
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

<!-- section_id: "ad72813a-934c-4e43-9eae-4ceb42c963d1" -->
### Deployment Workflow

```bash
# Apply schema
instant.db schema apply schema.js

# Export current data
instant.db export > backup.json

# Import data
instant.db import < backup.json
```

<!-- section_id: "a8324745-7c5d-4c11-8283-4f6de183cf15" -->
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

<!-- section_id: "391a747c-cbeb-41c0-b3ac-50a2e5a3828c" -->
### Best Practices

- ✅ Define schema in code
- ✅ Version control schema files
- ✅ Use migrations for changes
- ✅ Export data regularly
- ✅ Test schema changes locally
- ✅ Document field types

---

<!-- section_id: "97fe15d4-8f5a-40e5-bd59-a6061e5dc62d" -->
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

