# Design: contentレイアウト再設計

## 変更箇所

### pptx_builder.py
`LAYOUT_MAP`のcontent定義を変更：
```python
# Before
"content": {"light": 15, "dark": 15}

# After
"content": {"light": 7, "dark": 7}
```

contentの処理をtitle_onlyと同じにする（タイトル設定＋elements自由配置）

### tech.md
Layout Mapテーブルを更新：
- contentのmasterIndex: 15→7
- contentの用途説明を更新

---
**Created**: 2026-02-04
