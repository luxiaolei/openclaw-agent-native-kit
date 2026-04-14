#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys

REQUIRED_AGENT_FILES = [
    'AGENTS.md', 'BOOTSTRAP.md', 'HEARTBEAT.md', 'IDENTITY.md',
    'MEMORY.md', 'README.md', 'SOUL.md', 'TOOLS.md', 'USER.md'
]
REQUIRED_SKILLS = [
    'autonomous-master-plan-executor',
    'stitch',
    'openclaw-agent-governance',
]
EXPECTED_AGENTS = [
    'specialist-stitch-designer',
    'specialist-frontend-fullstack',
    'specialist-backend-systems',
    'specialist-review-architect',
    'specialist-qa-governor',
    'specialist-openclaw-governor',
]

def fail(msg):
    print(f'FAIL: {msg}')
    return 1

def main():
    parser = argparse.ArgumentParser(description='Validate OpenClaw Agent Native Kit install or repo layout')
    parser.add_argument('--home', help='Validate an installed ~/.openclaw home')
    parser.add_argument('--repo', help='Validate the kit repo root')
    args = parser.parse_args()

    if not args.home and not args.repo:
        parser.error('provide --home or --repo')

    errors = 0

    if args.repo:
        repo = Path(args.repo).expanduser().resolve()
        for skill in REQUIRED_SKILLS:
            if not (repo / 'skills' / skill / 'SKILL.md').exists():
                errors += fail(f'missing repo skill: {skill}')
        for agent in EXPECTED_AGENTS:
            agent_dir = repo / 'agent-templates' / agent
            if not agent_dir.exists():
                errors += fail(f'missing repo agent template: {agent}')
                continue
            for fname in REQUIRED_AGENT_FILES:
                if not (agent_dir / fname).exists():
                    errors += fail(f'missing template file for {agent}: {fname}')
        if not (repo / 'scripts' / 'install.py').exists():
            errors += fail('missing repo install.py')
        if not (repo / 'scripts' / 'validate.py').exists():
            errors += fail('missing repo validate.py')
        if not (repo / 'config' / 'specialized-agents.sample.json').exists():
            errors += fail('missing sample config')

    if args.home:
        home = Path(args.home).expanduser().resolve()
        cfg_path = home / 'openclaw.json'
        if not cfg_path.exists():
            errors += fail(f'missing config: {cfg_path}')
        else:
            cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
            agent_list = cfg.get('agents', {}).get('list', [])
            by_id = {a.get('id'): a for a in agent_list if isinstance(a, dict)}
            seen_agent_dirs = {}
            for agent in EXPECTED_AGENTS:
                if agent not in by_id:
                    errors += fail(f'agent not registered: {agent}')
                    continue
                entry = by_id[agent]
                if entry.get('model', {}).get('primary') != 'openai-codex/gpt-5.4':
                    errors += fail(f'wrong primary model for {agent}')
                if 'bailian/qwen3.6-plus' not in (entry.get('model', {}).get('fallbacks') or []):
                    errors += fail(f'missing fallback for {agent}')
                agent_dir = entry.get('agentDir')
                if not agent_dir:
                    errors += fail(f'missing agentDir for {agent}')
                elif agent_dir in seen_agent_dirs:
                    errors += fail(f'duplicate agentDir: {agent_dir}')
                else:
                    seen_agent_dirs[agent_dir] = agent
            for skill in REQUIRED_SKILLS:
                if not (home / 'skills' / skill / 'SKILL.md').exists():
                    errors += fail(f'missing installed skill: {skill}')
            for agent in EXPECTED_AGENTS:
                agent_dir = home / 'specialized-agents' / agent
                if not agent_dir.exists():
                    errors += fail(f'missing installed specialist workspace: {agent}')
                    continue
                for fname in REQUIRED_AGENT_FILES:
                    if not (agent_dir / fname).exists():
                        errors += fail(f'missing installed file for {agent}: {fname}')

    if errors:
        print(f"\nValidation finished with {errors} error(s).")
        sys.exit(1)
    print('OK: validation passed')

if __name__ == '__main__':
    main()
