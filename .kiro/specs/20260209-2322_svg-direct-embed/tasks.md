# Tasks: SVG直接埋め込み

## Implementation Checklist
- [ ] `add_svg_to_slide()` / `get_svg_dimensions()` 実装
- [ ] `_add_image()` にSVG分岐追加
- [ ] `convert_to_png_if_needed()` / cairosvg import / ICON_CACHE_DIR 削除
- [ ] Pillow依存のアスペクト比計算をSVG viewBoxベースに変更
- [ ] `pyproject.toml` からcairosvg削除
- [ ] ドキュメント更新（setup.md, README.md, tech.md）
- [ ] `poc_svg_direct.py` 削除

## Validation
- [ ] `uv sync` が成功する（cairosvg不要）
- [ ] SVGアイコン付きスライドが生成できる
- [ ] iconColorによるリカラーが動作する
- [ ] widthのみ指定時のアスペクト比が正しい
- [ ] PowerPointで開いてSVGが表示される
- [ ] previewコマンドが動作する

---
**Created**: 2026-02-09
