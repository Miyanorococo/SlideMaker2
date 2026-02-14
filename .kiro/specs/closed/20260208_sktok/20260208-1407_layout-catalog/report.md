# Report: layout-catalog

## Summary
- **Problem**: エージェントがスライド作成時に座標計算で試行錯誤が多く、品質にばらつきがあった
- **Solution**: 19種のレイアウトプリミティブを計算式+デフォルト座標テーブルで提供。area(x,y,w,h)パラメータで任意領域にスケール可能
- **Impact**: エージェントは座標計算なしでレイアウトを適用でき、入れ子組み合わせで複雑なスライドも構築可能

## Technical Insights
- GAP=57(3%)は2〜4列で統一感のある間隔。process-flowのみgap=80（矢印余白確保）
- GAP_SM=24は入れ子レイアウト用。split右側にcolumns等
- 右端チェック `last_x + last_w = AX + AW = 1824` で座標精度を担保
- cycle/centric/vennは三角関数座標。min(aw,ah)/2で半径決定のため横長エリアでは左右に余白

## Unexpected Discoveries
- columns-2/grid-2x2で初回GAP=0のバグ。col_x計算でGAP加算漏れ
- process-flowのgap=57では矢印(triangle tailEnd)がboxに近すぎた→80に変更
- matrixは既存2x2-matrixパターンと整合させることで実用性向上
- ganttはSA業務で頻出パターンとして追加。格子座標+バー配置で実用的

## Reusable Patterns
- 計算式パラメータ方式: `layout(N, ax, ay, aw, ah, gap=GAP)` → 任意領域にスケール
- 入れ子組み合わせ: 外側GAP=57、内側GAP_SM=24の使い分け
- 検証ワークフロー: JSON生成→プレビュー→右端チェック→座標修正

## Metadata
- **Status**: Completed
- **Category**: foundation

---
**Closed**: 2026-02-08
