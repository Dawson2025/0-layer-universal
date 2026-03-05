---
resource_id: "01104001-339b-4436-9432-67786386c7a9"
resource_type: "knowledge"
resource_name: "parallel_execution"
---
<!-- section_id: "da01e5d8-2b90-434e-82b9-0d2049d2894c" -->
## Parallel Execution Cookbook

This document provides concrete patterns and examples for parallelizing work across the AI manager hierarchy system.

It covers:
- When and how to parallelize tasks
- Workload decomposition strategies
- Synchronization and aggregation patterns
- Common pitfalls and solutions

---

<!-- section_id: "ddc82d29-336e-43f9-be00-e454bc81f669" -->
## 1. Parallelization Opportunities

<!-- section_id: "7074cbc1-e89e-4e7f-8dc5-0b53fc87b458" -->
### 1.1 Where to Parallelize

**Layer 2 (Feature Level):**
- Decompose feature into independent components
- Each component becomes a parallel L3 task

**Layer 3 (Component Level):**
- Split component into sub-components (L4)
- Parallelize UI, logic, tests, docs

**Stage Level:**
- Some stages can run in parallel:
  - Implementation + documentation
  - Multiple test suites
  - Independent fixes

<!-- section_id: "514906b0-2273-4377-86aa-19fa6b9bc2ec" -->
### 1.2 When NOT to Parallelize

**Sequential Dependencies:**
- Design must complete before implementation
- Implementation before testing
- Testing before fixing

**Shared State:**
- Multiple agents modifying same files
- Database migrations
- Configuration changes

**Cost Constraints:**
- Near budget limits
- API rate limits
- Limited worker capacity

---

<!-- section_id: "16241fd0-3969-4dab-82cf-787aa4ff8e0b" -->
## 2. Decomposition Strategies

<!-- section_id: "607f98b3-1fbf-4cc5-902e-f55dc1f44842" -->
### 2.1 Feature to Components

```python
def decompose_feature_to_components(feature_handoff):
    """Decompose feature into parallelizable components."""

    # Example: Auth System feature
    components = {
        "login": {
            "task": "Implement login component",
            "files": ["LoginForm.tsx", "useLogin.ts", "login.test.tsx"],
            "dependencies": []  # No deps, can start immediately
        },
        "registration": {
            "task": "Implement registration component",
            "files": ["RegisterForm.tsx", "useRegister.ts", "register.test.tsx"],
            "dependencies": []  # Independent
        },
        "password-reset": {
            "task": "Implement password reset flow",
            "files": ["ResetForm.tsx", "useReset.ts", "reset.test.tsx"],
            "dependencies": []  # Independent
        },
        "auth-api": {
            "task": "Implement authentication API handlers",
            "files": ["auth.routes.ts", "auth.controller.ts", "auth.service.ts"],
            "dependencies": []  # Backend, independent of UI
        },
        "auth-tests": {
            "task": "Write integration tests for auth system",
            "files": ["auth.integration.test.ts"],
            "dependencies": ["login", "registration", "password-reset", "auth-api"]  # Needs all components
        },
        "auth-docs": {
            "task": "Write authentication documentation",
            "files": ["docs/authentication.md"],
            "dependencies": []  # Can start early
        }
    }

    return components

def create_component_handoffs(components, feature_handoff):
    """Create handoff for each component."""

    handoffs = []

    for component_id, component_spec in components.items():
        handoff = {
            "schemaVersion": "1.0.0",
            "id": f"{feature_handoff['id']}-{component_id}",
            "layer": 3,
            "stage": "implementation",
            "task": component_spec["task"],
            "constraints": feature_handoff["constraints"],
            "artifacts": {
                "target_files": component_spec["files"]
            },
            "dependencies": component_spec["dependencies"],
            "parent_id": feature_handoff["id"]
        }

        handoffs.append((component_id, handoff))

    return handoffs
```

<!-- section_id: "0d3952ee-ac75-4129-807a-dfe1f38816e6" -->
### 2.2 Dependency Graph

```python
import networkx as nx

def build_dependency_graph(components):
    """Build DAG of component dependencies."""

    G = nx.DiGraph()

    # Add nodes
    for component_id in components:
        G.add_node(component_id)

    # Add edges (dependencies)
    for component_id, spec in components.items():
        for dep in spec.get("dependencies", []):
            G.add_edge(dep, component_id)  # dep must complete before component_id

    # Check for cycles
    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("Circular dependencies detected!")

    return G

def get_parallel_batches(dependency_graph):
    """Get components grouped into parallel execution batches."""

    # Topological sort gives correct execution order
    batches = []

    # Work with a copy
    G = dependency_graph.copy()

    while G.nodes():
        # Find nodes with no incoming edges (no unmet dependencies)
        ready = [n for n in G.nodes() if G.in_degree(n) == 0]

        if not ready:
            raise ValueError("Cycle detected in dependency graph")

        # This batch can execute in parallel
        batches.append(ready)

        # Remove completed nodes
        G.remove_nodes_from(ready)

    return batches

# Example usage
components = decompose_feature_to_components(feature_handoff)
dep_graph = build_dependency_graph(components)
batches = get_parallel_batches(dep_graph)

# Output:
# Batch 0 (parallel): ["login", "registration", "password-reset", "auth-api", "auth-docs"]
# Batch 1 (after batch 0): ["auth-tests"]
```

---

<!-- section_id: "36add50e-020d-4875-8881-f44810f0163c" -->
## 3. Parallel Execution Patterns

<!-- section_id: "869c1e93-fde6-45bc-b8ba-b520feba3b7b" -->
### 3.1 Fork-Join Pattern

```python
import concurrent.futures

def execute_parallel_batch(batch, handoffs, layer, stage):
    """Execute all components in batch in parallel, then join."""

    results = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(batch)) as executor:
        # Fork: Submit all tasks
        futures = {
            executor.submit(execute_component, handoffs[comp_id], layer, stage): comp_id
            for comp_id in batch
        }

        # Join: Wait for all to complete
        for future in concurrent.futures.as_completed(futures):
            comp_id = futures[future]

            try:
                result = future.result()
                results[comp_id] = result
            except Exception as e:
                print(f"Component {comp_id} failed: {e}")
                results[comp_id] = {"status": "failed", "error": str(e)}

    return results

def execute_with_dependencies(batches, handoffs, layer, stage):
    """Execute batches sequentially, components within batch in parallel."""

    all_results = {}

    for batch_idx, batch in enumerate(batches):
        print(f"Executing batch {batch_idx}: {batch}")

        # Execute this batch in parallel
        batch_results = execute_parallel_batch(batch, handoffs, layer, stage)

        all_results.update(batch_results)

        # Check for failures
        failures = [comp for comp, result in batch_results.items()
                   if result.get("status") == "failed"]

        if failures:
            print(f"Batch {batch_idx} had failures: {failures}")
            # Decide: continue or abort?
            if len(failures) > len(batch) * 0.5:  # More than 50% failed
                print("Too many failures, aborting remaining batches")
                break

    return all_results
```

<!-- section_id: "b0ee1af2-cc4a-4656-a3d9-a1ec713405f3" -->
### 3.2 Worker Pool Pattern

```python
from multiprocessing import Pool, Queue
import queue

def worker_process(task_queue, result_queue, worker_id):
    """Worker process that consumes tasks from queue."""

    while True:
        try:
            # Get task (with timeout to allow graceful shutdown)
            task = task_queue.get(timeout=5)

            if task is None:  # Poison pill
                break

            # Execute task
            result = execute_task(task)

            # Put result
            result_queue.put({
                "task_id": task["id"],
                "worker_id": worker_id,
                "result": result
            })

        except queue.Empty:
            continue
        except Exception as e:
            result_queue.put({
                "task_id": task.get("id"),
                "worker_id": worker_id,
                "error": str(e)
            })

def execute_with_worker_pool(tasks, num_workers=4):
    """Execute tasks using worker pool."""

    task_queue = Queue()
    result_queue = Queue()

    # Start workers
    workers = []
    for i in range(num_workers):
        p = Process(target=worker_process, args=(task_queue, result_queue, i))
        p.start()
        workers.append(p)

    # Enqueue tasks
    for task in tasks:
        task_queue.put(task)

    # Send poison pills
    for _ in range(num_workers):
        task_queue.put(None)

    # Collect results
    results = []
    for _ in range(len(tasks)):
        result = result_queue.get()
        results.append(result)

    # Wait for workers
    for p in workers:
        p.join()

    return results
```

<!-- section_id: "a385d324-6c36-45f6-9f14-7dfacb7b0087" -->
### 3.3 Async/Await Pattern (Python)

```python
import asyncio

async def execute_component_async(component_id, handoff, layer, stage):
    """Execute component asynchronously."""

    print(f"Starting {component_id}")

    # Simulate work (replace with actual CLI call)
    await asyncio.sleep(random.uniform(5, 15))

    result = {
        "component_id": component_id,
        "status": "completed",
        "duration": random.uniform(5, 15)
    }

    print(f"Completed {component_id}")

    return result

async def execute_batch_async(batch, handoffs, layer, stage):
    """Execute batch asynchronously."""

    # Create tasks
    tasks = [
        execute_component_async(comp_id, handoffs[comp_id], layer, stage)
        for comp_id in batch
    ]

    # Execute all in parallel
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Process results
    batch_results = {}
    for comp_id, result in zip(batch, results):
        if isinstance(result, Exception):
            batch_results[comp_id] = {"status": "failed", "error": str(result)}
        else:
            batch_results[comp_id] = result

    return batch_results

# Usage
async def main():
    batches = get_parallel_batches(dependency_graph)

    for batch in batches:
        results = await execute_batch_async(batch, handoffs, layer=3, stage="implementation")
        print(f"Batch complete: {results}")

asyncio.run(main())
```

---

<!-- section_id: "1bde52b0-4aa3-4668-b818-00c7a3f0dd2f" -->
## 4. Synchronization and Aggregation

<!-- section_id: "a74171f7-4894-48e7-9cd2-35cf2be3ef42" -->
### 4.1 Result Aggregation

```python
def aggregate_component_results(component_results, feature_handoff):
    """Aggregate component results into feature-level handoff."""

    # Collect all artifacts
    all_artifacts = {
        "files_created": [],
        "files_modified": [],
        "tests_added": []
    }

    for comp_id, result in component_results.items():
        all_artifacts["files_created"].extend(result.get("files_created", []))
        all_artifacts["files_modified"].extend(result.get("files_modified", []))
        all_artifacts["tests_added"].extend(result.get("tests_added", []))

    # Check if all components succeeded
    all_succeeded = all(
        result.get("status") == "completed"
        for result in component_results.values()
    )

    # Aggregate metrics
    total_cost = sum(result.get("cost", 0) for result in component_results.values())
    total_duration = max(result.get("duration", 0) for result in component_results.values())  # Parallel, so max not sum

    # Create aggregated handoff
    aggregated = {
        "schemaVersion": "1.0.0",
        "id": feature_handoff["id"] + "-aggregated",
        "status": "completed" if all_succeeded else "partial",
        "artifacts": all_artifacts,
        "component_results": component_results,
        "metrics": {
            "total_cost": total_cost,
            "total_duration": total_duration,
            "components_completed": sum(1 for r in component_results.values() if r.get("status") == "completed"),
            "components_failed": sum(1 for r in component_results.values() if r.get("status") == "failed")
        }
    }

    return aggregated
```

<!-- section_id: "d6d1da9e-97a3-479b-9147-af2761464673" -->
### 4.2 Barrier Synchronization

```python
import threading

class Barrier:
    """Synchronization primitive for parallel workers."""

    def __init__(self, n_workers):
        self.n_workers = n_workers
        self.count = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def wait(self):
        """Wait for all workers to reach barrier."""
        with self.condition:
            self.count += 1

            if self.count == self.n_workers:
                # Last worker, wake everyone
                self.count = 0
                self.condition.notify_all()
            else:
                # Wait for others
                self.condition.wait()

# Usage
barrier = Barrier(n_workers=5)

def worker_with_barrier(task, barrier):
    """Worker that synchronizes at barrier."""

    # Phase 1: Execute component
    result = execute_component(task)

    # Wait for all workers to finish phase 1
    barrier.wait()

    # Phase 2: Integration test (requires all components ready)
    integration_result = run_integration_test(result)

    return integration_result
```

---

<!-- section_id: "b5add8c6-a078-43f3-98ce-a8de872d8a5b" -->
## 5. Error Handling and Partial Failures

<!-- section_id: "3c7e3187-7523-4f8b-b0d7-052fa2721feb" -->
### 5.1 Graceful Degradation

```python
def execute_with_partial_failure_tolerance(batch, handoffs, layer, stage):
    """Execute batch, continuing even if some components fail."""

    results = {}
    futures = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit all tasks
        for comp_id in batch:
            future = executor.submit(execute_component, handoffs[comp_id], layer, stage)
            futures[future] = comp_id

        # Collect results as they complete
        for future in concurrent.futures.as_completed(futures):
            comp_id = futures[future]

            try:
                result = future.result()
                results[comp_id] = result

            except Exception as e:
                # Log error but continue with other components
                print(f"Component {comp_id} failed: {e}")
                results[comp_id] = {
                    "status": "failed",
                    "error": str(e),
                    "recoverable": is_recoverable_error(e)
                }

    # Decide what to do based on failures
    failed = [c for c, r in results.items() if r.get("status") == "failed"]

    if not failed:
        return results, "full_success"

    elif len(failed) < len(batch) * 0.5:
        # Less than 50% failed - partial success
        print(f"Partial success: {len(failed)}/{len(batch)} components failed")
        return results, "partial_success"

    else:
        # Too many failures
        print(f"Batch failed: {len(failed)}/{len(batch)} components failed")
        return results, "batch_failed"
```

<!-- section_id: "d0c2598f-4b84-4d53-be3d-54e04d0bb763" -->
### 5.2 Retry Failed Components

```python
def retry_failed_components(results, handoffs, layer, stage, max_retries=3):
    """Retry failed components with backoff."""

    failed = {
        comp_id: result
        for comp_id, result in results.items()
        if result.get("status") == "failed" and result.get("recoverable")
    }

    for attempt in range(max_retries):
        if not failed:
            break

        print(f"Retrying {len(failed)} failed components (attempt {attempt + 1})")

        # Wait before retry
        time.sleep(2 ** attempt)

        # Retry in parallel
        retry_results = execute_parallel_batch(
            list(failed.keys()),
            handoffs,
            layer,
            stage
        )

        # Update results
        for comp_id, result in retry_results.items():
            results[comp_id] = result

            # Remove from failed if now succeeded
            if result.get("status") == "completed":
                del failed[comp_id]

    return results
```

---

<!-- section_id: "159ad531-0b02-42e8-aa77-25ecd731f73e" -->
## 6. Resource Management

<!-- section_id: "4b1e12d5-9942-4b69-991d-e19a31a80514" -->
### 6.1 Concurrency Limiting

```python
from threading import Semaphore

class ConcurrencyLimiter:
    """Limit number of concurrent tasks."""

    def __init__(self, max_concurrent):
        self.semaphore = Semaphore(max_concurrent)

    def execute_with_limit(self, tasks, executor_func):
        """Execute tasks with concurrency limit."""

        def limited_executor(task):
            with self.semaphore:
                return executor_func(task)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(limited_executor, task) for task in tasks]
            results = [f.result() for f in futures]

        return results

# Usage: Limit to 4 concurrent model API calls
limiter = ConcurrencyLimiter(max_concurrent=4)
results = limiter.execute_with_limit(tasks, execute_component)
```

<!-- section_id: "b5285169-690e-4221-ad72-0ecd264ae20a" -->
### 6.2 Rate Limiting

```python
import time
from collections import deque

class RateLimiter:
    """Token bucket rate limiter."""

    def __init__(self, rate_per_second):
        self.rate = rate_per_second
        self.timestamps = deque()

    def acquire(self):
        """Wait if necessary to stay within rate limit."""

        now = time.time()

        # Remove timestamps older than 1 second
        while self.timestamps and self.timestamps[0] < now - 1:
            self.timestamps.popleft()

        # Check if we're at limit
        if len(self.timestamps) >= self.rate:
            # Wait until oldest timestamp expires
            sleep_time = 1 - (now - self.timestamps[0])
            if sleep_time > 0:
                time.sleep(sleep_time)

            # Recurse to recheck
            return self.acquire()

        # Add timestamp
        self.timestamps.append(now)

# Usage: Limit to 60 API calls per second
rate_limiter = RateLimiter(rate_per_second=60)

def execute_with_rate_limit(task):
    rate_limiter.acquire()
    return execute_component(task)
```

---

<!-- section_id: "65db01b1-e46d-4174-8fc6-433fb19e8857" -->
## 7. Performance Optimization

<!-- section_id: "3e968227-80af-486d-9fc7-e3a8f80e5aa4" -->
### 7.1 Optimal Parallelism

```python
def calculate_optimal_workers(tasks, avg_task_duration, budget, cost_per_task):
    """Calculate optimal number of parallel workers."""

    # Cost constraint
    max_workers_by_budget = int(budget / cost_per_task)

    # Latency constraint (Amdahl's Law)
    # With N workers, completion time = avg_task_duration / N (if fully parallelizable)
    target_completion_time = avg_task_duration * 0.2  # Want 5x speedup
    max_workers_by_latency = int(avg_task_duration / target_completion_time)

    # Resource constraint (API rate limits, machine capacity)
    max_workers_by_resources = 20  # Example limit

    # Take minimum
    optimal = min(
        max_workers_by_budget,
        max_workers_by_latency,
        max_workers_by_resources,
        len(tasks)  # No point in more workers than tasks
    )

    return max(optimal, 1)  # At least 1 worker
```

<!-- section_id: "24685ec3-84ff-4e61-a143-12459e2ad582" -->
### 7.2 Work Stealing

```python
from queue import Queue
import threading

class WorkStealingPool:
    """Worker pool where idle workers steal work from busy workers."""

    def __init__(self, n_workers):
        self.n_workers = n_workers
        self.worker_queues = [Queue() for _ in range(n_workers)]
        self.global_queue = Queue()
        self.results = []
        self.lock = threading.Lock()

    def worker(self, worker_id):
        """Worker that processes its queue and steals from others."""

        my_queue = self.worker_queues[worker_id]

        while True:
            task = None

            # Try my queue first
            if not my_queue.empty():
                task = my_queue.get()

            # Try global queue
            elif not self.global_queue.empty():
                task = self.global_queue.get()

            # Try stealing from other workers
            else:
                for other_id in range(self.n_workers):
                    if other_id != worker_id and not self.worker_queues[other_id].empty():
                        task = self.worker_queues[other_id].get()
                        break

            if task is None:
                break  # No more work

            # Execute task
            result = execute_component(task)

            with self.lock:
                self.results.append(result)

    def execute(self, tasks):
        """Execute tasks using work stealing."""

        # Distribute tasks to worker queues
        for i, task in enumerate(tasks):
            self.worker_queues[i % self.n_workers].put(task)

        # Start workers
        threads = []
        for i in range(self.n_workers):
            t = threading.Thread(target=self.worker, args=(i,))
            t.start()
            threads.append(t)

        # Wait for completion
        for t in threads:
            t.join()

        return self.results
```

---

<!-- section_id: "56cedcad-3eee-49f6-8f24-0df702023678" -->
## 8. Summary

Effective parallelization requires:

1. **Smart Decomposition**: Break work into independent units
2. **Dependency Management**: Respect dependencies, parallelize where possible
3. **Appropriate Patterns**: Fork-join, worker pools, async/await
4. **Error Handling**: Graceful degradation, retries, partial failures
5. **Resource Management**: Concurrency limits, rate limits, quotas
6. **Performance Tuning**: Optimal worker count, work stealing

The key is finding the right balance between parallelism (speed), cost (more workers = more expense), and complexity (harder to debug).

Start conservative, measure, then optimize.
