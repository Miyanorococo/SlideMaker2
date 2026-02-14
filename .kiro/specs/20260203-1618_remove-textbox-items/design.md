# Design: textbox内itemsの廃止

## Implementation Strategy

### pptx_builder.py
- `items`分岐を削除
- `paragraphs`と`text`の2パターンのみに

```python
# Before
if paragraphs:
    ...
elif items:      # ← 削除
    ...
else:
    ...

# After
if paragraphs:
    ...
else:
    # text処理
```

### pptx_to_json.py
- 複数段落を`items`ではなく`paragraphs`形式で出力
- 箇条書きの場合は`bullet: true`を付与

```python
# Before
if items:
    result["items"] = items

# After
if paragraphs:
    result["paragraphs"] = [{"text": t, "bullet": True} for t in paragraphs]
```

### ドキュメント
- SKILL.md: textbox内`items`の記載削除
- tech.md: スキーマから`items`削除

---
**Created**: 2026-02-03
