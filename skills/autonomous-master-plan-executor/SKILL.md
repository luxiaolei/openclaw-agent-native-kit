---
name: autonomous-master-plan-executor
description: Execute an approved master plan through a conductor session that delegates to specialized agents and subagents, runs staged reviews, uses bounded fan-out, and installs a single cleanup watchdog when detached work may stall. Use when the user wants the main agent to turn a completed plan or checklist into end-to-end autonomous execution, especially for overnight runs, long multi-step builds, docs/code/governance work, or mixed specialist coordination with minimal supervision.
---

# Autonomous Master Plan Executor

Turn a finished plan into a controlled execution program.

## Core operating mode

- Keep the current session as the conductor.
- Keep the conductor responsible for plan state, wave control, blocker handling, final synthesis, and final user updates.
- Prefer specialized agents for domain work. Use plain same-agent subagents only when no good specialist exists or the task is too small to justify a specialist handoff.
- Keep leaf tasks small, single-goal, and stoppable.
- Use push-based completion. After launching a wave, prefer `sessions_yield` over home-grown polling loops.

## Start only after these checks

1. Normalize the master plan into a checklist with stable task IDs.
2. For each item, record:
   - objective
   - inputs
   - expected output path or deliverable
   - acceptance check
   - stop condition
3. Read `references/specialist-routing.md` when routing work to specialists.
4. If the plan includes frontend/full-stack/browser testing work, verify that a qualified frontend specialist exists. That specialist must have both:
   - `remote-opencli`
   - `stitch`
5. If the plan includes agent-native governance, skill design, specialist roster work, or install-packaging work, route it to the OpenClaw governance specialist instead of a generic reviewer.
6. If a required specialist or required global skill is missing, stop early and report the gap instead of silently routing to a weaker agent.

## Conductor routing policy

Use these defaults unless the task clearly needs a different lane:

- Stitch design or design-system work → `specialist-stitch-designer`
- frontend implementation with browser verification → `specialist-frontend-fullstack`
- backend, API, scripts, data flow → `specialist-backend-systems`
- milestone review or architecture review → `specialist-review-architect`
- browser QA, regression, accessibility, release gating → `specialist-qa-governor`
- OpenClaw agent governance, skill governance, pack design, registration work → `specialist-openclaw-governor`

If a task crosses lanes, split it into separate checklist items rather than asking one child to do everything.

## Execution policy

- Default to GPT-5.4 for delegated work.
- Use reasoning/thinking `high` for meaningful implementation tasks.
- Escalate to `xhigh` only for hard planning, hard debugging, governance design, or stage reviews that justify the cost.
- Do not review after every tiny task. Review by milestone, wave, or risk boundary.
- Use an independent reviewer for staged review when possible.
- Keep one parent wave to at most 3 concurrent children.
- In live, high-context, or long-topic situations, prefer only 1 to 2 concurrent children.
- If more than 3 tasks are ready, split them into waves.

## Routing rules

- Use `sessions_spawn` for detached execution, parallel work, staged review, or any task that should report back asynchronously.
- Use `sessions_send` only when a persistent specialist session should continue with its own history.
- Pass explicit `agentId` whenever a specialist exists.
- Pass explicit `runTimeoutSeconds` for every detached child.
- Give each child a narrow prompt with:
  - exact objective
  - allowed scope
  - files or paths it may touch
  - verification command or acceptance test
  - output format
  - stop condition
- Do not ask a child to both build and continuously self-review unless the task is tiny. Prefer separate build and review children at milestone boundaries.

## Watchdog rule

Use at most one watchdog cron per active wave.

Create a watchdog only when detached work can plausibly stall long enough to matter. Do not create one for every child.

Read `references/watchdog-pattern.md` before creating the watchdog.

### When to create it

Create one watchdog if all are true:
- at least one detached child is running
- the wave is expected to last long enough that a silent stall would hurt progress
- the conductor is likely to yield and rely on background completion

### When not to create it

Do not create a watchdog when:
- the wave is short
- all children are likely to finish before a meaningful check time
- the conductor is still actively supervising in the same turn

### What the watchdog must do

- inspect whether all children finished
- identify stalled, timed out, failed, or lost work
- check likely causes before relaunching blindly
- steer, relaunch, or escalate only when justified
- reschedule itself only if active work still exists
- cancel or remove itself once the wave is fully drained

## Review policy

Use staged review at these boundaries:
- after a logically independent milestone
- before merge or synthesis
- after a risky bug-fix wave
- before final commit when code or docs changed materially

Skip or defer review when:
- the change is trivial and reversible
- the wave is still exploratory and outputs are incomplete
- the cost of immediate review is higher than the risk

## Completion policy

Before declaring success:
- consolidate child outputs into the conductor checklist
- verify every acceptance check
- run stage review when needed
- update relevant docs when code or behavior changed
- commit if the task called for commit-worthy changes
- avoid touching unrelated dirty files that belong to other agents or humans
- report blockers clearly if anything remains unresolved

## Failure policy

If a wave degrades:
- reduce concurrency before increasing it
- prefer narrower relaunches over broad retries
- do not keep spawning more children into a jammed system
- report missing specialist coverage explicitly
- if frontend/browser work is required and the qualified frontend specialist is absent, block and report that gap
- if agent governance work is required and no governance specialist exists, block and report that gap

## Resources

- `references/specialist-routing.md` for specialist selection and required capabilities
- `references/watchdog-pattern.md` for watchdog timing and cron message patterns
