# Tasks: 座標単位を%からpxに変更

## Implementation Checklist

### Phase 1: マイグレーション準備
- [x] `scripts/migrate_pct_to_px.py` 作成
- [x] demo.json, showcase.json を変換
- [x] examples/*.md 内のJSONを変換

### Phase 2: コア実装
- [x] pptx_builder.py: `_pct_to_emu()` → `_px_to_emu()` に変更
- [x] pptx_builder.py: 全呼び出し箇所を修正
- [x] pptx_to_json.py: EMU→px変換式を修正

### Phase 3: ドキュメント
- [x] .kiro/steering/tech.md 更新
- [x] SKILL.md 更新

## Validation
- [x] 変換後のJSONでPPTX生成が成功
- [x] 正方形指定（width=height）が実際に正方形になる
- [x] pptx_to_json で逆変換した値がpxで出力される

---
**Created**: 2026-02-05
