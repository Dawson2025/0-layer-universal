---
resource_id: "21a9a223-5320-4f1b-a14e-7dfd963a07bb"
resource_type: "output"
resource_name: "COMPLETE_ARCHITECTURE"
---
# Gemini — Complete Architecture

**Date**: 2026-02-27
**Focus**: How native mechanisms + application-implemented strategy work together

---

## System Overview

Gemini combines **native mechanisms** (what it provides) with **application-implemented strategy** (what you provide):

```
┌─────────────────────────────────────────────┐
│  Gemini Native Mechanisms                   │
├─────────────────────────────────────────────┤
│  • System instructions (prompt-based role)  │
│  • Session management (stateful/stateless)  │
│  • File upload & storage (48-hour ephemeral)│
│  • Multimodal input (text, images, video)   │
│  • Context caching (implicit + explicit)    │
│  • Function calling (structured output)     │
│  • Multiple models (3, 2.5, 1.5 families)   │
│  • Streaming output (real-time tokens)      │
│  • Generation parameters (temperature, etc.)│
│  • Safety filtering (built-in)              │
└─────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────┐
│  Your Application Strategy                  │
├─────────────────────────────────────────────┤
│  • System instruction content & strategy    │
│  • Session boundary decisions               │
│  • File upload & retention policy           │
│  • Caching strategy (implicit vs. explicit) │
│  • Model selection per task                 │
│  • Generation parameter tuning              │
│  • Error handling & retry logic             │
│  • Cost tracking & budget management        │
└─────────────────────────────────────────────┘
                           ↓
                    Working System
```

---

## Request-Response Flow

### Every Request (What Happens)

```
1. Your application prepares:
   - System instruction (context setup)
   - User message (prompt)
   - Optional: files to include
   - Optional: generation parameters

2. You call Gemini API:
   client.models.generate_content(
       model="gemini-2.5-flash",
       contents=user_message,
       system_instruction=system_instruction,
       generation_config={...},
       cache_control={...} (if using explicit caching)
   )

3. Gemini processes:
   - Parse system instruction (token-count it)
   - Parse user message
   - Check cache (implicit or explicit)
   - Route to specified model
   - Apply generation parameters
   - Generate response token-by-token

4. You receive response:
   - Response text
   - Token usage (input, output, cache_creation, cache_read)
   - Stop reason (stop_sequence, max_tokens, safety, etc.)

5. Your application handles:
   - Save to session (if stateful)
   - Log tokens for cost tracking
   - Handle errors (retry, fallback, notify)
   - Display response
```

### Token Counting (Before Request)

```python
# Before expensive request, estimate token usage
token_count = client.models.count_tokens(
    model="gemini-2.5-pro",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part.from_text(user_message)]
        ),
    ],
    system_instruction=system_instruction,
)

estimated_cost = estimate_cost(
    token_count.total_tokens,
    output_estimate=2000,  # Guess output size
    model="gemini-2.5-pro"
)

if estimated_cost['total'] > budget:
    # Use Flash instead of Pro
    # Or break request into smaller parts
```

---

## System Instruction Strategy

### What You Control

System instructions define the model's role and constraints. **You write these from scratch.**

```python
system_instruction = """
You are an expert software architect specializing in distributed systems.

Guidelines:
- Prioritize scalability and fault tolerance
- Suggest trade-offs explicitly
- Prefer industry-standard patterns over novel approaches
- Include rough implementation estimates

Output format:
1. Architecture diagram (ASCII art)
2. Component descriptions (3-5 lines each)
3. Trade-offs and alternatives (2-3 alternatives for each decision)
4. Implementation roadmap (phased approach)
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Design a notification system for 10M users",
    system_instruction=system_instruction,
)
```

### System Instruction Impact

| Aspect | Effect | Trade-off |
|--------|--------|-----------|
| **Instruction length** | Token budget consumed | Longer instructions = fewer tokens for user input/output |
| **Instruction clarity** | Response quality | Vague = unpredictable, over-specified = inflexible |
| **Role definition** | Model behavior | "Expert" vs "helpful assistant" vs "rigorous reviewer" |
| **Constraint specificity** | Adherence | Specific constraints improve compliance but may limit creativity |

---

## Session Management Strategy

### Stateless (Default)

Each request is independent:

```python
# Request 1
response1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain React hooks",
    system_instruction=system_instruction,
)

# Request 2 (no history from Request 1)
response2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How do I use useState?",  # No context from response1
    system_instruction=system_instruction,
)
```

**When to use**: One-off questions, stateless APIs, no need for conversation history.

### Stateful with Resumption

Multi-turn conversation with history:

```python
# Create session
session = client.messages.create(
    model="gemini-2.5-flash",
    max_tokens=1024,
    system=[{"type": "text", "text": system_instruction}],
    messages=[
        {"role": "user", "content": "Explain React hooks"},
        {"role": "assistant", "content": "[response1]"},
        {"role": "user", "content": "How do I use useState?"},
        {"role": "assistant", "content": "[response2]"},
    ]
)

# Later (within 2 hours): resume session
continued = client.messages.create(
    model="gemini-2.5-flash",
    system=[...],
    messages=[...],  # History carries forward
)
```

**When to use**: Multi-turn conversations, debugging sessions, projects where history is valuable.

### Session Lifetime Limits

- **2-hour resumption window**: Sessions expire after 2 hours. After that, you must start fresh.
- **Token accumulation**: Long conversations consume more tokens (billing impact).
- **Context window limit**: Even in stateful mode, total context is capped (though Gemini's 1M/2M token windows are large).

---

## File Upload & Storage

### When to Upload

```python
# Upload large document
with open("research_paper.pdf", "rb") as f:
    response = client.beta.files.upload(
        file=("research_paper.pdf", f, "application/pdf"),
    )
    file_id = response.id

# Use in request
message = client.beta.messages.create(
    model="gemini-2.5-flash",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Summarize the key findings"
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

# File is auto-deleted after 48 hours
# If you need it later, re-upload
```

### Storage Quota & Retention

| Aspect | Limit | Your Decision |
|--------|-------|---------------|
| **File size limit** | 2GB per file | Break large files into chunks if needed |
| **Storage quota** | 20GB per project | Track uploads, clean up as needed |
| **Retention** | 48 hours auto-delete | Plan for re-uploads if sessions span days |

### Alternative: Base64 Inline

For small files (<100MB), encode as base64:

```python
import base64

with open("document.pdf", "rb") as f:
    file_data = base64.standard_b64encode(f.read()).decode("utf-8")

message = client.beta.messages.create(
    model="gemini-2.5-flash",
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Analyze this document"
            },
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": file_data,
                }
            }
        ]
    }]
)
```

**Trade-off**: Base64 is faster for small files but inline in requests, consuming tokens. Files API requires upload but provides 48-hour reuse.

---

## Caching Strategy

### Implicit Caching (Automatic)

After a request with 4,096+ tokens, Gemini automatically caches the prefix:

```python
# First request: creates implicit cache
response1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part.from_text(long_system_instruction + user_q1)]
        ),
    ],
)

# Second request with same prefix: hits cache (~50% cost reduction)
response2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part.from_text(long_system_instruction + user_q2)]
        ),
    ],
)
```

**When to use**: Repetitive queries with same context.

### Explicit Caching (Guaranteed)

For critical contexts, use explicit caching with TTL:

```python
# Explicitly cache expensive system instruction
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part.from_text(user_message)]
        ),
    ],
    system_instruction=system_instruction,  # Will be cached
    cache_control={"type": "ephemeral"},  # 5 minute TTL
)
```

**Cost comparison**:
- Regular tokens: $0.075 per 1M input (Flash)
- Implicit cache hit: ~$0.038 per 1M (50% reduction)
- Explicit cache hit: ~$0.008 per 1M (90% reduction)

**When to use**: Large documents, expensive prefixes, multi-request workflows.

---

## Model Selection Strategy

### Available Models

| Model | Speed | Intelligence | Cost | Best For |
|-------|-------|--------------|------|----------|
| **Gemini 3 Flash** | Very Fast | Good | $ | Real-time, lightweight tasks |
| **Gemini 3 Pro** | Slow | Excellent | $$$ | Complex reasoning, depth |
| **Gemini 2.5 Flash** | Very Fast | Good | $ | General-purpose, production |
| **Gemini 2.5 Pro** | Slow | Excellent | $$$ | Research, analysis, writing |

### Routing Strategy

```python
def choose_model(task_complexity):
    if task_complexity == "simple":
        # Quick questions: Flash
        return "gemini-2.5-flash"
    elif task_complexity == "moderate":
        # Standard coding/writing: Flash
        return "gemini-2.5-flash"
    elif task_complexity == "complex":
        # Deep analysis, reasoning: Pro
        return "gemini-2.5-pro"

# Cost optimization: start with Flash, upgrade if needed
result = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    system_instruction=system_instruction,
)

if result_quality_low():
    # Retry with Pro
    result = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt,
        system_instruction=system_instruction,
    )
```

---

## Error Handling & Retry Strategy

### Common Errors

| Error | Status Code | Handling |
|-------|-------------|----------|
| Rate limited | 429 | Exponential backoff + queue |
| Server error | 500, 503 | Retry with exponential backoff |
| Auth failed | 401, 403 | Re-authenticate or notify |
| Bad request | 400 | Fix prompt, don't retry |
| Safety violation | 400 | Adjust system instruction, try again |

### Retry Logic

```python
import time
import random

def call_gemini_with_retry(
    prompt,
    model="gemini-2.5-flash",
    max_retries=3,
    initial_backoff=1
):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model=model,
                contents=prompt,
                system_instruction=system_instruction,
            )
        except Exception as e:
            if attempt == max_retries - 1:
                # Last attempt failed
                return fallback_response(e)

            # Exponential backoff with jitter
            backoff = initial_backoff * (2 ** attempt)
            jitter = random.uniform(0, backoff * 0.1)
            time.sleep(backoff + jitter)
```

---

## Cost Tracking & Optimization

### Token Accounting

Every Gemini request reports:
- `input_tokens`: Tokens in your message + system instruction
- `output_tokens`: Tokens in the response
- `cache_creation_input_tokens`: Tokens used to create cache
- `cache_read_input_tokens`: Tokens read from cache

### Cost Calculation

```python
def calculate_cost(usage, model="gemini-2.5-flash"):
    """Calculate cost from token usage."""

    # Pricing (as of 2026) — check official docs for updates
    pricing = {
        "gemini-2.5-flash": {
            "input": 0.075 / 1_000_000,
            "output": 0.30 / 1_000_000,
            "cache_creation": 0.10 * 0.075 / 1_000_000,  # 10% of input rate
            "cache_read": 0.02 * 0.075 / 1_000_000,      # 2% of input rate
        },
        "gemini-2.5-pro": {
            "input": 3.0 / 1_000_000,
            "output": 12.0 / 1_000_000,
            "cache_creation": 0.10 * 3.0 / 1_000_000,
            "cache_read": 0.02 * 3.0 / 1_000_000,
        },
    }

    rates = pricing[model]
    cost = (
        usage.input_tokens * rates["input"] +
        usage.output_tokens * rates["output"] +
        usage.cache_creation_input_tokens * rates["cache_creation"] +
        usage.cache_read_input_tokens * rates["cache_read"]
    )

    return cost
```

### Optimization Strategies

1. **Use Flash by default** → Upgrade to Pro only for complex tasks
2. **Enable explicit caching** → For documents used in multiple requests (90% savings)
3. **Batch requests** → Combine multiple questions into one request
4. **Token budget before request** → Estimate before calling expensive models
5. **Streaming responses** → Can stop early if answer is found (saves tokens)
6. **Compress documents** → Only upload necessary content, not full files

### Budget Enforcement

```python
class GeminiBudget:
    def __init__(self, monthly_limit=50.0):  # $50/month example
        self.limit = monthly_limit
        self.spent = 0.0

    def check_cost(self, estimated_cost):
        """Check if request exceeds budget."""
        if self.spent + estimated_cost > self.limit:
            remaining = self.limit - self.spent
            raise BudgetExceeded(f"Budget exceeded. ${remaining:.2f} remaining")

    def track_usage(self, token_usage):
        """Record actual cost after request."""
        cost = calculate_cost(token_usage)
        self.spent += cost
        if self.spent > self.limit * 0.8:
            print(f"⚠️ WARNING: 80% of budget consumed (${self.spent:.2f})")
```

---

## Context Composition (What's Actually Used)

At any point, your request contains:

```
┌─ System Instruction (your role definition)
├─ User Message(s) (current request + history if stateful)
├─ File References (uploaded documents)
├─ Generation Config (temperature, max_tokens, top_p)
├─ Cache Control (implicit vs. explicit caching)
└─ Remaining context window: Available for response
```

**Token Budget** (2.5M token example):
- ~100 tokens: System instruction
- ~200-500 tokens: User message
- ~100-1000 tokens: File content (if any)
- ~X tokens: Session history (if stateful, grows with conversation)
- ~Y tokens: Available for response

---

## Summary: The System Works When

✅ **System instructions are clear and accurate** (model behavior depends on them)
✅ **Session boundaries match your use case** (stateless vs. stateful decision)
✅ **Files are uploaded strategically** (only when needed, managed for 48-hour retention)
✅ **Caching strategy matches request patterns** (implicit for ad-hoc, explicit for batch)
✅ **Model selection matches task complexity** (Flash for simple, Pro for complex)
✅ **Error handling is robust** (retries with backoff, fallbacks, cost limits)
✅ **Cost is tracked and budgeted** (monitor spend, optimize expensive requests)

The system fails when any of these are missing or outdated.

