# Requirements: ブランドフォントルール適用

## Background & Context
### User Problems
- 生成されるPPTXのフォントがブランドガイドラインに準拠していない
- 全角/半角で異なるフォントを使用するルールがある

### Related Issues
- 現状フォント指定なし（箇条書きのArialのみ）

## Objectives
- 全テキストにブランドルール準拠のフォントを自動適用

## Scope
### In Scope
- 全角文字 → メイリオ
- 半角文字 → Amazon Ember
- 適用対象: textbox, table, shape内テキスト

### Out of Scope
- JSONからの個別フォント指定（将来拡張）

## Detailed Requirements
- 文字コードベースで全角/半角を判定
- run単位でフォントを切り替え
- styled text（{{bold:...}}等）にも適用

---
**Created**: 2026-02-03
