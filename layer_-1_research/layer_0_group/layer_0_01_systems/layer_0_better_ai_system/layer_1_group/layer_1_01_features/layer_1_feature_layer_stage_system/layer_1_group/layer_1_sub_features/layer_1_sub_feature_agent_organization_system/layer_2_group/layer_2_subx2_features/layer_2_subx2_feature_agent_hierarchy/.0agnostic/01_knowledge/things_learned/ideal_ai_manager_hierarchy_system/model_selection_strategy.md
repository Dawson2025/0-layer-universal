---
resource_id: "8320c2a2-678c-4fe5-bd4b-cbc11bf2c58e"
resource_type: "knowledge"
resource_name: "model_selection_strategy"
---
## Model Selection and Cost-Aware Routing Strategy

This document provides detailed guidance on choosing models and routing tasks to optimize for cost, quality, and latency.

It extends the policy concepts from:
- `token_and_policy_strategy.md`
- `tools_and_context_systems.md`

---

## 1. Model Selection Dimensions

When selecting a model for a specific task, consider:

1. **Task Complexity**
   - Simple: code formatting, basic refactors, test generation
   - Medium: feature implementation, API integration
   - Complex: architecture design, debugging, multi-file refactors

2. **Context Requirements**
   - Small: single file, focused task
   - Medium: multiple files, module-level
   - Large: cross-module, system-level reasoning

3. **Quality vs Cost Tradeoff**
   - High quality required: production code, security-critical
   - Balanced: feature development, testing
   - Cost-optimized: bulk operations, experimental work

4. **Latency Sensitivity**
   - Interactive: human waiting for response
   - Batch: background workers, CI/CD
   - Async: long-running research, planning

---

## 2. Model Tiers and Characteristics

### 2.1 Tier 1: Premium Reasoning Models

**Models:**
- Claude Opus 4.5
- Claude Sonnet 4.5
- GPT-4 Turbo
- Gemini Pro 2.0

**Characteristics:**
- Highest quality reasoning
- Best for complex, multi-step tasks
- Higher cost ($10-60 per million tokens)
- Slower inference (2-10s per response)

**Best For:**
- L0-L2 managers requiring deep reasoning
- Criticism and fixing stages
- Complex debugging and architecture decisions
- Security-critical code review

**Avoid For:**
- Bulk code generation
- Simple formatting or refactors
- Repetitive tasks with clear patterns

### 2.2 Tier 2: Balanced Models

**Models:**
- Claude Haiku
- GPT-4o Mini
- Gemini Flash 2.0

**Characteristics:**
- Good reasoning at moderate cost
- Faster inference (1-3s per response)
- Moderate cost ($0.50-5 per million tokens)

**Best For:**
- L2-L3 feature and component managers
- Implementation and testing stages
- General-purpose coding tasks
- Request and instructions stages

**Avoid For:**
- Extremely complex reasoning
- Bulk operations where cost matters most

### 2.3 Tier 3: Code-Specialized Models

**Models:**
- Qwen-Coder-32B
- StarCoder2-15B
- Codestral (Mistral)
- DeepSeek Coder

**Characteristics:**
- Optimized for code generation
- Very fast inference (<1s per response)
- Low cost ($0.10-1 per million tokens)
- May lack broader reasoning

**Best For:**
- L3-L4 leaf implementation workers
- Test generation
- Code completion and formatting
- Bulk refactoring with clear patterns

**Avoid For:**
- High-level planning
- Architecture decisions
- Complex debugging requiring reasoning

### 2.4 Tier 4: Local and Self-Hosted Models

**Models:**
- Llama 3.1 70B/8B
- Mistral 7B/22B
- CodeLlama
- Phi-3

**Characteristics:**
- Zero marginal cost (after hardware)
- Complete privacy and control
- Inference speed depends on hardware
- Quality varies widely

**Best For:**
- Privacy-sensitive tasks
- High-volume batch processing
- Experimentation and prototyping
- Organizations with GPU infrastructure

**Avoid For:**
- Tasks requiring cutting-edge reasoning
- When latency is critical (unless you have fast GPUs)

---

## 3. Cost-Aware Routing Policies

### 3.1 Policy Matrix

| Layer | Stage | Task Type | Primary Model | Fallback | Cost Ceiling |
|-------|-------|-----------|---------------|----------|--------------|
| L0 | Any | Manager/Coordination | Claude Sonnet 4.5 | GPT-4 Turbo | $5/task |
| L1 | Request/Instructions | Dialogue-heavy | Gemini Pro 2.0 | Claude Sonnet 4.5 | $3/task |
| L1 | Planning | Complex reasoning | Claude Sonnet 4.5 | GPT-4 Turbo | $4/task |
| L1 | Design | Architecture | Claude Sonnet 4.5 | GPT-4 Turbo | $4/task |
| L2 | Planning | Feature decomposition | Claude Haiku | Gemini Flash 2.0 | $1/task |
| L2 | Implementation | Coordination | Claude Haiku | Gemini Flash 2.0 | $1/task |
| L3 | Implementation | Single component | Codestral | Qwen-Coder | $0.20/task |
| L3 | Testing | Test generation | StarCoder2 | Codestral | $0.10/task |
| L3 | Criticism | Code review | Claude Sonnet 4.5 | GPT-4 Turbo | $2/task |
| L3 | Fixing | Simple fixes | Codestral | Claude Haiku | $0.50/task |
| L3 | Fixing | Complex fixes | Claude Sonnet 4.5 | GPT-4 Turbo | $2/task |
| L4 | Implementation | Atomic tasks | Local Llama | Codestral | $0.05/task |

### 3.2 Dynamic Routing Algorithm

```python
def select_model(layer: int, stage: str, task: dict) -> ModelConfig:
    """
    Select optimal model based on task characteristics and budget.
    """
    # Calculate task complexity score
    complexity = estimate_complexity(task)

    # Check budget constraints
    remaining_budget = get_remaining_budget(layer, stage)

    # Get task priority
    priority = task.get("priority", "normal")

    # Select tier based on complexity and priority
    if priority == "critical" or complexity > 0.8:
        tier = "premium"
    elif complexity > 0.5 or remaining_budget > budget_threshold:
        tier = "balanced"
    elif layer >= 3 and stage in ["implementation", "testing"]:
        tier = "code_specialized"
    else:
        tier = "balanced"

    # Map tier to specific model
    model_map = {
        "premium": ["claude-sonnet-4.5", "gpt-4-turbo"],
        "balanced": ["claude-haiku", "gemini-flash-2"],
        "code_specialized": ["codestral", "qwen-coder"],
        "local": ["llama-3-70b", "mistral-22b"]
    }

    # Try primary, fall back if needed
    for model in model_map[tier]:
        if is_available(model) and within_budget(model, remaining_budget):
            return ModelConfig(
                model=model,
                max_tokens=get_max_tokens(complexity),
                temperature=get_temperature(stage)
            )

    # Last resort: cheapest available
    return ModelConfig(model="llama-3-8b", max_tokens=4000, temperature=0.7)

def estimate_complexity(task: dict) -> float:
    """
    Estimate task complexity (0.0-1.0) based on characteristics.
    """
    score = 0.0

    # File count
    file_count = len(task.get("artifacts", {}).get("files", []))
    score += min(file_count / 10, 0.3)

    # Constraints complexity
    constraints = task.get("constraints", [])
    score += min(len(constraints) / 20, 0.2)

    # Task description keywords
    description = task.get("task", "").lower()
    complex_keywords = ["refactor", "architecture", "debug", "security", "performance"]
    score += sum(0.1 for kw in complex_keywords if kw in description)

    # Previous failures
    if task.get("retry_count", 0) > 0:
        score += 0.2

    return min(score, 1.0)
```

### 3.3 Budget Management

**Per-Task Budgets:**
```python
# Example budget configuration
BUDGET_CONFIG = {
    "L0": {
        "daily_limit": 100.00,  # $100/day for L0 management
        "task_limits": {
            "planning": 10.00,
            "criticism": 5.00,
            "coordination": 3.00
        }
    },
    "L1": {
        "daily_limit": 200.00,  # $200/day for all L1 projects
        "task_limits": {
            "request": 5.00,
            "instructions": 5.00,
            "planning": 8.00,
            "design": 8.00
        }
    },
    "L2": {
        "daily_limit": 150.00,  # $150/day for all L2 features
        "task_limits": {
            "planning": 3.00,
            "design": 4.00,
            "implementation": 2.00
        }
    },
    "L3": {
        "daily_limit": 100.00,  # $100/day for all L3 components
        "task_limits": {
            "implementation": 0.50,
            "testing": 0.20,
            "fixing": 1.00
        }
    }
}

def check_budget(layer: int, stage: str, estimated_cost: float) -> bool:
    """Check if task is within budget limits."""
    config = BUDGET_CONFIG[f"L{layer}"]

    # Check daily limit
    today_spent = get_today_spending(layer)
    if today_spent + estimated_cost > config["daily_limit"]:
        return False

    # Check task-specific limit
    task_limit = config["task_limits"].get(stage, float('inf'))
    if estimated_cost > task_limit:
        return False

    return True
```

---

## 4. Quality-Cost Optimization Strategies

### 4.1 Cascading Fallback

Start cheap, escalate on failure:

```python
def execute_with_fallback(task: dict, layer: int, stage: str):
    """Try progressively more expensive models until success."""

    tiers = [
        ("code_specialized", 0.5),  # Cheap, 50% confidence
        ("balanced", 0.8),          # Moderate, 80% confidence
        ("premium", 0.95)           # Expensive, 95% confidence
    ]

    for tier, quality_threshold in tiers:
        model = select_model_from_tier(tier, layer, stage)
        result = execute_task(task, model)

        # Check quality
        quality_score = evaluate_quality(result, task)

        if quality_score >= quality_threshold:
            return result

        # Log failure and escalate
        log_failure(model, quality_score, task)

    # All tiers failed - escalate to human
    return escalate_to_human(task, "Quality threshold not met")
```

### 4.2 Parallel Ensemble

For critical tasks, run multiple models and vote:

```python
def ensemble_execution(task: dict, layer: int, stage: str):
    """Execute with multiple models and aggregate results."""

    if not task.get("critical", False):
        return execute_with_fallback(task, layer, stage)

    # Run in parallel with diverse models
    models = [
        "claude-sonnet-4.5",
        "gpt-4-turbo",
        "gemini-pro-2"
    ]

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(execute_task, task, model)
            for model in models
        ]
        results = [f.result() for f in futures]

    # Aggregate (e.g., majority vote, most confident, etc.)
    return aggregate_results(results, strategy="best_quality")
```

### 4.3 Caching and Deduplication

Avoid redundant expensive calls:

```python
def execute_with_cache(task: dict, model: str):
    """Check cache before executing expensive model calls."""

    # Create cache key from task content
    cache_key = hash_task(task, model)

    # Check cache
    cached = get_from_cache(cache_key)
    if cached and not task.get("force_fresh", False):
        log_cache_hit(cache_key)
        return cached

    # Execute and cache
    result = execute_task(task, model)
    store_in_cache(cache_key, result, ttl=3600)  # 1 hour TTL

    return result

def hash_task(task: dict, model: str) -> str:
    """Create deterministic hash of task content."""
    relevant_fields = {
        "task": task.get("task"),
        "constraints": sorted(task.get("constraints", [])),
        "artifacts": task.get("artifacts", {}),
        "model": model
    }
    return hashlib.sha256(
        json.dumps(relevant_fields, sort_keys=True).encode()
    ).hexdigest()
```

---

## 5. Model-Specific Optimizations

### 5.1 Claude Sonnet 4.5

**When to Use:**
- Complex reasoning, architecture decisions
- Multi-file refactors
- Security and correctness-critical code

**Optimization Tips:**
- Use extended thinking for complex problems
- Leverage system prompts heavily (re-injected every call)
- Keep context focused - trim irrelevant history

### 5.2 Codestral / Qwen-Coder

**When to Use:**
- Single-file implementation
- Test generation
- Code formatting and simple refactors

**Optimization Tips:**
- Keep prompts concise and code-focused
- Provide clear examples for pattern matching
- Batch similar tasks together

### 5.3 Gemini Pro 2.0

**When to Use:**
- Long-context research and planning
- Web search and documentation synthesis
- Multi-turn dialogue (request/instructions)

**Optimization Tips:**
- Leverage large context window for full docs
- Use grounding for factual accuracy
- Suitable for parallel research tasks

### 5.4 Local Llama/Mistral

**When to Use:**
- Privacy-sensitive code
- High-volume batch tasks
- Prototyping and experimentation

**Optimization Tips:**
- Quantization (4-bit, 8-bit) for speed
- Batch inference for throughput
- Fine-tune on domain-specific code if possible

---

## 6. Monitoring and Continuous Optimization

### 6.1 Key Metrics

Track per model, layer, and stage:

- **Cost Metrics:**
  - Total spend per day/week/month
  - Cost per task by layer and stage
  - Cost per line of code generated
  - Budget utilization (actual vs allocated)

- **Quality Metrics:**
  - Task success rate (first attempt)
  - Retry/escalation rate
  - Code quality scores (linting, test pass rate)
  - Human review feedback

- **Performance Metrics:**
  - Latency (p50, p95, p99)
  - Throughput (tasks per hour)
  - Utilization (active vs idle time)

### 6.2 Optimization Loop

```python
def optimize_model_selection():
    """Periodically review and update model selection policy."""

    # Analyze last 30 days
    metrics = analyze_metrics(days=30)

    # Identify underperforming models
    for model in metrics["models"]:
        if model["success_rate"] < 0.7:
            # Consider replacing or escalating earlier
            update_policy(model["name"], action="escalate_threshold")

        if model["cost_per_task"] > expected_cost * 1.5:
            # Model is too expensive for results
            update_policy(model["name"], action="reduce_usage")

    # Identify opportunities to use cheaper models
    for layer_stage in metrics["layer_stages"]:
        if layer_stage["success_rate"] > 0.95:
            # Try cheaper model tier
            suggest_tier_downgrade(layer_stage["layer"], layer_stage["stage"])

    # Generate report
    generate_optimization_report(metrics)
```

---

## 7. Example Policies by Use Case

### 7.1 Startup / Cost-Conscious

```yaml
policy:
  default_tier: balanced
  premium_gates:
    - layer: 0
      stages: [planning, criticism]
    - priority: critical

  models:
    premium: [claude-haiku]
    balanced: [gemini-flash-2, codestral]
    code_specialized: [qwen-coder, starcoder2]
    local: [llama-3-8b]

  budgets:
    daily_total: 50.00
    emergency_reserve: 20.00
```

### 7.2 Enterprise / Quality-First

```yaml
policy:
  default_tier: premium
  cost_optimization: moderate

  models:
    premium: [claude-sonnet-4.5, gpt-4-turbo]
    balanced: [claude-haiku, gpt-4o-mini]
    code_specialized: [codestral]
    local: [llama-3-70b]

  budgets:
    daily_total: 1000.00
    L0_allocation: 30%
    L1_allocation: 40%
    L2_allocation: 20%
    L3_allocation: 10%

  quality_gates:
    - stage: implementation
      min_test_coverage: 80%
    - stage: security_review
      require_premium: true
```

### 7.3 Research / Experimentation

```yaml
policy:
  default_tier: local
  cloud_fallback: enabled

  models:
    premium: [claude-sonnet-4.5]  # rare use
    balanced: [gemini-flash-2]
    code_specialized: [codestral]
    local: [llama-3-70b, mistral-22b, qwen-coder]

  budgets:
    daily_total: 20.00
    local_preferred: true
    cloud_only_for:
      - complexity_score > 0.8
      - retry_count > 2
```

---

## 8. Summary

Effective model selection balances:
- **Quality**: Right model for task complexity
- **Cost**: Budget-aware routing and caching
- **Latency**: Fast models for interactive, slower for batch
- **Adaptability**: Continuous monitoring and optimization

The policy layer decouples architecture from model choices, allowing seamless updates as:
- New models are released
- Prices change
- Quality requirements evolve

Start with conservative policies, gather metrics, and optimize based on your actual patterns.
