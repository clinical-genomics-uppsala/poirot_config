#!/usr/bin/env python3
"""Validate variant_catalog_hg38.json using stranger's parse_json function."""
import logging
import sys

from stranger.utils import parse_json


class WarningHandler(logging.Handler):
    def __init__(self):
        super().__init__(level=logging.WARNING)
        self.warnings = []

    def emit(self, record):
        self.warnings.append(self.format(record))


logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
warning_handler = WarningHandler()
warning_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logging.getLogger().addHandler(warning_handler)

catalog_path = "config/str_catalog/variant_catalog_hg38.json"

print(f"Validating: {catalog_path}")
try:
    with open(catalog_path) as fh:
        repeat_info = parse_json(fh)
    if warning_handler.warnings:
        for w in warning_handler.warnings:
            print(w, file=sys.stderr)
        print(f"FAILED — {len(warning_handler.warnings)} warning(s) during parsing.", file=sys.stderr)
        sys.exit(1)
    print(f"OK — {len(repeat_info)} repeat entries parsed successfully.")
except SyntaxError as err:
    print(f"FAILED — {err}", file=sys.stderr)
    sys.exit(1)
except FileNotFoundError:
    print(f"FAILED — file not found: {catalog_path}", file=sys.stderr)
    sys.exit(1)
