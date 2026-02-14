# Design: Slide Override

## JSON Schema

### 新規キー
| Key | Type | Description |
|-----|------|-------------|
| `id` | string (optional) | スライド識別子。他スライドからoverrideで参照可能 |
| `override` | string (optional) | 継承元スライドのid |

### 制約
- `id`と`override`は同一スライドに共存可能（チェーン継承）
- `override`指定時、layout/title/notesは継承しない

## Implementation Strategy

### 処理フロー
```
1. 全スライドをパース
2. id → slideデータのマップを構築
3. 各スライドを処理:
   - overrideなし: 通常処理
   - overrideあり:
     a. 継承元を解決（循環検出）
     b. ベースのelementsをコピー
     c. override側のelementsを追加
     d. スライド生成
```

### 変更箇所
- `pptx_builder.py`:
  - `generate`関数内でoverride解決処理を追加
  - 新規関数: `resolve_override(slide, id_map, visited)`

### エラーハンドリング
- 存在しないidへのoverride → `ValueError: Override target 'xxx' not found`
- 循環参照 → `ValueError: Circular override detected: a -> b -> a`

---
**Created**: 2026-02-06
