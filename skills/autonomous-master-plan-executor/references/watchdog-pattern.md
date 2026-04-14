# Watchdog pattern

Use one watchdog per active execution wave, not one per child.

## Purpose

The watchdog exists to catch silent stalls after the conductor has yielded. It is a recovery tool, not the normal completion path.

Normal completion should remain push-driven through task completion, announce delivery, and heartbeat wake.

## Scheduling rule

Choose the watchdog time from the wave, not from the shortest child.

Recommended rule:
- compute the longest child timeout in the wave
- schedule the watchdog for `longest timeout + 10m slack`
- floor: 20m
- cap: 90m

If no child timeout is available, choose a conservative one-shot check that matches the expected wave duration. Avoid very short watchdogs.

## Cron shape

Prefer a one-shot cron bound to the current conductor session.

Use the cron job to inject a clear reminder-style agent turn that tells the conductor to:
- inspect active child runs for the wave
- identify finished, running, failed, timed out, or lost children
- diagnose stalls before retrying
- steer or relaunch only the minimal necessary work
- remove or cancel the watchdog if the wave is already complete

## Message pattern

Write the cron message in plain language, for example:

"Reminder: watchdog check for wave W2. Inspect the active delegated runs for this wave. If all runs are complete, remove this watchdog and continue the plan. If any run is stalled, timed out, failed, or lost, investigate why, then steer, relaunch, or escalate with the smallest safe intervention. Do not fan out new work until the wave is healthy again."

Adapt the wave ID, expected child labels, and relevant timeout context.

## Cancellation rule

Cancel or remove the watchdog when:
- every child in the wave is complete, failed and handled, or deliberately cancelled
- the conductor is moving to the next wave and the current watchdog is no longer relevant
- the plan has already ended

## Intervention order

When the watchdog fires, use this order:
1. confirm whether the child already completed and delivery was merely delayed
2. inspect task or session state
3. steer a live child if it is recoverable
4. relaunch a narrow replacement if needed
5. reduce concurrency before launching more work
6. escalate clearly if the failure pattern suggests gateway, auth, or tool-surface problems

## Anti-patterns

Do not:
- create one watchdog per child
- reschedule forever without diagnosis
- use heartbeat as a precise timer
- poll `sessions_list` or `subagents list` in tight loops
- blindly relaunch the whole wave when one child is sick
