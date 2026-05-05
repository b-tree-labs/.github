#!/usr/bin/env python
# Copyright (c) 2026 B-Tree Ventures, LLC
# SPDX-License-Identifier: Apache-2.0
"""Regenerate PNG exports from the SVG masters.

Usage:
    python _export.py

Produces favicon bundle and PNG exports for every SVG in this directory.
"""

from __future__ import annotations

import pathlib
import sys

import cairosvg

HERE = pathlib.Path(__file__).parent

# (svg-filename, [(png-filename, px), ...])
JOBS = [
    (
        "btree-labs-favicon.svg",
        [
            ("btree-labs-favicon-16.png", 16),
            ("btree-labs-favicon-32.png", 32),
            ("btree-labs-favicon-180.png", 180),
            ("btree-labs-favicon-512.png", 512),
        ],
    ),
    ("btree-labs-mark.svg", [("btree-labs-mark-1024.png", 1024)]),
    ("btree-labs-mark-dark.svg", [("btree-labs-mark-dark-1024.png", 1024)]),
    ("btree-labs-mark-mono-light.svg", [("btree-labs-mark-mono-light-1024.png", 1024)]),
    ("btree-labs-mark-mono-dark.svg", [("btree-labs-mark-mono-dark-1024.png", 1024)]),
    ("btree-labs-wordmark-horizontal.svg", [("btree-labs-wordmark-horizontal.png", 2400)]),
    ("btree-labs-wordmark-stacked.svg", [("btree-labs-wordmark-stacked.png", 1600)]),
    ("btree-labs-social-card.svg", [("btree-labs-social-card.png", 1200)]),
]


def main() -> int:
    for svg_name, pngs in JOBS:
        svg_path = HERE / svg_name
        if not svg_path.exists():
            print(f"  [skip] {svg_name} (missing)")
            continue
        svg_bytes = svg_path.read_bytes()
        for png_name, px in pngs:
            out = HERE / png_name
            cairosvg.svg2png(
                bytestring=svg_bytes,
                write_to=str(out),
                output_width=px,
                output_height=None,  # preserve aspect ratio
            )
            print(f"  [ok]   {png_name} ({px}px)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
