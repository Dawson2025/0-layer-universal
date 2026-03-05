---
resource_id: "6ce094f5-90f4-4d30-8e91-8d0001c4acba"
resource_type: "document"
resource_name: "migration-tools-comparison"
---
# Migration Tools Comparison
*Choosing the Right Database Migration Tool*

<!-- section_id: "a53cc166-c102-40a7-8128-f6aa0a51e175" -->
## Overview

This guide compares popular database migration tools to help you choose the right one for your project. Each tool has different strengths, and the best choice depends on your specific needs.

<!-- section_id: "80bb4f95-cb14-4598-ba6f-65860203644c" -->
## Quick Comparison Table

| Tool | Type | SQL Support | NoSQL Support | CI/CD | GUI | Best For |
|------|------|-------------|---------------|-------|-----|----------|
| **Liquibase** | Standalone | ✅ | ✅ | ✅ | ✅ | Enterprise, multiple DBs |
| **Flyway** | Standalone/Java | ✅ | ❌ | ✅ | ❌ | Java/Spring, simplicity |
| **Supabase CLI** | Platform | ✅ PostgreSQL | ❌ | ✅ | ❌ | Supabase projects |
| **Firebase CLI** | Platform | ❌ | ✅ Firebase | ✅ | ❌ | Firebase projects |
| **Bytebase** | Standalone | ✅ | ❌ | ✅ | ✅ | Teams, visual management |
| **Django Migrations** | Framework | ✅ | ❌ | ✅ | ❌ | Django projects |
| **Rails Migrations** | Framework | ✅ | ❌ | ✅ | ❌ | Rails projects |
| **Alembic** | Framework | ✅ PostgreSQL | ❌ | ✅ | ❌ | SQLAlchemy projects |
| **Prisma** | ORM | ✅ | ❌ | ✅ | ✅ | Modern web apps |
| **TypeORM** | ORM | ✅ | ❌ | ✅ | ❌ | TypeScript/Node.js |

<!-- section_id: "479a2221-857d-4bf1-80d5-dff97901afc3" -->
## Detailed Tool Profiles

<!-- section_id: "c91ef2c4-0b8a-458f-b7e3-332aa5c2bcef" -->
### Liquibase

**Type**: Standalone migration tool
**License**: Apache 2.0
**Language**: Java (runs JVM)

#### Key Features
- ✅ Supports 40+ databases
- ✅ Multiple migration formats (SQL, XML, YAML, JSON)
- ✅ Built-in rollback support
- ✅ Change generation (diff)
- ✅ Branch merging
- ✅ GUI available
- ✅ Open source

#### Supported Databases
PostgreSQL, MySQL, Oracle, SQL Server, MongoDB, H2, Derby, DB2, Firebird, HSQL, Informix, Ingres, and many more.

#### Installation

```bash
# Using Homebrew (macOS)
brew install liquibase

# Or download from https://www.liquibase.org/download
```

#### Basic Usage

```xml
<!-- changelog.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

  <changeSet id="1" author="jdoe">
    <createTable tableName="users">
      <column name="id" type="INT" autoIncrement="true">
        <constraints primaryKey="true"/>
      </column>
      <column name="email" type="VARCHAR(255)"/>
      <column name="created_at" type="TIMESTAMP"/>
    </createTable>
  </changeSet>

</databaseChangeLog>
```

```bash
# Apply migrations
liquibase --changeLogFile=changelog.xml update

# Rollback
liquibase --changeLogFile=changelog.xml rollback-count 1

# Generate diff
liquibase diff
```

#### Pros
- Extremely flexible
- Many database support
- Advanced features (branching, merge)
- Active development
- Strong community

#### Cons
- Java dependency
- XML configuration verbose
- Can be complex for simple projects
- Slower than SQL-native tools

#### Best For
- Teams working with multiple database types
- Enterprise projects needing flexibility
- Projects needing advanced features
- Mixed database environments

---

<!-- section_id: "671f393f-a9c5-4421-a130-e70de9721132" -->
### Flyway

**Type**: Standalone or Maven plugin
**License**: Apache 2.0
**Language**: Java

#### Key Features
- ✅ SQL-based migrations (simple)
- ✅ Java callbacks
- ✅ Undo migrations (commercial)
- ✅ Multiple databases
- ✅ Clean and intuitive API
- ✅ Rapid adoption

#### Supported Databases
PostgreSQL, MySQL, SQL Server, Oracle, DB2, H2, Derby, SQLite, MariaDB, Redshift, Snowflake, and more.

#### Installation

```bash
# Using Homebrew
brew install flyway

# Or via Docker
docker pull flyway/flyway
```

#### Basic Usage

```bash
# Create migration file
touch db/migrations/V1__Create_users_table.sql

# Migration file
# V1__Create_users_table.sql
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```bash
# Apply migrations
flyway migrate

# Rollback (with Pro license)
flyway undo

# Repair
flyway repair

# Info
flyway info
```

#### Pros
- Simplicity and ease of use
- SQL-first approach
- Strong Java/Spring integration
- Fast execution
- Clear documentation
- Free version is feature-complete for many needs

#### Cons
- Limited undo support (Pro version only)
- No GUI (use Liquibase Hub)
- Less flexibility than Liquibase
- No branching/merging out of box

#### Best For
- Java/Spring projects
- Teams wanting simplicity
- SQL-focused migrations
- CI/CD integration
- PostgreSQL, MySQL projects

---

<!-- section_id: "aeec342d-3b2a-435f-a857-3cd6a0a1a3bd" -->
### Supabase CLI

**Type**: Platform-specific tool
**License**: MIT
**Language**: TypeScript/Node.js

#### Key Features
- ✅ PostgreSQL migration support
- ✅ Built-in for Supabase
- ✅ Local development support
- ✅ Type generation
- ✅ Row Level Security (RLS)
- ✅ Studio GUI for management

#### Supported Databases
PostgreSQL (Supabase only)

#### Installation

```bash
npm install -g supabase
```

#### Basic Usage

```bash
# Create migration
supabase migration new create_users_table

# Migration file: supabase/migrations/20251027_143022_create_users_table.sql
CREATE TABLE public.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

# Apply migration
supabase db push

# Generate TypeScript types
supabase gen types typescript --local > types/supabase.ts
```

#### Pros
- Excellent Supabase integration
- Local development support
- Type generation
- Good documentation
- Active development
- Free and open source

#### Cons
- Supabase-specific only
- Less flexible than generic tools
- Newer tool (less mature)

#### Best For
- Supabase projects
- PostgreSQL only
- Real-time features needed
- Modern web applications

---

<!-- section_id: "ca080d0b-affc-4473-b902-1e0ebeae3382" -->
### Bytebase

**Type**: Standalone tool with GUI
**License**: Commercial (with free tier)
**Language**: Go

#### Key Features
- ✅ Web-based GUI
- ✅ Migration and schema change management
- ✅ Team collaboration features
- ✅ Audit logging
- ✅ Approval workflows
- ✅ Multi-environment support

#### Supported Databases
MySQL, PostgreSQL, ClickHouse, and more.

#### Installation

```bash
# Docker
docker run --init \
  --name bytebase \
  --platform linux/amd64 \
  --restart always \
  --publish 8080:8080 \
  --health-cmd "wget --no-verbose --tries=1 --spider http://localhost:8080/healthz || exit 1" \
  --health-interval 5m \
  --health-timeout 10s \
  bytebase/bytebase:%%BYTEBASE_VERSION%% \
  --data /var/opt/bytebase \
  --port 8080
```

#### Pros
- Excellent GUI for non-technical users
- Strong team collaboration
- Audit and compliance features
- Approval workflows
- Good for enterprises

#### Cons
- Commercial product
- Database support limited
- Less automation than CLI tools
- Newer product

#### Best For
- Teams needing visual management
- Compliance/audit requirements
- Organizations with mixed technical levels
- Enterprise deployments

---

<!-- section_id: "1c1d970a-0904-4baf-b8cb-6786ef161462" -->
### Firebase CLI

**Type**: Platform-specific tool
**License**: Apache 2.0
**Language**: Node.js

#### Key Features
- ✅ Firebase project management
- ✅ Rules and index deployment
- ✅ Emulator support
- ✅ Multiple services support
- ✅ Free tier availability

#### Supported Databases
Firebase Realtime Database, Firestore

#### Installation

```bash
npm install -g firebase-tools
firebase login
```

#### Basic Usage

```javascript
// Deploy Firestore rules
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read: if request.auth.uid == userId;
      allow write: if request.auth.uid == userId;
    }
  }
}
```

```bash
# Deploy rules
firebase deploy --only firestore:rules

# Deploy indexes
firebase deploy --only firestore:indexes

# Local development
firebase emulators:start
```

#### Pros
- Official Firebase tool
- Real-time database support
- Free tier
- Good for Firebase ecosystem
- Strong documentation

#### Cons
- Firebase/Firestore specific
- Limited migration features
- Manual data management
- NoSQL only

#### Best For
- Firebase/Firestore projects
- Real-time applications
- Mobile applications
- Serverless architectures

---

<!-- section_id: "72ee2017-c058-4e1b-a425-ceb5c9c4740b" -->
## Tool Selection Decision Tree

```
What type of database?
├─ SQL Database
│  ├─ Already using framework?
│  │  ├─ Django → Django Migrations
│  │  ├─ Rails → Rails Migrations
│  │  ├─ Spring → Flyway
│  │  ├─ SQLAlchemy → Alembic
│  │  └─ Prisma/TypeORM → Built-in migrations
│  ├─ Single database type?
│  │  ├─ PostgreSQL + Supabase → Supabase CLI
│  │  ├─ MySQL → Flyway or Liquibase
│  │  └─ Multiple → Liquibase
│  └─ Team needs GUI?
│     ├─ Yes → Bytebase
│     └─ No → Flyway or Liquibase
├─ NoSQL Database
│  ├─ Firebase → Firebase CLI
│  ├─ MongoDB → Liquibase or native tools
│  └─ Other → Platform-specific tools
└─ Multiple Database Types
   └─ Liquibase (broadest support)
```

<!-- section_id: "21552d9f-bbfc-46ab-aa20-72cdc44b7d8d" -->
## Feature Comparison Matrix

<!-- section_id: "0a75898d-490a-4caf-9865-68a76e4b3291" -->
### Core Features

| Feature | Liquibase | Flyway | Supabase CLI | Bytebase | Firebase CLI |
|---------|-----------|--------|--------------|----------|--------------|
| SQL Migrations | ✅ | ✅ | ✅ | ✅ | ❌ |
| XML/YAML Support | ✅ | ❌ | ❌ | ✅ | ❌ |
| Undo/Rollback | ✅ | ⚠️ Pro | ✅ | ✅ | Manual |
| Branch Merging | ✅ | ❌ | ❌ | ✅ | ❌ |
| GUI | ✅ | ✅ | ✅ Studio | ✅ | ❌ |
| Schema Diff | ✅ | ✅ | ⚠️ | ✅ | ❌ |
| Multi-DB Support | ✅ | ✅ | PostgreSQL | ✅ | Firebase |

<!-- section_id: "6dac33ab-5a18-4781-941b-07d58ff18cf0" -->
### Database Support

| Database | Liquibase | Flyway | Supabase | Bytebase | Firebase |
|----------|-----------|--------|----------|----------|----------|
| PostgreSQL | ✅ | ✅ | ✅ | ✅ | ❌ |
| MySQL | ✅ | ✅ | ❌ | ✅ | ❌ |
| SQL Server | ✅ | ✅ | ❌ | ✅ | ❌ |
| Oracle | ✅ | ✅ | ❌ | ✅ | ❌ |
| MongoDB | ✅ | ❌ | ❌ | ⚠️ | ❌ |
| Firebase | ❌ | ❌ | ❌ | ❌ | ✅ |

<!-- section_id: "29f935ed-0697-446b-82d5-ddd4f1a5b27d" -->
### CI/CD Integration

| CI/CD Platform | Liquibase | Flyway | Supabase | Bytebase | Firebase |
|----------------|-----------|--------|----------|----------|----------|
| GitHub Actions | ✅ | ✅ | ✅ | ✅ | ✅ |
| GitLab CI | ✅ | ✅ | ✅ | ✅ | ✅ |
| Jenkins | ✅ | ✅ | ✅ | ✅ | ✅ |
| CircleCI | ✅ | ✅ | ✅ | ✅ | ✅ |
| Azure DevOps | ✅ | ✅ | ✅ | ✅ | ✅ |

<!-- section_id: "b51887d7-eefd-4129-a406-5b6c9f0f769d" -->
## Use Case Recommendations

<!-- section_id: "dae72b12-925b-492b-b63e-9db337028c00" -->
### Small Projects / Startups
**Recommended**: Flyway or Prisma
- Simplicity and speed
- Quick setup
- Free and open source
- Fast iteration

<!-- section_id: "a0c47d2d-8a61-4b60-80ba-472d3220cafd" -->
### Enterprise / Large Teams
**Recommended**: Liquibase or Bytebase
- Advanced features
- Multi-database support
- Team collaboration
- Audit requirements

<!-- section_id: "662dd7d8-53fe-4531-8b00-a4733153929f" -->
### Supabase Projects
**Recommended**: Supabase CLI
- Native integration
- Built-in features
- Best developer experience
- Free tier

<!-- section_id: "d86ee671-597d-4c5f-afb4-d1b88fafc098" -->
### Firebase Projects
**Recommended**: Firebase CLI
- Official tool
- Platform integration
- Emulator support
- Real-time features

<!-- section_id: "9245793b-0ba4-4a87-99fd-fb7e9a09060d" -->
### Java/Spring Projects
**Recommended**: Flyway
- Excellent integration
- Simplicity
- Maven/Gradle support
- Common in ecosystem

<!-- section_id: "b1f76eae-a25f-49ab-b6fa-4c5c81b9aaa7" -->
### Python/Django Projects
**Recommended**: Django Migrations
- Built-in to Django
- Zero additional setup
- Excellent ORM integration
- Python-friendly

<!-- section_id: "cb4c1993-b9d9-467f-a656-942ac1600d22" -->
### Node.js/TypeScript Projects
**Recommended**: Prisma or TypeORM
- TypeScript-first
- Modern workflows
- Good type safety
- Active communities

<!-- section_id: "e99d2bcc-95be-433e-80cd-c5ed99de1dbe" -->
## Migration Complexity Support

<!-- section_id: "cc440e0f-3f47-4a6a-b0f2-341a8e4dc15e" -->
### Simple Migrations
All tools handle simple schema changes:
- ✅ Creating tables
- ✅ Adding columns
- ✅ Creating indexes
- ✅ Adding constraints

**Best Tool**: Flyway (simplest)

<!-- section_id: "f81b2ea0-9f10-4e01-8e88-ad5fe76593ac" -->
### Complex Migrations
Advanced features for complex changes:
- Refactoring tables
- Data transformations
- Conditional migrations
- Multi-step changes

**Best Tool**: Liquibase (most flexible)

<!-- section_id: "a61d9a04-65dd-40f7-9bcd-8be8c2111409" -->
### Undo/Rollback
Rolling back changes:

| Tool | Undo Support |
|------|--------------|
| Liquibase | ✅ Full support |
| Flyway | ⚠️ Pro version only |
| Supabase | ✅ Manual rollback |
| Bytebase | ✅ Full support |
| Firebase | ❌ Manual only |

<!-- section_id: "997ae010-255d-4725-b07a-9c10fb0f765b" -->
## Cost Comparison

<!-- section_id: "8a9e3c99-acf6-4f7a-9a6b-913cdd820d00" -->
### Free/Open Source
- ✅ Liquibase (open source)
- ✅ Flyway (open source)
- ✅ Supabase CLI (free)
- ✅ Firebase CLI (free tier)
- ✅ Framework migrations (free)

<!-- section_id: "8fccca1e-57db-4220-971a-45d62e4ac897" -->
### Commercial
- 💰 Bytebase (free tier available)
- 💰 Flyway Pro (commercial features)
- 💰 Liquibase Hub (commercial features)

<!-- section_id: "dfeaa22e-e66e-4dbb-bc2d-09a224550f96" -->
## Integration with Development Workflows

<!-- section_id: "91314979-1575-4599-80ea-c5b27b2ec4f4" -->
### Git Flow
All tools support:
- ✅ Store migrations in Git
- ✅ Review via pull requests
- ✅ Branch management
- ✅ Tagging releases

<!-- section_id: "3e894c71-bf5a-4b73-b4a1-463053ffe986" -->
### Testing
Migration testing support:

| Tool | Testing Support |
|------|----------------|
| Liquibase | ✅ Test databases |
| Flyway | ✅ Test databases |
| Supabase | ✅ Local emulator |
| Bytebase | ✅ Staging environments |
| Firebase | ✅ Emulator |

<!-- section_id: "149ee600-e399-4711-a38f-716b2796089b" -->
## Conclusion

<!-- section_id: "fd0fab66-2eca-4dbf-81c5-a2ff629f49db" -->
### Quick Picks by Scenario

**New Project Starting**:
- PostgreSQL + Modern Stack → **Supabase CLI**
- Java/Spring → **Flyway**
- Django → **Django Migrations**
- Rails → **Rails Migrations**

**Enterprise/Large Team**:
- **Liquibase** (flexibility)
- **Bytebase** (GUI + compliance)

**Firebase/Firestore**:
- **Firebase CLI** (official tool)

**Already Using ORM**:
- **Prisma** / **TypeORM** (built-in migrations)

<!-- section_id: "6cd21360-7213-4aa6-a71b-6ecf31668fc8" -->
### General Recommendation

For most projects: **Flyway** or **Liquibase**
- Battle-tested
- Large community
- Good documentation
- CI/CD ready
- Flexible

Choose based on:
- Team preference (SQL vs XML/YAML)
- Database types needed
- Feature requirements
- Budget considerations

---

*For platform-specific workflows, see [Platform-Specific Guides](./platform-specific-guides.md). For troubleshooting, see [Troubleshooting Guide](./troubleshooting-guide.md).*

