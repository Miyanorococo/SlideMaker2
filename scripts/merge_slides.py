#!/usr/bin/env python3
"""Merge individual slide JSON files into a single presentation JSON."""
import json
import sys
from pathlib import Path


def merge(slide_dir: str, output: str, theme: str = "dark"):
    slide_dir = Path(slide_dir)
    slides = []
    for f in sorted(slide_dir.glob("slide_*.json")):
        with open(f) as fh:
            data = json.load(fh)
            if isinstance(data, list):
                slides.extend(data)
            else:
                slides.append(data)

    if not slides:
        print(f"Error: No slide_*.json files found in {slide_dir}", file=sys.stderr)
        sys.exit(1)

    presentation = {"theme": theme, "slides": slides}
    with open(output, "w") as fh:
        json.dump(presentation, fh, ensure_ascii=False, indent=2)
    print(f"Merged {len(slides)} slides → {output}")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("slide_dir", help="Directory containing slide_*.json files")
    p.add_argument("-o", "--output", required=True, help="Output presentation JSON")
    p.add_argument("--theme", default="dark", choices=["dark", "light"])
    args = p.parse_args()
    merge(args.slide_dir, args.output, args.theme)
