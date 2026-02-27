#!/usr/bin/env node
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const BASE_URL = process.env.MCP_URL ?? 'http://localhost:3334/mcp';

async function main() {
  const client = new Client(
    {
      name: 'codex-cli',
      version: '0.1.0',
    },
    {
      capabilities: {
        tools: {},
        resources: {},
        prompts: {},
      },
    },
  );

  client.onerror = (err) => {
    console.error('[mcp-client] error', err);
  };

  const transport = new StreamableHTTPClientTransport(new URL(BASE_URL));
  await client.connect(transport);

  const tools = await client.listTools();
  console.log('Tools:', JSON.stringify(tools, null, 2));

  await client.close();
}

main().catch((err) => {
  console.error('[mcp-client] failed', err);
  process.exit(1);
});
