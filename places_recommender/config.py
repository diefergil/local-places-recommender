import logging
import logging.config
import pathlib
import sys

from rich.logging import RichHandler
PACKAGE_ROOT = pathlib.Path(__file__).parent.parent.resolve()
DATA_DIR = pathlib.Path(PACKAGE_ROOT, "data")
RAW_DATA_DIR = DATA_DIR / "raw_data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"