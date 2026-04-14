#!/usr/bin/env python3
from pathlib import Path
import argparse, json, shutil

ROOT = Path(__file__).resolve().parents[1]
SKILLS_SRC = ROOT / 'skills'
AGENTS_SRC = ROOT / 'agent-templates'
CONFIG_SRC = ROOT / 'config' / 'specialized-agents.sample.json'

parser = argparse.ArgumentParser(description='Install OpenClaw agent-native kit into ~/.openclaw')
parser.add_argument('--home', default='~/.openclaw', help='Target OpenClaw home directory')
parser.add_argument('--register', action='store_true', help='Patch openclaw.json with sample specialist registrations')
args = parser.parse_args()

home = Path(args.home).expanduser()
(home / 'skills').mkdir(parents=True, exist_ok=True)
(home / 'specialized-agents').mkdir(parents=True, exist_ok=True)
(home / 'agents').mkdir(parents=True, exist_ok=True)

for src in SKILLS_SRC.iterdir():
    if src.is_dir():
        shutil.copytree(src, home / 'skills' / src.name, dirs_exist_ok=True)

for src in AGENTS_SRC.iterdir():
    if src.is_dir():
        shutil.copytree(src, home / 'specialized-agents' / src.name, dirs_exist_ok=True)
        (home / 'agents' / src.name / 'agent').mkdir(parents=True, exist_ok=True)

print('Installed skills and specialist templates.')

if args.register:
    cfg_path = home / 'openclaw.json'
    if not cfg_path.exists():
        raise SystemExit(f'Missing config: {cfg_path}')
    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    agent_list = cfg.setdefault('agents', {}).setdefault('list', [])
    by_id = {a.get('id'): a for a in agent_list if isinstance(a, dict) and a.get('id')}
    sample = json.loads(CONFIG_SRC.read_text(encoding='utf-8'))['agents']
    for agent in sample:
        if agent['id'] in by_id:
            by_id[agent['id']].update(agent)
        else:
            agent_list.append(agent)
    cfg_path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Registered {len(sample)} specialists in {cfg_path}.')
