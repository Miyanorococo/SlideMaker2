# Notes: examples体系の再設計

Guidelines:
- **Append-only**: Never edit existing content
- **Capture thought process**: "Initially thought X, but actually Y"
- **Be specific**: Include errors, commands, numbers

## Log

### [2026-02-07 15:06] SPEC作成
ヒアリングで決定した方針：
- Atomic Design的な Component + Pattern の2層構造
- frontmatterの category フィールドで分類
- ディレクトリは分けない（examples/ のまま）
- コマンドインターフェースは変更なし、表示のみグルーピング

---
**Created**: 2026-02-07

### [2026-02-07 15:53] 設計方針の深掘り結果

ヒアリングで以下の方針に収束：

**構成:**
- component-catalog.md: 1ファイルに全部品を集約。毎回読む
- patterns/各パターン: レイアウト骨格の参考。必要なものだけ読む
- ユーザーが独自カタログを追加して拡張可能

**役割分担:**
- カタログ = 「何で作るか」（部品 + テクニック + 応用ガイド）
- パターン = 「どう並べるか」（レイアウト骨格）

**重要な設計原則:**
- カタログとパターンは制約ではなく引き出し
- エージェントの独創性を支援する。縛らない
- JSONの切り出しより設計意図と応用ガイドの言語化に価値がある

**検討過程:**
- 最初: コンポーネント種類ごとにファイル分割 → 全部読み込みそうで分ける意味が薄い
- 次: basic/rich分割 → エージェントは常にいいものを作ろうとするので結局両方読む
- 最終: 1ファイルカタログ + バリエーション併記が最も合理的

**既存の個別componentファイル（5個）は廃止してcatalogに統合する**

### [2026-02-07 17:10] プリミティブ再定義の調査・検討

**きっかけ:**
カタログのレビュー中に「kpi-cardは用途限定的すぎる」「frameのバリエーションは応用ガイドで十分」という議論から、コンポーネントを「プリミティブ」と「レシピ（組み合わせ例）」に分離する方針に。

**方針:**
- プリミティブ: 単体で意味を持つ最小部品。バリエーションを充実させる
- レシピ: プリミティブの組み合わせ例。バリエーションは書かない（プリミティブを応用して自分で考えさせる）
- パターンはレシピを組み合わせたもの → プリミティブ → レシピ → パターンの3層

**プレゼンデザイン要素の調査結果:**

現状カタログにあるもの:
- Container/Frame（枠）
- Connector/Flow（矢印、フロー）
- Text Decoration（グラデーション、ハイライト）
- Overlay（progressive-overlay）
- Separator/Divider（fade-line）
- Badge/Tag
- Bullet List（dot-bullet-list）
- Axis/Scale（spectrum-axis）

漏れている要素:
- Number Marker: 円の中に番号（①②③）。ステップ番号やリスト番号に。oval + textboxで実現
- Divider: シンプルな区切り線。fade-lineはリッチすぎて基本の線がない
- Callout/Annotation: 吹き出し的な注釈。rounded_rectangle + triangle + textboxで実現
- Progress Bar: 進捗バー。2つのrectangle重ね（背景+前景）で実現

**プリミティブ一覧案（13個）:**
1. frame - 枠（単色、グラデーション、アクセントボーダー、破線）
2. divider - 区切り線（単色、フェード、グラデーション）← fade-lineを吸収
3. flow-step - フロー接続（矢印、三角形セパレーター、シェブロン）
4. number-marker - 番号付き円（新規）
5. progress-bar - 進捗バー（新規）
6. spectrum-axis - 両端ラベル軸
7. badge - ステータスバッジ
8. callout - 吹き出し注釈（新規）
9. text-gradient-title - テキストグラデーション
10. section-header-bar - 見出しバー
11. highlight-text-item - アクセントカラーテキスト
12. dot-bullet-list - リッチ箇条書き
13. progressive-overlay - オーバーレイ

**レシピ候補（要検討）:**
- kpi-card = frame + 大数値textbox + ラベルtextbox
- icon-with-desc = image + textbox × 2
- quote-block = frame + 引用符textbox + 本文textbox

**削除済み（この回のカタログ改善）:**
- labeled-arrow, elbow-arrow: line仕様を知っていれば作れる
- difficulty-axis → spectrum-axisにリネーム
- パターン参照の「※」行: 不要
- Style Guideセクション: 各コンポーネントの文脈で読むべき情報。集約するとかえって文脈が切れる

### [2026-02-07 17:20] 追加調査: ビジネスプレゼン要素の深掘り

コンサルスライド・ビジネスプレゼン特有の要素を追加調査。

**追加で発見した要素:**
- Bracket/Brace（波括弧）: 複数要素をグルーピングして「まとめるとこう」を示す。コンサルスライド定番。freeformまたは`{`テキストで実現
- Icon Circle（アイコン背景円）: アイコンの後ろに色付き円。機能紹介やステップ表示で頻出。oval + imageで実現
- Funnel（ファネル）: 段階的絞り込み。台形の積み重ね → レシピ/パターン寄り
- Pyramid（ピラミッド）: 階層構造。三角形+水平線 → レシピ/パターン寄り
- Vertical Timeline: 縦型タイムライン。line + number-marker + textboxの組み合わせ → レシピ寄り

**プリミティブ判定:**
- Bracket → プリミティブ候補。グルーピング表現の基本部品
- Icon Circle → プリミティブ候補。アイコン装飾の基本
- Funnel/Pyramid/Timeline → レシピまたはパターン。プリミティブの組み合わせ

**更新後のプリミティブ一覧案（15個）:**
1. frame - 枠（単色、グラデーション、アクセントボーダー、破線）
2. divider - 区切り線（単色、フェード、グラデーション）← fade-lineを吸収
3. flow-step - フロー接続（矢印、三角形セパレーター、シェブロン）
4. number-marker - 番号付き円
5. progress-bar - 進捗バー
6. spectrum-axis - 両端ラベル軸
7. badge - ステータスバッジ
8. callout - 吹き出し注釈
9. bracket - 波括弧グルーピング
10. icon-circle - アイコン背景円
11. text-gradient-title - テキストグラデーション
12. section-header-bar - 見出しバー
13. highlight-text-item - アクセントカラーテキスト
14. dot-bullet-list - リッチ箇条書き
15. progressive-overlay - オーバーレイ

### [2026-02-07 17:48] カタログ実装の詳細記録

**プリミティブ15個を6カテゴリで実装完了:**

Containers（2）: frame, section-header-bar
Connectors（2）: flow-step, brace
Indicators（4）: number-marker, badge, progress-bar, spectrum-axis
Text Styles（2）: text-gradient-title, highlight-text-item
Decorations（3）: divider, icon-circle, dot-bullet-list
Techniques（2）: progressive-overlay, callout

**レシピをcomponent-recipe.mdに分離:**
- kpi-card, icon-with-desc, quote-block

**shape_map追加:**
- left_brace, right_brace, left_bracket, right_bracket

**ピクセルパーフェクトの原則:**
shape上にtextboxを重ねる場合、以下が必須:
- textboxにheight指定（shapeと同じ高さ）
- verticalAnchor: 1（垂直中央）
- align: "center"（水平中央）
- marginLeft/Right/Top/Bottom: 0（デフォルトマージンによるずれ防止）

隣接テキストの垂直中央揃え:
- y = shapeのy + (shapeのheight - textboxのheight) / 2

**検討・却下した案:**
- Style Guideセクション: 各コンポーネントの文脈で読むべき情報。集約すると文脈が切れる → 削除
- bracketをline組み合わせで実現: MSO_SHAPEにright_brace/left_braceがあった → shape使用
- margin=0不要説: badgeサイズでは差が出る → 必要
