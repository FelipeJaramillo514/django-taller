from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent
LOCAL_PACKAGES = BASE_DIR / ".packages"

if LOCAL_PACKAGES.exists():
    sys.path.insert(0, str(LOCAL_PACKAGES))
