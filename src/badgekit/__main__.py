"""Allow ``python -m badgekit``."""

import sys

from .cli import main

sys.exit(main())
