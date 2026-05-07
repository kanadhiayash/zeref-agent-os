#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

EXPECTED_VERSION = "1.1.2"
EXPECTED_SKILLS = 112

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main(root='.'):
    root=Path(root)
    marketplace=root/'.claude-plugin'/'marketplace.json'
    plugin=root/'plugins'/'zeref-skills-fleet'/' .claude-plugin'
    plugin=root/'plugins'/'zeref-skills-fleet'/'.claude-plugin'/'plugin.json'
    skills_dir=root/'plugins'/'zeref-skills-fleet'/'skills'
    errors=[]
    for p in [marketplace, plugin, skills_dir]:
        if not p.exists(): errors.append(f'Missing: {p}')
    if errors:
        print('\n'.join(errors)); return 1
    m=load_json(marketplace); p=load_json(plugin)
    if m.get('version') != EXPECTED_VERSION: errors.append(f'Marketplace version mismatch: {m.get("version")}')
    if p.get('version') != EXPECTED_VERSION: errors.append(f'Plugin version mismatch: {p.get("version")}')
    entries=m.get('plugins',[])
    if not entries: errors.append('Marketplace has no plugins.')
    else:
        e=entries[0]
        if e.get('name') != 'zeref-skills-fleet': errors.append('Marketplace plugin name mismatch.')
        if e.get('version') != EXPECTED_VERSION: errors.append(f'Marketplace entry version mismatch: {e.get("version")}')
        if e.get('source') != './plugins/zeref-skills-fleet': errors.append(f'Marketplace source mismatch: {e.get("source")}')
    skill_dirs=[d for d in skills_dir.iterdir() if d.is_dir()]
    if len(skill_dirs) != EXPECTED_SKILLS: errors.append(f'Skill count mismatch: {len(skill_dirs)} != {EXPECTED_SKILLS}')
    name_re=re.compile(r'^name:\s*([^\n]+)',re.M)
    desc_re=re.compile(r'^description:\s*>?',re.M)
    kebab=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
    for d in skill_dirs:
        if not kebab.match(d.name): errors.append(f'Not kebab-case: {d.name}')
        f=d/'SKILL.md'
        if not f.exists(): errors.append(f'Missing SKILL.md: {d.name}'); continue
        txt=f.read_text(encoding='utf-8')
        mn=name_re.search(txt)
        if not mn: errors.append(f'Missing name frontmatter: {d.name}')
        elif mn.group(1).strip() != d.name: errors.append(f'Name/folder mismatch: {d.name} != {mn.group(1).strip()}')
        if not desc_re.search(txt): errors.append(f'Missing description frontmatter: {d.name}')
    report={'version':EXPECTED_VERSION,'skills_checked':len(skill_dirs),'errors':errors,'status':'pass' if not errors else 'fail'}
    out=root/'plugins'/'zeref-skills-fleet'/'manifests'/'validation_report.json'
    out.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    return 0 if not errors else 1
if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else '.'))
