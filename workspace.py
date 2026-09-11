"""Validate and test the current sibling folders, without Git or commit pins."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent


def run(command, cwd=ROOT):
    subprocess.run([str(item) for item in command], cwd=cwd, check=True, timeout=180)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['doctor', 'test'])
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        parser.error('Python 3.11+ required')
    if not __debug__:
        parser.error('Unset PYTHONOPTIMIZE; model checks use assertions')

    manifest = json.loads((ROOT / 'workspace.json').read_text())
    if manifest.get('schema') != 1 or manifest.get('mode') != 'sibling-workspace':
        parser.error('Expected schema 1 sibling-workspace manifest')
    components = manifest['components']
    for name, record in components.items():
        if not re.fullmatch(r'[a-z][a-z0-9-]*', name):
            parser.error('Invalid component folder name')
        folder = WORKSPACE / name
        if not folder.is_dir():
            parser.error(f'Missing sibling folder: {name}')
        for required in record['required_files']:
            relative = Path(required)
            if relative.is_absolute() or '..' in relative.parts:
                parser.error(f'Invalid required file path for {name}')
            if not (folder / relative).is_file():
                parser.error(f'Missing required file: {name}/{required}')

    print(f'PASS {len(components)} component folders found; testing current files', flush=True)
    for tool in ['iverilog', 'vvp']:
        if not shutil.which(tool):
            parser.error(f'Missing {tool}; install Icarus Verilog')
    if args.command == 'doctor':
        print('PASS doctor: component files, Python and Icarus available')
        return

    build = ROOT / 'build'
    build.mkdir(exist_ok=True)
    vectors = build / 'mac-vectors.txt'
    run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=WORKSPACE / 'ml-models')
    run([sys.executable, WORKSPACE / 'ml-models/generate_vectors.py',
         '--contract', WORKSPACE / 'architecture/contracts/mac-v0.json', '--output', vectors])
    run([sys.executable, WORKSPACE / 'verification/run.py',
         '--rtl-root', WORKSPACE / 'rtl-compute', '--vectors', vectors])
    print('PASS integration: contract -> ml-models -> compute RTL -> independent verification')
    scaffolds = ', '.join(name for name, record in components.items() if record['status'] == 'scaffold')
    print(f'Scope: MAC only. Implementation pending: {scaffolds}.')


if __name__ == '__main__':
    main()
