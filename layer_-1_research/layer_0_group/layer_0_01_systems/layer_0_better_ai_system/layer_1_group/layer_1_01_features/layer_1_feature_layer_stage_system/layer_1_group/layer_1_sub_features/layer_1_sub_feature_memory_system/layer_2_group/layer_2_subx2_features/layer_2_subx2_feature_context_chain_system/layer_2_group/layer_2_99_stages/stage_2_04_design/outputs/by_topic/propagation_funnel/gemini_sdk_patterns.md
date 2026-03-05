---
resource_id: "66c0a2ed-4acc-43bd-aadd-d9ac45ac0eab"
resource_type: "output"
resource_name: "gemini_sdk_patterns"
---
# Gemini SDK Patterns & Best Practices

This document covers production-ready patterns, common pitfalls, and optimizations for using Gemini in real applications.

---

<!-- section_id: "b8dfdb7c-44e8-40fb-8429-69b16651a894" -->
## 1. Client Initialization Patterns

<!-- section_id: "cd26affc-6695-4c92-8213-060f638aef11" -->
### Pattern 1.1: Singleton Client (Recommended)

In production, create one client instance and reuse it:

```python
# config.py
from google import genai

# Global client instance
_client = None

def get_client():
    """Get or create singleton client"""
    global _client
    if _client is None:
        _client = genai.Client()  # Uses GEMINI_API_KEY env var
    return _client

# main.py
from config import get_client

client = get_client()
response = client.models.generate_content(...)
response2 = client.models.generate_content(...)  # Reuses client
```

**Benefits**:
- Single HTTP connection pool
- Better resource utilization
- Faster subsequent requests

<!-- section_id: "7840c013-f25c-4706-91bd-da9cb3e42544" -->
### Pattern 1.2: Environment-Based Configuration

```python
import os
from google import genai
from google.genai.types import HttpOptions

def create_client(environment="production"):
    """Create client with environment-specific settings"""

    config = {
        "development": {
            "timeout": 30,
            "api_version": "v1beta",
        },
        "production": {
            "timeout": 60,
            "api_version": "v1",
        },
        "testing": {
            "timeout": 10,
            "api_version": "v1beta",
        }
    }

    settings = config.get(environment, config["production"])

    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
        http_options=HttpOptions(
            timeout=settings["timeout"],
            api_version=settings["api_version"]
        )
    )

# Usage
if __name__ == "__main__":
    env = os.getenv("APP_ENV", "production")
    client = create_client(env)
```

<!-- section_id: "cd01f96f-50d4-44f6-99af-f8f2ad490ce6" -->
### Pattern 1.3: Context Manager Pattern

```python
from contextlib import contextmanager
from google import genai

@contextmanager
def gemini_client():
    """Context manager for Gemini client"""
    client = genai.Client()
    try:
        yield client
    finally:
        # Cleanup if needed
        pass

# Usage
with gemini_client() as client:
    response = client.models.generate_content(...)
    # Client automatically cleaned up
```

---

<!-- section_id: "5cf2f083-d00b-4987-81c8-93ed1a1ecd3f" -->
## 2. Request Configuration Patterns

<!-- section_id: "0c65e65a-2984-41a9-afdb-5dee0c3b649e" -->
### Pattern 2.1: Config Builder

```python
from google.genai.types import GenerateContentConfig

class GenerationConfig:
    """Builder pattern for generation config"""

    def __init__(self):
        self._config = {}

    def with_temperature(self, temp):
        self._config["temperature"] = temp
        return self

    def with_max_tokens(self, tokens):
        self._config["max_output_tokens"] = tokens
        return self

    def with_system_instruction(self, instruction):
        self._config["system_instruction"] = instruction
        return self

    def with_safety_settings(self, settings):
        self._config["safety_settings"] = settings
        return self

    def build(self):
        return GenerateContentConfig(**self._config)

# Usage
config = (GenerationConfig()
    .with_temperature(0.7)
    .with_max_tokens(500)
    .with_system_instruction("You are helpful")
    .build())

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Your prompt",
    config=config
)
```

<!-- section_id: "2b9e01b9-708a-4c5d-8a3d-8baeaa3fd06c" -->
### Pattern 2.2: Preset Configurations

```python
from dataclasses import dataclass
from google.genai.types import GenerateContentConfig

@dataclass
class GenerationPreset:
    """Named generation configurations"""
    name: str
    temperature: float
    top_p: float
    max_tokens: int

# Define presets
PRESETS = {
    "deterministic": GenerationPreset(
        name="deterministic",
        temperature=0.2,
        top_p=0.8,
        max_tokens=1000
    ),
    "balanced": GenerationPreset(
        name="balanced",
        temperature=0.7,
        top_p=0.9,
        max_tokens=1500
    ),
    "creative": GenerationPreset(
        name="creative",
        temperature=1.5,
        top_p=0.95,
        max_tokens=2000
    ),
}

def get_preset(name="balanced"):
    """Get preset configuration"""
    preset = PRESETS.get(name, PRESETS["balanced"])
    return GenerateContentConfig(
        temperature=preset.temperature,
        top_p=preset.top_p,
        max_output_tokens=preset.max_tokens,
    )

# Usage
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Your prompt",
    config=get_preset("creative")
)
```

---

<!-- section_id: "5c7e2157-704f-43d2-b77f-d14c6b184db9" -->
## 3. Chat/Session Patterns

<!-- section_id: "b69dd367-77be-431c-bd9e-7b46de07c48f" -->
### Pattern 3.1: Typed Chat Handler

```python
from typing import Optional, List
from dataclasses import dataclass
from google import genai

@dataclass
class ChatMessage:
    role: str
    text: str

class ChatHandler:
    """Strongly-typed chat management"""

    def __init__(self, model="gemini-2.5-flash"):
        self.model = model
        self.chat = None
        self.message_history: List[ChatMessage] = []

    def start_chat(self):
        """Initialize new chat"""
        self.chat = client.chats.create(model=self.model)
        self.message_history = []

    def send_message(self, text: str) -> str:
        """Send message and track history"""
        if self.chat is None:
            self.start_chat()

        response = self.chat.send_message(text)

        self.message_history.append(ChatMessage("user", text))
        self.message_history.append(ChatMessage("assistant", response.text))

        return response.text

    def get_history(self) -> List[ChatMessage]:
        return self.message_history

    def clear_history(self):
        """Start fresh conversation"""
        self.chat = None
        self.message_history = []

# Usage
handler = ChatHandler()
handler.start_chat()

response1 = handler.send_message("What is photosynthesis?")
response2 = handler.send_message("Explain in simpler terms")

print(f"Conversation history: {len(handler.get_history())} messages")
```

<!-- section_id: "3f72fbf7-e984-48a8-aa55-02ae0bc99db9" -->
### Pattern 3.2: Conversation with Rollback

```python
from copy import deepcopy

class RollbackChat:
    """Chat with ability to rollback to previous state"""

    def __init__(self, model="gemini-2.5-flash"):
        self.model = model
        self.chat = None
        self.checkpoints = {}

    def start_chat(self):
        self.chat = client.chats.create(model=self.model)

    def checkpoint(self, name: str):
        """Save conversation state"""
        self.checkpoints[name] = {
            "history_len": len(self.chat.history),
        }
        print(f"Checkpoint '{name}' created")

    def rollback(self, name: str):
        """Rollback to checkpoint"""
        if name not in self.checkpoints:
            raise ValueError(f"Unknown checkpoint: {name}")

        target_len = self.checkpoints[name]["history_len"]

        # Create new chat with truncated history
        new_history = self.chat.history[:target_len]
        self.chat = client.chats.create(
            model=self.model,
            history=[
                {"role": msg.role, "parts": msg.parts}
                for msg in new_history
            ]
        )
        print(f"Rolled back to checkpoint '{name}'")

    def send_message(self, text: str) -> str:
        if self.chat is None:
            self.start_chat()
        return self.chat.send_message(text).text

# Usage
chat = RollbackChat()
chat.start_chat()

response1 = chat.send_message("What is AI?")
chat.checkpoint("after_ai_intro")

response2 = chat.send_message("Go deeper")
response3 = chat.send_message("Even deeper")

# Go back
chat.rollback("after_ai_intro")
response4 = chat.send_message("Different direction")  # Continues from checkpoint
```

---

<!-- section_id: "5865cac6-c6ca-450f-83f1-5c31f965f3c2" -->
## 4. Error Handling Patterns

<!-- section_id: "6f7714ba-992d-4180-a73e-7d61a48c88eb" -->
### Pattern 4.1: Retry with Exponential Backoff

```python
import time
import random
from functools import wraps
from google import genai

def retry_with_backoff(max_retries=3, base_delay=1):
    """Decorator for automatic retry with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Check if retryable error
                    if attempt == max_retries - 1:
                        raise

                    error_str = str(e)
                    if any(code in error_str for code in ["429", "503", "504"]):
                        # Exponential backoff with jitter
                        delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                        print(f"Retry {attempt + 1}/{max_retries} after {delay:.1f}s")
                        time.sleep(delay)
                    else:
                        raise
            return None
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=3, base_delay=1)
def generate_text(client, prompt):
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

response = generate_text(client, "Explain quantum computing")
```

<!-- section_id: "24162bfc-b0c4-4dfc-950a-d0d3cb47cdce" -->
### Pattern 4.2: Circuit Breaker Pattern

```python
from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, Any

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    """Prevent cascading failures with circuit breaker pattern"""

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: int = 60,
        name: str = "default"
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.name = name

        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with circuit breaker protection"""

        if self.state == CircuitState.OPEN:
            if self._should_attempt_recovery():
                self.state = CircuitState.HALF_OPEN
                print(f"[{self.name}] Circuit HALF-OPEN, attempting recovery")
            else:
                raise Exception(f"Circuit breaker {self.name} is OPEN")

        try:
            result = func(*args, **kwargs)

            # Success
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
                print(f"[{self.name}] Circuit CLOSED, recovered")

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = datetime.now()

            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                print(f"[{self.name}] Circuit OPEN after {self.failure_count} failures")

            raise

    def _should_attempt_recovery(self) -> bool:
        if self.last_failure_time is None:
            return False

        elapsed = datetime.now() - self.last_failure_time
        return elapsed.total_seconds() >= self.recovery_timeout

    def reset(self):
        """Manual reset"""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None

# Usage
breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=60, name="gemini")

def generate_with_breaker(prompt):
    def _gen():
        return client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
    return breaker.call(_gen)

# Will open circuit after 3 failures, then try recovery every 60s
for i in range(10):
    try:
        response = generate_with_breaker("Test prompt")
        print(f"Request {i+1}: Success")
    except Exception as e:
        print(f"Request {i+1}: Failed - {e}")
    time.sleep(1)
```

---

<!-- section_id: "b3a6c1c5-967d-4cf8-bb54-61264d3d5ec3" -->
## 5. File Handling Patterns

<!-- section_id: "399a359f-b8f6-49f8-9973-8cdb33b4bc9a" -->
### Pattern 5.1: File Manager with Cleanup

```python
import os
from pathlib import Path
from typing import Optional
from google import genai

class FileManager:
    """Manage Gemini file uploads with automatic cleanup"""

    def __init__(self, client, cache_dir: Optional[str] = None):
        self.client = client
        self.cache_dir = Path(cache_dir or ".")
        self.uploaded_files = {}

    def upload(self, filepath: str, display_name: Optional[str] = None) -> str:
        """Upload file and track"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        uploaded = self.client.files.upload(
            file=filepath,
            config={
                "displayName": display_name or Path(filepath).name,
                "mimeType": self._get_mime_type(filepath),
            }
        )

        self.uploaded_files[filepath] = uploaded.name
        print(f"Uploaded: {filepath} -> {uploaded.name}")

        return uploaded.name

    def cleanup(self, filepath: Optional[str] = None):
        """Delete uploaded files"""
        if filepath:
            if filepath in self.uploaded_files:
                file_id = self.uploaded_files[filepath]
                self.client.files.delete(name=file_id)
                del self.uploaded_files[filepath]
                print(f"Deleted: {filepath}")
        else:
            # Cleanup all
            for filepath, file_id in list(self.uploaded_files.items()):
                self.client.files.delete(name=file_id)
                del self.uploaded_files[filepath]
            print("Cleaned up all files")

    def get_file(self, filepath: str):
        """Get file object"""
        if filepath not in self.uploaded_files:
            raise ValueError(f"File not tracked: {filepath}")
        return self.client.files.get(name=self.uploaded_files[filepath])

    def list_files(self):
        """List uploaded files"""
        return list(self.uploaded_files.keys())

    @staticmethod
    def _get_mime_type(filepath: str) -> str:
        ext = Path(filepath).suffix.lower()
        types = {
            ".pdf": "application/pdf",
            ".txt": "text/plain",
            ".md": "text/markdown",
            ".json": "application/json",
            ".jpg": "image/jpeg",
            ".png": "image/png",
            ".mp3": "audio/mpeg",
            ".mp4": "video/mp4",
        }
        return types.get(ext, "application/octet-stream")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

# Usage
with FileManager(client) as fm:
    fm.upload("document.pdf")
    fm.upload("image.png")
    # Files auto-deleted on exit
```

<!-- section_id: "b59ccfc8-5f22-49b7-88e4-63c816af8d1a" -->
### Pattern 5.2: Batch File Processing

```python
from typing import List
from pathlib import Path

class BatchFileProcessor:
    """Process multiple files efficiently"""

    def __init__(self, client, batch_size=5):
        self.client = client
        self.batch_size = batch_size

    def process_files(
        self,
        filepaths: List[str],
        prompt_template: str
    ) -> dict:
        """Process multiple files with same analysis"""
        results = {}

        for i, filepath in enumerate(filepaths):
            # Upload
            file_obj = self.client.files.upload(file=filepath)

            # Generate
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[file_obj, "\n\n", prompt_template]
            )

            results[filepath] = response.text

            # Cleanup
            self.client.files.delete(name=file_obj.name)

            print(f"Processed {i+1}/{len(filepaths)}: {filepath}")

        return results

# Usage
processor = BatchFileProcessor(client)
results = processor.process_files(
    filepaths=["doc1.pdf", "doc2.pdf", "doc3.pdf"],
    prompt_template="Summarize this document in 100 words"
)

for filepath, summary in results.items():
    print(f"{filepath}: {summary}")
```

---

<!-- section_id: "c4b9951e-92d4-42a0-bd3f-ff43170aee9a" -->
## 6. Caching Patterns

<!-- section_id: "2a82817d-158f-4376-a8bd-b1564e3f0a87" -->
### Pattern 6.1: Cache Manager

```python
from datetime import timedelta
from typing import Optional

class CacheManager:
    """Manage context caches efficiently"""

    def __init__(self, client):
        self.client = client
        self.caches = {}

    def create_cache(
        self,
        name: str,
        contents: str,
        ttl_hours: int = 1,
        display_name: Optional[str] = None
    ) -> str:
        """Create and track cache"""
        cache = self.client.caches.create(
            display_name=display_name or name,
            model="gemini-2.5-flash",
            contents=contents,
            ttl=timedelta(hours=ttl_hours),
        )

        self.caches[name] = {
            "id": cache.name,
            "display_name": cache.display_name,
            "expires_at": cache.expiration_time,
        }

        print(f"Created cache '{name}' (expires in {ttl_hours}h)")
        return cache.name

    def get_cache(self, name: str) -> Optional[str]:
        """Get cache ID"""
        return self.caches.get(name, {}).get("id")

    def extend_cache(self, name: str, ttl_hours: int = 1):
        """Extend cache TTL"""
        if name not in self.caches:
            raise ValueError(f"Unknown cache: {name}")

        cache_id = self.caches[name]["id"]
        self.client.caches.update(
            name=cache_id,
            ttl=timedelta(hours=ttl_hours)
        )
        print(f"Extended cache '{name}' TTL to {ttl_hours}h")

    def delete_cache(self, name: str):
        """Delete cache"""
        if name in self.caches:
            cache_id = self.caches[name]["id"]
            self.client.caches.delete(name=cache_id)
            del self.caches[name]
            print(f"Deleted cache '{name}'")

    def list_caches(self):
        """List all managed caches"""
        return list(self.caches.keys())

    def generate_with_cache(self, cache_name: str, prompt: str) -> str:
        """Generate using cache"""
        cache_id = self.get_cache(cache_name)
        if not cache_id:
            raise ValueError(f"Cache not found: {cache_name}")

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            cache_control={"cache_resource_name": cache_id}
        )

        # Log cache effectiveness
        metadata = response.usage_metadata
        if metadata.cached_content_input_token_count > 0:
            savings = (metadata.cached_content_input_token_count /
                      (metadata.cached_content_input_token_count +
                       metadata.input_token_count) * 100)
            print(f"Cache hit! Saved ~{savings:.0f}% on tokens")

        return response.text

# Usage
cache_mgr = CacheManager(client)

# Create cache
cache_mgr.create_cache(
    "large_doc",
    contents="[Your large document...]",
    ttl_hours=2
)

# Use cache multiple times
result1 = cache_mgr.generate_with_cache("large_doc", "What are the key points?")
result2 = cache_mgr.generate_with_cache("large_doc", "Summarize in 50 words")
result3 = cache_mgr.generate_with_cache("large_doc", "Extract entities")

cache_mgr.list_caches()
```

---

<!-- section_id: "0ed81efc-0780-4ba7-ba14-7445c1ff92b6" -->
## 7. Cost Tracking Patterns

<!-- section_id: "d994e7c3-191d-45ae-b21f-83a63854569c" -->
### Pattern 7.1: Cost Monitor with Alerts

```python
import json
from datetime import datetime
from pathlib import Path

class CostMonitor:
    """Monitor API costs and alert on budget threshold"""

    def __init__(self, budget_usd=20.0, log_file="gemini_costs.json"):
        self.budget = budget_usd
        self.log_file = Path(log_file)
        self.pricing = {
            "gemini-3-flash": {"input": 0.075, "output": 0.30},
            "gemini-2.5-flash": {"input": 0.075, "output": 0.30},
            "gemini-2.5-pro": {"input": 1.50, "output": 6.00},
        }
        self.logs = self._load_logs()

    def _load_logs(self):
        if self.log_file.exists():
            with open(self.log_file) as f:
                return json.load(f)
        return []

    def _save_logs(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)

    def log_request(self, model: str, response) -> float:
        """Log request and return cost"""
        metadata = response.usage_metadata

        rates = self.pricing.get(model, self.pricing["gemini-2.5-flash"])

        # Calculate costs
        input_cost = (metadata.input_token_count / 1_000_000) * rates["input"]
        output_cost = (metadata.output_token_count / 1_000_000) * rates["output"]
        cached_cost = (metadata.cached_content_input_token_count / 1_000_000) * rates["input"] * 0.1

        total_cost = input_cost + output_cost + cached_cost

        # Log
        entry = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "input_tokens": metadata.input_token_count,
            "output_tokens": metadata.output_token_count,
            "cached_tokens": metadata.cached_content_input_token_count,
            "cost_usd": total_cost,
        }
        self.logs.append(entry)
        self._save_logs()

        # Check alert
        self._check_budget_alert()

        return total_cost

    def get_monthly_spend(self) -> float:
        """Get current month spending"""
        today = datetime.now()
        return sum(
            log["cost_usd"]
            for log in self.logs
            if datetime.fromisoformat(log["timestamp"]).year == today.year
            and datetime.fromisoformat(log["timestamp"]).month == today.month
        )

    def _check_budget_alert(self):
        """Alert if budget threshold exceeded"""
        spent = self.get_monthly_spend()
        percentage = (spent / self.budget) * 100

        if percentage >= 100:
            print(f"🚨 CRITICAL: Spent ${spent:.2f} of ${self.budget} budget!")
        elif percentage >= 80:
            print(f"⚠️  WARNING: Spent ${spent:.2f} ({percentage:.0f}% of budget)")

    def print_summary(self):
        """Print spending summary"""
        spent = self.get_monthly_spend()
        remaining = max(0, self.budget - spent)

        print(f"\n--- Monthly Budget Summary ---")
        print(f"Budget: ${self.budget:.2f}")
        print(f"Spent: ${spent:.2f}")
        print(f"Remaining: ${remaining:.2f}")
        print(f"Usage: {(spent/self.budget)*100:.1f}%")

# Usage
monitor = CostMonitor(budget_usd=20.0)

response = client.models.generate_content(...)
cost = monitor.log_request("gemini-2.5-flash", response)

print(f"Request cost: ${cost:.6f}")
monitor.print_summary()
```

---

<!-- section_id: "2ec772fe-0c44-42c9-b9ba-4fabef1a1e4b" -->
## 8. Testing Patterns

<!-- section_id: "64a256b6-8464-4f61-a7b9-46d38a422454" -->
### Pattern 8.1: Mock Client for Testing

```python
from unittest.mock import Mock, MagicMock

class MockGeminiClient:
    """Mock Gemini client for testing"""

    def __init__(self, response_text="Mock response"):
        self.response_text = response_text
        self.call_count = 0

    def models(self):
        """Return mock models"""
        mock = MagicMock()
        mock.generate_content.return_value = self._create_response()
        return mock

    def _create_response(self):
        """Create mock response"""
        mock_response = MagicMock()
        mock_response.text = self.response_text
        mock_response.usage_metadata = MagicMock(
            input_token_count=100,
            output_token_count=50,
            cached_content_input_token_count=0,
        )
        self.call_count += 1
        return mock_response

# Usage in tests
def test_my_function():
    mock_client = MockGeminiClient("Expected response")

    # Use mock instead of real client
    result = my_function(client=mock_client)

    assert result == "Expected response"
    assert mock_client.call_count == 1
```

---

<!-- section_id: "054b0590-d6a6-4de4-85cd-31516428a9e1" -->
## 9. Production Checklist

- [ ] **API Key Management**: Use environment variables, never hardcode
- [ ] **Timeouts**: Configure appropriate timeouts based on request type
- [ ] **Error Handling**: Implement retry logic for transient errors
- [ ] **Cost Monitoring**: Track spending, set budget alerts
- [ ] **Rate Limiting**: Handle 429 responses with exponential backoff
- [ ] **Caching**: Use explicit caching for repeated context
- [ ] **File Management**: Clean up uploaded files after use
- [ ] **Logging**: Log all API requests for debugging
- [ ] **Testing**: Use mock clients for unit tests
- [ ] **Security**: Never include sensitive data in system instructions
- [ ] **Model Selection**: Use appropriate model for cost/performance tradeoff
- [ ] **Session Management**: Persist chat history if needed
- [ ] **Circuit Breaker**: Implement for graceful failure handling
- [ ] **Monitoring**: Track token usage, costs, error rates

