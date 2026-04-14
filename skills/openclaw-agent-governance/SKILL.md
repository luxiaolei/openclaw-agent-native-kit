---
name: openclaw-agent-governance
description: Govern OpenClaw agents as real runtime units. Use when creating or revising agent workspaces, AGENTS/SOUL/USER/TOOLS files, agent skill stacks, agent registration in openclaw.json, specialist rosters, or portable agent-native packs.
---

# OpenClaw Agent Governance

Use this skill when the work is not just "write some prompt files", but to make agents and skills line up with how OpenClaw actually runs.

## Governing model

Treat each OpenClaw agent as a runtime unit with:
- a workspace
- an `agentDir`
- an auth store
- a session store
- a skill surface
- model and thinking defaults
- channel or routing bindings when relevant

Do not design agents as if they are only text prompts.

## Primary workflows

### 1. Create a new specialized agent
- define the lane and stop conditions
- define the required skill stack
- author the workspace files coherently
- assign model, fallback, and thinking defaults
- register the agent in `~/.openclaw/openclaw.json`
- verify `agentDir` uniqueness and path correctness

### 2. Revise an existing agent
- identify the failure mode: overreach, weak boundaries, verbosity, bad delegation, poor review discipline, etc.
- update `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and optional `HEARTBEAT.md` surgically
- keep runtime behavior and registration aligned
- preserve stable parts of the persona when only governance needs to change

### 3. Govern a specialist roster
- ensure each lane has a clearly named owner
- map skills to specialists instead of leaving routing ambiguous
- prefer specialists over generic subagents for high-value repeated domains
- block unsafe silent downgrades when a critical specialist is missing

### 4. Package agent-native assets
- extract reusable skills, specialist templates, and install scripts into a portable repo
- remove user-specific secrets and private notes
- make installation explicit instead of relying on hidden local state

## Hard rules

- Never reuse `agentDir` across agents.
- Do not claim an agent is real until both workspace files and config registration are aligned.
- Prefer one coherent governance pass over scattered one-file tweaks that drift apart.
- If a change affects routing or registration, update docs and install path too.

## Required references

Read these when applicable:
- `references/agent-native-principles.md`
- `references/governance-file-authoring.md`
- `references/packaging-and-install.md`

## Relationship to built-in skills

- Use `agent-builder` as a useful baseline for workspace generation.
- Go beyond it when the work requires multi-agent routing, config registration, roster design, or public pack portability.
