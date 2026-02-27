#!/usr/bin/env node
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const scriptPath = path.join(currentDir, 'mcp-phoneme-admin.mjs');

const child = spawn(
  process.execPath,
  [scriptPath],
  {
    stdio: 'inherit',
    env: {
      ...process.env,
      RUN_NAVIGATION_MODE: 'realistic',
    },
  },
);

child.on('exit', (code, signal) => {
  if (signal) {
    process.exit(1);
  } else {
    process.exit(code ?? 0);
  }
});
