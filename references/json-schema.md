# JSON Schema Reference

## Top-level

```json
{
  "theme": "dark",
  "slides": [...]
}
```

- `"theme"`: `"light"` | `"dark"`

## コメント

JSONにはコメント構文がないため、`_comment`キーを使う。elements内でも使用可能（無視される）。

```json
{"_comment": "--- セクション: 課題 ---"}
```

## Slide Layouts

| layout | ユースケース | フィールド | 背景色(dark) |
|--------|-------------|-----------|-------------|
| title | 表紙 | title, subtitle, department, customer, date | |
| agenda | アジェンダ | title, items | #171D25 |
| section | セクション区切り | title | |
| subsection | サブセクション区切り | title | |
| content | 通常スライド（左ラインあり） | title, elements | #171D24 |
| title_only | 全面キャンバス（図解向き） | title, elements | #000000 |
| thankyou | 締め | (なし) | |

特別な指示がない限り、titleで始まり、thankyouで終わること。
title, agenda, section, プレゼン本体, thankyouが一般的な流れ。

※ content/title_onlyで`"title": ""`を指定するとタイトルプレースホルダを削除

## Slide Override（継承）

```json
{"id": "base", "layout": "content", "title": "Agenda", "elements": [...]}
{"override": "base", "layout": "content", "title": "Agenda - Section 1", "elements": [...]}
```

- 派生はベースの`elements`を継承、派生側`elements`が上に重なる
- `title`/`notes`/`layout`は継承しない
- チェーン継承可能（A → B → C）

**ユースケース:**
- **アジェンダハイライト**: ベースに全項目、派生で現在セクションをハイライト色のshapeで上書き
- **プログレッシブ開示**: アーキテクチャ図を段階的に構築。派生で1要素ずつ追加
- **ステップハイライト**: ベースに全ステップを薄い色で配置、派生で現在ステップだけ強調
- **繰り返しフレーム**: 顧客事例など同じ枠で中身だけ変わるスライドの共通化
- Progressive Disclosure, Highlight, Agendaなどで積極的に活用する

## Positioning

- 座標・サイズはピクセル（px）、1920×1080基準
- 推奨描画エリア: x=58〜1862, y=173〜950
- 最下部の要素: `y + height ≥ 850` 目安

### 座標早見表

| % | x (横) | y (縦) |
|---|--------|--------|
| 5 | 96 | 54 |
| 10 | 192 | 108 |
| 25 | 480 | 270 |
| 50 | 960 | 540 |
| 75 | 1440 | 810 |
| 100 | 1920 | 1080 |

**よく使うサイズ**: アイコン 100〜200px、カード幅 400〜600px、2カラム 各900px、3カラム 各600px、4カラム 各450px

## Elements

### textbox
```json
{
  "type": "textbox",
  "x": 58, "y": 216, "width": 1804, "height": 120,
  "align": "left|center|right",
  "fontSize": 18,
  "text": "テキスト",
  "fill": "#FF9900",
  "line": "#232F3E",
  "lineWidth": 2,
  "rotation": 45,
  "autoWidth": false,
  "marginLeft": 91440, "marginTop": 45720, "marginRight": 91440, "marginBottom": 45720,
  "verticalAnchor": 1,
  "textGradient": {"angle": 0, "stops": [{"position": 0, "color": "#..."}, {"position": 1, "color": "#..."}]}
}
```

- `height`: 指定→テキスト自動縮小、未指定→箱がテキストに合わせて伸びる
  - height目安: 1行=`fontSize × 3.5`、複数行=`行数 × fontSize × 2.7`（afterSpace等で変動）
- `autoWidth`: true→word_wrap無効（テキスト幅に合わせる）
- `margin*`: EMU単位
- `verticalAnchor`: 1=top, 3=middle, 4=bottom
- **改行**: `\n`で改行可能（内部的にparagraphに分割される）

**箇条書き / 番号付き**:
```json
{"type": "textbox", "paragraphs": [
  {"text": "項目1", "bullet": true},
  {"text": "手順1", "numbering": "arabicPeriod"}
]}
```

- `spaceAfter`: 段落後スペース（hundredths of a point。800 = 8pt）。textboxの`paragraphs`、shapeの`items`両方で使用可能
```json
{"text": "項目1", "bullet": true, "spaceAfter": 800}
```

### table
```json
{
  "type": "table",
  "x": 58, "y": 270, "width": 1804, "height": 250,
  "colWidths": [400, 500, 300, 604],
  "rowHeights": [50, 50, 50],
  "firstRow": true, "bandRow": true,
  "tableStyleId": "{5C22544A-...}",
  "headers": [
    {"text": "Service", "align": "center", "bold": true, "fontSize": 14, "fontColor": "#FFFFFF", "fill": "#232F3E"},
    "列2"
  ],
  "rows": [
    [
      {"text": "Lambda", "bold": true, "fontColor": "#FF9900"},
      {"text": "$120", "align": "right"}
    ],
    [
      {"text": "S3 + CF", "gridSpan": 2},
      {"merged": true, "text": ""}
    ]
  ]
}
```

- `height`: 省略時は行数から自動計算
- `colWidths`: 各列の幅（px配列）。省略時は均等分割
- `rowHeights`: 各行の高さ（px配列）。省略時はデフォルト
- `firstRow`/`lastRow`/`firstCol`/`lastCol`/`bandRow`/`bandCol`: テーブルスタイルフラグ
- `tableStyleId`: PPTXテーブルスタイルGUID（省略可）
- `headers`/`rows`のセル値: 文字列（テキストのみ）またはオブジェクト（プロパティ付き）

**セルオブジェクト**:
```json
{
  "text": "内容",
  "fill": "#232F3E",
  "fontColor": "#FFFFFF",
  "fontSize": 14,
  "bold": true,
  "italic": true,
  "align": "center|left|right",
  "anchor": "t|ctr|b",
  "gridSpan": 2,
  "rowSpan": 2,
  "merged": true,
  "margins": {"left": 10, "right": 10, "top": 5, "bottom": 5},
  "borders": {
    "left":   {"color": "#FFFFFF", "width": 1.0},
    "right":  {"color": "#FFFFFF", "width": 1.0},
    "top":    {"color": "#FFFFFF", "width": 1.0, "fill": "none"},
    "bottom": {"color": "#FFFFFF", "width": 1.0}
  }
}
```

- `merged: true`: gridSpan/rowSpanで消えたセル（空テキストで配置）
- `anchor`: 縦方向配置（t=上, ctr=中央, b=下）
- プロパティなしのセルは従来通り文字列でOK

### image
```json
{
  "type": "image",
  "src": "icons:Arch_AWS-Lambda_48",
  "x": 192, "y": 324, "width": 154, "height": 154,
  "rotation": 0,
  "label": "Lambda",
  "labelPosition": "bottom|right|none",
  "labelSize": 11,
  "link": "https://..."
}
```

- `src`: `icons:NAME`、ファイルパス、相対パス
- `height`: 省略時はアスペクト比維持
- `labelSize`: デフォルト11
- `iconColor`: （オプション）SVGアイコンの色を変更。単色SVGのみ対応（多色アイコンは無視）

### shape
```json
{
  "type": "shape",
  "shape": "rectangle|rounded_rectangle|oval|circle|arrow_right|arrow_left|arrow_up|arrow_down|arrow_circular|arrow_left_right|arrow_up_down|arrow_curved_right|arrow_curved_left|arrow_curved_up|arrow_curved_down|arrow_circular_left|arrow_circular_left_right|triangle|diamond|pentagon|hexagon|cross|trapezoid|parallelogram|chevron|donut|arc|block_arc|chord|pie|pie_wedge|cloud|lightning_bolt|star_5_point|no_symbol|callout_rectangle|callout_rounded_rectangle|callout_oval|flowchart_process|flowchart_decision|flowchart_terminator|left_brace|right_brace|left_bracket|right_bracket",
  "x": 192, "y": 216, "width": 576, "height": 162,
  "fill": "#FF9900",
  "opacity": 0.0-1.0,
  "gradient": {"angle": 90, "stops": [{"position": 0, "color": "#...", "opacity": 1.0}, {"position": 1, "color": "#..."}]},
  "line": "#232F3E",
  "lineWidth": 2,
  "lineGradient": {"angle": 90, "stops": [...]},
  "dashStyle": "solid|dash|dot|dash_dot|long_dash|square_dot",
  "adjustments": [0.06],
  "rotation": 0,
  "text": "ラベル",
  "fontSize": 14,
  "textAlign": "left|center|right",
  "verticalAnchor": 1-4,
  "items": ["箇条書き1", "箇条書き2"],
  "link": "https://..."
}
```

- `opacity`: 塗りの不透明度（デフォルト1.0）
- `adjustments`: 調整ハンドル値（rounded_rectangleの角丸等）
- `verticalAnchor`: 1=top, 3=middle, 4=bottom（デフォルト3）
- `rotation`: 回転角度（度数、時計回り）
- `gradient.angle`: グラデーション角度（0=左→右, 90=上→下, 180=右→左, 270=下→上）
- `circle`: ovalのエイリアス。min(width, height)で正方形化される
- `arrow_circular` / `arrow_circular_left` / `arrow_circular_left_right`: 循環図用の円弧矢印
- `arrow_curved_*`: 曲がった太い矢印
- `chevron`: プロセスフロー用
- `donut`: adjustments=[穴の大きさ(default:0.25)]
- `block_arc`: adjustments=[開始角, 終了角, 太さ(default:0.25)]。360度でドーナツ
- `arc`: adjustments=[開始角, 終了角]。線の円弧
- `pie`: adjustments=[開始角, 終了角]。扇形
- `chord`: adjustments=[開始角, 終了角]。弓形（弦で閉じた円弧）
- `pie_wedge`: 90度固定の扇形
- `callout_*`: 吹き出し
- `flowchart_*`: フローチャート図形

### line
```json
{
  "type": "line",
  "x": 192, "y": 324, "width": 384, "height": 0,
  "color": "#8FA7C4",
  "lineWidth": 1.25,
  "dashStyle": "solid|dash|dot|dash_dot|long_dash|square_dot",
  "connectorType": "straight|elbow|curved",
  "headEnd": "arrow|triangle|stealth|oval|diamond|none",
  "tailEnd": "arrow",
  "rotation": 0,
  "lineGradient": {"angle": 0, "stops": [...]}
}
```

### freeform
```json
{
  "type": "freeform",
  "x": 192, "y": 216, "width": 576, "height": 162,
  "fill": "none",
  "line": "#FFFFFF",
  "lineWidth": 3,
  "lineGradient": {"angle": 0, "stops": [{"position": 0, "color": "#295EFF"}, {"position": 1, "color": "#DB3300"}]},
  "path": [
    {"cmd": "M", "x": 0, "y": 162},
    {"cmd": "C", "pts": [[100, 162], [100, 80], [200, 80]]},
    {"cmd": "L", "x": 576, "y": 0},
    {"cmd": "Z"}
  ]
}
```

- `path`: パスコマンド配列（座標はpx単位、shape内部の相対座標）
  - `M` — 移動（`x`, `y`）
  - `C` — 3次ベジェ曲線（`pts`: [[cp1x,cp1y], [cp2x,cp2y], [endx,endy]]）
  - `L` — 直線（`x`, `y`）
  - `Z` — パスを閉じる
- `lineGradient`: 線のグラデーション（`line`の代わりに指定。stops/angle/opacity対応）
- `lineWidth`: pt単位。SVGからの変換: `stroke-width × (表示幅 / viewBox幅) / 2`
- `customGeometry`: 生XML文字列でも指定可能（`path`が優先）
- ベジェ制御点の考え方: CP1は始点方向に「引っ張る」、CP2は終点方向に「引っ張る」

### group
```json
{
  "type": "group",
  "elements": [{"type": "shape", ...}, {"type": "textbox", ...}]
}
```
- 子要素は展開されて個別に追加（グループ化されない）

## Styled Text

```
{{bold:太字}}
{{italic:斜体}}
{{#FF9900:オレンジ色}}
{{24pt:24ポイント}}
{{bold,24pt,#FF9900:複合スタイル}}
{{link:https://example.com:リンクテキスト}}
```

## プレースホルダ（ユーザー編集用）

```json
{
  "type": "shape", "shape": "rectangle",
  "fill": "#F0F0F0", "line": "#CCCCCC",
  "text": "{{#888888:<ここにスクリーンショットを挿入>}}"
}
```
