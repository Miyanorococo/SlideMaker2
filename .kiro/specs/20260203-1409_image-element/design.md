# Design: Image Element

## JSON Schema
```json
{
  "type": "image",
  "src": "aws:lambda",  // "aws:" prefix for icon lookup
  "x": 10,              // % from left
  "y": 20,              // % from top
  "width": 5            // % of slide width (required)
  // "height": 5        // optional, defaults to aspect ratio
}
```

## Icon Resolution
- `aws:lambda` → `Arch_AWS-Lambda_48.svg` (fuzzy match)
- `aws:s3` → `Arch_Amazon-Simple-Storage-Service_48.svg`

## Implementation Strategy
- Reuse: 既存の `add_element()` 関数を拡張
- New: `add_image_element()`, `resolve_icon_path()`, `convert_svg_to_png()`

## Dependencies
- cairosvg: SVG→PNG変換

## Cache
- Location: `~/.cache/pptx-maker/icons/`
- Naming: `{icon_name}_{scale}x.png`

---
**Created**: 2026-02-03
