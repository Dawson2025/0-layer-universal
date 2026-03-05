---
resource_id: "c4676dcd-20db-467d-a0cb-722891e30555"
resource_type: "knowledge"
resource_name: "mcp_extensions"
---
## MCP Extension Patterns

This document explains how to extend the AI manager hierarchy system with Model Context Protocol (MCP) servers and tools.

MCP provides a standardized way to expose tools and data sources to AI agents.

---

## 1. MCP Overview

**Model Context Protocol** is a protocol for connecting AI agents to external tools and data sources through a standardized interface.

**Key Concepts:**
- **MCP Server**: Exposes tools and resources
- **MCP Client**: AI agent that calls tools
- **Tools**: Functions the agent can invoke
- **Resources**: Data sources the agent can read

---

## 2. Adding MCP Servers to the Hierarchy

### 2.1 Layer-Specific MCP Configuration

Each layer can have its own MCP servers:

```yaml
# layer_2/auth-system/mcp_config.yaml
mcp_servers:
  # Authentication-specific tools
  auth_validator:
    command: "npx"
    args: ["@myorg/auth-validator-mcp"]
    env:
      AUTH_VALIDATION_MODE: "strict"

  # Password strength checker
  password_tools:
    command: "python"
    args: ["-m", "password_mcp_server"]

  # Database access (scoped to auth tables)
  auth_db:
    command: "mcp-server-database"
    args: ["--schema", "auth", "--read-only"]
    env:
      DATABASE_URL: "${AUTH_DB_URL}"
```

### 2.2 Tool Inheritance

Tools available at layer L are also available at L+1:

```
L0 (Universal):
  - filesystem tools
  - git tools
  - web search

L1 (Project):
  - inherits L0 tools
  + project-specific database
  + CI/CD tools

L2 (Feature):
  - inherits L0, L1 tools
  + feature-specific validators
  + domain-specific APIs

L3 (Component):
  - inherits L0, L1, L2 tools
  + component test runners
```

---

## 3. Common MCP Server Patterns

### 3.1 Filesystem Server (Universal)

```python
# mcp_servers/filesystem/server.py
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("filesystem")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="read_file",
            description="Read a file from the filesystem",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path to read"},
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="write_file",
            description="Write content to a file",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["path", "content"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name, arguments):
    if name == "read_file":
        with open(arguments["path"]) as f:
            content = f.read()
        return [TextContent(type="text", text=content)]

    elif name == "write_file":
        with open(arguments["path"], "w") as f:
            f.write(arguments["content"])
        return [TextContent(type="text", text="File written successfully")]
```

### 3.2 Database Server (Project-Level)

```python
# mcp_servers/database/server.py
from mcp.server import Server
import psycopg2

server = Server("database")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="query_database",
            description="Execute SQL query (read-only)",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL SELECT query"}
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name, arguments):
    if name == "query_database":
        # Enforce read-only
        if not arguments["query"].strip().upper().startswith("SELECT"):
            raise ValueError("Only SELECT queries allowed")

        # Execute query
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        cursor = conn.cursor()
        cursor.execute(arguments["query"])
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return [TextContent(type="text", text=json.dumps(results))]
```

### 3.3 API Client Server (Feature-Level)

```python
# mcp_servers/stripe_api/server.py
from mcp.server import Server
import stripe

server = Server("stripe_api")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="create_payment_intent",
            description="Create Stripe payment intent",
            inputSchema={
                "type": "object",
                "properties": {
                    "amount": {"type": "number"},
                    "currency": {"type": "string"}
                },
                "required": ["amount", "currency"]
            }
        ),
        Tool(
            name="get_customer",
            description="Retrieve customer information",
            inputSchema={
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string"}
                },
                "required": ["customer_id"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name, arguments):
    stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

    if name == "create_payment_intent":
        intent = stripe.PaymentIntent.create(
            amount=arguments["amount"],
            currency=arguments["currency"]
        )
        return [TextContent(type="text", text=json.dumps(intent))]

    elif name == "get_customer":
        customer = stripe.Customer.retrieve(arguments["customer_id"])
        return [TextContent(type="text", text=json.dumps(customer))]
```

---

## 4. Tool Discovery and Loading

### 4.1 Automatic Tool Discovery

```python
def discover_mcp_servers(layer_path):
    """Discover all MCP servers configured for a layer."""

    # Load config
    config_path = os.path.join(layer_path, "mcp_config.yaml")
    if not os.path.exists(config_path):
        return []

    with open(config_path) as f:
        config = yaml.safe_load(f)

    servers = []
    for server_name, server_config in config.get("mcp_servers", {}).items():
        servers.append({
            "name": server_name,
            "command": server_config["command"],
            "args": server_config.get("args", []),
            "env": server_config.get("env", {})
        })

    return servers

def load_all_tools(layer_path):
    """Load tools from this layer and all parent layers."""

    tools = []

    # Walk up the layer hierarchy
    current = layer_path
    while current:
        servers = discover_mcp_servers(current)

        for server in servers:
            # Start MCP server
            client = start_mcp_server(server)

            # List tools
            server_tools = client.list_tools()
            tools.extend(server_tools)

        # Move to parent layer
        current = get_parent_layer(current)

    return tools
```

### 4.2 Tool Injection into Agents

**Claude Code:**
```python
def inject_mcp_tools_claude(layer_path, handoff_id):
    """Make MCP tools available to Claude Code agent."""

    tools = load_all_tools(layer_path)

    # Start Claude with tools
    subprocess.run([
        "claude-code",
        "--tools", json.dumps(tools),
        "process-handoff", handoff_id
    ])
```

**Gemini CLI:**
```python
def inject_mcp_tools_gemini(layer_path, handoff_id):
    """Make MCP tools available to Gemini agent."""

    # Gemini supports function calling
    tools = load_all_tools(layer_path)

    # Convert to Gemini function declarations
    function_declarations = convert_to_gemini_format(tools)

    # Start Gemini with tools
    subprocess.run([
        "gemini",
        "--tools", json.dumps(function_declarations),
        "process", handoff_id
    ])
```

---

## 5. Custom MCP Server Template

### 5.1 Server Skeleton

```python
# my_custom_mcp_server/server.py
from mcp.server import Server
from mcp.types import Tool, TextContent, Resource
import asyncio

# Initialize server
server = Server("my_custom_server")

# List available tools
@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="my_tool",
            description="Description of what this tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {"type": "string", "description": "First parameter"},
                    "param2": {"type": "number", "description": "Second parameter"}
                },
                "required": ["param1"]
            }
        )
    ]

# Handle tool calls
@server.call_tool()
async def call_tool(name, arguments):
    if name == "my_tool":
        # Implement tool logic
        result = do_something(arguments["param1"], arguments.get("param2"))

        return [TextContent(type="text", text=str(result))]

    else:
        raise ValueError(f"Unknown tool: {name}")

# Optional: List resources (data sources)
@server.list_resources()
async def list_resources():
    return [
        Resource(
            uri="custom://data/source1",
            name="Data Source 1",
            mimeType="application/json",
            description="Example data source"
        )
    ]

# Optional: Read resources
@server.read_resource()
async def read_resource(uri):
    if uri == "custom://data/source1":
        data = {"example": "data"}
        return [TextContent(type="text", text=json.dumps(data))]

# Run server
if __name__ == "__main__":
    asyncio.run(server.run())
```

### 5.2 Server Configuration

```yaml
# mcp_config.yaml entry
mcp_servers:
  my_custom_server:
    command: "python"
    args: ["-m", "my_custom_mcp_server.server"]
    env:
      CUSTOM_API_KEY: "${MY_API_KEY}"
      LOG_LEVEL: "info"
```

---

## 6. Security Considerations

### 6.1 Tool Sandboxing

```python
class SecureMCPServer(Server):
    """MCP server with security boundaries."""

    def __init__(self, name, allowed_paths=None, dangerous_tools=None):
        super().__init__(name)
        self.allowed_paths = allowed_paths or []
        self.dangerous_tools = dangerous_tools or []

    async def call_tool(self, name, arguments):
        # Check if tool is allowed
        if name in self.dangerous_tools:
            raise PermissionError(f"Tool {name} is not allowed")

        # Validate file paths
        if "path" in arguments:
            self.validate_path(arguments["path"])

        # Call actual tool
        return await super().call_tool(name, arguments)

    def validate_path(self, path):
        """Ensure path is within allowed boundaries."""
        resolved = os.path.realpath(path)

        if not any(resolved.startswith(allowed) for allowed in self.allowed_paths):
            raise PermissionError(f"Path not allowed: {path}")
```

### 6.2 Rate Limiting MCP Calls

```python
class RateLimitedMCPClient:
    """Client that rate limits tool calls."""

    def __init__(self, server, calls_per_minute=60):
        self.server = server
        self.rate_limiter = RateLimiter(calls_per_minute / 60)

    async def call_tool(self, name, arguments):
        """Call tool with rate limiting."""
        self.rate_limiter.acquire()
        return await self.server.call_tool(name, arguments)
```

---

## 7. Testing MCP Servers

```python
import pytest
from mcp.client import Client

@pytest.mark.asyncio
async def test_my_tool():
    """Test MCP server tool."""

    # Start server
    server_process = start_server("my_custom_server")

    # Connect client
    client = Client()
    await client.connect(server_process)

    # List tools
    tools = await client.list_tools()
    assert any(t.name == "my_tool" for t in tools)

    # Call tool
    result = await client.call_tool("my_tool", {"param1": "test"})
    assert result[0].text == "expected_output"

    # Cleanup
    await client.disconnect()
    server_process.terminate()
```

---

## 8. Summary

MCP servers provide a standardized way to extend agent capabilities:

1. **Filesystem, Database, API Clients**: Common server patterns
2. **Layer-Specific Tools**: Inherit tools from parent layers
3. **Automatic Discovery**: Load tools based on configuration
4. **Security**: Sandbox tools, rate limit, validate inputs
5. **Testing**: Unit test servers before deployment

Use MCP to give agents safe, controlled access to external systems while maintaining the handoff protocol as the primary coordination mechanism.
