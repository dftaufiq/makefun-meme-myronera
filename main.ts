// Entry runner for the "Post the Meme, Win the Feed" bounty on make.fun.
//
// This program does one small job: it takes POST.json, which points at the
// meme video already posted on X, and drops a copy into the output directory
// so the bounty gate can find it and read the post's stats from X.
//
// Node 22, standard library only. No network calls, no dependencies — the
// post itself is the entry; this file just hands its address to the grader.
//
// Local check:
//   mkdir -p /tmp/meme-out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=/tmp/meme-out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

// Inside the grader's container these resolve to /bot and /output; the env
// variables let me point them elsewhere when testing on my own machine.
const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const source = join(botDir, 'POST.json');
const destination = join(outputDir, 'POST.json');

try {
  // Validate the source is well-formed JSON before copying it, so a
  // corrupted POST.json fails here with a clear message instead of
  // handing the grader a broken file.
  try {
    JSON.parse(readFileSync(source, 'utf8'));
  } catch (parseError) {
    throw new Error(`POST.json at ${source} is not valid JSON: ${(parseError as Error).message}`);
  }
  // Make sure the destination folder exists before writing into it.
  mkdirSync(outputDir, { recursive: true });
  copyFileSync(source, destination);
} catch (error) {
  console.error(`Failed to copy ${source} to ${destination}: ${(error as Error).message}`);
  process.exit(1);
}
