# Notes: SVG直接埋め込み

Guidelines:
- **Append-only**: Never edit existing content
- **Capture thought process**: "Initially thought X, but actually Y"
- **Be specific**: Include errors, commands, numbers

## Log

### [2026-02-09 23:19] PoC成功
- `poc_svg_direct.py` でSVGをPPTXに直接埋め込むことに成功
- python-pptx + lxml のみ、cairosvg不使用
- OpenXMLの `asvg:svgBlip` 拡張を使用
- PowerPointで開いて表示確認済み

### [2026-02-09 23:22] preview調査
- previewはPowerPoint AppleScript → PDF → pdftoppm → PNGの流れ
- SVGのラスタライズはPowerPoint自体が行うのでcairo不要
- PillowはグリッドオーバーレイとSVGアスペクト比計算のみ
- アスペクト比はSVGのviewBoxから取得すればPillow依存も減る

---
**Created**: 2026-02-09
