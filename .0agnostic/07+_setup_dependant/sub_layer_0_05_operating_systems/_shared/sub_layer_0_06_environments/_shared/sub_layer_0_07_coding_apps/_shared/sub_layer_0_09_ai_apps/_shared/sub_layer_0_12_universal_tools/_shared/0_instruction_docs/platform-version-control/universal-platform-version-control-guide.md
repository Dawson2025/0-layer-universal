---
resource_id: "cde0f16d-1672-4158-8fe4-558a9a06b2af"
resource_type: "document"
resource_name: "universal-platform-version-control-guide"
---
# Universal Platform Version Control Guide
*Core Principles and Practices for All Platforms*

<!-- section_id: "c6a6091b-b20c-4655-b496-d7c071449629" -->
## Overview

This guide covers universal principles and practices for version controlling any platform or service your application uses - from infrastructure and hosting to authentication, storage, APIs, and third-party services. These principles apply regardless of which specific platforms you use.

<!-- section_id: "47b9823f-fffd-47c0-a6ad-5985cc109663" -->
## Core Concepts

<!-- section_id: "d95b86e7-c85b-4d7f-a8a7-0f785f11a38e" -->
### What is Platform Version Control?

Platform version control means managing all platform configurations, settings, and deployments through version control systems (like Git). This includes:

- **Infrastructure definitions** (servers, networking, databases)
- **Application deployments** (hosting, CDN, edge functions)
- **Service configurations** (authentication, storage, APIs)
- **Environment settings** (dev, staging, production)
- **Secrets and credentials** (managed securely outside Git)
- **CI/CD pipelines** (automated deployments)
- **Documentation** (why and how decisions were made)

<!-- section_id: "4f97b756-019c-4fcb-894e-3a3b65c67bfc" -->
### Why Version Control Platforms?

#### Without Version Control
- Manual, error-prone configurations
- No audit trail of changes
- Inconsistent environments
- Hard to replicate setups
- Difficult to coordinate teams
- Risk of production failures

#### With Version Control
- Automated, reproducible setups
- Complete change history
- Consistent environments
- Easy to spin up new environments
- Team coordination through PRs
- Safe, tested deployments

<!-- section_id: "d7accb7f-0efd-438b-9881-3c1e22ece671" -->
## Universal Principles

<!-- section_id: "29a3795d-8f66-492b-a414-773790ba7767" -->
### 1. Everything as Code

#### Infrastructure as Code (IaC)
Define infrastructure in code:
- **Terraform**: Multi-cloud IaC (HCL language)
- **Pulumi**: IaC with real programming languages
- **CloudFormation**: AWS-specific (YAML/JSON)
- **ARM Templates**: Azure-specific (JSON)
- **Configuration files**: JSON, YAML, TOML

**Example**:
```hcl
# terraform/main.tf
resource "aws_s3_bucket" "app_storage" {
  bucket = "my-app-storage"
  
  versioning {
    enabled = true
  }
  
  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

#### Configuration as Code
Store configurations in files:
```yaml
# vercel.json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build"
    }
  ],
  "routes": [
    { "src": "/api/(.*)", "dest": "/api/$1" }
  ]
}
```

<!-- section_id: "25b098e3-aff8-42d0-820d-0487b3db268c" -->
### 2. Environment Parity

#### Three-Environment Model

**Development** → **Staging** → **Production**

Each environment should:
- Use same configuration structure
- Only differ in environment variables
- Follow same deployment process
- Have same monitoring in place

```bash
# .env.development
DATABASE_URL=postgresql://localhost:5432/dev
API_KEY=dev_api_key
ENVIRONMENT=development

# .env.staging
DATABASE_URL=postgresql://staging.example.com:5432/staging
API_KEY=staging_api_key
ENVIRONMENT=staging

# .env.production
DATABASE_URL=postgresql://prod.example.com:5432/prod
API_KEY=prod_api_key_secret
ENVIRONMENT=production
```

<!-- section_id: "132963f7-5ea0-4000-a2bd-b9dfbe0d5278" -->
### 3. Secrets Management

**NEVER** commit secrets to Git. Instead:

#### Use Secret Managers
- **AWS Secrets Manager**
- **Google Cloud Secret Manager**
- **Azure Key Vault**
- **HashiCorp Vault**
- **1Password CLI**
- **Doppler**

#### Environment Variables
```bash
# .env.local (gitignored)
DATABASE_PASSWORD=secret123
API_KEY=key456
STRIPE_SECRET_KEY=sk_live_...

# .env.example (committed as template)
DATABASE_PASSWORD=
API_KEY=
STRIPE_SECRET_KEY=
```

<!-- section_id: "e58b2676-d4ff-4b15-8c35-8e0579e406f0" -->
### 4. Immutable Deployments

#### Blue-Green Deployment
```
Blue (Production)  →  Green (New Version)
   ↓                       ↓
Keep running          Deploy new version
   ↓                       ↓
Wait for verification   →
   ↓                       ↓
Switch traffic          →
   ↓                       ↓
Shut down Blue
```

#### Benefits
- Zero downtime deployments
- Easy rollback (switch back to blue)
- Safe testing in production environment
- Low risk

<!-- section_id: "f2087819-5900-4a64-974c-7b3016994050" -->
### 5. Rollback Strategy

Always have a way to revert changes:

```yaml
# Rollback procedure
1. Identify problematic deployment
2. Revert to previous known-good state
3. Verify system integrity
4. Investigate root cause
5. Fix and redeploy when ready
```

<!-- section_id: "5cc06437-9bb6-4a31-a9fd-fc8070b29e2b" -->
## Configuration Patterns

<!-- section_id: "b85aaefc-f8c7-4108-92bf-21700f0ecf8a" -->
### Pattern 1: Monorepo with All Platforms

```
project/
├── infrastructure/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── environments/
│       ├── dev.tfvars
│       ├── staging.tfvars
│       └── prod.tfvars
│
├── platforms/
│   ├── vercel.json
│   ├── netlify.toml
│   └── railway.json
│
├── databases/
│   ├── migrations/
│   └── seeds/
│
├── auth/
│   ├── auth0-config.json
│   └── clerk-config.json
│
├── services/
│   ├── stripe/
│   ├── sendgrid/
│   └── twilio/
│
└── .env.example
```

<!-- section_id: "3ea5241f-07f4-4d00-95fa-32aea7a394bb" -->
### Pattern 2: Environment-Specific Structure

```
environments/
├── development/
│   ├── config.yaml
│   ├── secrets.yaml  # encrypted
│   └── deploy.sh
│
├── staging/
│   ├── config.yaml
│   ├── secrets.yaml
│   └── deploy.sh
│
└── production/
    ├── config.yaml
    ├── secrets.yaml
    └── deploy.sh
```

<!-- section_id: "9fe585bc-87a2-4d14-b1b4-28bbcbb44def" -->
### Pattern 3: Platform per Directory

```
platforms/
├── vercel/
│   ├── vercel.json
│   └── .vercelignore
│
├── supabase/
│   ├── config.toml
│   └── migrations/
│
├── firebase/
│   ├── firebase.json
│   └── firestore.rules
│
└── aws/
    ├── terraform/
    └── lambda/
```

<!-- section_id: "6f46fcbe-776a-406b-aec2-9d296a203ba6" -->
## Version Control Strategies

<!-- section_id: "fec7eed7-c5a8-49cc-b184-fc13c6ada8a9" -->
### Strategy 1: Git-Based (Recommended)

Store all configurations in Git:
- ✅ Complete history
- ✅ Easy collaboration
- ✅ PR-based reviews
- ✅ Branch-based testing
- ✅ Tagged releases

<!-- section_id: "8a1b62ee-a5e4-46ca-bde2-9dfc8e91c385" -->
### Strategy 2: Platform APIs

Use platform APIs for version control:
- GitHub/GitLab for code + config
- Platform dashboards for visualization
- Platform CLIs for deployment
- CI/CD for automation

<!-- section_id: "c716164d-7bfc-4fa3-bce6-c2840746ec04" -->
### Strategy 3: Hybrid Approach

Combine Git + Platform features:
- Git for configuration
- Platform APIs for deployment
- Platform features for monitoring
- Both for backup and redundancy

<!-- section_id: "5dbd98b8-663b-4c93-a6e8-66357095b422" -->
## Deployment Workflows

<!-- section_id: "e995ebae-90a7-4872-a570-74d5423bf0bf" -->
### Workflow 1: Git Push to Deploy

```bash
# Developer workflow
git commit -am "Update API endpoints"
git push origin main

# CI/CD automatically
# 1. Lint configuration
# 2. Run tests
# 3. Deploy to staging
# 4. Run integration tests
# 5. Deploy to production
# 6. Monitor and alert
```

<!-- section_id: "0f8afffe-7ef7-4c93-851c-3997700b2ad2" -->
### Workflow 2: Manual Approval

```bash
# Push to main
git push origin main

# CI/CD pipeline
# 1. Deploy to staging
# 2. Wait for manual approval
# 3. Deploy to production
# 4. Notify team
```

<!-- section_id: "b48260a9-e52f-4cd9-a199-48f1c69157e3" -->
### Workflow 3: Feature Branch Deployments

```bash
# Feature branch
git checkout -b feature/new-auth
# ... make changes ...

# Deploy preview environment
git push origin feature/new-auth
# Automated: Create preview deployment

# Merge to main
git checkout main
git merge feature/new-auth
# Automated: Deploy to production
```

<!-- section_id: "327c9f58-59ef-4568-a88d-b1f1633cbb97" -->
## Best Practices

<!-- section_id: "044db14e-421b-4c7c-b5a9-d043e2dc9169" -->
### 1. Document Decisions

```markdown
# Why this configuration?

## Decision Log

### 2025-10-27: Use Vercel for hosting

**Context**: Need fast, global CDN with edge functions
**Decision**: Use Vercel
**Alternatives**: Netlify, AWS Amplify
**Consequences**: 
- Pros: Great Next.js support, fast global CDN
- Cons: Platform-specific lock-in
```

<!-- section_id: "e0542a81-2d9c-4f94-9346-1ace281550f7" -->
### 2. Test Configuration Changes

```bash
# Test locally first
./scripts/test-local.sh

# Test in development
git push origin feature/update-config

# Test in staging
# (automatic deployment to staging)

# Approve for production
# (manual approval required)
```

<!-- section_id: "e75f2681-d485-4361-9c74-8df8ce9ec6ea" -->
### 3. Use Tags for Releases

```bash
# Tag releases
git tag -a v1.0.0 -m "Production release 1.0.0"
git push origin v1.0.0

# Deploy specific tag
git checkout v1.0.0
./scripts/deploy.sh production
```

<!-- section_id: "e1e4d1b2-7720-4834-969e-84ef43498bea" -->
### 4. Keep Configurations Simple

```yaml
# ✅ Good: Simple and clear
api:
  version: 2
  timeout: 30

# ❌ Bad: Overly complex
api:
  version: 2
  timeout: 30
  advanced:
    nested:
      deeply:
        nested:
          config: "hard to read"
```

<!-- section_id: "43884917-475c-4f77-b40d-263a5885d617" -->
### 5. Validate Configurations

```bash
# Validate before deployment
terraform validate
vercel --debug build
docker-compose config
```

<!-- section_id: "2e21d8fe-535d-45ce-a50b-8c2c3e369063" -->
### 6. Version Platform-Specific Settings

```json
// Always include platform metadata
{
  "version": "1.0.0",
  "platform": "vercel",
  "environment": "production",
  "lastUpdated": "2025-10-27",
  "managedBy": "infrastructure as code"
}
```

<!-- section_id: "f544e7ca-de92-4e11-9228-630f2a7ab827" -->
## Common Patterns

<!-- section_id: "4df122f3-ec10-47d1-99f4-a47c70e7bb4d" -->
### Pattern 1: Multi-Platform Coordination

```bash
# Deploy in order
1. Infrastructure (Terraform)
2. Databases (Migrations)
3. Application (Vercel/Netlify)
4. Services (Auth, Storage, etc.)
5. Monitoring (Setup alerts)

# Verify each step
terraform apply -auto-approve && \
db-migrate up && \
vercel deploy --prod && \
# ... continue ...
```

<!-- section_id: "211a7f50-b3ca-4f76-8f8a-d4dd8b99d013" -->
### Pattern 2: Feature Flags

```yaml
# config.yaml
features:
  newAuth:
    enabled: false  # Toggle feature
    rollout:
      percentage: 25  # Gradual rollout
      regions:
        - us-east
```

<!-- section_id: "df6bc55d-ebdb-44e5-8f71-e6b7ff0c8348" -->
### Pattern 3: Environment-Specific Settings

```yaml
# config/staging.yaml
database:
  connectionPool: 20
  
performance:
  cache:
    ttl: 300  # 5 minutes

# config/production.yaml
database:
  connectionPool: 100
  
performance:
  cache:
    ttl: 600  # 10 minutes
```

<!-- section_id: "63ea51ed-5bbc-4e6e-b966-24542621e4ba" -->
## Troubleshooting Universal Issues

<!-- section_id: "cc5724ee-0780-47f1-b0d7-7ff5502f9782" -->
### Issue: Config Drift

**Symptoms**: Local and production configs differ

**Solution**: Use config synchronization tools and always deploy from Git

<!-- section_id: "e9644758-728c-487a-9c5a-36e2a5a3ebaa" -->
### Issue: Missing Secrets

**Symptoms**: Deployment fails due to missing credentials

**Solution**: Use secret managers and validate before deployment

<!-- section_id: "78ce1006-0554-4db1-a155-057102a78db4" -->
### Issue: Environment Mismatch

**Symptoms**: Dev works but production fails

**Solution**: Ensure environment parity and use same deployment process

<!-- section_id: "a69525c5-5ef2-4faf-b927-cc8687869651" -->
### Issue: Rollback Failure

**Symptoms**: Cannot revert to previous version

**Solution**: Keep previous versions in Git and test rollback procedures

<!-- section_id: "3b67da80-46ef-427d-a549-cf5579869744" -->
## Summary

Universal platform version control means:
- ✅ Treat all configurations as code
- ✅ Maintain environment parity
- ✅ Never commit secrets
- ✅ Automate deployments
- ✅ Test before production
- ✅ Have rollback procedures
- ✅ Document decisions
- ✅ Monitor deployments

**Key Takeaway**: Version control is not just for application code - it's for everything your application depends on.

---

*For platform-specific implementations, see the guides for [Infrastructure as Code](./infrastructure-as-code-guide.md), [Hosting Platforms](./hosting-platforms-guide.md), [Cloud Platforms](./cloud-platforms-guide.md), and others.*

