---
resource_id: "71e17a40-3d7b-4662-99dc-012fb4b68269"
resource_type: "document"
resource_name: "universal-platform-version-control-guide"
---
# Universal Platform Version Control Guide
*Core Principles and Practices for All Platforms*

<!-- section_id: "4db04586-d6b8-4938-9f87-c11e58aa241c" -->
## Overview

This guide covers universal principles and practices for version controlling any platform or service your application uses - from infrastructure and hosting to authentication, storage, APIs, and third-party services. These principles apply regardless of which specific platforms you use.

<!-- section_id: "a3064a22-fde8-465e-bab3-fdaf54c60cc0" -->
## Core Concepts

<!-- section_id: "55b3a750-6913-49bc-9416-7e8d9401f78a" -->
### What is Platform Version Control?

Platform version control means managing all platform configurations, settings, and deployments through version control systems (like Git). This includes:

- **Infrastructure definitions** (servers, networking, databases)
- **Application deployments** (hosting, CDN, edge functions)
- **Service configurations** (authentication, storage, APIs)
- **Environment settings** (dev, staging, production)
- **Secrets and credentials** (managed securely outside Git)
- **CI/CD pipelines** (automated deployments)
- **Documentation** (why and how decisions were made)

<!-- section_id: "9b591319-7b8a-4ff3-b0f8-62926e47df0f" -->
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

<!-- section_id: "1f2d29aa-88d8-4ebb-bfaa-d7592a3c51e6" -->
## Universal Principles

<!-- section_id: "af5bf795-0fe8-44c4-a954-06a7b790d327" -->
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

<!-- section_id: "3ceff41f-7609-487e-ad9a-5ca61a3946b5" -->
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

<!-- section_id: "ed81e443-ef7a-4696-a096-3c11b15e8c78" -->
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

<!-- section_id: "359d1025-b51a-418f-b6ed-82929390f3de" -->
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

<!-- section_id: "98ff99e7-dc1c-42ea-85e8-0590cb535e55" -->
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

<!-- section_id: "860a3283-2395-4d5d-a813-ae6776cf6fea" -->
## Configuration Patterns

<!-- section_id: "0f8fc177-f044-4726-b0e0-430225dd7a0b" -->
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

<!-- section_id: "c547ebd6-6caa-40e3-8f19-43aa8c9afc18" -->
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

<!-- section_id: "a443c49b-4403-4eb6-9d2c-7d258932daa5" -->
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

<!-- section_id: "78ea38ca-2a89-4336-87da-d7e164a2e956" -->
## Version Control Strategies

<!-- section_id: "7ac2f937-57de-4559-ac1a-b9082780de63" -->
### Strategy 1: Git-Based (Recommended)

Store all configurations in Git:
- ✅ Complete history
- ✅ Easy collaboration
- ✅ PR-based reviews
- ✅ Branch-based testing
- ✅ Tagged releases

<!-- section_id: "8c892e36-334b-4b19-a911-5e94a710119b" -->
### Strategy 2: Platform APIs

Use platform APIs for version control:
- GitHub/GitLab for code + config
- Platform dashboards for visualization
- Platform CLIs for deployment
- CI/CD for automation

<!-- section_id: "6e04050a-2997-40a3-9e5a-3ba87f4e29d3" -->
### Strategy 3: Hybrid Approach

Combine Git + Platform features:
- Git for configuration
- Platform APIs for deployment
- Platform features for monitoring
- Both for backup and redundancy

<!-- section_id: "76dd4f6b-2d78-480a-917f-7465480d3011" -->
## Deployment Workflows

<!-- section_id: "b356fb6f-3a88-47e0-a640-bd7c94dcca9f" -->
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

<!-- section_id: "ce2f5a48-31a6-4b92-8449-239210e4551b" -->
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

<!-- section_id: "8bbc90d0-fa8f-493b-b634-7a3c14ea19e3" -->
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

<!-- section_id: "0aa58799-8511-4646-afec-29ba39b23b43" -->
## Best Practices

<!-- section_id: "a78549c6-8228-4f51-b754-4db181058aa7" -->
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

<!-- section_id: "fc0434b4-fea4-4e6f-bd0c-79da3b55484f" -->
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

<!-- section_id: "05349a72-d1d8-4bb5-8e2c-0251da205371" -->
### 3. Use Tags for Releases

```bash
# Tag releases
git tag -a v1.0.0 -m "Production release 1.0.0"
git push origin v1.0.0

# Deploy specific tag
git checkout v1.0.0
./scripts/deploy.sh production
```

<!-- section_id: "14003c0d-3a9f-42db-ae28-9f964bfdf09d" -->
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

<!-- section_id: "86afa7cc-8c01-4dbc-b7b7-083445521bfa" -->
### 5. Validate Configurations

```bash
# Validate before deployment
terraform validate
vercel --debug build
docker-compose config
```

<!-- section_id: "74bf4523-ad02-42f6-a8b0-0a6075c79dd9" -->
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

<!-- section_id: "235debe1-7dc6-4f3d-9f59-9e06a50c6918" -->
## Common Patterns

<!-- section_id: "15d11160-3401-4039-9828-2c0769b6a501" -->
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

<!-- section_id: "91c01665-9cc9-4c91-b3dc-b127d29ee0c1" -->
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

<!-- section_id: "99a42595-5c39-4b41-8bba-464c4a46410c" -->
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

<!-- section_id: "ef5aaff3-7378-4a9b-80fc-07edc34e27a6" -->
## Troubleshooting Universal Issues

<!-- section_id: "d78d11be-5199-41d8-8686-aa160ba09e59" -->
### Issue: Config Drift

**Symptoms**: Local and production configs differ

**Solution**: Use config synchronization tools and always deploy from Git

<!-- section_id: "6d4209aa-f167-4de2-a1e4-6ef89db49b19" -->
### Issue: Missing Secrets

**Symptoms**: Deployment fails due to missing credentials

**Solution**: Use secret managers and validate before deployment

<!-- section_id: "7650da80-800b-49bf-9917-a1086234bf4b" -->
### Issue: Environment Mismatch

**Symptoms**: Dev works but production fails

**Solution**: Ensure environment parity and use same deployment process

<!-- section_id: "f8766746-5099-40bf-b0fe-506e6bf519b3" -->
### Issue: Rollback Failure

**Symptoms**: Cannot revert to previous version

**Solution**: Keep previous versions in Git and test rollback procedures

<!-- section_id: "b6ec97bf-cd64-4860-b6f5-8649ca763f4a" -->
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

