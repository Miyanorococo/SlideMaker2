# Notes: pattern-dsl

Guidelines:
- **Append-only**: Never edit existing content
- **Capture thought process**: "Initially thought X, but actually Y"
- **Be specific**: Include errors, commands, numbers

## Log

### [2026-02-08 19:38] 着想メモ

layout-catalog（19レイアウト）+ component-catalog + component-recipe が揃った段階で、
パターン（完成形スライド）を生JSONではなく「プリミティブの組み合わせ記述」で表現できるのでは？

#### 現状の問題
- 既存パターン（2x2-matrix.md等）は生JSONがハードコードされている
- 座標値が直書きで、レイアウト変更時に全座標を再計算する必要がある
- コンポーネントとレイアウトの知識が重複している

#### 構想: パターンDSL（宣言的記述）

```markdown
# AWS Migration Assessment

## layout
split(60:40)

## left
- hero-text: "クラウド移行でコスト最適化を実現" (48pt, bold)
- body-text: "現行オンプレミス環境の..." (20pt, #8FA7C4)
- cta-button: "詳細を見る →" (accent)

## right
columns(3, gap=GAP_SM)
- kpi-card: label="TCO削減", value="40%", sub="3年間累計", color=accent
- kpi-card: label="移行対象", value="128", sub="サーバー台数", color=accent1
- kpi-card: label="完了予定", value="6ヶ月", sub="Phase 1完了まで", color=accent3
```

#### 設計判断ポイント
1. **パーサー不要案**: エージェントがDSLを読んでJSONに展開。エージェントの読解力がパーサー
2. **パーサー実装案**: pptx_builder.pyにDSL→JSON変換を追加
3. **自由度**: DSLで表現しきれないカスタマイズ（微妙な位置調整等）の扱い
4. **形式化の度合い**: ゆるい自然言語寄り vs 厳密な構文定義
5. **既存パターンとの互換性**: 全書き換え or 段階的移行

#### 期待効果
- パターンの記述量が大幅削減（JSON数百行 → DSL数十行）
- レイアウト変更時に座標再計算不要（layout-catalogが解決）
- コンポーネントの再利用が明示的になる
- パターンの意図（何をどこに置くか）が読みやすくなる

#### 検証済みの前提
- layout-catalogの計算式は area(ax,ay,aw,ah) パラメータで入れ子可能
- split(60:40)右側にcolumns(3,GAP_SM)の組み合わせで実践的スライド作成を確認済み
- component-recipeのkpi-card等は再利用可能な部品として定義済み

---
**Created**: 2026-02-08

### [2026-02-08 19:47] 方針の明確化

- DSLという言葉は堅すぎた。パーサー不要、エージェントが読めればいい
- 「パターン記述言語」ではなく「パターンの構成記述」
- three-column-cards-skeleton が既にこの方向に近い（座標テーブル + 構造図 + 部品名）
- もう少し自然言語寄りに、レイアウト関数名 + コンポーネント名で構成を宣言する

#### 書き換え対象
- フルJSON型パターン（split-hero-bullets, three-column-cards等）→ 構成記述に
- スケルトン型（three-column-cards-skeleton）→ 座標をlayout-catalog参照に置き換え
- architecture-diagram, component-*, layout-catalog → 変更なし

#### 懸念
- 現状 `examples パターン名` でJSON即コピペできる即時性が失われる
- エージェントの展開精度が未検証
- → まず1パターンで試して検証する

### [2026-02-08 19:47] 方針の明確化

- 形式は自然言語でOK。DSL的な構文定義は不要
- 重要なのは「誤解なくレイアウトが伝わること」
- layout-catalogの関数名 + component-recipeの部品名を自然言語の中で使う
- パーサー実装なし。エージェントが読んでJSON展開する前提
- three-column-cards-skeleton が方向性として近い

#### 書き換え対象
- フルJSON型パターン → 自然言語の構成記述に
- スケルトン型 → 座標をlayout-catalog参照に置き換え
- component-*, layout-catalog, architecture-diagram → 変更なし

#### 次のステップ
- 1パターンで試して、エージェントがJSON展開できるか検証
