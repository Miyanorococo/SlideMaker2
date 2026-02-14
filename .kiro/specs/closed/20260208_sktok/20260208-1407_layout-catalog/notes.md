# Notes: layout-catalog

Guidelines:
- **Append-only**: Never edit existing content
- **Capture thought process**: "Initially thought X, but actually Y"
- **Be specific**: Include errors, commands, numbers

## Log

### [2026-02-08 14:07] SPEC作成
- PoCでthree-column-cardsをスケルトン化し、座標テーブル + 最小JSONで十分な品質が出ることを確認
- 議論の中で「抽象度の高いパターンはコンポーネント（レイアウト）である」という発見
- component = 部品 + レイアウト、pattern = ショーケース（完成形）という整理に到達
- Webリサーチで17種のレイアウトパターンを特定
- poc-skeleton.json, three-column-cards-skeleton.md はPoC用の一時ファイル

---
**Created**: 2026-02-08

### [2026-02-08 19:35] Phase 1-3 完了 + matrix/gantt追加

- Phase 1 (columns, split, grid-2x2, rows, timeline, process-flow): 座標バグ修正済み
  - columns-2/4, grid-2x2: GAP加算漏れ修正
  - rows: 3行/4行のy値再計算
  - timeline: line_y比率0.35→0.45
  - process-flow: gap=57→80に変更（矢印周りの余白確保）
- Phase 2 (bento, hero-body, centered, comparison, funnel, pyramid): 一発OK、comparison中央線のみ修正
- Phase 3 (cycle, centric, venn, dashboard, full-bleed): 三角関数座標を計算検証+プレビュー
- 追加: matrix（2x2-matrixパターン参考）、gantt（SA業務で頻出）
- 組み合わせ検証: split(60:40)+columns-3(GAP_SM)で実践的スライド作成確認
- GAP=57固定（計算式パラメータで変更可能）、GAP_SM=24は入れ子用
- 全19レイアウト完成
