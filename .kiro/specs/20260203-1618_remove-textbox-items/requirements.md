# Requirements: textbox内itemsの廃止

## Background & Context
### User Problems
- textbox内に`text`、`items`、`paragraphs`の3つのテキスト指定方法があり冗長
- `items`は`paragraphs`の簡易版だが、`paragraphs`で完全に代替可能

### Related Issues
- スライド直下の`items`（agenda/content用）は頻出パターンのため残す

## Objectives
- textbox内の`items`を廃止し、`paragraphs`に一本化
- APIの一貫性を向上

## Scope
### In Scope
- textbox内の`items`処理削除
- PPTX→JSON変換時の出力を`paragraphs`に統一
- ドキュメント更新

### Out of Scope
- スライド直下の`items`（agenda/contentレイアウト用）は維持

## Detailed Requirements
### Before
```json
{"type": "textbox", "items": ["A", "B"]}
```

### After
```json
{"type": "textbox", "paragraphs": [
  {"text": "A", "bullet": true},
  {"text": "B", "bullet": true}
]}
```

---
**Created**: 2026-02-03
