# Requirements: SVG直接埋め込みによるcairo依存の排除

## Background & Context
### User Problems
- cairosvg/cairoはシステムレベルの依存（Mac: `brew install cairo`, Windows: GTKランタイム）で、初回セットアップの障壁が高い
- 特にWindowsユーザーにとってcairoのインストールは困難
- `uv sync` だけで全依存が解決する状態が理想

### Related Issues
- PoC（poc_svg_direct.py）でSVGをPPTXに直接埋め込めることを確認済み
- PowerPoint 2019+がSVGをネイティブサポート
- previewコマンドはPowerPoint→PDF→PNGの流れなのでcairo不要

## Objectives
- cairosvg/cairo依存を完全に排除する
- 全プラットフォームで `uv sync` のみでセットアップ完了にする

## Scope
### In Scope
- `convert_to_png_if_needed` + `add_picture` → SVG直接埋め込みに置換
- `iconColor`（SVGリカラー）をlxmlベースに維持
- SVGのアスペクト比取得をviewBoxから行う（Pillow不要に）
- `pyproject.toml` からcairosvg削除
- ドキュメント更新（setup.md等からcairo記載を削除）
- PoCスクリプト削除

### Out of Scope
- Pillow削除（グリッドオーバーレイで引き続き使用）
- 古いPowerPoint（2016以前）のサポート
- preview機能の変更

## Detailed Requirements
- SVGアイコンはPNG変換せず、OpenXMLの `asvg:svgBlip` で直接埋め込む
- iconColorによるリカラーは、SVG XMLを直接書き換えてから埋め込む
- widthのみ指定時のアスペクト比計算は、SVGのviewBox/width/height属性から取得
- PNGアイコンキャッシュ（`~/.cache/pptx-maker/icons/`）は不要になる

---
**Created**: 2026-02-09
