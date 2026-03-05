---
resource_id: "6c8bbfda-f923-4546-9aec-0c762c58433a"
resource_type: "output"
resource_name: "gemini_practical_guide"
---
# Gemini API: Practical Implementation Guide

**Research Date**: February 27, 2026

This guide covers how Gemini is actually used and configured in real applications, with code examples for initialization, configuration, session management, file handling, and cost optimization.

---

<!-- section_id: "b7d52f5d-03b0-444b-9a65-3b5081b46119" -->
## 1. SDK Configuration & Initialization

<!-- section_id: "6cc3f5e8-fa76-458b-b5c2-32b2d745fb75" -->
### 1.1 Python SDK Setup

**Installation**:
```bash
pip install google-genai --upgrade
```

**Basic Initialization**:
```python
from google import genai

# Automatic: Uses GEMINI_API_KEY environment variable
client = genai.Client()

# Explicit API key
client = genai.Client(api_key="your-api-key-here")
```

**With Custom HTTP Options**:
```python
from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions

client = genai.Client(http_options=HttpOptions(api_version="v1"))
```

<!-- section_id: "bfb046db-3e88-4174-8484-b878e49004cd" -->
### 1.2 JavaScript/TypeScript SDK Setup

**Installation**:
```bash
npm install @google/genai
```

**Node.js Initialization**:
```javascript
import { GoogleGenAI } from '@google/genai';

// Using API key
const ai = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY
});
```

**Browser Initialization** (identical):
```javascript
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({
  apiKey: 'GEMINI_API_KEY'
});
```

**Vertex AI Initialization**:
```javascript
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your-project-id',
  location: 'us-central1'
});
```

<!-- section_id: "52bdb116-4a4b-4156-9e2c-2b52af3fcdae" -->
### 1.3 Java/Go SDK Setup

**Java**:
```java
import com.google.cloud.vertexai.api.*;

try (Client client = Client.builder()
    .location("global")
    .vertexAI(true)
    .build()) {
    // Use client
}
```

**Go**:
```go
import "cloud.google.com/go/vertexai/genai"

ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithCredentialsFile("path/to/credentials.json"))
defer client.Close()
```

---

<!-- section_id: "5065b228-57ad-4270-8f3b-0d14be121b35" -->
## 2. System Instructions Implementation

System instructions are processed before any user message, setting the behavior, persona, and constraints for the model.

<!-- section_id: "c2c71c65-4f87-4c4d-bdf8-d0067cb59e13" -->
### 2.1 Python Implementation

```python
from google import genai
from google.genai.types import GenerateContentConfig

client = genai.Client()

# Single system instruction
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is the sky blue?",
    config=GenerateContentConfig(
        system_instruction="You are a language translator. Translate English to French."
    ),
)

# Multiple parts (list)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is the sky blue?",
    config=GenerateContentConfig(
        system_instruction=[
            "You are a language translator.",
            "Your mission is to translate text in English to French.",
            "Never translate proper nouns.",
        ]
    ),
)
```

<!-- section_id: "1f7958f2-d1ca-4e4c-97c7-a5c7e255c03e" -->
### 2.2 JavaScript/TypeScript Implementation

```javascript
const ai = new GoogleGenAI({ apiKey: 'GEMINI_API_KEY' });

const response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: "Why is the sky blue?",
  config: {
    systemInstruction: {
      parts: [
        { text: 'You are a helpful language translator.' },
        { text: 'Your mission is to translate text in English to French.' },
      ],
    },
  },
});
```

<!-- section_id: "69cd2155-1d81-4310-b20f-01c3f156e8fe" -->
### 2.3 Role-Based System Instructions (Front-End Developer Example)

```typescript
const DEVELOPER_SYSTEM_INSTRUCTION = `
You are a highly skilled front-end developer specializing in crafting clean, semantic HTML and inline CSS.
When I describe a user interface component or layout, respond with the complete HTML and inline CSS required to implement it.
Do not include explanations, comments, or additional text — return only the code.
Ensure the code is minimal, accessible, and visually accurate to the described design.
`;

const response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: "A light theme flexbox with a large text logo in rainbow colors aligned left and a list of links aligned right.",
  config: {
    systemInstruction: DEVELOPER_SYSTEM_INSTRUCTION,
  },
});
```

<!-- section_id: "f3d70fcf-e78c-44d7-a758-cb17182303d6" -->
### 2.4 Important Security Note

**System instructions cannot fully prevent jailbreaks or leaks**. Never include sensitive information (API keys, credentials, private data) in system instructions.

---

<!-- section_id: "cdbd23c3-6a8f-4302-be81-6fdad8760739" -->
## 3. Session Management & Conversation History

Gemini SDKs provide two approaches to conversation management: stateful sessions via the Chat API and stateless request-by-request generation.

<!-- section_id: "99ab10bd-c4d3-42a8-91cf-4d6a738a305b" -->
### 3.1 Python Chat Sessions

```python
from google import genai

client = genai.Client()

# Create a chat session
chat = client.chats.create(model="gemini-2.5-flash")

# Send first message
response1 = chat.send_message("What is photosynthesis?")
print(response1.text)

# Continue conversation (history maintained automatically)
response2 = chat.send_message("Explain it in simpler terms")
print(response2.text)

# Access full history
for message in chat.history:
    print(f"{message.role}: {message.parts}")
```

<!-- section_id: "9c8cc72a-9252-4877-9f0b-b37875ff507f" -->
### 3.2 JavaScript Chat Sessions

```javascript
const ai = new GoogleGenAI({ apiKey: 'GEMINI_API_KEY' });

// Create chat
const chat = ai.chats.create({
  model: 'gemini-2.5-flash',
  history: [], // Start empty or with previous messages
});

// Send messages
const response1 = await chat.sendMessage("What is photosynthesis?");
console.log(response1.text);

const response2 = await chat.sendMessage("Explain it in simpler terms");
console.log(response2.text);

// View history
console.log(chat.history);
```

<!-- section_id: "78a39dea-8cbf-4ca0-9b29-34ab3066c6a1" -->
### 3.3 Persisting Conversation History

To resume sessions across application restarts:

**Python - Save/Load History**:
```python
import json
from google import genai

client = genai.Client()

# Save history to JSON
def save_chat(chat, filename):
    history = [
        {
            "role": msg.role,
            "content": [{"text": part.text} for part in msg.parts]
        }
        for msg in chat.history
    ]
    with open(filename, 'w') as f:
        json.dump(history, f)

# Load history from JSON
def load_chat(filename, model="gemini-2.5-flash"):
    with open(filename, 'r') as f:
        history = json.load(f)

    chat = client.chats.create(
        model=model,
        history=[
            {"role": h["role"], "parts": h["content"]}
            for h in history
        ]
    )
    return chat

# Usage
chat = load_chat("session.json")
response = chat.send_message("Continue from where we left off")
save_chat(chat, "session.json")
```

<!-- section_id: "df777d2c-a7b5-4b59-a6cd-cdaec0b56112" -->
### 3.4 Multi-User Session Management

```python
from google import genai
from datetime import datetime

client = genai.Client()

class SessionManager:
    def __init__(self, storage_dir="sessions"):
        self.storage_dir = storage_dir
        import os
        os.makedirs(storage_dir, exist_ok=True)

    def create_session(self, user_id, model="gemini-2.5-flash"):
        """Create new session for user"""
        session_file = f"{self.storage_dir}/{user_id}_latest.json"
        chat = client.chats.create(model=model)
        self._save_session(user_id, chat)
        return chat

    def get_session(self, user_id, model="gemini-2.5-flash"):
        """Load user's session or create new"""
        session_file = f"{self.storage_dir}/{user_id}_latest.json"
        try:
            with open(session_file, 'r') as f:
                history = json.load(f)
            return client.chats.create(
                model=model,
                history=[
                    {"role": h["role"], "parts": h["content"]}
                    for h in history
                ]
            )
        except FileNotFoundError:
            return self.create_session(user_id, model)

    def _save_session(self, user_id, chat):
        """Persist session to disk"""
        history = [
            {
                "role": msg.role,
                "content": [{"text": part.text} for part in msg.parts],
                "timestamp": datetime.now().isoformat()
            }
            for msg in chat.history
        ]
        session_file = f"{self.storage_dir}/{user_id}_latest.json"
        with open(session_file, 'w') as f:
            json.dump(history, f, indent=2)

# Usage
manager = SessionManager()
user_chat = manager.get_session("user123")
response = user_chat.send_message("Hello!")
manager._save_session("user123", user_chat)
```

---

<!-- section_id: "d30d759d-e765-4973-b758-fcff755858a8" -->
## 4. File Upload & Management

The Files API allows uploading media for use in requests, with automatic storage management.

<!-- section_id: "d1c526d5-19cd-4639-aae2-0a3628750045" -->
### 4.1 File Upload (Python)

```python
from google import genai

client = genai.Client()

# Upload a file
my_file = client.files.upload(file="path/to/document.pdf")
print(f"Uploaded: {my_file.name}")

# Use uploaded file in generation
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "\n\n", "Summarize this document"],
)
print(response.text)
```

<!-- section_id: "8f3931a5-aac0-42fd-89a5-c8a6f4af0412" -->
### 4.2 File Upload (JavaScript)

```javascript
const ai = new GoogleGenAI({ apiKey: 'GEMINI_API_KEY' });
const fs = require('fs');
const path = require('path');

// Upload file
const mdFile = await ai.files.upload({
  file: fs.readFileSync('path/to/document.pdf'),
  config: {
    displayName: "document.pdf",
    mimeType: "application/pdf",
  },
});

console.log(`Uploaded: ${mdFile.name}`);

// Use in generation
const response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: [
    { fileData: { mimeType: mdFile.mimeType, fileUri: mdFile.uri } },
    { text: "Summarize this document" }
  ],
});
```

<!-- section_id: "6352d13f-1e21-4909-8c76-b79498adbe4a" -->
### 4.3 File Management

**Python - List, Get, Delete**:
```python
from google import genai

client = genai.Client()

# List all files
print("My files:")
for f in client.files.list():
    print(f"  {f.name} ({f.display_name}) - {f.mime_type}")

# Get specific file info
my_file = client.files.get(name="files/abc123")
print(f"Created: {my_file.create_time}")
print(f"Expires: {my_file.expiration_time}")

# Delete file
client.files.delete(name=my_file.name)
print("File deleted")
```

<!-- section_id: "afb1a75d-ec50-4699-aebe-b60577810d6b" -->
### 4.4 File Storage Limits & Considerations

- **Maximum storage**: 20 GB per project
- **Per-file limit**: 2 GB maximum
- **Retention**: 48 hours (automatic deletion)
- **PDF limit**: 50 MB
- **Use Files API when**: Total request size > 100 MB
- **Cost**: Free across all regions

---

<!-- section_id: "d3f81b91-4af3-4d86-bd1e-4a86c3874ef8" -->
## 5. Prompt Caching Configuration

Prompt caching reduces costs for repeated requests by storing large context on Google's servers.

<!-- section_id: "1877d65c-07b4-475f-8771-3fcf5e4569a0" -->
### 5.1 Two Caching Approaches

**Implicit Caching** (default, automatic):
- Enabled by default, no configuration needed
- Minimum tokens: 1,024-4,096 depending on model
- Cost saving not guaranteed

**Explicit Caching** (manual, guaranteed):
- You create and manage caches explicitly
- Guaranteed cost reduction on cache hits
- Set custom TTL (time-to-live)

<!-- section_id: "11db14fe-f77e-4dbd-b06d-2ba538c9ffaf" -->
### 5.2 Explicit Caching (Python)

```python
from google import genai
from google.genai.types import CachedContent, Content, Part
from datetime import datetime, timedelta

client = genai.Client()

# Create a cached content object (e.g., large document)
document_content = """
[Your large document or context here - can be thousands of tokens]
This will be cached on Google's servers.
"""

# Create cache with explicit TTL
cached_content = client.caches.create(
    display_name="large_document_cache",
    model="gemini-2.5-flash",
    system_instruction="You are a document analyzer.",
    contents=document_content,
    ttl=timedelta(hours=1),  # Expires in 1 hour
)

print(f"Cache created: {cached_content.name}")
print(f"Token usage: {cached_content.usage_metadata}")

# Use cached content in subsequent requests
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What are the key points in the cached document?",
    cache_control={"cache_resource_name": cached_content.name},
)

print(f"Response: {response.text}")
print(f"Cached tokens used: {response.usage_metadata.cached_content_input_token_count}")
```

<!-- section_id: "27efe729-2c36-4d27-b608-f4b1958270dc" -->
### 5.3 Explicit Caching (JavaScript)

```javascript
const ai = new GoogleGenAI({ apiKey: 'GEMINI_API_KEY' });

// Create cache
const cache = await ai.caches.create({
  displayName: "large_document_cache",
  model: "gemini-2.5-flash",
  systemInstruction: "You are a document analyzer.",
  contents: "[Your large document here]",
  ttl: "3600s", // 1 hour in seconds
});

console.log(`Cache created: ${cache.name}`);

// Use cache in generation
const response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: "What are the key points?",
  cacheControl: {
    cacheResourceName: cache.name
  },
});

console.log(`Cached tokens: ${response.usageMetadata.cachedContentInputTokenCount}`);
```

<!-- section_id: "c973fcbf-e177-46ce-aae3-8b3105876486" -->
### 5.4 Cache Management

**Python - Update TTL, Delete Cache**:
```python
from google import genai
from datetime import datetime, timedelta

client = genai.Client()

# Update TTL
cache = client.caches.update(
    name="cache-id",
    ttl=timedelta(hours=2),  # Extend to 2 hours
)

# Delete cache
client.caches.delete(name="cache-id")
print("Cache deleted")

# List caches
for cache in client.caches.list():
    print(f"{cache.name}: expires at {cache.expiration_time}")
```

<!-- section_id: "f39f560e-ff79-495f-843c-1523888bc5a3" -->
### 5.5 Caching Best Practices

1. **Keep static content at the beginning** of the request (system instructions, large documents)
2. **Put dynamic content at the end** (user questions, changing parameters)
3. **Cache minimum tokens**: 1,024 for 2.5 Flash, 4,096 for 3.1 Pro
4. **TTL defaults to 1 hour** - set explicitly for longer retention
5. **Cache hits reduce input token cost by ~90%**

---

<!-- section_id: "b84fa461-afde-4931-b1cf-5d385b231469" -->
## 6. Model Selection & Generation Parameters

<!-- section_id: "3d27d641-2290-4b21-a7ad-d0ba135ded03" -->
### 6.1 Available Models (2026)

**Latest Models**:
- `gemini-3-flash` - Latest, fastest, cost-effective
- `gemini-3-pro` - Highest intelligence/reasoning
- `gemini-2.5-flash` - Fast, suitable for most tasks
- `gemini-2.5-pro` - Advanced reasoning (retiring June 1, 2026)
- `gemini-1.5-pro` - Legacy (retiring June 1, 2026)
- `gemini-1.5-flash` - Legacy (retiring June 1, 2026)

<!-- section_id: "0966d5f7-6790-4421-86d1-c06478aaf267" -->
### 6.2 Generation Parameters

```python
from google import genai
from google.genai.types import GenerateContentConfig, SafetySetting

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain quantum computing",
    config=GenerateContentConfig(
        # Temperature: 0.0-2.0 (default: 1.0)
        # Lower = more deterministic, Higher = more creative
        temperature=0.7,

        # Top-P: 0-1 (default: 0.94 for Gemini 1.5)
        # Controls diversity of token selection
        top_p=0.9,

        # Top-K: integer
        # Consider only top K most probable tokens
        top_k=40,

        # Max output tokens
        max_output_tokens=1000,

        # Stop sequences
        stop_sequences=["END", "STOP"],

        # Candidate count (for multiple responses)
        candidate_count=1,
    ),
)
```

<!-- section_id: "3b87fd79-94ce-453e-829b-24f08fdd097b" -->
### 6.3 Parameter Recommendations by Use Case

```python
# For factual/deterministic tasks (summarization, translation)
deterministic_config = GenerateContentConfig(
    temperature=0.2,  # Low randomness
    top_p=0.8,
)

# For creative tasks (writing, brainstorming)
creative_config = GenerateContentConfig(
    temperature=1.5,  # Higher randomness
    top_p=0.95,
)

# For balanced use (most applications)
balanced_config = GenerateContentConfig(
    temperature=0.7,
    top_p=0.9,
)

# For Gemini 3 (recommended not to change from default)
gemini3_config = GenerateContentConfig(
    temperature=1.0,  # Don't change - model is optimized at 1.0
)
```

---

<!-- section_id: "76cb4105-402d-4749-9ddd-9b283185d606" -->
## 7. Cost Management & Token Usage

<!-- section_id: "04807fdf-b910-4a95-b8ad-bbe57ec02225" -->
### 7.1 Token Counting (Before Making Requests)

**Python**:
```python
from google import genai

client = genai.Client()

# Count tokens before making a request
message = "Explain photosynthesis in detail"
token_count = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents=message,
)

print(f"Input tokens: {token_count.total_tokens}")

# Estimate cost (example pricing)
# Gemini 2.5 Flash: $0.075/1M input tokens, $0.30/1M output tokens
input_cost = (token_count.total_tokens / 1_000_000) * 0.075
print(f"Estimated input cost: ${input_cost:.6f}")
```

**JavaScript**:
```javascript
const ai = new GoogleGenAI({ apiKey: 'GEMINI_API_KEY' });

const tokenCount = await ai.models.countTokens({
  model: 'gemini-2.5-flash',
  contents: "Explain photosynthesis in detail"
});

console.log(`Input tokens: ${tokenCount.totalTokens}`);
```

<!-- section_id: "90c8b2ef-03d2-490b-8421-d1e3c0fce7a1" -->
### 7.2 Monitoring Token Usage in Responses

```python
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain photosynthesis",
)

# Access usage metadata
metadata = response.usage_metadata
print(f"Input tokens: {metadata.input_token_count}")
print(f"Output tokens: {metadata.output_token_count}")
print(f"Cached tokens: {metadata.cached_content_input_token_count}")

# Calculate cost
input_cost = (metadata.input_token_count / 1_000_000) * 0.075
output_cost = (metadata.output_token_count / 1_000_000) * 0.30
cached_cost = (metadata.cached_content_input_token_count / 1_000_000) * 0.0075  # 90% discount
total_cost = input_cost + output_cost + cached_cost

print(f"Input cost: ${input_cost:.6f}")
print(f"Output cost: ${output_cost:.6f}")
print(f"Cached cost: ${cached_cost:.6f}")
print(f"Total cost: ${total_cost:.6f}")
```

<!-- section_id: "00131895-fed2-4e0e-b6c1-e8751897a968" -->
### 7.3 Cost Optimization Strategies

```python
from google import genai
from google.genai.types import GenerateContentConfig, CachedContent
from datetime import timedelta

client = genai.Client()

class CostOptimizer:
    """Reduce Gemini API costs"""

    @staticmethod
    def use_caching_for_repeated_context(large_document):
        """Use explicit caching for documents analyzed multiple times"""
        cache = client.caches.create(
            model="gemini-2.5-flash",
            display_name="repeated_doc",
            contents=large_document,
            ttl=timedelta(hours=1),
        )
        return cache

    @staticmethod
    def use_flash_model_by_default():
        """Flash models are 5-10x cheaper than Pro"""
        return "gemini-2.5-flash"  # Not "gemini-2.5-pro"

    @staticmethod
    def batch_requests():
        """Process multiple queries together when possible"""
        # Instead of 3 separate requests, combine into 1
        prompt = """
        Question 1: What is photosynthesis?
        Question 2: What is the water cycle?
        Question 3: What is the nitrogen cycle?

        Answer each briefly.
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response

    @staticmethod
    def use_shorter_outputs():
        """Reduce output tokens when possible"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Summarize in 50 words: [document]",
            config=GenerateContentConfig(max_output_tokens=50),
        )
        return response

    @staticmethod
    def prefer_cached_tokens():
        """Leverage cached content for cost reduction"""
        # Cache hit = 90% cost reduction on input tokens
        # 1M input tokens: $0.075 vs cached: $0.0075
        pass

# Pricing reference (Feb 2026)
PRICING = {
    "gemini-3-flash": {"input": 0.075, "output": 0.30},
    "gemini-3-pro": {"input": 1.50, "output": 6.00},
    "gemini-2.5-flash": {"input": 0.075, "output": 0.30},
    "gemini-2.5-pro": {"input": 1.50, "output": 6.00},
    # Cached input tokens cost 90% less
    "cached_discount": 0.1,
}
```

<!-- section_id: "f680ac85-eb33-4bb0-9bdb-2789055abecc" -->
### 7.4 Cost Tracking Dashboard

```python
import json
from datetime import datetime
from pathlib import Path

class CostTracker:
    def __init__(self, log_file="gemini_costs.json"):
        self.log_file = Path(log_file)
        self.load_logs()

    def load_logs(self):
        if self.log_file.exists():
            with open(self.log_file) as f:
                self.logs = json.load(f)
        else:
            self.logs = []

    def log_request(self, model, input_tokens, output_tokens, cached_tokens=0):
        """Log API request and calculate cost"""
        cost = self._calculate_cost(model, input_tokens, output_tokens, cached_tokens)

        entry = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cached_tokens": cached_tokens,
            "cost_usd": cost,
        }
        self.logs.append(entry)
        self._save_logs()

        return cost

    def _calculate_cost(self, model, input_tokens, output_tokens, cached_tokens=0):
        """Calculate cost in USD"""
        pricing = {
            "gemini-3-flash": {"input": 0.075, "output": 0.30},
            "gemini-2.5-flash": {"input": 0.075, "output": 0.30},
            "gemini-2.5-pro": {"input": 1.50, "output": 6.00},
        }

        rates = pricing.get(model, pricing["gemini-2.5-flash"])

        # Regular input tokens
        regular_input_tokens = input_tokens - cached_tokens
        input_cost = (regular_input_tokens / 1_000_000) * rates["input"]

        # Cached tokens (90% discount)
        cached_cost = (cached_tokens / 1_000_000) * rates["input"] * 0.1

        output_cost = (output_tokens / 1_000_000) * rates["output"]

        return input_cost + cached_cost + output_cost

    def _save_logs(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)

    def get_daily_total(self, date=None):
        """Get total cost for a day"""
        if date is None:
            date = datetime.now().date()

        total = sum(
            log["cost_usd"]
            for log in self.logs
            if datetime.fromisoformat(log["timestamp"]).date() == date
        )
        return total

    def get_monthly_total(self):
        """Get total cost for current month"""
        today = datetime.now()
        total = sum(
            log["cost_usd"]
            for log in self.logs
            if datetime.fromisoformat(log["timestamp"]).year == today.year
            and datetime.fromisoformat(log["timestamp"]).month == today.month
        )
        return total

    def print_summary(self):
        """Print cost summary"""
        monthly_total = self.get_monthly_total()
        daily_total = self.get_daily_total()

        print(f"Today: ${daily_total:.4f}")
        print(f"This month: ${monthly_total:.4f}")
        print(f"Budget remaining: ${20.00 - monthly_total:.4f}")  # Assuming $20 budget

        if monthly_total > 20 * 0.8:
            print("⚠️  WARNING: 80% of budget consumed!")

# Usage
tracker = CostTracker()

# Log a request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain photosynthesis",
)

cost = tracker.log_request(
    model="gemini-2.5-flash",
    input_tokens=response.usage_metadata.input_token_count,
    output_tokens=response.usage_metadata.output_token_count,
    cached_tokens=response.usage_metadata.cached_content_input_token_count,
)

print(f"Request cost: ${cost:.6f}")
tracker.print_summary()
```

---

<!-- section_id: "0d0e9ca7-7b23-4d6c-a8f8-27f48e1f6573" -->
## 8. Error Handling & Retry Logic

<!-- section_id: "484d65fe-17d4-4b47-954c-44de4007133a" -->
### 8.1 Common Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 400 | Bad Request (validation error) | Fix the request format |
| 401 | Unauthorized (invalid API key) | Check GEMINI_API_KEY |
| 429 | Rate Limited (quota exceeded) | Implement exponential backoff |
| 500 | Server Error | Retry with exponential backoff |
| 503 | Service Unavailable | Retry with exponential backoff |
| 504 | Deadline Exceeded (timeout) | Increase timeout or reduce prompt |

<!-- section_id: "09c7996d-2240-4383-bcf7-0eca85ac1b0f" -->
### 8.2 Basic Error Handling (Python)

```python
from google import genai
import time
import random

client = genai.Client()

def generate_with_retry(prompt, model="gemini-2.5-flash", max_retries=3):
    """Generate content with exponential backoff retry"""

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )
            return response

        except Exception as e:
            # Handle rate limiting
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                wait_time = 2 ** attempt + random.uniform(0, 1)
                print(f"Rate limited. Waiting {wait_time:.1f}s before retry...")
                time.sleep(wait_time)
                continue

            # Handle server errors
            elif "500" in str(e) or "503" in str(e):
                wait_time = 2 ** attempt + random.uniform(0, 1)
                print(f"Server error. Waiting {wait_time:.1f}s before retry...")
                time.sleep(wait_time)
                continue

            # Unrecoverable errors
            else:
                print(f"Unrecoverable error: {e}")
                raise

    raise Exception("Max retries exceeded")

# Usage
try:
    response = generate_with_retry("Explain quantum computing")
    print(response.text)
except Exception as e:
    print(f"Failed after retries: {e}")
```

<!-- section_id: "8c963718-5db9-420d-93c3-9724e94a4993" -->
### 8.3 Advanced Retry with Circuit Breaker (Python)

```python
from google import genai
from enum import Enum
import time
import random
from datetime import datetime, timedelta

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, client, prompt, model="gemini-2.5-flash"):
        """Execute request with circuit breaker protection"""

        if self.state == CircuitState.OPEN:
            # Check if recovery timeout elapsed
            if datetime.now() - self.last_failure_time > timedelta(seconds=self.recovery_timeout):
                self.state = CircuitState.HALF_OPEN
                print("Circuit HALF-OPEN: Testing recovery...")
            else:
                raise Exception("Circuit breaker is OPEN. Service unavailable.")

        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )

            # Success: reset circuit
            self.failure_count = 0
            self.state = CircuitState.CLOSED
            return response

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = datetime.now()

            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                print(f"Circuit OPEN: {self.failure_count} failures detected")

            raise

# Usage
breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=60)
client = genai.Client()

for i in range(10):
    try:
        response = breaker.call(client, "Explain quantum computing")
        print(f"Request {i+1}: Success")
    except Exception as e:
        print(f"Request {i+1}: Failed - {e}")

    time.sleep(1)
```

<!-- section_id: "4814c82b-220a-4c81-9aae-e1a630627dc1" -->
### 8.4 Timeout Configuration

```python
from google import genai
from google.genai.types import HttpOptions

# Set custom timeout
client = genai.Client(
    http_options=HttpOptions(timeout=30)  # 30 seconds
)

# For slow operations, increase timeout
client = genai.Client(
    http_options=HttpOptions(timeout=120)  # 2 minutes
)
```

<!-- section_id: "1c4bbf86-b9b8-4df0-92a0-386231908c3e" -->
### 8.5 JavaScript Error Handling

```javascript
const ai = new GoogleGenAI({ apiKey: 'GEMINI_API_KEY' });

async function generateWithRetry(prompt, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await ai.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: prompt,
      });
      return response;
    } catch (error) {
      // Rate limiting
      if (error.status === 429) {
        const waitTime = Math.pow(2, attempt) + Math.random();
        console.log(`Rate limited. Waiting ${waitTime.toFixed(1)}s...`);
        await new Promise(resolve => setTimeout(resolve, waitTime * 1000));
        continue;
      }

      // Server errors
      if ([500, 503].includes(error.status)) {
        const waitTime = Math.pow(2, attempt) + Math.random();
        console.log(`Server error. Waiting ${waitTime.toFixed(1)}s...`);
        await new Promise(resolve => setTimeout(resolve, waitTime * 1000));
        continue;
      }

      // Unrecoverable
      throw error;
    }
  }
  throw new Error('Max retries exceeded');
}

// Usage
try {
  const response = await generateWithRetry("Explain quantum computing");
  console.log(response.text);
} catch (error) {
  console.error("Failed after retries:", error);
}
```

---

<!-- section_id: "de57dcf6-eb50-4e75-8399-b9f796f8f5ce" -->
## 9. Complete Application Example

Here's a complete example combining all concepts:

```python
from google import genai
from google.genai.types import GenerateContentConfig, CachedContent
from datetime import timedelta
import json
from pathlib import Path
import time

class GeminiApplication:
    """Complete Gemini API application with all features"""

    def __init__(self, api_key=None):
        self.client = genai.Client(api_key=api_key)
        self.cost_tracker = {}
        self.session_file = Path("session.json")

    def initialize_chat_with_system_instructions(self, system_prompt):
        """Create chat with system instructions"""
        self.chat = self.client.chats.create(
            model="gemini-2.5-flash",
        )
        self.system_instruction = system_prompt
        return self.chat

    def send_message(self, user_message):
        """Send message and track costs"""
        try:
            # Send with timeout handling
            response = self.chat.send_message(user_message)

            # Track costs
            self._track_costs(response)

            return response.text

        except Exception as e:
            if "429" in str(e):
                print("Rate limited, waiting 60 seconds...")
                time.sleep(60)
                return self.send_message(user_message)
            raise

    def upload_and_analyze_file(self, filepath, question):
        """Upload file and analyze with caching"""
        # Upload file
        uploaded_file = self.client.files.upload(file=filepath)
        print(f"Uploaded: {uploaded_file.name}")

        # Analyze file
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[uploaded_file, "\n\n", question],
            config=GenerateContentConfig(max_output_tokens=1000),
        )

        self._track_costs(response)
        return response.text

    def create_cached_context(self, context_text, ttl_hours=1):
        """Create cached context for repeated use"""
        cache = self.client.caches.create(
            display_name="app_context",
            model="gemini-2.5-flash",
            contents=context_text,
            ttl=timedelta(hours=ttl_hours),
        )
        self.cached_content = cache
        print(f"Created cache: {cache.name}")
        return cache

    def generate_with_cache(self, prompt):
        """Generate using cached content"""
        if not hasattr(self, 'cached_content'):
            raise ValueError("No cached content available")

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            cache_control={"cache_resource_name": self.cached_content.name},
        )

        self._track_costs(response)
        return response.text

    def save_session(self):
        """Persist conversation"""
        history = [
            {
                "role": msg.role,
                "content": [{"text": part.text} for part in msg.parts]
            }
            for msg in self.chat.history
        ]
        with open(self.session_file, 'w') as f:
            json.dump(history, f, indent=2)
        print(f"Session saved to {self.session_file}")

    def load_session(self):
        """Resume previous conversation"""
        if not self.session_file.exists():
            return None

        with open(self.session_file) as f:
            history = json.load(f)

        self.chat = self.client.chats.create(
            model="gemini-2.5-flash",
            history=[
                {"role": h["role"], "parts": h["content"]}
                for h in history
            ],
        )
        return len(history)

    def _track_costs(self, response):
        """Track request costs"""
        metadata = response.usage_metadata

        input_cost = (metadata.input_token_count / 1_000_000) * 0.075
        output_cost = (metadata.output_token_count / 1_000_000) * 0.30
        cached_cost = (metadata.cached_content_input_token_count / 1_000_000) * 0.0075

        total = input_cost + output_cost + cached_cost

        self.cost_tracker['last_request'] = {
            'input_tokens': metadata.input_token_count,
            'output_tokens': metadata.output_token_count,
            'cached_tokens': metadata.cached_content_input_token_count,
            'cost': total,
        }
        self.cost_tracker['total_cost'] = self.cost_tracker.get('total_cost', 0) + total

        print(f"Cost: ${total:.6f} | Total: ${self.cost_tracker['total_cost']:.4f}")

    def print_stats(self):
        """Print application statistics"""
        print(f"\nTotal API cost: ${self.cost_tracker.get('total_cost', 0):.4f}")
        print(f"Chat history length: {len(self.chat.history)}")

# Usage
if __name__ == "__main__":
    app = GeminiApplication()

    # Initialize with system instructions
    app.initialize_chat_with_system_instructions(
        "You are a helpful AI assistant specializing in technology topics."
    )

    # Continue conversation
    response = app.send_message("What is machine learning?")
    print(response)
    print()

    response = app.send_message("Explain it more simply")
    print(response)
    print()

    # Save session
    app.save_session()

    # Print stats
    app.print_stats()
```

---

<!-- section_id: "52fcbbbc-0412-487d-a7bb-d04d2af05988" -->
## 10. References

- [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [System Instructions Documentation](https://ai.google.dev/gemini-api/docs/system-instructions)
- [Context Caching Guide](https://ai.google.dev/gemini-api/docs/caching)
- [Files API Documentation](https://ai.google.dev/gemini-api/docs/files)
- [Models Reference](https://ai.google.dev/gemini-api/docs/models/generative-models)
- [Billing and Pricing](https://ai.google.dev/gemini-api/docs/billing)
- [Rate Limits and Retries](https://geminibyexample.com/029-rate-limits-retries/)
- [Google AI Python SDK](https://github.com/google-gemini/generative-ai-python)
- [Google AI JavaScript SDK](https://github.com/googleapis/js-genai)

