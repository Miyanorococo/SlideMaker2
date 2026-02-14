# Requirements: pptx_builder機能マージ

## Background & Context
### User Problems
- Downloads版（旧バージョン）に存在する機能が現在版に欠けている
- 両バージョンで重複実装があり、統一が必要

### Related Issues
- PPTX逆変換（pptx_to_json.py）で抽出した要素を再生成できない

## Objectives
- Downloads版の有用な機能を現在版にマージ
- 重複実装を整理し、最適な実装に統一

## Scope
### In Scope
Downloads版から追加する機能：
- `_add_group` - グループ要素対応
- `_add_freeform_shape` - フリーフォーム図形対応
- `adjustments` - 図形調整値
- `imagePath` - 抽出画像パス対応
- margin/verticalAnchor - テキストフレーム設定
- グラデーションのopacity対応

### Out of Scope
- `items`（paragraphsに統合済み、廃止）
- `lineDash`（dashStyleに統一）
- `opacity` 0-100形式（0-1に統一）

## Detailed Requirements

### 統一方針
| 機能 | 採用 | 理由 |
|------|------|------|
| 破線スタイル | 現在版 `dashStyle` | enum使用でシンプル |
| 不透明度 | 現在版 0-1 | 標準的な形式 |
| グラデーション | Downloads版ベース | エラーハンドリング、opacity対応 |
| フォント切替 | 現在版 | normalize_spacing含め維持 |

---
**Created**: 2026-02-04
