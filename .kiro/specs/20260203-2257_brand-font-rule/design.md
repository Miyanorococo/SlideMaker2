# Design: ブランドフォントルール適用

## 定数定義
```python
FONT_FULLWIDTH = "メイリオ"
FONT_HALFWIDTH = "Amazon Ember"
```

## 文字判定ロジック
```python
def is_fullwidth(char):
    """全角文字判定（CJK文字、全角記号等）"""
    return ord(char) > 127
```

## 実装戦略
- `apply_text_to_shape()` 内でrunにフォント設定を追加
- 既存の `_parse_styled_text()` は変更不要（run分割後にフォント適用）

## 影響範囲
- textbox: `apply_text_to_shape()` 経由
- table: セル内テキストに同様の処理
- shape: `apply_text_to_shape()` 経由

---
**Created**: 2026-02-03
