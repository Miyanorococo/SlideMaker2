# Requirements: Image Element

## Background & Context
- AWSアイコン（SVG）をスライドに挿入したい
- `~/Library/Application Support/com.raycast.macos/extensions/aws-icons/icons/` に903個のSVGアイコンあり
- python-pptxはSVGを直接サポートしないため、PNG変換が必要

## Objectives
- elements配列にimage typeを追加
- AWSアイコンを `aws:icon_name` 形式で指定可能に
- 高解像度PNG変換で品質維持

## Scope
### In Scope
- `{"type": "image", "src": "aws:lambda", "x": 10, "y": 20, "width": 5}` 形式
- SVG→PNG変換（3x解像度）
- キャッシュによる再変換回避

### Out of Scope
- 一般画像ファイルの挿入（将来対応）
- SVG直接埋め込み（lxml操作が複雑）

## Detailed Requirements
- `width` 必須（スライド幅の%）
- `height` 省略時はアスペクト比維持
- 変換済みPNGはキャッシュディレクトリに保存

---
**Created**: 2026-02-03
