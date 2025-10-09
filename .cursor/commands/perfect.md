do not build project after completing tasks, just do tsc --noEmit

🔎 1. Understand

Map entry → flow → exit.

Identify trust boundaries + invariants.

Review @web best practices → list options → pick one → explain to user how many and why chosen.

🧹 2. Standards

Clean: names, modules, no "utils dump."

Secure: validate inputs, enforce authZ, no secrets in logs.

Performant: avoid N+1, cap concurrency, add timeouts.

🕵️ 3. Review

Bugs: nulls, races, off-by-one.

Anti-patterns: globals, copy-paste, magic values.

Outdated: deprecated APIs, weak libs.

🧭 4. Diagnose

Logs: structured + req_id.

Traces: full stack, correlation IDs.

Tests: failing unit → integration.

📝 5. Plan

🟥 Critical → auth, crashes, leaks.

🟧 Major → logic, perf.

🟨 Minor → style, nits.

Order: secure → correct → fast → pretty.

🛠️ 6. Fix

Illegal states impossible (types).

Pure core, impure edges.

Consistent patterns.

Comments only for why.

🧪 7. Test

Mock data tests if needed.

Integration (flows) clearly.

Regression (bugs) + debug.

Property-based if valuable.

📊 8. Monitor

Error rate, latency, memory.

Logs: no secrets, no noise.

Feature flags for risky code.

✅ 9. Verify

Type + lint clean.

Tests green.

Changelog updated.

Peer reviewed.

Inform user about @web practice choice.

🔄 10. Autonomous Planning & Repetition

If task takes more time than expected:

- **Reassess Scope:** Break down complex tasks into smaller, manageable chunks
- **Plan Iterations:** Create phased approach with clear milestones
- **Autonomous Execution:** Continue working independently without user intervention
- **Progress Tracking:** Update task status and log progress regularly
- **Quality Gates:** Run verification steps after each iteration
- **Adaptive Strategy:** Adjust approach based on intermediate results

For long-running tasks:

- Set clear checkpoints every 30-60 minutes
- Document decisions and rationale
- Maintain momentum with incremental progress
- Escalate only if blocked by external dependencies

🗂️ 11. Task File Workflow

For each task cycle, create a file:
corrents-task/time-test.md like (corrent-tasks/27.09-08:22-test.md)

Inside: checkboxes for all tasks.

test one by one

if there is issue , skip and move next

if goes successfull, make checked

After all complete (if there are no issues for each task) → move file to:
corrent-tasks/archive-tasks/, then remove from corrent-tasks
