# Requirements: icon-search manifest活用改善

## Background & Context
### User Problems
- 現在のicon-searchはファイル名のみで検索、画像読み込みでaspectRatio取得
- manifest.jsonに名前・カテゴリ・タイプ・aspectRatioが既にある

### Related Issues
- パフォーマンス改善の余地
- 表示が分かりにくい（ファイル名のみ）

## Objectives
- manifest.json活用でパフォーマンス改善・表示改善
- タイプ別フィルタ追加

## Scope
### In Scope
- manifest.json読み込み・活用
- `--type` フィルタ（単一指定、全キーワードに適用）
- 表示改善: `AWS Lambda [Compute/service] (w:10%, h:10.0%)`
- 複数キーワード検索の形式維持

### Out of Scope
- `--category` フィルタ
- JSON出力オプション
- 複数タイプ指定

## Detailed Requirements
- manifestからaspectRatio取得（画像読み込み不要）
- name, category, typeで検索・フィルタ
- `--type service|resource|group|category|general|shape|third-party`

---
**Created**: 2026-02-04
