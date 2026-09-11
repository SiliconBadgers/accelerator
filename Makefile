.PHONY: setup doctor test clean
PYTHON ?= python3
setup:
	$(PYTHON) -c "import sys; assert sys.version_info >= (3, 11), 'Python 3.11+ required'; print('PASS setup: standard-library starter, no packages required')"
doctor:
	$(PYTHON) workspace.py doctor
test:
	$(PYTHON) workspace.py test
clean:
	$(PYTHON) -c "from pathlib import Path; import shutil; root=Path.cwd().parent; paths=list(root.glob('*/build'))+list(root.rglob('__pycache__')); [shutil.rmtree(p) for p in paths if p.is_dir() and not p.is_symlink()]"
