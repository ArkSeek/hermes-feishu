"""Hermes Feishu Plugin - root loader for Git-based installation.

When installed via `hermes plugins install arkseek/hermes-feishu`, Hermes
looks for __init__.py in the repository root. This file delegates to the
actual implementation in src/hermes_feishu/.
"""

import sys
from pathlib import Path

# Add src/ to path so we can import the real module
_src = Path(__file__).parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from hermes_feishu import register  # noqa: E402, F401
