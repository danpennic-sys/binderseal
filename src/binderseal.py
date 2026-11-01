# Deprecated shim for older docs that say `python3 src/binderseal.py`.
# Prefer: python -m binderseal   or   pip install . && binderseal
from binderseal.core import main

if __name__ == "__main__":
    raise SystemExit(main())
