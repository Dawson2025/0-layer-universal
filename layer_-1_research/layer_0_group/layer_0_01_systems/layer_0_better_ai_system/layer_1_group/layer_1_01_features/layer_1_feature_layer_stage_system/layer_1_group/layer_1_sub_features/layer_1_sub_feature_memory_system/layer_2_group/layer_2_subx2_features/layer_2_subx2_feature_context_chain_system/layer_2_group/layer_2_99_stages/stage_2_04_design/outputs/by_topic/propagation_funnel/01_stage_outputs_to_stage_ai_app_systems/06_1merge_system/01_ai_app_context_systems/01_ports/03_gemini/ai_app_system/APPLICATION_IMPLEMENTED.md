---
resource_id: "6bb9840e-a26b-4603-ad8a-758121cf7d1e"
resource_type: "output"
resource_name: "APPLICATION_IMPLEMENTED"
---
# Gemini — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What developers must create/customize (the content and strategy)

---

<!-- section_id: "94eacb1e-9650-4d74-b2dc-8cce0359e180" -->
## Overview

Gemini provides the **mechanisms**. Developers/applications must provide the **strategy and content**:

1. **System Instructions** (what instructions to define)
2. **Session Management Strategy** (when to resume vs. create new)
3. **File Upload Strategy** (which files to upload, retention policy)
4. **Caching Strategy** (when to use implicit vs. explicit caching)
5. **Model Selection** (which model for each task)
6. **Generation Parameters** (temperature, top_p, token limits)
7. **Error Handling** (retry logic, fallback strategies)
8. **Cost Tracking** (monitoring API spend)

---

<!-- section_id: "cf74f510-7945-4207-951c-c91fd84d2bae" -->
## 1. System Instructions — Content & Strategy

<!-- section_id: "cd0e546a-0bd7-4602-9d50-7781403633a1" -->
### What You Must Create

Gemini's system instructions are entirely application-defined. Gemini just **applies** them; you decide **what goes in them**.

<!-- section_id: "caab2c90-2588-4288-9ee5-39826d7ce0f5" -->
### Examples of Decisions YOU Make

**Instructions Content**:
- What is the model's role? (expert developer, teacher, analyst, code reviewer)
- What constraints apply? (don't suggest unsafe patterns, prioritize performance, prefer clarity over brevity)
- What output format? (markdown, JSON, plain text, code blocks)
- What tone? (formal, conversational, technical, creative)

**Instructions Scope**:
- Global instructions (applied to entire session)
- Per-request instructions (overrides for specific calls)
- Context-dependent instructions (vary by conversation phase)

<!-- section_id: "16e3f331-aa3f-43f7-9e31-2ee61c521c65" -->
### User Responsibility

- **Write** system instructions from scratch
- **Maintain** accuracy (outdated instructions mislead the model)
- **Update** when task context changes
- **Test** instructions with sample requests
- **Balance** instruction length (token budget is limited)

<!-- section_id: "b05699d3-c9ea-49f7-8235-7eccb2c9dc03" -->
### Example

```python
system_instruction = """
You are an expert Python data analyst.

Guidelines:
- Prefer pandas for tabular data manipulation
- Use numpy for numerical operations
- Always include docstrings in functions
- Add type hints to function signatures
- Default to readable code over clever one-liners
- Explain trade-offs when suggesting approaches

Output format: Code in markdown blocks, followed by brief explanation.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    system_instruction=system_instruction,
)
```

---

<!-- section_id: "fe63d588-2bd3-4f34-b0b5-8f7fedbf2b6c" -->
## 2. Session Management Strategy — When to Resume vs. Create

<!-- section_id: "26799dcc-8742-46af-a9b4-9cdf8c7c5c0e" -->
### What You Must Decide

Gemini supports two session models, but **you** decide **when to use each**:

**Stateless** (default):
- Single request → response
- Fast, simple, no history
- Best for: One-off questions

**Stateful with Resumption** (Interactions API):
- Multi-turn conversation
- Sessions resumable for 2 hours
- Best for: Multi-step projects, debugging

<!-- section_id: "83501f09-793e-44a9-af27-6f178ab1ed68" -->
### Strategic Decisions YOU Make

**Session Boundaries**:
- One session per task? (coherent context, can get long)
- One session per day? (natural boundary, may lose context)
- One session per feature? (focused, but many sessions)

**Resumption Policy**:
- When is old context valuable? (debugging same issue, continuing work)
- When should you start fresh? (new feature, unrelated task)
- How long to keep sessions active? (2-hour limit is hard stop)

<!-- section_id: "0d95b873-4b79-4e8d-a616-eeb01215a96e" -->
### User Responsibility

- **Decide** session boundaries (no right answer)
- **Implement** session creation/resumption logic
- **Track** active session IDs
- **Handle** session expiry (2-hour limit)
- **Balance** context retention vs. token cost

<!-- section_id: "6c56a9ab-3064-4e79-8d82-e806091640cc" -->
### Example

```python
# Start new session for new task
session = client.messages.create(
    model="gemini-2.5-flash",
    max_tokens=1024,
    system=[{"type": "text", "text": system_instruction}],
    messages=[{"role": "user", "content": "Explain async/await"}]
)

# Later: resume session if within 2 hours
if session_expiry_valid():
    continued = client.messages.create(
        model="gemini-2.5-flash",
        system=[...],
        messages=[...],
        # Gemini maintains history automatically within session
    )
```

---

<!-- section_id: "981f0e8c-8a9a-49fd-b872-da7164a04125" -->
## 3. File Upload Strategy — What, When, How Long

<!-- section_id: "e569f8b5-e92a-4789-9132-5c0c412e3133" -->
### What You Must Decide

Gemini stores files for 48 hours automatically, but **you** decide:

**What to Upload**:
- Which documents are needed? (upload only what's referenced)
- Supplement with context or upload documents directly?
- Batch multiple files or request-by-request?

**Upload Timing**:
- Pre-upload all resources (faster later, more tokens)
- Upload on-demand per request (less tokens upfront, slower initial)
- Hybrid (cache documents, upload supplements)

**Retention Strategy**:
- Files auto-delete after 48 hours
- Plan for re-uploads if sessions span multiple days
- Track file IDs to avoid redundant uploads

<!-- section_id: "39085f96-28e0-49fd-b556-748491725c02" -->
### User Responsibility

- **Choose** upload method (base64, Files API, URLs)
- **Decide** what documents to include
- **Track** file upload timing (48-hour expiry)
- **Manage** file quota (20GB per project limit)
- **Re-upload** as needed for long-running projects

<!-- section_id: "e55b23ba-52e2-4e09-84b9-2b9a7c6fdd48" -->
### Example

```python
import anthropic
import json

client = anthropic.Anthropic()

# Upload a document
with open("research_paper.pdf", "rb") as f:
    response = client.beta.files.upload(
        file=("research_paper.pdf", f, "application/pdf"),
    )
    file_id = response.id

# Use uploaded file in request
message = client.beta.messages.create(
    model="gemini-2.5-flash",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Summarize the key findings from this paper"
            },
            {
                "type": "document",
                "source": {
                    "type": "file",
                    "file_id": file_id,
                }
            }
        ]
    }]
)

# File auto-deletes after 48 hours
# If needed later, re-upload
```

---

<!-- section_id: "0ad8fae7-7d08-4a09-8e72-bc6fd2d348a6" -->
## 4. Caching Strategy — When to Cache, Which Type

<!-- section_id: "9b738629-eae5-44f3-9988-08fbd223abc5" -->
### What You Must Decide

Gemini offers two caching modes; **you** decide **when to use each**:

**Implicit Caching** (automatic):
- Minimum 4,096 tokens
- Automatic after first identical request
- ~50% cost reduction

**Explicit Caching** (developer-managed):
- Minimum 1,024 tokens
- Guaranteed availability for TTL
- ~90% cost reduction

<!-- section_id: "faf6e8ba-8a85-4fda-9d07-7400fb2a2102" -->
### Strategic Decisions YOU Make

**When to Use Implicit**:
- Repetitive requests with same prefix?
- Standard queries that may repeat?
- Cost savings are optional, not critical?

**When to Use Explicit**:
- Critical context that must persist?
- Expensive prefixes (large documents)?
- Multi-request workflows with shared context?

**Cache TTL**:
- How long to cache? (5 min to 1 hour)
- When to refresh? (when context changes)
- Cost of re-creating cache vs. TTL cost?

<!-- section_id: "002e9352-b66f-4975-baed-16f2dd36c77b" -->
### User Responsibility

- **Identify** cacheable content (stable prefixes)
- **Choose** caching strategy (implicit vs. explicit)
- **Set** TTL appropriately (balance cost vs. availability)
- **Monitor** cache hits (verify caching is working)
- **Refresh** when context changes

<!-- section_id: "57ba269d-4691-4ce6-bcd6-b136d3e41cbb" -->
### Example

```python
# Explicit caching for expensive system instruction
system_instruction = """
You are an expert code reviewer specializing in Python security patterns.
[500 lines of security guidelines...]
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part.from_text("Review this code for security issues")]
        ),
    ],
    system_instruction=system_instruction,
    cache_control={"type": "ephemeral"},  # 5 minute cache
)

# Second request with same system instruction hits cache
response2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[...],
    system_instruction=system_instruction,  # Same = cache hit
    cache_control={"type": "ephemeral"},
)
```

---

<!-- section_id: "e25b6689-adee-475c-8b47-f464db7efd70" -->
## 5. Model Selection — Which Model for Each Task

<!-- section_id: "eadbd6cb-6131-4e61-b0c2-78c176a60ffb" -->
### What You Must Decide

Multiple models available; **you** choose **for each request**:

| Model | Speed | Intelligence | Cost | Best For |
|-------|-------|--------------|------|----------|
| **Gemini 3 Flash** | Very Fast | Good | $ | Quick answers, lightweight |
| **Gemini 3 Pro** | Slow | Excellent | $$$ | Complex reasoning, depth |
| **Gemini 2.5 Flash** | Very Fast | Good | $ | Production, real-time |
| **Gemini 2.5 Pro** | Slow | Excellent | $$$ | Research, advanced tasks |

<!-- section_id: "fb52e22a-4e36-4554-ace2-e931ce03781f" -->
### Strategic Decisions YOU Make

**Model Strategy**:
- Default model for standard requests? (usually Flash)
- When to upgrade to Pro? (complex tasks, reasoning-heavy)
- Cost constraints? (optimize for Flash if budget-sensitive)

**Per-Request Selection**:
- Should different tasks use different models?
- Auto-routing based on complexity?
- User-override capability?

<!-- section_id: "8306f50e-d262-47fc-bf79-563d3386190b" -->
### User Responsibility

- **Choose** default model
- **Route** complex tasks to Pro
- **Monitor** cost per model
- **Decide** speed vs. quality trade-off
- **Update** strategy as new models release

<!-- section_id: "87ea47ab-ad73-4dbd-bbab-e6009bd61553" -->
### Example

```python
# Standard question → Flash (fast, cheap)
simple = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is 2+2?",
)

# Complex analysis → Pro (slower, smarter)
complex_response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Design a distributed caching system for a high-traffic e-commerce platform"
)
```

---

<!-- section_id: "e7514397-76f3-4a78-8bfa-c4eb93dabdcd" -->
## 6. Generation Parameters — Temperature, Top P, Token Limits

<!-- section_id: "be54793f-050e-41bd-9686-3feb0c3f582f" -->
### What You Must Decide

Fine-tune model behavior for each request:

| Parameter | Range | Purpose | When to Adjust |
|-----------|-------|---------|-----------------|
| `temperature` | 0.0-2.0 | Randomness (0=deterministic, 2=creative) | Deterministic: 0.0, Balanced: 0.7, Creative: 1.5+ |
| `top_p` | 0.0-1.0 | Nucleus sampling (diversity) | Default 1.0 works; lower = stricter |
| `top_k` | 1-40 | Top-K sampling (restricted vocabulary) | Default 40; lower = more focused |
| `max_output_tokens` | 1-2048 | Response length limit | Match expected response size |

<!-- section_id: "1dd35389-acda-4bf0-8a6a-b08e45c0c27d" -->
### Strategic Decisions YOU Make

**Temperature Strategy**:
- Code generation? (0.0 = deterministic)
- Brainstorming? (1.0+ = creative)
- Analysis? (0.7 = balanced)

**Token Budget**:
- How long should responses be?
- Limit to save cost?
- Expand for detailed explanations?

**Parameter Combinations**:
- Should different tasks have different presets?
- User-customizable parameters?
- Auto-adjust based on request type?

<!-- section_id: "d991006b-7569-4141-ad86-f1b13c1060e2" -->
### User Responsibility

- **Set** temperature based on task (deterministic for code, creative for ideas)
- **Choose** token limits (balance response length vs. cost)
- **Test** parameter combinations
- **Document** what works for each use case
- **Update** as you learn model behavior

<!-- section_id: "281da3e2-399a-4134-bfed-9c8777835b91" -->
### Example

```python
# Code generation: deterministic
config_code = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Generate a Python function to parse JSON",
    generation_config={
        "temperature": 0.0,  # Always same output
        "max_output_tokens": 512,
    }
)

# Creative writing: high temperature
story = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Write a sci-fi story about AI discovering consciousness",
    generation_config={
        "temperature": 1.5,  # More creative variation
        "max_output_tokens": 2048,
    }
)
```

---

<!-- section_id: "8e723052-8a1b-45f9-a1d4-38cc518720d6" -->
## 7. Error Handling — Retry Logic, Fallbacks, Graceful Degradation

<!-- section_id: "9287c424-7d90-4ee3-9a92-b7a3adfbebcc" -->
### What You Must Decide

Gemini can fail in several ways; **you** decide **how to handle each**:

**API Errors**:
- Rate limits (429 Too Many Requests)
- Server errors (500, 503)
- Auth failures (401, 403)
- Client errors (400 Bad Request)

**Handling Strategy**:
- Retry immediately or back off?
- Fallback to different model?
- Queue for later?
- Notify user of failure?

<!-- section_id: "4859b433-0254-4c5f-a74b-5e2768fd1df3" -->
### User Responsibility

- **Implement** retry logic with exponential backoff
- **Catch** and handle specific error types
- **Log** errors for debugging
- **Provide** fallback responses
- **Test** error scenarios

<!-- section_id: "45011d9b-3ed1-4540-9e41-001ade98ce81" -->
### Example

```python
import time
import random

def call_gemini_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                generation_config={
                    "max_output_tokens": 1024,
                }
            )
            return response.text
        except Exception as e:
            if attempt == max_retries - 1:
                # Last attempt failed, return fallback
                return "Unable to generate response. Please try again."

            # Exponential backoff
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait_time)
```

---

<!-- section_id: "e5990879-6fc3-435f-9ab9-327a0dbfa954" -->
## 8. Cost Tracking — Monitoring Spend, Optimization

<!-- section_id: "426f0de8-5af0-4faf-9866-721461bc4dee" -->
### What You Must Decide

Gemini pricing is token-based; **you** decide **how to manage costs**:

**Cost Factors**:
- Token count (input + output)
- Model choice (Flash cheaper than Pro)
- Caching (reduces token cost 50-90%)
- Context window (larger = more tokens)

<!-- section_id: "97a81be0-b82f-411c-84ba-8375c1820704" -->
### Strategic Decisions YOU Make

**Monitoring**:
- Track spend per request?
- Per-session budgets?
- Per-user quotas?

**Optimization**:
- Use caching for large documents?
- Prefer Flash over Pro when possible?
- Batch requests to reduce overhead?

**Budget Enforcement**:
- Hard limit per month?
- Alert at percentage of budget?
- Auto-disable when limit reached?

<!-- section_id: "d1d90709-8a50-4a21-8cf0-f2bc30f9cf39" -->
### User Responsibility

- **Monitor** API costs
- **Estimate** tokens before expensive requests
- **Implement** cost controls
- **Optimize** for budget constraints
- **Review** cost patterns monthly

<!-- section_id: "47165e4b-8634-4f7b-aeaf-ac3eb9a07f68" -->
### Example

```python
def estimate_cost(input_tokens, output_tokens, model="gemini-2.5-flash"):
    """Estimate cost for Gemini request."""

    # Pricing (as of 2026): subject to change
    pricing = {
        "gemini-2.5-flash": {
            "input": 0.075 / 1_000_000,    # $0.075 per 1M input tokens
            "output": 0.30 / 1_000_000,    # $0.30 per 1M output tokens
        },
        "gemini-2.5-pro": {
            "input": 3.0 / 1_000_000,      # $3.0 per 1M input tokens
            "output": 12.0 / 1_000_000,    # $12.0 per 1M output tokens
        },
    }

    rates = pricing.get(model, pricing["gemini-2.5-flash"])
    input_cost = input_tokens * rates["input"]
    output_cost = output_tokens * rates["output"]

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total": input_cost + output_cost,
    }

# Before expensive request, estimate cost
estimated = estimate_cost(input_tokens=10000, output_tokens=2000, model="gemini-2.5-pro")
print(f"Estimated cost: ${estimated['total']:.4f}")
```

---

<!-- section_id: "4e93da03-0a1e-4b3a-95de-fb7203742ccb" -->
## Summary: Application-Implemented = Strategy & Content

| Aspect | Gemini Does | You Must Provide |
|--------|-----------|------------------|\
| **System Instructions** | Applies them to every request | Write content, decide what constraints matter |
| **Session Management** | Maintains history automatically | Decide boundaries, when to resume |
| **File Uploads** | Stores files for 48 hours | Choose what to upload, manage retention |
| **Caching** | Implements caching mechanism | Decide caching strategy (implicit vs. explicit) |
| **Model Selection** | Routes to specified model | Choose model for each task |
| **Generation Parameters** | Applies to response generation | Choose temperature, tokens, top_p based on task |
| **Error Handling** | Returns errors with status codes | Implement retry logic, fallbacks |
| **Cost Tracking** | Counts tokens, charges API | Monitor spend, set budgets, optimize |

---

<!-- section_id: "4d2fad75-00da-4a78-a23a-d4e82dfad90d" -->
## Key Principle

**Gemini provides the mechanisms. You provide the strategy and content.**

If Gemini is not working well, the issue is usually:
- Unclear or outdated system instructions
- Wrong model choice (using expensive Pro for simple tasks)
- Poor session management (not resuming when you should)
- No error handling (failures cause application crashes)
- No cost monitoring (bills are unexpectedly high)
- Suboptimal caching strategy (not using implicit/explicit appropriately)

All of these are **your** decisions, not Gemini's.

