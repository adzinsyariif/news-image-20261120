// One Day — 20 November 2026: the world's news of Friday 20 November
// 2026, summed up in a single front-page image.
//
// The finished page lives in this repository as entry.png, composed by
// build_frontpage.py from the day's market-crash artwork. This program
// is the publisher: it delivers that file to the grader's output
// folder — "/output" inside the harness container, or the directory
// named by $MAKEFUN_OUTPUT_DIR when that variable is set, which is how
// the program is exercised locally:
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// Node 22 standard library only, no network access, and deterministic:
// the bytes written are exactly the bytes of entry.png, every run.

import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoDir = dirname(fileURLToPath(import.meta.url));
const source = join(repoDir, "entry.png");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(targetDir, "entry.png");

mkdirSync(targetDir, { recursive: true });
copyFileSync(source, target);

const { size } = statSync(target);
console.log(`One Day — 20 November 2026: wrote ${target} (${size} bytes)`);
