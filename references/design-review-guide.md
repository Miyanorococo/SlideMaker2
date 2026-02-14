# Design Review Guide

プレビューPNG画像を確認し、デザイン品質の問題を報告する。

## 前提: 自動検査との役割分担

Phase 3 の `generate` コマンドが以下を自動検知する（プレビュー不要）:
- テキストの過剰縮小（fontScale実測値ベース、100%正確）
- テキストボックスのスライド外はみ出し

Phase 4 のプレビューレビューでは、**自動検査では検知できない問題**に集中する。

## 入力

1. **プレビュー画像パス**: PPTXから生成されたPNG画像のディレクトリまたはファイルパス
2. **出力JSONパス**: 修正が必要な場合の参照用

## 手順

### 1. プレビュー画像を読み込む

スライドのプレビュー画像をfs_readのImageモードで読み込む。

### 2. 各スライドをチェック

以下の観点で問題を検出する：

#### わかりやすさ
- スライドとしてわかりやすいか
- 効果的な構成になっているか
- 構成として改善点はあるか

#### レイアウト
- 要素が画面外にはみ出していないか
- 上部や下部に不自然な空白がないか
- 要素が重なっていないか（意図的な重なり — shape背景+textbox、icon-circle等 — は問題なし）
- テキストが切れていないか
- 図形の上のテキストは要素内の視覚的に理想な場所にあるか（例えば上下中央に綺麗に表示されているか）
- 余白が偏っていないか（上下・左右のバランス）。コンテンツが上寄りで下半分が空いている等
- アイコンとラベルのサイズ・間隔が適切か（アイコンが小さすぎないか、ラベルが窮屈でないか）

#### テキスト
- テキストの内容がおかしくないか
- テキストが小さすぎて読めないか
- テキストの折り返しが不自然でないか
- `{{bold:...}}` や `{{#FF9900:...}}` などの独自記法がそのまま表示されていないか（パース漏れ）

#### テーブル（特に注意）
テーブルはPowerPointのauto-fit（自動縮小）が効かないため、Phase 3の自動検査では検知できない。
プレビューで以下を重点的に確認する：
- セル内テキストが切れていないか（行高が足りずにテキストが途中で見えなくなっている）
- 改行を含むセルの行高が十分か
- 列幅に対してテキストが窮屈でないか
- ヘッダー行とデータ行のフォントサイズバランス

#### コンポーネント整合性
- 複合パーツ（KPIカード、icon-circle等）のアイコンが中心からズレていないか
- 矢印（line）の向きが論理的なフロー（左→右、上→下）と合致しているか
- 検索されたアイコン（例: `icons:Arch_AWS-Lambda_48`）が文脈と合致しているか

#### デザイン
- 色のコントラストが十分か（暗い背景に暗いテキスト等）
- `design-rules.md` で定義されたカラーパレット外の色が混ざっていないか
- グラデーションが派手すぎて可読性を損なっていないか
- 全体的な統一感があるか
- 空白の使い方が適切か

### 3. レビュー結果を報告

問題があるスライドについて、以下の形式で報告する：

```
## レビュー結果

### Slide 2: Architecture Overview
- [テーブル切れ] 3行目のセル内テキストが途中で見えなくなっている
  → Fix: rowHeights の3行目を 50 → 80 に拡張
- [整列] 3つのカードの y 座標が揃っていない（Card2 が 2px 下にずれている）
  → Fix: Card2 の y を 220 に統一

### Slide 5: Cost Comparison
- [コントラスト] 暗い青(#0072E5)のテキストが Dark背景で見にくい
  → Fix: テキスト色を #41B3FF に変更

### 問題なし
- Slide 1, 3, 4, 6 は問題なし
```

**Constraints:**
- You MUST read ALL preview images before reporting
- You MUST be specific about what is wrong and where
- You MUST suggest concrete fixes (e.g. "y座標を50px下げる", "fontSizeを20ptに変更", "rowHeightsを80に拡張")
- You MUST NOT report minor aesthetic preferences as issues — focus on actual problems
- You MUST pay special attention to TABLE elements — they are the most common source of visual issues that cannot be caught automatically
