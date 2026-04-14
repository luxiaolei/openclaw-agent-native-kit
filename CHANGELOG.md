# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-04-14

### Added
- Initial public release of **OpenClaw Agent Native Kit**.
- Six specialized agent templates:
  - `specialist-stitch-designer`
  - `specialist-frontend-fullstack`
  - `specialist-backend-systems`
  - `specialist-review-architect`
  - `specialist-qa-governor`
  - `specialist-openclaw-governor`
- Three shared skills:
  - `autonomous-master-plan-executor`
  - `stitch`
  - `openclaw-agent-governance`
- Sample specialist registration config.
- Installer script for copying skills and specialist templates into `~/.openclaw`.
- Validation script for checking repo completeness and installed OpenClaw state.
- Architecture and routing docs.
- Public repo packaging structure for multi-machine reuse.

### Changed
- Refined specialist routing so conductor orchestration prefers explicit specialist lanes over generic subagents.
- Added OpenClaw governance as a first-class specialist lane and governance skill.
- Reworked README into a more public, shareable project overview.
