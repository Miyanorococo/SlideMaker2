# Requirements: layout-catalog

## Background & Context
### User Problems
- エージェントがスライド作成時、座標計算が最も苦手で試行錯誤が多い
- 既存patternは完成形JSONが混在し、「配置の骨格」と「部品の装飾」が分離されていない
- three-column-cardsのPoCで、スケルトン（座標テーブル + 最小JSON）方式が有効と確認済み

### Related Issues
- component-catalog.md: 部品（見た目の表現）を提供
- component-recipe.md: 部品の組み合わせレシピを提供
- → layout-catalog.md: 配置（座標テーブル）を提供する新ファイル

## Objectives
- プレゼンで頻出するレイアウトパターンの座標テーブルを網羅的に提供
- エージェントが座標計算なしで配置できるようにする
- component-catalogの部品と組み合わせてスライドを構成する基盤にする

## Scope
### In Scope
- layout-catalog.md の新規作成（category: component）
- 17種のレイアウトパターンの座標テーブル + スケルトンJSON + 応用ガイド
- tech.md の Examples Frontmatter セクションに component/pattern の役割分離ガイドを追記
- 既存patternの扱い方針の整理

### Out of Scope
- 既存pattern mdファイルの書き換え（別SPECで段階的に実施）
- pptx-maker本体の機能拡張（venn等で必要になった場合は別SPEC）
- catalog-showcase.pptxのようなビジュアル検証（座標テーブルの正確性はJSON生成+プレビューで確認）

## Detailed Requirements

### レイアウト17種

**カラム系**
1. columns — 2/3/4列均等配置
2. split — 左右非対称分割（50:50, 60:40, 70:30）

**グリッド系**
3. grid-2x2 — 2×2マトリクス
4. bento — 不均等グリッド（大1+小2、大1+小3等）

**縦積み系**
5. rows — 横線区切りの行配置（2〜4行）
6. hero-body — 上部ヒーロー領域 + 下部コンテンツ

**中央系**
7. centered — 中央集中（big number, quote, statement）
8. full-bleed — 全面画像 + オーバーレイテキスト

**フロー系**
9. timeline — 横/縦タイムライン（3〜6ステップ）
10. process-flow — 矢印接続のプロセスフロー
11. funnel — ファネル（上から下へ絞り込み）

**構造系**
12. pyramid — ピラミッド/階層
13. cycle — 循環図
14. centric — 中心+放射（ハブ&スポーク）
15. comparison — 左右対比（VS形式）
16. venn — ベン図（2〜3重なり）

**特殊**
17. dashboard — 複数KPI/チャートの配置（bento応用）

### 各レイアウトの記載内容
- 一言説明 + ユースケース
- 座標テーブル（バリエーション別: ステップ数、カラム数等）
- スケルトンJSON（骨格のみ、装飾なし）
- 応用ガイド（枠線、部品差し替え、スケール変更の方向性）

### 設計方針
- 座標テーブルが最大の価値。検証済みの数値を提供する
- JSONは骨格のみ（frame, line等の最小構成）
- 部品の装飾はcomponent-catalogを参照する旨をガイドで示す
- 1920×1080基準、推奨描画エリア x=58〜1862, y=173〜950

---
**Created**: 2026-02-08
