# OpenClaw Agent Native Kit

A portable pack of OpenClaw-native specialist agents and skills.

一个可移植的 OpenClaw Agent Native 套件，包含专精 agents、共享 skills、注册样例和安装脚本，方便在多台机器上复用。

## What this includes

- Specialized agent templates for:
  - Stitch design
  - Frontend fullstack
  - Backend systems
  - Review architect
  - QA governor
  - OpenClaw governor
- Shared skills:
  - `autonomous-master-plan-executor`
  - `stitch`
  - `openclaw-agent-governance`
- Sample agent registration config
- Installer script for copying the pack into `~/.openclaw`
- Validation script for checking pack completeness and config consistency

## Included structure

```text
agent-templates/   reusable specialist workspace templates
skills/            shared execution and governance skills
config/            sample registration JSON
scripts/           install + validation helpers
docs/              architecture and routing notes
```

## Design goals

- OpenClaw-native, not generic prompt bundles
- specialists over vague generalist fan-out
- conductor-centered autonomous execution
- portable git repo first, plugin later if justified

## 为什么先做成 Git 仓库

先做成 repo 比直接做 plugin 更稳，因为它：

- 更容易跨机器安装
- 更容易版本管理
- 更容易公开发布和协作
- 更容易先验证结构是否稳定
- 稳定后再 plugin 化也不晚

## Install

```bash
python3 scripts/install.py --home ~/.openclaw --register
python3 scripts/validate.py --home ~/.openclaw
```

## Routing overview

- Stitch design → `specialist-stitch-designer`
- Frontend design-to-code + browser verification → `specialist-frontend-fullstack`
- Backend / API / automation → `specialist-backend-systems`
- Milestone review / architecture review → `specialist-review-architect`
- Browser QA / regression / accessibility → `specialist-qa-governor`
- Agent governance / skill governance / packaging → `specialist-openclaw-governor`

See also:
- `docs/architecture.md`
- `docs/routing.md`

## Source inspirations

- `stitch-skills`
- `gstack`
- `agency-agents`
- OpenClaw multi-agent and agent-workspace docs

## Notes

- This repo intentionally excludes secrets, auth stores, and private memory.
- Fill in environment-specific `TOOLS.md` details locally after install.
- Adjust models, bindings, and channel routing per machine.
