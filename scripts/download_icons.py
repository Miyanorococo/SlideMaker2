#!/usr/bin/env python3
"""Download AWS icons from CDN for pptx-maker (non-Raycast users)."""
import argparse
import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor, as_completed

MANIFEST_URL = "https://d24ck1wc2tejct.cloudfront.net/manifest.json"
OUTPUT_DIR = Path(__file__).parent.parent / "icons"
HEADERS = {"X-Raycast-Extension": "aws-icons-v1"}


def download_file(url: str, dest: Path) -> bool:
    """Download a single file."""
    try:
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=30) as resp:
            dest.write_bytes(resp.read())
        return True
    except Exception as e:
        print(f"  Failed: {dest.name} - {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Download AWS icons for pptx-maker")
    parser.add_argument("-o", "--output", type=Path, default=OUTPUT_DIR, help="Output directory")
    parser.add_argument("-t", "--type", choices=["service", "resource", "group", "category", "general", "third-party"], help="Filter by type")
    parser.add_argument("-j", "--jobs", type=int, default=10, help="Parallel downloads (default: 10)")
    parser.add_argument("--manifest-url", default=MANIFEST_URL, help="Manifest URL")
    args = parser.parse_args()

    print(f"Fetching manifest: {args.manifest_url}")
    try:
        req = Request(args.manifest_url, headers=HEADERS)
        with urlopen(req, timeout=30) as resp:
            manifest = json.load(resp)
    except Exception as e:
        print(f"Error: Failed to fetch manifest - {e}", file=sys.stderr)
        sys.exit(1)

    icons = manifest["icons"]
    base_url = manifest["baseUrl"]
    
    if args.type:
        icons = [i for i in icons if i["type"] == args.type]
    
    print(f"Icons: {len(icons)} (version: {manifest['version']})")
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Save manifest
    manifest_path = args.output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"Saved: {manifest_path}")
    
    # Download icons
    print(f"Downloading to: {args.output}")
    success = 0
    failed = 0
    
    def download_icon(icon):
        url = f"{base_url}{icon['file']}"
        dest = args.output / icon["file"]
        return download_file(url, dest), icon["file"]
    
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = [executor.submit(download_icon, icon) for icon in icons]
        for i, future in enumerate(as_completed(futures), 1):
            ok, name = future.result()
            if ok:
                success += 1
            else:
                failed += 1
            if i % 100 == 0 or i == len(icons):
                print(f"  Progress: {i}/{len(icons)}")
    
    print(f"\nComplete: {success} downloaded, {failed} failed")


if __name__ == "__main__":
    main()
