---
name: layout-catalog
description: レイアウト座標テーブル集。必ず読み込む。
category: component
---

# Layout Catalog

配置パターンの計算式 + 座標テーブル集。
各レイアウトは任意の領域 `area(x, y, w, h)` に適用可能。組み合わせ（split右側にcolumns等）もarea指定で実現。
Pythonを用いて座標計算をすることを推奨する。

## 共通定数

| 定数 | 値 | 用途 |
|---|---|---|
| AX | 96 | デフォルト描画エリア左端 |
| AY | 173 | タイトル下の描画開始y |
| AW | 1728 | デフォルト描画エリア幅 (1920 - 96×2) |
| AH | 777 | デフォルト描画エリア高さ (950 - 173) |
| GAP | 57 | 要素間の標準間隔 |
| GAP_SM | 24 | 要素間の狭い間隔 |

---

## columns
N列均等配置。

```
col_w = (aw - gap × (N-1)) / N
col_x[i] = ax + i × (col_w + gap)
```

3列 (デフォルト):
| | Col 1 | Col 2 | Col 3 |
|---|---|---|---|
| x | 96 | 691 | 1286 |
| w | 538 | 538 | 538 |

y=173, h=777 共通。2列: w=835, x=96/988。4列: w=389, x=96/542/988/1434。

---

## split
左右非対称分割。

```
left_w = aw × ratio - gap / 2
right_x = ax + left_w + gap
right_w = aw - left_w - gap
```

| | 50:50 | 60:40 | 70:30 |
|---|---|---|---|
| left w | 835 | 1008 | 1181 |
| right x | 988 | 1161 | 1334 |
| right w | 836 | 663 | 490 |

---

## grid-2x2
2×2マトリクス。

```
cell_w = (aw - gap) / 2
cell_h = (ah - gap) / 2
cell[row][col]_x = ax + col × (cell_w + gap)
cell[row][col]_y = ay + row × (cell_h + gap)
```

| | 左 | 右 |
|---|---|---|
| 上 | (96, 173, 835, 360) | (988, 173, 836, 360) |
| 下 | (96, 590, 835, 360) | (988, 590, 836, 360) |

---

## rows
N行の横帯配置。

```
row_h = (ah - gap × (N-1)) / N
row_y[i] = ay + i × (row_h + gap)
```

3行: h=221, y=173/451/729。x=96, w=1728 共通。

---

## timeline
横タイムライン。columnsと同じ分割 + 横線・マーカー。

```
step_w/step_x: columnsと同じ
line_y = ay + ah × 0.45
marker_y = line_y - 12
desc_y = line_y + 28
```

---

## process-flow
矢印接続のプロセスフロー。columnsと同じ分割 + 矢印。

```
box_w = (aw - gap × (N-1)) / N
box_h = ah × 0.4
box_y = ay + (ah - box_h) / 2
arrow_x[i] = box_x[i] + box_w + (gap - 40) / 2
```

---

## bento
不均等グリッド。split + rows の組み合わせ。

大1+小2:
| セル | x | y | w | h |
|---|---|---|---|---|
| 大 | 96 | 173 | 835 | 777 |
| 小・上 | 988 | 173 | 836 | 360 |
| 小・下 | 988 | 590 | 836 | 360 |

---

## hero-body
上部ヒーロー + 下部コンテンツ。

```
hero_h = ah × ratio
body_y = ay + hero_h + gap
body_h = ah - hero_h - gap
```

40:60: hero_h=311, body_y=541, body_h=409。

---

## centered
中央集中配置。

```
cx = ax + (aw - cw) / 2
cy = ay + (ah - ch) / 2
```

---

## comparison
左右対比。columns-2 + 中央divider line。divider_x=959。

---

## funnel
上から下へ絞り込み。

```
step_h = (ah - gap × (N-1)) / N
shrink = aw × 0.15
step_w[i] = aw - shrink × i
step_x[i] = ax + (aw - step_w[i]) / 2  # 中央揃え
step_y[i] = ay + i × (step_h + gap)
```

## pyramid
funnelの逆。`step_w[i] = aw - shrink × (N-1-i)`

---

## cycle
ノードを円周上に配置。

```
cx = ax + aw / 2;  cy = ay + ah / 2
r = min(aw, ah) / 2 - node_w / 2 - 20
angle[i] = -π/2 + 2π × i / N
node_x[i] = cx + r × cos(angle[i]) - node_w / 2
node_y[i] = cy + r × sin(angle[i]) - node_h / 2
```

## centric
cycle + 中心ハブノード。hub: (860, 461, 200, 200)。

---

## venn
重なり合う円。

```
overlap = circle_d × 0.3
offset = (circle_d - overlap) / 2
```

2円 (d=400): 左(620, 361), 右(900, 361)。

---

## dashboard
bento + rows + columns の組み合わせ。

2+2 (grid-2x2と同一):
| セル | x | y | w | h |
|---|---|---|---|---|
| 上左 | 96 | 173 | 835 | 360 |
| 上右 | 988 | 173 | 836 | 360 |
| 下左 | 96 | 590 | 835 | 360 |
| 下右 | 988 | 590 | 836 | 360 |

1+3 (上1大 + 下3列):
| セル | x | y | w | h |
|---|---|---|---|---|
| 上 | 96 | 173 | 1728 | 360 |
| 下左 | 96 | 590 | 538 | 360 |
| 下中 | 691 | 590 | 538 | 360 |
| 下右 | 1286 | 590 | 538 | 360 |

## full-bleed
全面画像(0,0,1920,1080) + 半透明オーバーレイ(opacity=0.6) + テキスト。

| バリエーション | overlay_x | overlay_y | overlay_w | overlay_h |
|---|---|---|---|---|
| 下部 | 0 | 780 | 1920 | 300 |
| 中央 | 0 | 390 | 1920 | 300 |
| 左寄せ | 0 | 0 | 960 | 1080 |

## matrix
2軸象限図。cross=(960, 561)。軸線は両端矢印(headEnd/tailEnd: "triangle")。

| 象限 | x | y | w | h |
|---|---|---|---|---|
| 左上 | 156 | 173 | 784 | 368 |
| 右上 | 980 | 173 | 784 | 368 |
| 左下 | 156 | 581 | 784 | 369 |
| 右下 | 980 | 581 | 784 | 369 |

軸ラベル: 上(860,173), 下(860,920), 左(96,546), 右(1764,546)。

## gantt
タスク名列(w=300) + タイムライン格子。

```
tx = ax + 300 + gap          # タイムライン開始x
ty = ay + 50 + gap           # ヘッダー下
tw = aw - 300 - gap          # タイムライン幅
th = ah - 50 - gap           # タイムライン高さ
row_h = (th - gap × (N_tasks - 1)) / N_tasks
col_w = tw / N_periods
```

4タスク×6期間 (デフォルト):
| 要素 | x | y | w | h |
|---|---|---|---|---|
| タスク名列 | 96 | 247 | 300 | — |
| ヘッダー行 | 420 | 173 | 1404 | 50 |
| タイムライン | 420 | 247 | 1404 | 703 |

行: y=247/428/609/790, h=157。列: x=420から234px刻み。
バー: rounded_rectangle（該当期間のx〜x+col_w×期間数）。
