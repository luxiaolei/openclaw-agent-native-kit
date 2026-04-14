# Agent-native principles

OpenClaw agents are runtime-scoped units, not just prompt folders.

## Minimum reality check

A governed agent should have:
- a coherent workspace
- a unique `agentDir`
- a model policy
- a thinking policy
- a clear skill stack
- a lane definition and stop conditions

## Authoring rule

Write governance files so they survive contact with real execution:
- subagents may inherit only partial workspace context
- skills can be shared or per-agent
- routing and bindings live in config, not just prose
- session behavior matters as much as prompt tone
