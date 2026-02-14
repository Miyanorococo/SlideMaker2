# Design: layout-catalog

## ファイル構成
- `examples/layout-catalog.md` — 新規作成（category: component）
- `.kiro/steering/tech.md` — Examples Frontmatterセクションに役割分離ガイド追記

## layout-catalog.md 構造

```markdown
---
name: layout-catalog
description: レイアウト座標テーブル集。計算式+デフォルト定数で任意領域にスケール可能
category: component
---

# Layout Catalog

配置パターンの計算式 + 座標テーブル集。部品はcomponent-catalogから選択して組み合わせる。
各レイアウトは任意の領域 area(x, y, w, h) に適用可能。

## 共通定数（検証済み）
| 定数 | 値 | 用途 |
|---|---|---|
| MARGIN | 58 | スライド端からの余白 |
| CONTENT_X | 58 | 描画エリア左端 |
| CONTENT_Y | 173 | タイトル下の描画開始y |
| CONTENT_W | 1804 | 描画エリア幅 (1920 - 58×2) |
| CONTENT_H | 777 | 描画エリア高さ (950 - 173) |
| GAP | 57 | 要素間の標準間隔 |
| GAP_SM | 24 | 要素間の狭い間隔 |

---

### layout-name
一言説明。ユースケース。

**計算式** (area_x, area_y, area_w, area_h):
- param = formula

**デフォルト座標**（全幅適用時）:
| バリエーション | param1 | param2 | ... |
|---|---|---|---|

**スケルトンJSON**: （最小構成）

**応用ガイド**: 枠線、部品差し替え、スケール等
```

### 設計原則
- **計算式が主、座標テーブルが副**: 計算式で任意領域にスケール可能。デフォルト座標は全幅適用時の便利表
- **検証済み定数を提供**: gap, margin等のデザイン的に良い値はカタログ側で決定済み
- **組み合わせ可能**: split右側にcolumns、grid内にfunnel等、area指定で入れ子適用できる

## 各レイアウトの設計

### columns
- バリエーション: 2列, 3列, 4列
- 座標テーブル: x, width, 中央x, gap
- スケルトン: frame × N

### split
- バリエーション: 50:50, 60:40, 70:30（左右反転も）
- 座標テーブル: 左x/width, 右x/width, gap

### grid-2x2
- 固定: 2行×2列
- 座標テーブル: 4セルのx, y, width, height

### bento
- バリエーション: 大1+小2（L字）, 大1+小3, 大2+小2
- 座標テーブル: 各セルのx, y, width, height

### rows
- バリエーション: 2行, 3行, 4行
- 座標テーブル: y, height, divider y

### hero-body
- バリエーション: hero高さ 40%, 50%
- 座標テーブル: hero領域, body領域

### centered
- 固定: 中央配置の座標
- 座標テーブル: 各要素サイズ別のx, y

### full-bleed
- 固定: 全面 + オーバーレイ領域
- 座標テーブル: overlay位置バリエーション（下部, 中央, 左寄せ）

### timeline
- バリエーション: 3, 4, 5, 6ステップ（横）
- 座標テーブル: 各ステップのx, マーカーy, ラベルy

### process-flow
- バリエーション: 3, 4, 5ステップ（横）
- 座標テーブル: box x/y/width, arrow x/y

### funnel
- バリエーション: 3, 4, 5段
- 座標テーブル: 各段のx, y, width, height

### pyramid
- バリエーション: 3, 4, 5段
- 座標テーブル: 各段のx, y, width, height

### cycle
- バリエーション: 3, 4, 5, 6ノード
- 座標テーブル: 各ノードのx, y + 接続線

### centric
- バリエーション: 4, 5, 6周辺ノード
- 座標テーブル: 中心x/y, 各ノードのx, y

### comparison
- 固定: 左右対比
- 座標テーブル: 左領域, VS中央, 右領域

### venn
- バリエーション: 2円, 3円
- 座標テーブル: 各円のx, y, width/height, 重なり領域

### dashboard
- バリエーション: 2+2, 1+3, 3+1
- bento応用、座標テーブルで提供

## tech.md 追記内容

```markdown
## Examples の役割分離

### component（プリミティブ）
- `component-catalog.md` — 部品。見た目の表現（frame, badge, divider等）
- `component-recipe.md` — 部品の組み合わせレシピ（kpi-card, icon-with-desc等）
- `layout-catalog.md` — 配置座標。レイアウトの骨格（columns, split, grid等）

### pattern（ショーケース）
目的特化の完成形デザイン。component + layoutを組み合わせた見本。
エージェントはpatternをゴールイメージとして参照し、
component-catalogとlayout-catalogから部品と配置を選んで構成する。
```

## 実装戦略
- 優先度高（頻出・座標計算が複雑）: columns, split, grid-2x2, rows, timeline, process-flow
- 優先度中: bento, hero-body, centered, comparison, funnel, pyramid
- 優先度低（複雑な図形が必要）: cycle, centric, venn, dashboard, full-bleed

各レイアウトは:
1. 計算式を定義（area_x, area_y, area_w, area_h パラメータ）
2. デフォルト座標テーブルを算出（全幅適用: area=CONTENT_X, CONTENT_Y, CONTENT_W, CONTENT_H）
3. スケルトンJSONを作成
4. generate + preview で検証

---
**Created**: 2026-02-08
