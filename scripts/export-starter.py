"""Export reviewed learner templates, never live reference progress or app files."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def prepare():
    manifest = json.loads((ROOT / 'course/starter-manifest.json').read_text())
    output = {}
    for destination, source in manifest.items():
        dest = Path(destination)
        src = ROOT / source
        if dest.is_absolute() or '..' in dest.parts or dest.parts[0] == '.git':
            raise ValueError(f'Unsafe destination: {destination}')
        if not src.resolve().is_relative_to((ROOT / 'course/starter').resolve()) or src.is_symlink():
            raise ValueError(f'Not a learner template: {source}')
        data = src.read_bytes()
        if destination.startswith('docs/epics/') and b'- [x]' in data.lower():
            raise ValueError(f'Learner epic contains completed tasks: {destination}')
        output[destination] = data
    output['starter-provenance.json'] = (json.dumps({
        'source': 'https://github.com/AhmedAGadir/repgarden',
        'templates': {name: hashlib.sha256(data).hexdigest() for name, data in output.items()},
    }, indent=2) + '\n').encode()
    return output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args()
    target = args.target.resolve()
    if target == ROOT or target.is_relative_to(ROOT):
        parser.error('Target must be outside the reference repository')
    if args.write:
        try:
            remote = subprocess.check_output(['git', '-C', str(target), 'remote', 'get-url', 'origin'], text=True).strip()
            top = Path(subprocess.check_output(['git', '-C', str(target), 'rev-parse', '--show-toplevel'], text=True).strip()).resolve()
            dirty = subprocess.check_output(['git', '-C', str(target), 'status', '--porcelain', '--untracked-files=all'], text=True).strip()
        except subprocess.CalledProcessError:
            parser.error('Write target must be the existing starter Git checkout')
        if top != target or remote not in ('https://github.com/AhmedAGadir/repgarden-starter.git', 'git@github.com:AhmedAGadir/repgarden-starter.git'):
            parser.error('Write target must be the repgarden-starter origin and repository root')
        if dirty:
            parser.error('Starter checkout has uncommitted files; review and commit or preserve them before export')
    output = prepare()
    changed = []
    for name, data in output.items():
        path = target / name
        if not path.resolve().is_relative_to(target) or path.is_symlink():
            parser.error(f'Unsafe target path: {name}')
        if not path.exists() or path.read_bytes() != data:
            changed.append(name)
    # Only these explicit template paths are managed; all other target files survive.
    if args.write:
        for name in changed:
            path = target / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(output[name])
    print(('Updated: ' if args.write else 'Drift: ') + (', '.join(changed) or 'none'))
    if args.check and changed:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
