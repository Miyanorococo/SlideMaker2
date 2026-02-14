# Tasks: examples体系の再設計

## Implementation Checklist
- [x] `_get_frontmatter_description` を `_get_frontmatter` に変更し、dict返却（name, description, category）
- [x] `cmd_examples` の一覧表示をカテゴリ別グルーピングに変更
- [x] 既存examples（10ファイル）に `category: pattern` 追加
- [x] 初期Component作成（kpi-card, icon-with-desc, flow-step, quote-block, section-header-bar）
- [x] SKILL.md にComponent/Patternの使い分け説明追記

## Validation
- [x] `python3 scripts/pptx_builder.py examples` でカテゴリ別表示される
- [x] `python3 scripts/pptx_builder.py examples kpi-card` で詳細表示される
- [x] category未指定のexampleがpatternとして表示される（後方互換）

---
**Created**: 2026-02-07
