---
resource_id: "1b6f2524-1e47-44bf-b2e2-6c5cacfd3934"
resource_type: "document"
resource_name: "platform-specific-guides"
---
# Platform-Specific Guides
*Detailed Database Version Control Workflows for Each Platform*

<!-- section_id: "f42357b7-6b41-47c9-a555-1b3c4357517c" -->
## Overview

This guide provides detailed, platform-specific instructions for version controlling databases across different platforms. Each section includes installation, configuration, common workflows, and examples.

<!-- section_id: "ece17bb8-c2e4-403a-90a8-6d2e6b81b5c4" -->
## Table of Contents

1. [Supabase](#supabase)
2. [Firebase Realtime Database](#firebase-realtime-database)
3. [Firestore](#firestore)
4. [Google Cloud SQL](#google-cloud-sql)
5. [BigQuery](#bigquery)
6. [Vertex AI](#vertex-ai)
7. [instant.db](#instantdb)

---

<!-- section_id: "04e2fc5d-3540-4f3d-97fb-50c4ac9fc1d0" -->
## Supabase

<!-- section_id: "173a9333-8c31-416b-a614-47bcc5f2c5eb" -->
### Overview

Supabase is a PostgreSQL-based platform with built-in migration support through the Supabase CLI. It provides excellent version control capabilities with native Git integration.

<!-- section_id: "440afb9e-2940-44c1-9099-ad3b9bdbcd13" -->
### Prerequisites

- Supabase account
- Supabase CLI installed
- Node.js 18+ or Python 3.8+

<!-- section_id: "9ad52589-72ae-409a-8702-ac1a83c19efe" -->
### Installation

```bash
# Install Supabase CLI
npm install -g supabase

# Or via Homebrew (macOS)
brew install supabase/tap/supabase

# Login
supabase login
```

<!-- section_id: "47c3b30d-402a-44ac-a1a1-52b6f0cb69f4" -->
### Initialization

```bash
# Initialize a new project
supabase init

# Link to existing project
supabase link --project-ref your-project-ref
```

<!-- section_id: "f2a2b077-e658-4946-9707-2a110ffd9bdb" -->
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

<!-- section_id: "5cc17696-9778-48a5-be53-cd08a5143128" -->
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

<!-- section_id: "5b9ecd58-0a2d-4266-b75a-37156a844250" -->
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

<!-- section_id: "cd865512-2fe5-4f11-90c1-6fc0b0b86d60" -->
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

<!-- section_id: "b1508296-5e3a-45af-831f-e4af4dedd3f7" -->
### Best Practices

- ✅ Use timestamped migration names
- ✅ Include up and down migrations when possible
- ✅ Test locally before pushing
- ✅ Review migrations in PRs
- ✅ Use Supabase RLS for security
- ✅ Keep migrations small and focused

---

<!-- section_id: "96028b37-38b2-429d-9255-ec7bd1678603" -->
## Firebase Realtime Database

<!-- section_id: "52fe0b01-b550-4104-a185-6e49ed6cbd4a" -->
### Overview

Firebase Realtime Database uses JSON and requires manual export/import for version control. The Firebase CLI manages configuration and deployments.

<!-- section_id: "1265ac72-ae8d-420d-a9b3-5394a8cd3a7b" -->
### Prerequisites

- Firebase account
- Firebase CLI installed
- Node.js 8.0+

<!-- section_id: "fce3db10-c335-406b-afa4-2650b7316e09" -->
### Installation

```bash
npm install -g firebase-tools

# Login
firebase login
```

<!-- section_id: "b28237c4-e186-40c9-b33f-192ae5d2d39f" -->
### Initialization

```bash
# Initialize Firebase project
firebase init

# Select:
# - Realtime Database
# - Configure security rules
```

<!-- section_id: "97a03931-33b2-44ca-9677-b85c0fad5347" -->
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

<!-- section_id: "115dbbeb-b689-4c96-9387-0fe7d2ed068a" -->
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

<!-- section_id: "6aa0373b-4579-427a-a16a-b0ed7969b02e" -->
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

<!-- section_id: "a18f4fc2-20a8-4684-a8d4-2e9fe17ab7db" -->
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

<!-- section_id: "3add4e1f-b3a8-424e-8db5-f9d6df04e38c" -->
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

<!-- section_id: "4eae51be-bf93-44ba-9428-23e0e9555654" -->
### Best Practices

- ✅ Store rules in Git
- ✅ Use different rules for environments
- ✅ Regularly export data for backup
- ✅ Document data structures
- ✅ Use TypeScript for type safety
- ✅ Test rules with Firebase emulator

---

<!-- section_id: "f1e54ace-72a9-439c-b7b3-1891ec837155" -->
## Firestore

<!-- section_id: "52a35385-3161-4950-b636-960cb9bff22b" -->
### Overview

Firestore is a NoSQL document database. Like Firebase Realtime Database, it requires configuration versioning and manual data management.

<!-- section_id: "38af4d83-a4c3-4f92-9d69-58b86d30044b" -->
### Prerequisites

- Firebase account
- Firebase CLI installed

<!-- section_id: "4bee3a4a-fcaf-407b-aede-2abbc766b7c3" -->
### Installation and Setup

Same as Firebase Realtime Database installation.

<!-- section_id: "cb9ac078-518e-4072-b9bd-3bc00110c6e7" -->
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

<!-- section_id: "00350f83-35d9-43fc-b7e2-e57010ceb761" -->
### Deployment Workflow

```bash
# Deploy rules and indexes
firebase deploy --only firestore

# Deploy only rules
firebase deploy --only firestore:rules

# Deploy only indexes
firebase deploy --only firestore:indexes
```

<!-- section_id: "67c3f831-504c-4cda-8294-e87ef853f336" -->
### Data Export/Import

```bash
# Export Firestore data
gcloud firestore export gs://your-bucket/export

# Import Firestore data
gcloud firestore import gs://your-bucket/export
```

<!-- section_id: "8ba59fbb-feef-49ee-91cb-966e048a8af4" -->
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

<!-- section_id: "e5889588-3eb5-4fde-afd0-317d87c71c33" -->
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

<!-- section_id: "4e16b7b4-b42a-484d-b69d-c5de57c49b70" -->
### Best Practices

- ✅ Version control rules and indexes
- ✅ Use emulator for testing
- ✅ Regularly backup data
- ✅ Use batch operations
- ✅ Monitor index creation
- ✅ Document data models

---

<!-- section_id: "12840181-fec4-4583-af43-6881c348fb4f" -->
## Google Cloud SQL

<!-- section_id: "65ddd6bd-91cd-44c6-8642-6cd85fb15786" -->
### Overview

Cloud SQL provides managed MySQL, PostgreSQL, and SQL Server databases. Use migration tools like Flyway or Liquibase for version control.

<!-- section_id: "caa785c8-99ec-421f-91da-1bd197dd2ab4" -->
### Prerequisites

- Google Cloud account
- gcloud CLI installed
- Migration tool (Flyway or Liquibase)

<!-- section_id: "6043beb7-489b-46bb-9ba5-37016b1c5c07" -->
### Installation

```bash
# Install gcloud CLI
curl https://sdk.cloud.google.com | bash

# Install Flyway
# Download from https://flywaydb.org/download/

# Or use via Docker
docker pull flyway/flyway
```

<!-- section_id: "388a88cc-917d-4fea-a3f8-7c7b49722f79" -->
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

<!-- section_id: "7fca47fb-18ff-409f-aaab-fc57e4edd197" -->
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

<!-- section_id: "61bc2cc5-8b8c-4e16-b584-2767f2af965a" -->
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

<!-- section_id: "15008304-d903-4ddf-b706-8c2960c304c2" -->
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

<!-- section_id: "ba827acf-9602-4ee1-aa26-b7b5064cce7d" -->
### Best Practices

- ✅ Use Flyway or Liquibase for migrations
- ✅ Version control all migration files
- ✅ Test on staging before production
- ✅ Use cloud proxy for security
- ✅ Monitor migration execution
- ✅ Keep backups before migrations

---

<!-- section_id: "bacce68d-6deb-440d-aed1-2d40a324d1ff" -->
## BigQuery

<!-- section_id: "1521892d-b0d6-47fb-b4c8-3aff1026d3c5" -->
### Overview

BigQuery is a serverless data warehouse. Version control SQL queries, views, routines, and datasets through SQL files in Git.

<!-- section_id: "c8f47497-d482-413a-a217-b9285643f63a" -->
### Prerequisites

- Google Cloud account
- bq CLI installed
- gcloud authenticated

<!-- section_id: "041f2996-979b-43bd-b0e3-c6cf75dcaac7" -->
### Installation

```bash
# Install gcloud CLI
# Then install bq component
gcloud components install bq
```

<!-- section_id: "b8ee96d7-b44e-4213-bd99-db31db299f88" -->
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

<!-- section_id: "d8c5e361-16ea-406c-8dee-010b8a8fc224" -->
### Deployment Workflow

```bash
# Deploy view
bq query --use_legacy_sql=false < db/bigquery/views/v_user_stats.sql

# Deploy function
bq query --use_legacy_sql=false < db/bigquery/routines/f_calculate_revenue.sql

# Create dataset (if needed)
bq mk --dataset --location=US project:dataset
```

<!-- section_id: "870ed0d1-1856-494a-ac03-7dff4a398f9c" -->
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

<!-- section_id: "d13e4b64-be9d-425e-8bdb-847dab4e6c2e" -->
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

<!-- section_id: "d5072c84-3daf-4a9b-9676-bf76b42d5174" -->
### Best Practices

- ✅ Store all SQL in Git
- ✅ Use views instead of direct queries
- ✅ Version control routine definitions
- ✅ Document data schemas
- ✅ Keep test and production separate
- ✅ Use Dataform for complex pipelines

---

<!-- section_id: "2e967b7f-613a-4182-9f61-96f56fad42a2" -->
## Vertex AI

<!-- section_id: "8ae1efae-00ed-48f5-a436-e84b55611fa4" -->
### Overview

Vertex AI manages ML models and pipelines. Version control model definitions, pipeline configurations, and training code.

<!-- section_id: "73212850-46d8-4e84-92e3-566a4c5ec63b" -->
### Prerequisites

- Google Cloud account
- Vertex AI enabled
- Python 3.8+ with Vertex AI SDK

<!-- section_id: "3b4ae16d-489e-4d72-85b3-97bb227effee" -->
### Installation

```bash
pip install google-cloud-aiplatform
```

<!-- section_id: "18ffe4da-3d13-49b5-b172-69d779631f1d" -->
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

<!-- section_id: "e8583236-bf47-4482-93ec-2b1268b4a493" -->
### Deployment Workflow

```bash
# Deploy pipeline
python scripts/deploy_pipeline.py

# Submit training job
python scripts/submit_training.py --version v1.0
```

<!-- section_id: "804927af-41b3-400b-bb07-8ab9f2062502" -->
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

<!-- section_id: "79f459e8-c17d-4b15-80cb-d489f9014500" -->
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

<!-- section_id: "f3e231d2-261e-4164-92cb-4122537c7199" -->
### Best Practices

- ✅ Version control model definitions
- ✅ Use semantic versioning for models
- ✅ Track training hyperparameters
- ✅ Monitor model performance
- ✅ A/B test new models
- ✅ Document model architecture

---

<!-- section_id: "336267e8-8316-40cb-8202-3cdb463000f4" -->
## instant.db

<!-- section_id: "9f630a38-4646-40bc-81f6-d27eab25fa38" -->
### Overview

instant.db is a developer-friendly NoSQL database with instant setup. Version control schema definitions and use CLI tools for schema management.

<!-- section_id: "eb3674b0-fc96-424e-9639-787dbf395721" -->
### Prerequisites

- Node.js 18+
- npm or yarn

<!-- section_id: "4cf419f1-12ff-404b-a015-e994f4c3604a" -->
### Installation

```bash
# Install instant.db CLI
npm install -g instant.db

# Or use locally in project
npm install instant.db
```

<!-- section_id: "da14a9cc-728b-4f5c-8afa-7c27d993c76c" -->
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

<!-- section_id: "5b4640e8-e33f-446d-85cc-b019580d9844" -->
### Deployment Workflow

```bash
# Apply schema
instant.db schema apply schema.js

# Export current data
instant.db export > backup.json

# Import data
instant.db import < backup.json
```

<!-- section_id: "bb4f9f94-1e8d-4643-816e-b508c595508e" -->
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

<!-- section_id: "2d45f9af-a710-4c20-9b28-23a0abbead22" -->
### Best Practices

- ✅ Define schema in code
- ✅ Version control schema files
- ✅ Use migrations for changes
- ✅ Export data regularly
- ✅ Test schema changes locally
- ✅ Document field types

---

<!-- section_id: "c6dbee5d-1412-4d83-b62e-42168df5749a" -->
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

