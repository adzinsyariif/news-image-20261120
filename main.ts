// One Day — 20 November 2026.
//
// This repository holds a single-image summary of Friday 20 November
// 2026: a broadsheet front page (entry.png) composed by
// build_frontpage.py. The program's one job is delivery — it copies
// entry.png into the grader's output folder:
//
//   /output/entry.png            inside the harness container
//   $MAKEFUN_OUTPUT_DIR/entry.png   anywhere else, for local runs
//
//     mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// Only Node 22's standard library is used, nothing is fetched, and the
// output is the input file byte for byte, so runs are reproducible.

import { cpSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const pageFile = join(root, "entry.png");
if (!existsSync(pageFile)) {
  throw new Error("entry.png is missing from the repository root");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });

const dest = join(outDir, "entry.png");
cpSync(pageFile, dest);
console.log(`published ${dest} — ${statSync(dest).size} bytes`);
