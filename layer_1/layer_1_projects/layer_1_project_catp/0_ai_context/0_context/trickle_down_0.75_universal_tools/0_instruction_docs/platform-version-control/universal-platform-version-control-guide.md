---
resource_id: "45d1cc0c-c771-4928-b68c-50972f156ba1"
resource_type: "document"
resource_name: "universal-platform-version-control-guide"
---
# Universal Platform Version Control Guide
*Core Principles and Practices for All Platforms*

<!-- section_id: "75352b77-895c-487e-9341-198aef8c23c8" -->
## Overview

This guide covers universal principles and practices for version controlling any platform or service your application uses - from infrastructure and hosting to authentication, storage, APIs, and third-party services. These principles apply regardless of which specific platforms you use.

<!-- section_id: "c2b48bee-e5eb-4c66-97ba-ed2c3a9b5b88" -->
## Core Concepts

<!-- section_id: "d259a6d3-0ddd-4145-a067-eb0ce5fa9853" -->
### What is Platform Version Control?

Platform version control means managing all platform configurations, settings, and deployments through version control systems (like Git). This includes:

- **Infrastructure definitions** (servers, networking, databases)
- **Application deployments** (hosting, CDN, edge functions)
- **Service configurations** (authentication, storage, APIs)
- **Environment settings** (dev, staging, production)
- **Secrets and credentials** (managed securely outside Git)
- **CI/CD pipelines** (automated deployments)
- **Documentation** (why and how decisions were made)

<!-- section_id: "8ad44219-5ff9-44bf-bf5a-b1ae56b857f2" -->
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

<!-- section_id: "289d0572-2e42-468f-8416-5c359d634f59" -->
## Universal Principles

<!-- section_id: "7989ef4d-fbf0-4580-a0ba-99c67cfca1c3" -->
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

<!-- section_id: "5fc4c398-c0b3-44df-a1c8-ebf4876082f7" -->
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

<!-- section_id: "6d7f5183-c4bf-4140-9cd9-7277ad8f0841" -->
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

<!-- section_id: "27543677-e4ec-4499-b6f1-667007381a6e" -->
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

<!-- section_id: "c1e056a0-597f-468a-8971-76c13b1a6c13" -->
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

<!-- section_id: "fa5e31fe-14da-469a-8c71-5b4888f6897d" -->
## Configuration Patterns

<!-- section_id: "6c06d08a-d2f4-494c-87be-bf6f6c6f79c7" -->
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

<!-- section_id: "ab2fb0de-e292-4b09-bbac-da94a453dfab" -->
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

<!-- section_id: "b626c973-1612-47ce-93dd-87ac1d1eec87" -->
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

<!-- section_id: "c53e55bb-cef4-48d8-8315-8b7e87d613a5" -->
## Version Control Strategies

<!-- section_id: "4cf1e87b-9d88-48ca-bb60-3b20b05abcde" -->
### Strategy 1: Git-Based (Recommended)

Store all configurations in Git:
- ✅ Complete history
- ✅ Easy collaboration
- ✅ PR-based reviews
- ✅ Branch-based testing
- ✅ Tagged releases

<!-- section_id: "418a4c5b-0266-4a1e-b6db-01c1c85c32b0" -->
### Strategy 2: Platform APIs

Use platform APIs for version control:
- GitHub/GitLab for code + config
- Platform dashboards for visualization
- Platform CLIs for deployment
- CI/CD for automation

<!-- section_id: "da24ff4f-80b8-4458-971c-44e38d1fd406" -->
### Strategy 3: Hybrid Approach

Combine Git + Platform features:
- Git for configuration
- Platform APIs for deployment
- Platform features for monitoring
- Both for backup and redundancy

<!-- section_id: "43d879b6-5e2d-4eb0-adca-9d330720c2f3" -->
## Deployment Workflows

<!-- section_id: "360f09d1-f923-43b0-83e2-4430f76f35f1" -->
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

<!-- section_id: "169e7187-9425-4562-9e3e-5fa4c8c57785" -->
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

<!-- section_id: "994009df-8358-4137-961b-28a4b15111be" -->
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

<!-- section_id: "e50bd6c5-d908-4aab-8c0e-c538c5ebc6ee" -->
## Best Practices

<!-- section_id: "9edb30a4-8a20-4d21-9172-cf58bc155e18" -->
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

<!-- section_id: "222266db-6a0d-4118-9454-108ac8523fd5" -->
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

<!-- section_id: "25b7b597-52a3-485f-8594-a1c995de4829" -->
### 3. Use Tags for Releases

```bash
# Tag releases
git tag -a v1.0.0 -m "Production release 1.0.0"
git push origin v1.0.0

# Deploy specific tag
git checkout v1.0.0
./scripts/deploy.sh production
```

<!-- section_id: "20e555c3-595e-4ff1-ab0d-34b1ec4a4f66" -->
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

<!-- section_id: "b7fa00a0-8067-46d5-bccf-cf0156c74b38" -->
### 5. Validate Configurations

```bash
# Validate before deployment
terraform validate
vercel --debug build
docker-compose config
```

<!-- section_id: "1f7d4a19-337e-4125-ab72-b7a1ab66671c" -->
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

<!-- section_id: "a3d714a4-8683-41aa-8e77-82d69b237a2a" -->
## Common Patterns

<!-- section_id: "acb8ce79-0618-4235-bfec-7d0131ad48df" -->
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

<!-- section_id: "a4457d5f-35dc-42bb-97b8-93a7ad9c3ddb" -->
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

<!-- section_id: "75c7dcd2-8faf-492d-800b-bca71024fc06" -->
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

<!-- section_id: "077d3d56-c01e-43be-959d-2531a79f10f7" -->
## Troubleshooting Universal Issues

<!-- section_id: "51f712cc-6dcb-42b6-b527-78638c492078" -->
### Issue: Config Drift

**Symptoms**: Local and production configs differ

**Solution**: Use config synchronization tools and always deploy from Git

<!-- section_id: "d2ab0807-3a2f-4ed2-8ab0-eaa3ddf9b1f9" -->
### Issue: Missing Secrets

**Symptoms**: Deployment fails due to missing credentials

**Solution**: Use secret managers and validate before deployment

<!-- section_id: "ff9e39c8-c9b6-41e6-b195-fad0bf58fb71" -->
### Issue: Environment Mismatch

**Symptoms**: Dev works but production fails

**Solution**: Ensure environment parity and use same deployment process

<!-- section_id: "bc59c76f-2cec-4776-ae4c-18f83a80006d" -->
### Issue: Rollback Failure

**Symptoms**: Cannot revert to previous version

**Solution**: Keep previous versions in Git and test rollback procedures

<!-- section_id: "2e765e7d-ab4f-4b05-92c8-c8baaba5634c" -->
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

