#!/usr/bin/env node

import { watch } from 'fs';
import { resolve } from 'path';
import { spawn } from 'child_process';

const CONTENT_ROOT = resolve('src/content/saber');
const npmCmd = process.platform === 'win32' ? 'npm.cmd' : 'npm';

let running = false;
let pendingReason = null;
let debounceTimer = null;

function runRefresh(reason) {
  if (running) {
    pendingReason = reason;
    return;
  }

  running = true;
  const startedAt = new Date().toLocaleTimeString();
  console.log(`\n[workshops-watch] ${startedAt} -> refresh (${reason})`);

  const child = spawn(npmCmd, ['run', 'workshops:refresh:dev'], {
    stdio: 'inherit',
    shell: false,
  });

  child.on('exit', (code) => {
    running = false;
    const finishedAt = new Date().toLocaleTimeString();
    console.log(`[workshops-watch] ${finishedAt} -> done (exit ${code ?? 'unknown'})`);

    if (pendingReason) {
      const queued = pendingReason;
      pendingReason = null;
      runRefresh(`queued:${queued}`);
    }
  });
}

function scheduleRefresh(reason) {
  if (debounceTimer) {
    clearTimeout(debounceTimer);
  }

  debounceTimer = setTimeout(() => {
    runRefresh(reason);
  }, 350);
}

function isWorkshopFile(filePath) {
  const normalized = String(filePath || '').replace(/\\/g, '/');
  return /\/taller\.(md|mdx)$/i.test(`/${normalized}`);
}

console.log(`[workshops-watch] watching ${CONTENT_ROOT}`);
runRefresh('startup');

watch(
  CONTENT_ROOT,
  { recursive: true },
  (_eventType, filename) => {
    if (!filename || !isWorkshopFile(filename)) return;
    scheduleRefresh(filename);
  }
);
