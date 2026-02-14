# Design: line要素のAWS推奨デフォルト値

## Implementation Strategy

### pptx_builder.py
`_add_line`メソッドでテーマに応じたデフォルト色・線幅を適用：

```python
# デフォルト色（テーマ依存）
default_color = "#8FA7C4" if self.theme == "dark" else "#000000"
color = elem.get("color", default_color)

# デフォルト線幅
line_width = elem.get("lineWidth", 1.25)
```

### SKILL.md
アーキテクチャ図の推奨パターンセクションを追加

### tech.md
line要素のデフォルト値を更新

---
**Created**: 2026-02-03
