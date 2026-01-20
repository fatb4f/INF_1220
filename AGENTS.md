# agents.md

## Purpose
This repo uses **Codex skills** as the primary execution contract. `agents.md` is a high-level operator guide:
- where the **authority** lives,
- which **skills** to use,
- where **outputs/evidence** go,
- what **constraints** must be respected.

## Authority model
- **INF1220 course materials** are authoritative (especially pseudocode conventions).
- **Python** is allowed only as a **verification oracle** (trace tables, truth tables, sanity checks) and must be labeled **NON-SUBMISSION** unless explicitly requested.

## Skills registry
### INF1220 M1 skill (primary)
- Skill ID: `inf1220-m1`
- Contract:
  - `.codex/skills/inf1220-m1/SKILL.md` (prompt + workflow)
  - `.codex/skills/inf1220-m1/skill.json` (machine-readable metadata)
- Authority snapshot:
  - `.codex/skills/inf1220-m1/assets/inf1220_m1.json` (vendored for reproducibility)

## How to use Codex in this repo
### Input types you can provide to the skill
1) INF1220-style problem statement  
2) Objective key(s) from the JSON (e.g., `m1-07.boolean_logic`)  
3) Draft pseudocode / Python snippet to debug

### Required method lenses (always explicit in output)
- **3 Pillars:** Computation as a System; Statistics as Inference; Control & Adaptation
- **AlgoCtrl pipeline:** GEN → STRUCT → SELECT → FLOW → EVAL
- **Adaptive Control Strategies:** feedforward, feedback, guardrails/saturation, update locus

### Output structure (always)
The skill must return Markdown containing:
1) Observer Snapshot  
2) AlgoCtrl Run  
3) INF1220 Submission Form (INF1220 pseudocode) + optional Python oracle (NON-SUBMISSION)  
4) Coverage Report (objective keys)  
5) Micro-drills (2–4, <= 5 min; at least one tracing drill)

## Write policy and side effects
- Default behavior: **stdout only** (no file writes) unless explicitly requested.
- Allowed write locations (when artifact mode is requested):
  - `out/**`
  - `.codex/skills/inf1220-m1/**` (skill maintenance only)
- Forbidden: `.git/**`, `node_modules/**`, `.venv/**`, and unrelated refactors.
- Network access: **disallowed** unless explicitly requested.

## Outputs, evidence, and logs (artifact mode)
This repo uses **artifact mode** by default.

### Always write (under repo_root/out/)
- `out/inf1220_solution.md` — authoritative rendered solution
- `out/evidence.json` — structured evidence (objective_keys_used, assumptions, tests/trace summary, update_locus)
- `out/logs/inf1220-m1.log` — minimal operational log (no secrets; no large dumps)

### Optionally write (only if needed for verification)
- `out/python_oracle.py` — runnable verification script mirroring pseudocode; **NON-SUBMISSION**

