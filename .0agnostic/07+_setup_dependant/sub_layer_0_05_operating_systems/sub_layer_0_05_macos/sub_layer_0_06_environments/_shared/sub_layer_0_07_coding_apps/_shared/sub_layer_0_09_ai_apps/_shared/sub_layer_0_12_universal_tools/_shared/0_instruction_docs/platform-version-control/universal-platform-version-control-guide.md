---
resource_id: "0d7c25e3-dcce-43f4-84f2-f3206f58a82e"
resource_type: "document"
resource_name: "universal-platform-version-control-guide"
---
# Universal Platform Version Control Guide
*Core Principles and Practices for All Platforms*

<!-- section_id: "0a05f29b-b197-409b-9bc9-12b29b7faa94" -->
## Overview

This guide covers universal principles and practices for version controlling any platform or service your application uses - from infrastructure and hosting to authentication, storage, APIs, and third-party services. These principles apply regardless of which specific platforms you use.

<!-- section_id: "9ccae515-9935-4f40-b96c-665c0b081c99" -->
## Core Concepts

<!-- section_id: "f890281f-64c0-471a-92f5-1cd4d9ff2154" -->
### What is Platform Version Control?

Platform version control means managing all platform configurations, settings, and deployments through version control systems (like Git). This includes:

- **Infrastructure definitions** (servers, networking, databases)
- **Application deployments** (hosting, CDN, edge functions)
- **Service configurations** (authentication, storage, APIs)
- **Environment settings** (dev, staging, production)
- **Secrets and credentials** (managed securely outside Git)
- **CI/CD pipelines** (automated deployments)
- **Documentation** (why and how decisions were made)

<!-- section_id: "551f350f-8f27-4af9-a013-527ab93ae336" -->
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

<!-- section_id: "156c4b2e-d074-4ab6-a699-7c0eaa4d7bac" -->
## Universal Principles

<!-- section_id: "c7215be3-9004-4786-90b2-3468472e07ff" -->
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

<!-- section_id: "d1119747-ffbf-418f-9e48-c521ec6c3093" -->
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

<!-- section_id: "d7fefe79-483c-4f2b-9deb-e91ef263eddc" -->
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

<!-- section_id: "6f2b0b04-5e3c-47cd-822c-8a391cb58bc4" -->
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

<!-- section_id: "f7b1cad2-69bf-4f5d-9d23-13bc91acff22" -->
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

<!-- section_id: "85a03d28-7482-4e8f-99a5-49dfc2d18f06" -->
## Configuration Patterns

<!-- section_id: "14ab211d-6f79-4e1e-8a80-566c315dfd65" -->
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

<!-- section_id: "41fc85a4-d717-4515-8f4c-b3f8d3b91c02" -->
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

<!-- section_id: "6609356d-ee33-4fa6-9376-12cac1b0d0b3" -->
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

<!-- section_id: "f3c238e6-074a-4885-803a-8da413335e78" -->
## Version Control Strategies

<!-- section_id: "cea7c2bf-7294-460f-b39a-017c1f21ed71" -->
### Strategy 1: Git-Based (Recommended)

Store all configurations in Git:
- ✅ Complete history
- ✅ Easy collaboration
- ✅ PR-based reviews
- ✅ Branch-based testing
- ✅ Tagged releases

<!-- section_id: "d7759cb4-d8eb-4d6e-80ed-6c84c96ed03c" -->
### Strategy 2: Platform APIs

Use platform APIs for version control:
- GitHub/GitLab for code + config
- Platform dashboards for visualization
- Platform CLIs for deployment
- CI/CD for automation

<!-- section_id: "6932b693-5bf5-4afc-85ca-28b702d5fe65" -->
### Strategy 3: Hybrid Approach

Combine Git + Platform features:
- Git for configuration
- Platform APIs for deployment
- Platform features for monitoring
- Both for backup and redundancy

<!-- section_id: "f1fa561f-89c8-4a55-98bc-358b92c36796" -->
## Deployment Workflows

<!-- section_id: "557df875-2124-462b-8566-c0735a57db78" -->
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

<!-- section_id: "937cd5a7-cf1f-4b46-ac94-3985c0dcae42" -->
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

<!-- section_id: "3503b82a-cf93-400d-8ee3-4f3ff6180686" -->
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

<!-- section_id: "9afc84d2-4585-4117-b787-94e77cf749e6" -->
## Best Practices

<!-- section_id: "d1ded43b-ffc8-4ed4-9ea7-ba573fdfe1a8" -->
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

<!-- section_id: "18ee1ff8-9c37-4aaf-800b-195649718c3e" -->
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

<!-- section_id: "45745973-b3cb-40e0-9cb5-ddf190f17b75" -->
### 3. Use Tags for Releases

```bash
# Tag releases
git tag -a v1.0.0 -m "Production release 1.0.0"
git push origin v1.0.0

# Deploy specific tag
git checkout v1.0.0
./scripts/deploy.sh production
```

<!-- section_id: "3dbd0c34-48e6-4109-be9f-07cfd54d4092" -->
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

<!-- section_id: "e8340326-8e05-496e-affe-3b102e2c493f" -->
### 5. Validate Configurations

```bash
# Validate before deployment
terraform validate
vercel --debug build
docker-compose config
```

<!-- section_id: "05b7f136-559e-4344-90c9-6095c1cea2d2" -->
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

<!-- section_id: "56a7a5e1-4514-4f56-8c03-a5bab5fb13af" -->
## Common Patterns

<!-- section_id: "1f0dc9a2-bce1-4be4-806f-001b9656f31a" -->
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

<!-- section_id: "ef8f700a-86dd-47d7-a48d-c673860b8d54" -->
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

<!-- section_id: "ccdfc5f4-ca94-43cd-abe8-6be278cea5da" -->
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

<!-- section_id: "7b8e1c35-b1ff-4cc9-ac49-c4a91f418d7e" -->
## Troubleshooting Universal Issues

<!-- section_id: "25ad0986-5c1d-45d4-ba92-4ef0805ff899" -->
### Issue: Config Drift

**Symptoms**: Local and production configs differ

**Solution**: Use config synchronization tools and always deploy from Git

<!-- section_id: "8dc7bf9a-6d43-4faa-b61f-b8f637d279fb" -->
### Issue: Missing Secrets

**Symptoms**: Deployment fails due to missing credentials

**Solution**: Use secret managers and validate before deployment

<!-- section_id: "a61d6d04-7139-41f5-a094-40f413751e3d" -->
### Issue: Environment Mismatch

**Symptoms**: Dev works but production fails

**Solution**: Ensure environment parity and use same deployment process

<!-- section_id: "56e2309c-56c7-437f-bc51-8dc5b1d7d106" -->
### Issue: Rollback Failure

**Symptoms**: Cannot revert to previous version

**Solution**: Keep previous versions in Git and test rollback procedures

<!-- section_id: "83070b49-47ac-44f7-945d-4a7e0acaba19" -->
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

