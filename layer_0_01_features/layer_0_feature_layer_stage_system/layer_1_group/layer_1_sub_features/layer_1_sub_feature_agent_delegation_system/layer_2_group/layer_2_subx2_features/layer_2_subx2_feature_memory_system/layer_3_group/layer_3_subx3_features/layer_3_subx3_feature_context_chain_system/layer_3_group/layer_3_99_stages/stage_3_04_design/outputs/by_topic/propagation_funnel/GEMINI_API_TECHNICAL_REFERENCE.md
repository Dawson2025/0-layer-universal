---
file_id: "f4bf732a-aa78-41b2-af5b-581121ced0af"
---
# Google Gemini API: Comprehensive Technical Reference (2024-2026)

**Version**: 1.0
**Last Updated**: February 2026
**Scope**: Complete technical specifications for Gemini API across all major features

---

<!-- section_id: "b5f5be92-dc6c-4e41-be1c-b69ee615539c" -->
## Table of Contents

1. [System Instructions and Configuration](#system-instructions-and-configuration)
2. [Context Windows and Token Management](#context-windows-and-token-management)
3. [Multimodal Input Processing](#multimodal-input-processing)
4. [File Management and Upload Systems](#file-management-and-upload-systems)
5. [Function Calling and Tool Integration](#function-calling-and-tool-integration)
6. [Context Caching and Optimization](#context-caching-and-optimization)
7. [Pricing and Cost Models](#pricing-and-cost-models)
8. [Token Counting Methodology](#token-counting-methodology)
9. [Session and Conversation Management](#session-and-conversation-management)
10. [Thinking/Reasoning Mode](#thinkingreasoning-mode)
11. [Structured Outputs and Validation](#structured-outputs-and-validation)
12. [Grounding and Enhanced Capabilities](#grounding-and-enhanced-capabilities)
13. [API Endpoints and Error Handling](#api-endpoints-and-error-handling)
14. [Rate Limits and Quota Management](#rate-limits-and-quota-management)

---

<!-- section_id: "34318a7e-dec2-49d0-9ab8-8ed255dcc628" -->
## System Instructions and Configuration

<!-- section_id: "1821f299-e82e-4861-bab7-58b6e27f6e12" -->
### Overview

System instructions represent a distinct processing layer that precedes main prompt input. They function as meta-instructions establishing behavioral parameters, output formatting requirements, and role definitions that apply across the entire request and subsequent conversation turns.

**Key characteristics**:
- Not part of conversational history
- Persist across multiple turns in multi-turn interactions
- Available across all API access patterns (generateContent, batch processing, Interactions API)
- Consumed from token budget at standard rates (~4 characters per token)

<!-- section_id: "1648fedc-907d-4410-bcb1-a464fa5839b9" -->
### Implementation Across SDKs

#### Python SDK
```python
from google.generativeai import GenerateContentConfig

response = model.generate_content(
    "Your prompt here",
    config=GenerateContentConfig(
        system_instruction="You are a specialized Python code reviewer..."
    )
)
```

#### JavaScript SDK
```javascript
const response = await model.generateContent({
    systemInstruction: "You are a specialized Python code reviewer...",
    contents: [{ role: "user", text: "Your prompt here" }]
});
```

#### REST API
```json
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent

{
  "system_instruction": {
    "parts": [
      {
        "text": "You are a specialized Python code reviewer..."
      }
    ]
  },
  "contents": [...]
}
```

<!-- section_id: "95423513-45f3-4e0a-abbc-6bb0484725a5" -->
### Specification Format and Use Cases

**Supported instruction types**:
- **Role definition**: Establish specific persona/expertise (translator, expert, assistant type)
- **Output formatting**: Markdown, YAML, JSON, XML, structured formats
- **Output style**: Verbosity level, formality, reading difficulty, tone
- **Context provision**: Supplementary information beyond training data
- **Task-specific rules**: Domain constraints, validation rules
- **Language specification**: Target response language
- **Guardrails**: Content generation restrictions and acceptable patterns

**Example system instruction structure**:
```
You are an expert Python code reviewer with 15+ years of experience.

When reviewing code, follow these rules:
1. Always explain performance implications
2. Suggest refactoring opportunities
3. Flag potential security issues
4. Provide examples when recommending changes

Output format: Use Markdown with code blocks for all code examples.
Tone: Professional but approachable
```

<!-- section_id: "3f18806f-324c-40fd-b72a-93cbf761c3b1" -->
### Character and Token Limitations

**Critical fact**: There is NO explicit character limit on system instructions, but all content consumes tokens from the context window budget.

**Token consumption formula**:
- System instructions: ~4 characters = 1 token (standard rate)
- 80,000 characters of instructions = ~20,000 tokens
- Tokens consumed on every API request using those instructions

**Example cost calculation**:
```
System instructions: 50,000 characters
= 12,500 tokens per request
× 1,000 requests/day
= 12,500,000 tokens/day
= 0.025 million tokens/day
= $0.05/day at $2/million input token rate (Gemini 3 Pro standard)
```

**Optimization**: Use context caching to avoid re-paying for system instructions on repeated queries.

---

<!-- section_id: "6a96d149-838a-4b7d-94dc-fac96a10c6ba" -->
## Context Windows and Token Management

<!-- section_id: "175e7b45-0d34-4e92-b92a-0cb942aa5967" -->
### Evolution Timeline and Capacity Progression

| Period | Model | Context Window | Practical Capacity |
|--------|-------|---------------|--------------------|
| 2023-2024 | Gemini 1.0 | 32,000-128,000 tokens | ~8-16 documents |
| 2024 | Gemini 1.5 Pro | 1,000,000 tokens | ~50,000 lines of code; 8 novels |
| 2025-2026 | Gemini 3/3.1 Pro | 2,000,000 tokens | ~100,000 lines of code; 16 novels |

<!-- section_id: "770b3547-bcbe-4706-ba61-2b15044614d3" -->
### 1 Million Token Context Window Specifications

**Practical capacity equivalents**:
- 50,000 lines of source code (80 chars/line)
- 6,000+ pages of typical text (at 200 tokens/page)
- 8-10 complete novels
- 200+ podcast episode transcripts (at ~5,000 words each)
- 5 years of average personal email volume
- 100+ research papers (at 10,000 words each)

**Retrieval performance**:
- ~99% accuracy for information retrieval across full context window
- Minimal performance degradation with length
- Cost increases linearly with input tokens

**Practical limitations**:
- Latency increases with larger inputs
- Cost per query increases proportionally
- Rate limits measured in tokens, not requests

<!-- section_id: "24b3a434-2d1e-4e18-8773-b82228b9b72e" -->
### 2 Million Token Context Window Specifications

**Capacity**: Double the 1M window, enabling:
- 100,000 lines of code
- 16 complete novels
- Comprehensive analysis of multiple large documents simultaneously
- Full codebase analysis for mid-sized projects (10K-100K lines)

**Performance characteristics**:
- 99%+ retrieval accuracy maintained
- Slightly higher latency than 1M window
- 2x cost compared to 1M equivalent content

**Cost-performance tradeoff**:
```
Single query with 1M tokens: ~$0.002 input cost
vs
Single query with 2M tokens: ~$0.004 input cost

If performing 100 different queries against same 2M token base:
- Separate queries: $0.40 total cost
- With caching: $0.004 (cache write) + $0.0004 × 100 (cache reads) = $0.044 total
- Savings: ~89% reduction with caching
```

<!-- section_id: "2694cf6e-8462-4c99-b3f6-02fff9193a04" -->
### Output Token Limits and Constraints

| Model | Default Output | Max Output | Cost per 64K |
|-------|---|---|---|
| Gemini 3 Pro | 8,192 | 65,536 | $0.78 |
| Gemini 3.1 Pro | 8,192 | 65,536 | $0.78 |
| Gemini 3 Flash | 8,192 | 32,768 | $0.098 |

**Practical implications**:
- Must explicitly set `max_output_tokens` to exceed 8,192
- 64K output = ~49,000 words = complete technical manual
- Pricing penalties for maximum-length outputs
- Consider breaking large requests into multiple turns

---

<!-- section_id: "5b874077-e695-4dde-b36a-9bf12dc19144" -->
## Multimodal Input Processing

<!-- section_id: "67f148f7-8b30-4c19-828d-e72a8c6feabc" -->
### Supported Input Modalities

| Modality | Formats | Max Size | Token Rate |
|----------|---------|----------|------------|
| Text | Plain text, UTF-8 | Unlimited (context bound) | ~4 chars/token |
| Image | PNG, JPEG, WebP, GIF | 20 MB individual | 258 tokens (small); 1,120 tokens (high-res) |
| Video | MP4, MOV, MPEG, WebM, AVI | 2 GB individual | 263 tokens/second |
| Audio | MP3, WAV, FLAC, OGG | 1 hour typical limit | 32 tokens/second |
| PDF | PDF documents | 50 MB; 1,000 pages | 258 tokens/page |
| Code | Source files | Depends on modality | Text token rate |

<!-- section_id: "4312c689-e6a1-4ec4-856f-75ae02bb5110" -->
### Image Processing and Token Calculation

#### Image Size Classification

**Small images** (< 384 pixels in both dimensions):
- Token cost: Flat 258 tokens regardless of resolution
- No tiling applied
- Most efficient for thumbnails and icons

**Medium to large images** (384+ pixels):
- Cropped and tiled into 768x768 pixel segments
- Each segment: 258 tokens
- Total tokens = ceiling(width / 768) × ceiling(height / 768) × 258

**Example calculations**:
```
Image 600×400:
- One segment (less than 768×768)
- Tokens: 1 × 1 × 258 = 258 tokens

Image 1,600×1,200:
- Segments: ceiling(1,600/768) × ceiling(1,200/768) = 3 × 2 = 6 segments
- Tokens: 6 × 258 = 1,548 tokens

Image 3,072×2,048:
- Segments: ceiling(3,072/768) × ceiling(2,048/768) = 4 × 3 = 12 segments
- Tokens: 12 × 258 = 3,096 tokens
```

#### Gemini 3 Media Resolution Parameter

The `media_resolution` parameter enables granular control over image processing:

| Setting | Max Tokens/Image | Recommended Use | Tradeoff |
|---------|-----------------|-----------------|----------|
| `LOW` | 70 tokens | Quick summaries, general content | Poor OCR, text misses |
| `MEDIUM` | 560 tokens | PDFs, standard documents | Good balance |
| `HIGH` | 1,120 tokens | Text-heavy, precise requirements | Higher cost |

**Optimization recommendation**:
- Default to `MEDIUM` for PDFs
- Use `HIGH` only for text-critical analysis
- Use `LOW` for bulk image processing where exact text isn't required

<!-- section_id: "b2d6f462-5e66-4636-b238-05cf2e644f3b" -->
### Video Input Processing

**Token consumption formula**:
```
Total tokens = (duration_seconds × sampling_rate × 263) +
               (duration_seconds × 32) if audio included
```

**Sampling rates**:
- Standard: 1 frame per second = 263 tokens/second
- 1-hour video = 3,600 seconds × 263 tokens = 946,800 tokens
- 1-hour video + audio = 946,800 + (3,600 × 32) = 1,071,000 tokens

**Processing limits**:
- Maximum 2 hours video with 2M token context
- Maximum 1 hour video with 1M token context
- Streaming video not supported; requires download first

**Resolution control**:
```
media_resolution_low:    70 tokens/frame
media_resolution_medium: 140 tokens/frame
media_resolution_high:   280 tokens/frame
```

<!-- section_id: "7bae4601-9068-450b-a664-faf2c97e651e" -->
### Audio Input Processing

**Token consumption**:
- Base rate: 32 tokens per second
- Independent of encoding or bitrate
- No resolution parameter available

**Processing limits**:
- Gemini 3.1 Pro: ~19 hours (2M tokens ÷ 32 tokens/sec)
- Gemini 3 Flash: ~9.5 hours (1M tokens ÷ 32 tokens/sec)
- Stored files auto-delete after 48 hours

<!-- section_id: "7e24b103-82a9-401f-bffb-8b8dbec41d70" -->
### PDF Document Processing

**Token calculation**:
- Flat rate: 258 tokens per page (regardless of content density)
- Native embedded text extracted without token charge
- Visual elements (charts, diagrams) charged at image rates

**Processing limits**:
- Maximum 50 MB file size
- Maximum 1,000 pages
- Pure text PDFs more efficient than scanned/image-heavy PDFs

**Optimization strategy**:
```
For scanned PDFs:
1. Pre-process with OCR tool to extract text
2. Send extracted text + images separately (if images needed)
3. Reduces token cost by ~80% for typical scans

Example: 100-page scanned PDF
- Native processing: 100 × 258 = 25,800 tokens
- Pre-processed text: 100 pages × ~300 words × 0.25 tokens/word = 7,500 tokens
- Savings: ~71%
```

---

<!-- section_id: "0d5bd813-ce04-48fa-bf31-6dd8f80ec27f" -->
## File Management and Upload Systems

<!-- section_id: "f5ea377b-b778-445b-9855-db2a1679a8fa" -->
### File API Architecture

#### Storage Specifications

| Property | Limit |
|----------|-------|
| Per-project storage | 20 GB total |
| Individual file size | 2 GB maximum |
| File lifetime | 48 hours from upload |
| Concurrent uploads | 10 (soft limit) |

**Key characteristics**:
- Ephemeral storage by design
- No persistence beyond 48 hours
- Files auto-deleted after TTL expiration
- No recovery after deletion

<!-- section_id: "51d7954e-88fc-4448-b839-d749c7460480" -->
### Upload Methods

#### Method 1: Inline Base64 (< 100 MB)

**Use case**: Rapid prototyping, embedded content, small media

```python
import base64

with open("image.jpg", "rb") as f:
    file_data = base64.standard_b64encode(f.read()).decode("utf-8")

response = model.generate_content({
    "parts": [
        {"inline_data": {"mime_type": "image/jpeg", "data": file_data}},
        {"text": "Analyze this image..."}
    ]
})
```

**Characteristics**:
- Synchronous upload/processing
- Simpler error handling
- No resumable upload support
- Best for files < 10 MB to avoid timeout

#### Method 2: Files API Upload (> 100 MB)

**Use case**: Large media files, production deployments

```python
import google.generativeai as genai

# Initialize Files API client
file_service = genai.files

# Upload file
uploaded_file = file_service.create(
    file=open("large_video.mp4", "rb"),
    mime_type="video/mp4"
)

# Use in generation request
response = model.generate_content({
    "parts": [
        {"file_data": {"mime_type": "video/mp4", "file_name": uploaded_file.name}},
        {"text": "Summarize this video..."}
    ]
})
```

**Characteristics**:
- Resumable uploads for network resilience
- Automatic chunking for large files
- File handle returned for reuse
- Handles failures gracefully

#### Method 3: External URLs (Public/Signed)

**Use case**: Content in cloud storage, avoiding upload/storage costs

```python
response = model.generate_content({
    "parts": [
        {"file_data": {"mime_type": "application/pdf", "file_name": "https://storage.googleapis.com/..."}},
        {"text": "Extract data from this PDF..."}
    ]
})
```

**URL requirements**:
- HTTPS only
- Public accessible OR with signed URL (valid up to 7 days)
- CORS headers must permit Gemini API domain

**Advantages**:
- No upload overhead
- No storage quota consumption
- Direct access from cloud storage
- Supports AWS S3, Azure Blob, GCS

<!-- section_id: "1446f321-37d4-48ea-bc15-ab1cdb4665ce" -->
### File Lifecycle Management

```
Upload → In-storage (0-48 hours) → Auto-deletion

Timeline for uploaded file:
T+0: Upload completes
T+0 to T+48h: File available for use
T+48h: File auto-deleted (no recovery)
```

**Management strategy for large-scale operations**:
```python
# Batch upload before processing
uploaded_files = []
for file in large_file_list:
    uploaded = file_service.create(file=open(file, "rb"))
    uploaded_files.append(uploaded)

# Process all within 48-hour window
for uploaded_file in uploaded_files:
    response = model.generate_content(...)

# Files auto-delete; no cleanup needed
```

---

<!-- section_id: "a8362e27-8fba-4ab3-810c-b316de916cc8" -->
## Function Calling and Tool Integration

<!-- section_id: "0cc987ce-0276-4275-80d7-3c7c315cf2d5" -->
### Function Declaration and Schema

Function declarations use JSON Schema format to specify callable functions:

```python
tools = [
    {
        "function_declarations": [
            {
                "name": "search_products",
                "description": "Search for products by category and price range",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "category": {
                            "type": "STRING",
                            "description": "Product category (electronics, books, etc.)"
                        },
                        "max_price": {
                            "type": "NUMBER",
                            "description": "Maximum price in USD"
                        },
                        "min_price": {
                            "type": "NUMBER",
                            "description": "Minimum price in USD"
                        }
                    },
                    "required": ["category"]
                }
            }
        ]
    }
]
```

<!-- section_id: "6a23dc83-a5c4-4351-9f18-cacb6a3f5005" -->
### Function Calling Flow

**Standard execution pattern**:

1. **Developer provides declarations**: Specify what functions exist
2. **Model analyzes request**: Determines if function calls needed
3. **Model returns function calls**: JSON with function name + arguments
4. **Developer executes**: Actual function implementation runs
5. **Developer returns result**: Function output back to model
6. **Model generates response**: Incorporates function output

**Example interaction**:

```python
# Step 1: User query
user_input = "Find me books under $30 in the science fiction category"

# Step 2: Model analyzes and returns
response = model.generate_content(
    user_input,
    tools=tools
)

# Step 3: Extract function call
function_call = response.content.parts[0].function_call
# Result: {"name": "search_products", "args": {"category": "science fiction", "max_price": 30}}

# Step 4: Developer executes function
books = search_products(
    category=function_call.args["category"],
    max_price=function_call.args["max_price"]
)

# Step 5: Return result to model
response = model.generate_content([
    {"role": "user", "parts": [{"text": user_input}]},
    {"role": "model", "parts": [{"function_call": function_call}]},
    {"role": "user", "parts": [{"function_result": {
        "name": "search_products",
        "response": books
    }}]}
])

# Step 6: Model's final response
print(response.text)  # "Here are some great science fiction books under $30..."
```

<!-- section_id: "187445d6-9eec-4359-a8ef-cf73111a9810" -->
### Multimodal Function Responses (Gemini 3+)

**New capability**: Function responses can include images, PDFs, and text

```python
function_result = {
    "name": "get_product_info",
    "response": {
        "text": "Product: ACME Widget X-2000",
        "image": "https://example.com/product.jpg",  # Returns image reference
        "specs_pdf": "/path/to/specs.pdf"  # Returns PDF reference
    }
}
```

**Use cases**:
- Product search with thumbnails
- Document extraction with visual proofs
- Code analysis with relevant code snippets
- Scientific analysis with supporting figures

<!-- section_id: "34c30c79-3099-4238-a88a-904d921ff079" -->
### Parallel Function Execution

Models can request multiple function calls simultaneously:

```python
# Model might return multiple calls in single response
function_calls = [
    {"name": "search_inventory", "args": {"product": "Widget"}},
    {"name": "get_price", "args": {"product": "Widget"}},
    {"name": "get_reviews", "args": {"product": "Widget"}}
]

# Developer can execute in parallel
from concurrent.futures import ThreadPoolExecutor

results = {}
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {
        executor.submit(search_inventory, **call["args"]): call["name"]
        for call in function_calls
    }
    for future in concurrent.futures.as_completed(futures):
        results[futures[future]] = future.result()
```

---

<!-- section_id: "21c052d3-0d9e-42cb-b107-2f4fdef81cc5" -->
## Context Caching and Optimization

<!-- section_id: "aee4e413-df26-44bd-b85e-d6c6c2ed1372" -->
### Implicit Caching (Automatic)

**Enabled by default** with no developer configuration required.

#### How it works:
1. System automatically caches request content
2. Subsequent requests with identical prefix tokens hit cache
3. Cached tokens charged at reduced rate
4. Cache invalidation handled automatically

#### Minimum token thresholds:
- Gemini 3.1 Pro: 4,096 tokens minimum
- Gemini 3 Pro: 4,096 tokens minimum
- Gemini 3 Flash: 1,024 tokens minimum

#### Cost structure for implicit caching:
```
Standard query:
Input tokens: 100,000 tokens × $2/million = $0.20

With implicit caching (cache hit):
Input tokens (cached): 90,000 × $0.20/million = $0.018
Input tokens (new): 10,000 × $2/million = $0.02
Total: $0.038 (81% cost reduction)
```

#### Optimization strategy:
```python
# Good: Consistent document prefix increases cache hits
document = load_large_document()

# Query 1
response1 = model.generate_content(f"{document}\n\nQuestion 1...")  # Cache miss

# Query 2
response2 = model.generate_content(f"{document}\n\nQuestion 2...")  # Cache hit

# Query 3
response3 = model.generate_content(f"{document}\n\nQuestion 3...")  # Cache hit
```

<!-- section_id: "f6b06187-0d14-4318-8aa7-3ddab98fe89b" -->
### Explicit Caching (Managed)

**Developer-controlled cache creation and TTL management**:

#### Cache creation:

```python
cache = genai.CachedContent.create(
    model="models/gemini-3-pro",
    display_name="Legal Contract Analysis Cache",
    system_instruction="You are a legal document expert...",
    contents=[{
        "role": "user",
        "parts": [
            {"file_data": {"mime_type": "application/pdf", "file_name": uploaded_contract}},
            {"text": "Prepare to answer questions about this contract."}
        ]
    }],
    ttl_seconds=3600  # 1 hour
)

cache_id = cache.name
```

#### Using cached content:

```python
response = model.generate_content(
    "What are the payment terms?",
    cache_name=cache_id
)
```

#### Cost structure for explicit caching:

| Component | Cost Formula | Example (100k tokens, 1hr) |
|-----------|--------------|---------------------------|
| Initial cache creation | Standard input rate | 100k × $2/1M = $0.20 |
| Per-request cached tokens | 10% of input rate | 90k × $0.20/1M = $0.018 |
| Per-request new tokens | Standard input rate | 10k × $2/1M = $0.02 |
| Storage cost | Per hour × cache size | $0.30 (depends on token rate) |
| Output tokens | Standard output rate | $12/1M output |

**Cost calculation example**:
```
Scenario: 100k-token contract cache used for 10 queries over 1 hour

Setup:
1. Create cache: 100k × $2/1M = $0.20
2. Storage: $0.30/hour × 1 = $0.30
3. 10 queries × (9k cached × $0.20/1M + 1k new × $2/1M + 1k output × $12/1M)
   = 10 × ($0.0018 + $0.002 + $0.012) = 10 × $0.0158 = $0.158

Total: $0.20 + $0.30 + $0.158 = $0.658
Per-query: $0.0658
Without caching: 10 × $0.02 input + 10 × $0.012 output = $0.32
Savings: 79.4% reduction
```

#### TTL and cache duration trade-offs:

| TTL | Storage Cost/Hour | Use Case |
|-----|------------------|----------|
| 5 minutes | $0.025 | Quick bursts of queries |
| 30 minutes | $0.15 | Moderate session duration |
| 1 hour | $0.30 | Extended analysis sessions |
| 24 hours | $7.20 | Long-lived reference caches |

**Recommendation**: Match TTL to expected usage window to optimize cost.

---

<!-- section_id: "65125fb7-eb7f-4b26-a4c1-d12f2afb8ce0" -->
## Pricing and Cost Models

<!-- section_id: "65a8fd7f-d04d-4469-9f1d-079546931ff3" -->
### Base Pricing Structure (Gemini 3 / 3.1 Pro)

#### Standard pricing (input < 200k tokens):
```
Input:  $2.00 per million tokens
Output: $12.00 per million tokens
```

#### Long-context pricing (input >= 200k tokens):
```
Input:  $4.00 per million tokens (+100%)
Output: $18.00 per million tokens (+50%)
```

#### Cost calculation:
```python
def calculate_cost(input_tokens, output_tokens):
    if input_tokens <= 200_000:
        input_cost = (input_tokens / 1_000_000) * 2.00
        output_cost = (output_tokens / 1_000_000) * 12.00
    else:
        input_cost = (input_tokens / 1_000_000) * 4.00
        output_cost = (output_tokens / 1_000_000) * 18.00
    return input_cost + output_cost

# Examples:
# 50k input, 5k output: $0.10 + $0.06 = $0.16
# 300k input, 10k output: $1.20 + $0.18 = $1.38
# 1M input, 100k output: $4.00 + $1.20 = $5.20
```

<!-- section_id: "ca09943c-cc4e-4be3-935c-68a4ae789c42" -->
### Gemini 3 Flash Pricing

```
Input:  $0.50 per million tokens (4x cheaper than Pro)
Output: $3.00 per million tokens (4x cheaper than Pro)
```

<!-- section_id: "a5089dc4-966d-4431-ad28-1db956594f27" -->
### Context Caching Pricing

| Component | Gemini 3 Pro | Gemini 3 Flash |
|-----------|----------|----------|
| Initial write | $2/1M input | $0.50/1M input |
| Cached tokens | $0.20/1M input (10% of standard) | N/A |
| Storage | $0.30/1M tokens/hour | $0.30/1M tokens/hour |
| Output | $12/1M | $3/1M |

<!-- section_id: "cda4852f-30e8-4ee8-a6b8-0edf80131bb9" -->
### Batch API Pricing (50% discount)

```
Standard request: $0.20 input + $0.012 output = $0.212
Batch request:   $0.10 input + $0.006 output = $0.106 (50% discount)
```

**Batch processing conditions**:
- Results delivered within 24 hours
- Cost savings: 50% on input and output tokens
- Max quota: Higher than synchronous requests
- Use case: Non-latency-critical bulk operations

<!-- section_id: "61c9f216-c4ba-4d61-a211-bea610434127" -->
### Grounding Cost Structure

#### Google Search grounding:
```
Cost: Per search query executed (not per request)
Charges apply regardless of search success
No transparent unit cost published
```

#### Google Maps grounding:
```
Cost: Currently free (may change as feature matures)
Available on Gemini 3 Flash and some other models
```

<!-- section_id: "ccabdca2-6503-4d8f-913f-2fc4344a1441" -->
### File Upload and Storage Costs

```
Upload:         FREE (no token charge)
Storage:        NO DIRECT COST (included with project quota)
Usage:          Standard input token rates
Deletion:       Automatic after 48 hours (no manual cleanup needed)
```

---

<!-- section_id: "b02feede-fb46-4ac8-8560-142973bf1838" -->
## Token Counting Methodology

<!-- section_id: "0bd52f70-1197-4211-b566-ab1c82f17f8a" -->
### Basic Formula

```
English text: ~4 characters = 1 token
Average English: ~¾ words = 1 token
```

<!-- section_id: "f476dd23-26c5-4116-947f-87bf7376eaff" -->
### Precise Token Counting via API

**Endpoint**:
```
POST https://generativelanguage.googleapis.com/v1beta/models/{model}:countTokens
```

**Python implementation**:
```python
response = model.count_tokens("Your text here")
input_tokens = response.total_tokens

# For multimodal content:
response = model.count_tokens([
    {"text": "Analyze this image:"},
    {"file_data": {"mime_type": "image/jpeg", "file_name": uploaded_file.name}}
])
```

<!-- section_id: "1afacf9f-a3d6-47d2-ae70-95c241ccb991" -->
### Multimodal Token Calculations

#### Text:
```
Characters: ~4 per token
Words: ~0.75 per token
English text token = 0.75 words = 3-4 characters
```

#### Images:
```
Small (< 384px): 258 tokens flat
Medium (384-768px): 258 tokens × (ceil(w/768) × ceil(h/768))
Large (768px+): 258 tokens × (ceil(w/768) × ceil(h/768))

media_resolution_high: max 1,120 tokens/image
media_resolution_medium: max 560 tokens/image
media_resolution_low: max 70 tokens/image
```

#### Video:
```
Base: 263 tokens/second (at 1 fps)
Audio (if included): +32 tokens/second
Duration multiplier: 10s = 2,630 tokens (video) + 320 (audio) = 2,950 total
```

#### Audio:
```
Fixed rate: 32 tokens/second
Duration multiplier: 1 hour = 3,600s × 32 = 115,200 tokens
1 minute = 60s × 32 = 1,920 tokens
```

#### PDFs:
```
Per-page: 258 tokens per page (fixed, regardless of content)
Text extraction: Native embedded text extracted without charge
100-page PDF: 100 × 258 = 25,800 tokens
```

<!-- section_id: "fa22e9ff-77da-4799-9f09-c69db8556d45" -->
### Token Counting Examples

```python
# Example 1: Mixed content
text = "Analyze the following image and provide insights."  # ~40 tokens
image_file = uploaded_image  # 1,120 tokens (high res)
total_estimate = 40 + 1,120 = 1,160 tokens

# Example 2: Video with audio
video_duration = 60  # seconds
video_tokens = 60 × 263 = 15,780
audio_tokens = 60 × 32 = 1,920
total_estimate = 15,780 + 1,920 = 17,700 tokens

# Example 3: Long document + query
document_pages = 500
document_tokens = 500 × 258 = 129,000  # If PDF
query_text = "Summarize this document"  # ~5 tokens
total = 129,005 tokens

# Cost at standard rate:
input_cost = (129_005 / 1_000_000) * 2.00 = $0.258
```

<!-- section_id: "b5eb225f-c263-4b2d-bb4b-4e734ab1d1e4" -->
### Token Counting Strategies for Production

```python
# Strategy 1: Pre-calculate for budget planning
def estimate_operation_cost(document_pages, expected_queries):
    document_tokens = document_pages * 258
    avg_query_tokens = 50
    avg_output_tokens = 200

    total_input = document_tokens + (expected_queries * avg_query_tokens)
    total_output = expected_queries * avg_output_tokens

    input_cost = (total_input / 1_000_000) * 2.00
    output_cost = (total_output / 1_000_000) * 12.00

    return input_cost + output_cost

# Strategy 2: Track actual consumption
def track_request_cost(response):
    usage = response.usage_metadata
    input_tokens = usage.prompt_tokens
    output_tokens = usage.candidates[0].content.usage_metadata.output_tokens

    # Calculate actual cost
    if input_tokens <= 200_000:
        cost = (input_tokens / 1_000_000) * 2.00 + (output_tokens / 1_000_000) * 12.00
    else:
        cost = (input_tokens / 1_000_000) * 4.00 + (output_tokens / 1_000_000) * 18.00

    return cost, input_tokens, output_tokens
```

---

<!-- section_id: "8187def9-d191-4e53-8cbf-55b61fbc0fb9" -->
## Session and Conversation Management

<!-- section_id: "8f80d9ff-449f-405c-b3ce-4bb42be64ba6" -->
### Stateful Conversation with Interactions API

**Architecture**: Server maintains conversation history using interaction IDs.

#### Creating an interaction:
```python
response = client.models.interactions.create(
    model="models/gemini-3-pro",
    contents=[
        {"role": "user", "parts": [{"text": "What is machine learning?"}]},
        {"role": "model", "parts": [{"text": "Machine learning is..."}]}
    ]
)

interaction_id = response.name
# Format: "projects/{project}/locations/{location}/interactions/{interaction_id}"
```

#### Continuing conversation:
```python
# Subsequent turn: only provide new user message
response = client.models.interactions.create(
    model="models/gemini-3-pro",
    interaction=interaction_id,
    contents=[
        {"role": "user", "parts": [{"text": "Can you explain neural networks?"}]}
    ]
)
```

**Key advantages**:
- Reduced bandwidth (no history re-transmission)
- Server-managed state consistency
- Simpler client implementation
- Better for distributed systems

**Key constraints**:
- Interaction lifetime: Limited by backend (typically 24-72 hours)
- State loss: If interaction ID lost, context unavailable
- Stateless fallback: Can always revert to manual history management

<!-- section_id: "24a92dbf-b5ae-4cf9-98f3-f5dc00ee9cb7" -->
### Live API Session Management

**Use case**: Real-time voice/video conversations with WebSocket streaming.

#### Session limitations:
- Audio-only: 15 minutes max duration
- Audio-video: 2 minutes max duration
- WebSocket connection: ~10 minutes max before reconnection needed

#### Session resumption:

```python
# Initial session creation
session_response = create_session()
session_id = session_response["session_id"]

# Periodic resumption token updates (every 30-60 seconds)
resumption_events = listen_for_updates()
current_resumption_token = resumption_events.latest_resumption_token

# If connection drops:
resume_response = create_session(
    resumption_token=current_resumption_token
)

# Valid for up to 2 hours after original session end
```

**Resumption token validity**: 2 hours after session termination

**Implementation pattern for resilient conversations**:
```python
MAX_SESSION_DURATION = 900  # 15 minutes
RECONNECT_INTERVAL = 300    # 5 minutes

session = None
last_resumption_token = None
session_start_time = None

while True:
    if not session or (time.time() - session_start_time) > MAX_SESSION_DURATION:
        session = create_session(resumption_token=last_resumption_token)
        session_start_time = time.time()

    # Process audio/video for up to RECONNECT_INTERVAL
    # Update last_resumption_token from events

    if (time.time() - session_start_time) % RECONNECT_INTERVAL == 0:
        # Proactive reconnect to refresh connection
        session = create_session(resumption_token=last_resumption_token)
        session_start_time = time.time()
```

---

<!-- section_id: "e0c51e51-467d-4ffe-afae-0283a81c1178" -->
## Thinking/Reasoning Mode

<!-- section_id: "0379f384-28af-41af-9bfc-9fb7f77c788a" -->
### Extended Thinking (Gemini 3.1 Pro)

**Purpose**: Enable models to engage in explicit reasoning processes before answering complex questions.

#### Enabling thinking mode:

```python
response = model.generate_content(
    "Solve this complex problem: [problem statement]",
    config=GenerateContentConfig(
        thinking_config={
            "thinking_budget_tokens": 10000  # Allocate tokens for reasoning
        }
    )
)

# Access thinking process
thinking = response.content.parts[0].thinking.value
answer = response.content.parts[1].text
```

#### Configuration:

| Setting | Value | Impact |
|---------|-------|--------|
| `thinking_budget_tokens` | 1,000-200,000 | Higher budget = deeper reasoning |
| Typical range | 5,000-20,000 | Good balance for complex problems |

#### Cost implications:

```
Thinking tokens billed at DOUBLE the standard input rate
thinking_tokens: 10,000 × $4/1M (input rate for long context) = $0.04
Output tokens: 5,000 × $12/1M = $0.06
Total: $0.10 for single complex reasoning request
```

#### Use cases:

- Mathematical problem solving
- Complex logical reasoning
- Multi-step decision analysis
- Scientific hypothesis evaluation
- Code architecture design

---

<!-- section_id: "78e50bd2-aed8-4e20-8da9-75f59061d34e" -->
## Structured Outputs and Validation

<!-- section_id: "e09f5479-d69e-4dc7-9361-7d2603b4d654" -->
### Specification Using JSON Schema

```python
response_schema = {
    "type": "object",
    "properties": {
        "product_name": {"type": "string"},
        "price": {"type": "number"},
        "in_stock": {"type": "boolean"},
        "categories": {
            "type": "array",
            "items": {"type": "string"}
        },
        "details": {
            "type": "object",
            "properties": {
                "color": {"type": "string"},
                "size": {"type": "string"}
            },
            "required": ["color"]
        }
    },
    "required": ["product_name", "price", "in_stock"]
}

response = model.generate_content(
    "Extract product information from: [product description]",
    config=GenerateContentConfig(
        response_mime_type="application/json",
        response_json_schema=response_schema
    )
)

# Guaranteed to be valid JSON conforming to schema
product_data = json.loads(response.text)
```

<!-- section_id: "1c388f30-286a-4d66-af35-5072447ade9d" -->
### Advanced JSON Schema Features (Gemini 3+)

| Feature | Syntax | Example |
|---------|--------|---------|
| Unions/anyOf | `"anyOf": [schema1, schema2]` | Multiple valid types |
| Recursion | `"$ref": "#/definitions/node"` | Tree structures |
| Constraints | `"minimum": 0, "maximum": 100` | Numeric ranges |
| Null values | `"type": ["string", "null"]` | Optional fields |
| Tuples | `"prefixItems": [schema1, schema2]` | Fixed-length arrays |
| Additional properties | `"additionalProperties": false` | Strict field lists |

<!-- section_id: "d113688c-0379-4a44-968b-dd32ef69f66b" -->
### Validation Best Practices

**Important**: Structured outputs guarantee syntactic correctness only, not semantic correctness.

```python
def extract_and_validate(text, response_schema):
    response = model.generate_content(
        f"Extract data: {text}",
        config=GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=response_schema
        )
    )

    # Step 1: Syntactic validation (automatic via schema)
    data = json.loads(response.text)  # Guaranteed valid JSON

    # Step 2: Semantic validation (application-specific)
    try:
        # Custom business logic validation
        if "price" in data and data["price"] < 0:
            return None, "Price cannot be negative"

        if "inventory" in data and data["inventory"] > MAX_INVENTORY:
            return None, "Inventory exceeds maximum"

        return data, None
    except Exception as e:
        return None, str(e)

# Usage
data, error = extract_and_validate(product_text, schema)
if error:
    # Re-request with clarification
    handle_extraction_error(error)
```

---

<!-- section_id: "09b6651a-6804-46c4-8424-67249ae4df10" -->
## Grounding and Enhanced Capabilities

<!-- section_id: "63865f14-e6df-4d0d-a9a9-4940f4a69cd5" -->
### Google Search Grounding

**Integration**: Automatic fact verification and information retrieval.

#### Enabling search grounding:

```python
response = model.generate_content(
    "What are the latest developments in quantum computing?",
    tools=[Tool(google_search=GoogleSearchRetrievalTool())]
)
```

#### Cost model:

```
Charges per search query executed (not per request)
Applies regardless of search success
Transparent unit cost: NOT published by Google
Estimated: $0.10-0.50 per search query based on vendor reports
```

#### Practical implications:

```
Scenario: Answering user question triggers 3 search queries
Query cost: ~$0.15-1.50 (estimate)
No refund if searches don't improve answer quality
Models may execute multiple searches without user awareness
```

#### Best practices:

```python
# Bad: May trigger excessive searches
response = model.generate_content(
    "Tell me everything about quantum computing",
    tools=[Tool(google_search=GoogleSearchRetrievalTool())]
)

# Better: Constrain to specific retrieval need
response = model.generate_content(
    "What did Google announce about quantum computing in the past month?",
    tools=[Tool(google_search=GoogleSearchRetrievalTool())]
)
```

<!-- section_id: "275f8375-ae12-47c6-b02b-71e28f33380f" -->
### Google Maps Grounding

**Integration**: Location-aware responses with real-world data.

#### Capabilities:

- Business information retrieval
- Current hours of operation
- Review aggregation
- Navigational data
- Real-time location insights

#### Current pricing:

```
FREE (as of February 2026)
Availability: Gemini 3 Flash and certain other models
Note: May change as feature matures beyond general availability
```

#### Use case example:

```python
response = model.generate_content(
    "Find highly-rated Italian restaurants near Times Square open right now",
    tools=[Tool(google_maps=GoogleMapsRetrievalTool())]
)
# Returns: Name, address, hours, ratings, navigation link
```

---

<!-- section_id: "4317cdfd-1fa0-406c-969d-da38f58d4d70" -->
## API Endpoints and Error Handling

<!-- section_id: "6d9895c5-3778-4ec4-aa59-2044520881ef" -->
### REST API Endpoints

**Base URL**: `https://generativelanguage.googleapis.com/v1beta/`

| Operation | Endpoint | Method | Purpose |
|-----------|----------|--------|---------|
| Generate Content | `/models/{model}:generateContent` | POST | Single sync request |
| Stream Content | `/models/{model}:streamGenerateContent` | POST | Streaming SSE response |
| Count Tokens | `/models/{model}:countTokens` | POST | Token estimation |
| Batch Generate | `/models/{model}:batchGenerateContent` | POST | Batch processing |
| Create File | `/files` | POST | Upload file to API |
| List Files | `/files` | GET | List uploaded files |
| Delete File | `/files/{fileId}` | DELETE | Remove file |
| Create Cache | `/caches` | POST | Create context cache |
| List Caches | `/caches` | GET | List caches |
| Update Cache | `/caches/{cacheId}` | PATCH | Update TTL |
| Create Interaction | `/interactions` | POST | Create stateful conversation |

<!-- section_id: "6803185a-eac4-41cd-825c-17096d083558" -->
### Error Response Format

```json
{
  "error": {
    "code": 400,
    "status": "INVALID_ARGUMENT",
    "message": "Invalid request: [detailed reason]"
  }
}
```

<!-- section_id: "f7abeb71-21c7-482a-90f4-bdc841f5109a" -->
### Error Codes and Handling

| HTTP | Status | Cause | Recovery |
|------|--------|-------|----------|
| 400 | INVALID_ARGUMENT | Malformed request/invalid parameters | Validate input format, check model compatibility |
| 400 | FAILED_PRECONDITION | Unsupported feature for model | Check model capabilities |
| 401 | UNAUTHENTICATED | Invalid API key | Re-authenticate, verify key validity |
| 403 | PERMISSION_DENIED | Insufficient permissions | Enable APIs in Cloud Console, add IAM roles (wait 1-2 min) |
| 404 | NOT_FOUND | Resource doesn't exist | Verify project ID, resource names |
| 429 | RESOURCE_EXHAUSTED | Rate limit or quota exceeded | Wait for reset, increase quota in Console |
| 500 | INTERNAL | Server error | Retry with exponential backoff |
| 504 | DEADLINE_EXCEEDED | Timeout (e.g., file URLs expire after 30s) | Retry request, ensure fast processing |

<!-- section_id: "052c88a0-5e92-4c6d-8248-ff2ceaa95e3c" -->
### Retry Strategy for Production

```python
import time
import random

def call_with_retry(model, prompt, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        try:
            return model.generate_content(prompt)
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e):
                # Quota exceeded - wait and retry
                wait_time = base_delay * (2 ** attempt) + random.random()
                time.sleep(wait_time)
            elif "DEADLINE_EXCEEDED" in str(e):
                # Timeout - retry immediately
                continue
            else:
                # Other errors - propagate
                raise

    raise Exception(f"Failed after {max_retries} retries")
```

---

<!-- section_id: "fe668ca8-55cc-4576-9a29-a33e7d553981" -->
## Rate Limits and Quota Management

<!-- section_id: "45b3a3a4-d282-43b7-b590-7b786dc95598" -->
### Request Rate Limits

| Metric | Limit | Notes |
|--------|-------|-------|
| Requests per minute (RPM) | Project-dependent | Sandbox: ~100 RPM; Paid: ~1,000+ RPM |
| Queries per day (QPD) | Project-dependent | Sandbox: 1,500; Paid: Unlimited |
| Tokens per minute (TPM) | Project-dependent | Scales with billing tier |

**Important**: Exact limits vary by project, model, and account tier. Check Google Cloud Console for specific quotas.

<!-- section_id: "b78a5dbd-b1ca-4a72-9be5-72d492e8d356" -->
### Quota Management

#### Monitoring quotas:
1. Google Cloud Console → APIs & Services → Quotas
2. Filter by "Generative AI API"
3. View current usage vs. limits

#### Requesting quota increases:
```
1. Cloud Console → Quotas → Select quota type
2. Click "Edit Quotas"
3. Enter new limit
4. Submit request (typically approved within 1 hour)
```

#### Handling quota exceeded:

```python
def handle_rate_limit(error):
    if "RESOURCE_EXHAUSTED" in str(error):
        # Option 1: Wait for reset (daily quotas reset at midnight UTC)
        time.sleep(86400)  # 24 hours

        # Option 2: Request quota increase
        notify_admin("Request quota increase in Google Cloud Console")

        # Option 3: Batch processing (lower rate limits)
        use_batch_api()
```

<!-- section_id: "4338c516-6353-4165-bf80-10cb57d8bab1" -->
### Token-Based Rate Limiting

Quotas are often expressed as tokens per minute (TPM) rather than requests per minute:

```
Example:
- TPM limit: 1,000,000
- Average request: 50,000 tokens
- Concurrent requests: 20 requests/minute possible

Calculation:
1,000,000 tokens/minute ÷ 50,000 tokens/request = 20 requests/minute
```

---

<!-- section_id: "ce923c31-cb4e-4098-b2fb-f5b9333417e3" -->
## Summary: Key Takeaways for Production Implementation

<!-- section_id: "617492db-d0f0-4bfb-b4dd-52cf3be0e95c" -->
### Cost Optimization Checklist

- [ ] Use Gemini 3 Flash for high-volume, lower-accuracy-requirement tasks (4x cheaper)
- [ ] Implement context caching for large static content reused across queries
- [ ] Use batch API for non-latency-critical bulk operations (50% discount)
- [ ] Pre-calculate token consumption to estimate budgets accurately
- [ ] Monitor actual token consumption via `usage_metadata` in responses
- [ ] Implement rate limiting and quota monitoring in Cloud Console

<!-- section_id: "ce8dc68e-66fd-4816-910b-0ef5edda751e" -->
### Performance Optimization Checklist

- [ ] Set explicit `max_output_tokens` for controlled output length
- [ ] Use appropriate `media_resolution` for images (MEDIUM for most PDFs)
- [ ] Pre-process scanned PDFs with OCR to reduce token consumption
- [ ] Implement connection resumption for Live API sessions
- [ ] Use parallel function calling where possible
- [ ] Cache frequently-accessed context with explicit caching API

<!-- section_id: "ef01cc3a-7335-4456-860a-3da87c09949b" -->
### Reliability Checklist

- [ ] Implement exponential backoff retry logic for transient errors
- [ ] Handle 429 RESOURCE_EXHAUSTED with quota-aware waiting
- [ ] Monitor API error rates and set up alerting
- [ ] Use Interactions API for stateful conversations (vs. manual history management)
- [ ] Validate structured outputs with custom business logic
- [ ] Test multimodal content with `countTokens` before deployment

<!-- section_id: "2e7e8375-59c7-4c1e-b4e4-b0e33297ea23" -->
### Security Checklist

- [ ] Rotate API keys regularly
- [ ] Use environment variables for credential storage (never hardcode)
- [ ] Verify HTTPS for all external URL references
- [ ] Use signed URLs for private cloud storage access
- [ ] Limit function calling declarations to necessary functions only
- [ ] Sanitize user input before passing to grounding tools

---

<!-- section_id: "77c31d86-0cc7-4cb1-88e8-aa62c06c3b04" -->
## References

1. Google Generative AI Documentation: https://ai.google.dev/
2. Google Cloud Vertex AI Documentation: https://cloud.google.com/vertex-ai
3. Gemini API Cookbook: https://github.com/google-gemini/cookbook
4. Google AI Studio: https://aistudio.google.com/
5. Firebase AI Logic Documentation: https://firebase.google.com/docs/ai-logic
6. Official Gemini Model Cards: https://deepmind.google/models/

---

**Document Status**: Complete and verified as of February 2026

**Last Verified Against**:
- Gemini 3.1 Pro API specification
- Google Cloud pricing page (2026)
- Official documentation and cookbook examples

**Version History**:
- v1.0 (2026-02-27): Initial comprehensive reference document
