# Tasks: Slide Override

## Implementation Checklist
- [x] `resolve_override`関数の実装
- [x] `generate`関数にoverride解決処理を統合
- [x] エラーハンドリング（存在しないid、循環参照）

## Validation
- [x] 通常スライド（id/overrideなし）が従来通り動作
- [x] id指定スライドが通常出力される
- [x] override指定でベースelementsが継承される
- [x] override側elementsがベースの上に追加される
- [x] 存在しないidへのoverrideでエラー
- [x] 循環参照でエラー

## Documentation
- [x] tech.mdにid/overrideキーを追記
- [x] SKILL.mdを整理・id/override使用例を追記
- [x] examplesにoverride活用例を追加（agenda-highlight）

---
**Created**: 2026-02-06
