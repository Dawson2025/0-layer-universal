---
resource_id: "4d7fb18c-e948-4751-aaac-552dcb68246f"
resource_type: "document"
resource_name: "universal-platform-version-control-guide"
---
# Universal Platform Version Control Guide
*Core Principles and Practices for All Platforms*

<!-- section_id: "cc643c8b-1660-4dbd-be93-658bc5a55181" -->
## Overview

This guide covers universal principles and practices for version controlling any platform or service your application uses - from infrastructure and hosting to authentication, storage, APIs, and third-party services. These principles apply regardless of which specific platforms you use.

<!-- section_id: "88cc6573-8a9b-44fc-867f-3e77b2de972c" -->
## Core Concepts

<!-- section_id: "70931d88-d273-42ab-b323-09f807146ace" -->
### What is Platform Version Control?

Platform version control means managing all platform configurations, settings, and deployments through version control systems (like Git). This includes:

- **Infrastructure definitions** (servers, networking, databases)
- **Application deployments** (hosting, CDN, edge functions)
- **Service configurations** (authentication, storage, APIs)
- **Environment settings** (dev, staging, production)
- **Secrets and credentials** (managed securely outside Git)
- **CI/CD pipelines** (automated deployments)
- **Documentation** (why and how decisions were made)

<!-- section_id: "9b34467b-7999-429c-bed6-c28e5fc7ecc3" -->
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

<!-- section_id: "bb13816b-fe9c-412c-9f85-5e2a71596856" -->
## Universal Principles

<!-- section_id: "ec6b444a-cb6c-4d20-afc8-5b8aa86da53c" -->
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

<!-- section_id: "f3c9e5f9-b322-44ac-bfec-e1585976a4c1" -->
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

<!-- section_id: "361cf407-06ff-48a0-a480-d46e4ab62093" -->
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

<!-- section_id: "cb988b76-8b02-4b81-b35f-08b63c2cd6ad" -->
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

<!-- section_id: "e3684134-10c0-4c23-8ea0-59df2d3ebfe8" -->
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

<!-- section_id: "fa2ab7fc-f7c7-4577-9365-bc4de3ab8971" -->
## Configuration Patterns

<!-- section_id: "9a5e309f-2cd1-4c22-9383-d30b950da676" -->
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

<!-- section_id: "9a6f767e-4c3a-4f2a-a70f-a27c1d888ff3" -->
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

<!-- section_id: "b9a8854f-5123-4824-872a-5c2202f68971" -->
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

<!-- section_id: "55ef3a63-49bf-4161-bebb-112e6a630998" -->
## Version Control Strategies

<!-- section_id: "43455ead-27f3-4f4f-94ec-715895419a1c" -->
### Strategy 1: Git-Based (Recommended)

Store all configurations in Git:
- ✅ Complete history
- ✅ Easy collaboration
- ✅ PR-based reviews
- ✅ Branch-based testing
- ✅ Tagged releases

<!-- section_id: "fca81464-c25f-48e2-9ddf-decef65c1751" -->
### Strategy 2: Platform APIs

Use platform APIs for version control:
- GitHub/GitLab for code + config
- Platform dashboards for visualization
- Platform CLIs for deployment
- CI/CD for automation

<!-- section_id: "a796a450-c309-414f-9df3-dc457236a7eb" -->
### Strategy 3: Hybrid Approach

Combine Git + Platform features:
- Git for configuration
- Platform APIs for deployment
- Platform features for monitoring
- Both for backup and redundancy

<!-- section_id: "283c9186-856e-44db-80ed-5f0bc3722bb6" -->
## Deployment Workflows

<!-- section_id: "15b7a34e-c02e-4f20-931c-b410a83409b0" -->
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

<!-- section_id: "2a2ffbed-0474-45b2-a786-6b624833b9dc" -->
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

<!-- section_id: "2de1e359-7107-4984-b5de-a1e511a84ae2" -->
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

<!-- section_id: "2952d68c-ffaf-44e9-b391-b96929bb0212" -->
## Best Practices

<!-- section_id: "48703c7c-de48-49aa-8d76-f13f73c0793f" -->
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

<!-- section_id: "72e6dedf-a14b-4a34-aa15-ab02eb04dcc6" -->
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

<!-- section_id: "77a53785-dd6f-485d-abf0-0e92e36ba251" -->
### 3. Use Tags for Releases

```bash
# Tag releases
git tag -a v1.0.0 -m "Production release 1.0.0"
git push origin v1.0.0

# Deploy specific tag
git checkout v1.0.0
./scripts/deploy.sh production
```

<!-- section_id: "d8449aaf-e316-45a4-b3dd-ebcd3ef9e7a6" -->
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

<!-- section_id: "ee3b236c-9c81-4d08-82d9-5795f36f4619" -->
### 5. Validate Configurations

```bash
# Validate before deployment
terraform validate
vercel --debug build
docker-compose config
```

<!-- section_id: "0d3721b5-7e43-4232-94e2-b9218b5983aa" -->
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

<!-- section_id: "8ea22207-3562-4671-a696-eba643ce6357" -->
## Common Patterns

<!-- section_id: "2fecd44b-3df9-4565-aaa5-7d89d36921e1" -->
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

<!-- section_id: "d94bdd19-d0f1-4179-aca7-9da616ef148d" -->
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

<!-- section_id: "a0bb5b87-d563-4f76-997c-251bc0f333c7" -->
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

<!-- section_id: "5928c961-af98-4ac0-bcd6-a63e7f718914" -->
## Troubleshooting Universal Issues

<!-- section_id: "2e5b1527-7a52-4842-886a-92d843aca6f9" -->
### Issue: Config Drift

**Symptoms**: Local and production configs differ

**Solution**: Use config synchronization tools and always deploy from Git

<!-- section_id: "cd5d82fa-ec28-4934-8e70-3834979040d0" -->
### Issue: Missing Secrets

**Symptoms**: Deployment fails due to missing credentials

**Solution**: Use secret managers and validate before deployment

<!-- section_id: "19e30325-bf65-4822-a3bb-e3142786afb0" -->
### Issue: Environment Mismatch

**Symptoms**: Dev works but production fails

**Solution**: Ensure environment parity and use same deployment process

<!-- section_id: "13271d0a-9893-479b-9b30-4744b6d7c34e" -->
### Issue: Rollback Failure

**Symptoms**: Cannot revert to previous version

**Solution**: Keep previous versions in Git and test rollback procedures

<!-- section_id: "96557836-a0cf-4e46-84b8-b5d66096ec94" -->
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

