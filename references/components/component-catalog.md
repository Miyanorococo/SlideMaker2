---
name: component-catalog
description: プリミティブ部品集。必ず読み込む。
category: component
---

# Component Catalog

バリエーションを活用し、組み合わせて独自のデザインを生み出すこと。
light/darkテーマに合わせて色など適宜調整が必要。
パラメータはその場に応じて調整し、オリジナリティを出すこと。（同じデザインを多用すると安っぽくなる）

### ⚠️ 実装上の注意
- **textboxのverticalAnchorは信頼できない**: autofitが上書きするため、テキストの垂直中央が効かない。代わりにshapeのtext + `verticalAnchor: 3`を使うか、手動でy座標を計算する
- **heightを指定するとautofitで縮小される**: fontSizeを維持したい場合はheightを未指定にする。ただしテキストボックスが下に伸びるため、下の要素との重なりに注意
- **textboxのデフォルトmarginTop ≒ 5px**: 精密な位置合わせが必要な場合は`marginTop: 0`を明示指定する

---

## Containers（領域・囲み）

### frame
領域を区切る角丸矩形。カード、セクション区切り、背景ボックスに。
```json
{"type": "shape", "shape": "rounded_rectangle", "x": 96, "y": 346, "width": 538, "height": 540, "adjustments": [0.05], "line": "#8FA7C4", "lineWidth": 1.5}
```
- **fill背景**: `"fill": "#FFFFFF", "opacity": 0.08, "line": "none"` で半透明背景。0.05〜0.1が控えめ、0.15〜0.2で存在感
- **アクセントボーダー**: 左辺に `{"type": "shape", "shape": "rectangle", "x": 96, "y": 346, "width": 4, "height": 540, "fill": "#FF9900", "line": "none"}` を重ねる。上辺バリエーションも可
- **グラデーション枠**: `"lineGradient": {"angle": 0, "stops": [{"position": 0, "color": "#FF9900"}, {"position": 1, "color": "#FBD332"}]}` で枠線にグラデーション
- **破線枠**: `"dashStyle": "dash"` で破線。未確定エリアやオプション表現に

### section-header-bar
セクション内の小見出しバー。コンテンツの区切りに。
```json
{"type": "shape", "shape": "rounded_rectangle", "x": 96, "y": 250, "width": 1728, "height": 60, "fill": "#FFFFFF", "opacity": 0.15, "line": "none", "adjustments": [0.35]},
{"type": "textbox", "x": 115, "y": 258, "width": 500, "height": 48, "fontSize": 16, "verticalAnchor": 1, "marginLeft": 0, "marginTop": 0, "marginBottom": 0, "text": "{{bold:セクション見出し}}"}
```
- アクセント左ボーダー追加: x=96, width=4, fill=#FF9900の矩形を重ねる
- adjustments=[0.35]で角丸を強めにするとピル型に近づく

---

## Connectors（接続・フロー）

### flow-step
ステップ間を接続する横フロー。プロセスやタイムラインに。
```json
{"type": "shape", "shape": "rounded_rectangle", "x": 96, "y": 400, "width": 400, "height": 120, "line": "#FF9900", "lineWidth": 1.5, "adjustments": [0.15], "text": "{{bold,#FFFFFF:Step 1}}\n{{14pt,#8FA7C4:説明}}", "textAlign": "center"},
{"type": "line", "x": 496, "y": 455, "width": 134, "height": 0, "color": "#FF9900", "lineWidth": 1.5, "tailEnd": "arrow"},
{"type": "shape", "shape": "rounded_rectangle", "x": 630, "y": 400, "width": 400, "height": 120, "line": "#FF9900", "lineWidth": 1.5, "adjustments": [0.15], "text": "{{bold,#FFFFFF:Step 2}}\n{{14pt,#8FA7C4:説明}}", "textAlign": "center"}
```
- 重要ステップ: アクセント色での fill opacity=0.2 + 太枠で強調
- 3〜5ステップが視認性の限界
- その他のフロー表現
  - **三角形セパレーター**: `{"type": "shape", "shape": "triangle", "x": 500, "y": 430, "width": 40, "height": 60, "fill": "#FF9900", "line": "none", "rotation": 90}` でステップ間に▶を配置
  - **シェブロン**: ステップ自体を `arrow_right` shapeにして矢印型のステップにする

### brace
波括弧でグルーピング。複数要素をまとめて結論を示すコンサル定番表現。
```json
{"type": "shape", "shape": "right_brace", "x": 800, "y": 300, "width": 40, "height": 300, "line": "#8FA7C4", "lineWidth": 1.5}
```
- 左側に要素群、右側にbrace、その右に結論テキスト
- widthで括弧の深さ、heightで括弧の高さを調整
- adjustmentsで尖り位置を調整（デフォルト=中央）
- **左向き**: `left_brace` で逆方向のグルーピング
- **角括弧**: `right_bracket` / `left_bracket` でシャープな印象に
- **縦線代替**: `{"type": "line", "x": 800, "y": 300, "width": 0, "height": 300}` でシンプルなグルーピング

---

## Indicators（状態・数値）

### number-marker
番号付き円。ステップ番号やリスト番号に。
```json
{"type": "shape", "shape": "oval", "x": 96, "y": 400, "width": 56, "height": 56, "fill": "#FF9900", "line": "none", "text": "{{bold,#FFFFFF:1}}", "textAlign": "center", "verticalAnchor": 3, "fontSize": 24},
{"type": "textbox", "x": 166, "y": 416, "width": 400, "fontSize": 18, "marginTop": 0, "text": "{{bold:ステップタイトル}}"}
```
- 数字はshapeのtext属性 + `verticalAnchor: 3`で確実に垂直中央（textboxのverticalAnchorは効かない）
- ラベルのyは円の中央に合わせる: `oval_y + (oval_height / 2) - (fontSize相当px / 2)`
- **枠線のみ**: `"fill": "none", "line": "#FF9900", "lineWidth": 2` + テキスト色をアクセントに
- **グラデーション背景**: `"gradient": {"angle": 135, "stops": [...]}` で目立たせる
- **小サイズ（32px）**: インライン番号に。**大サイズ（64px）**: セクション番号に

### badge
ステータスバッジ。Preview, GA, New等のラベルに。
```json
{"type": "shape", "shape": "rounded_rectangle", "x": 54, "y": 788, "width": 211, "height": 54, "adjustments": [0.5], "fill": "#AD5CFF", "line": "none"},
{"type": "textbox", "x": 54, "y": 788, "width": 211, "height": 54, "fontSize": 20, "align": "center", "verticalAnchor": 1, "marginLeft": 0, "marginRight": 0, "marginTop": 0, "marginBottom": 0, "text": "{{bold,#FFFFFF:Preview}}"}
```
- adjustments=[0.5]で完全な角丸（ピル型）
- 色でステータスを表現（紫=Preview、緑=#00E500=GA、オレンジ=#FF9900=New）
- **枠線バリエーション**: fill無し + line色で軽い印象に

### progress-bar
進捗バー。達成率やスコア表現に。
```json
{"type": "shape", "shape": "rounded_rectangle", "x": 96, "y": 500, "width": 600, "height": 16, "fill": "#FFFFFF", "opacity": 0.15, "line": "none", "adjustments": [0.5]},
{"type": "shape", "shape": "rounded_rectangle", "x": 96, "y": 500, "width": 420, "height": 16, "fill": "#FF9900", "line": "none", "adjustments": [0.5]}
```
- 前景のwidthで進捗率を表現（420/600 = 70%）
- **グラデーション前景**: `"gradient": {"angle": 0, "stops": [{"position": 0, "color": "#FF9900"}, {"position": 1, "color": "#FBD332"}]}`
- 右端にパーセンテージtextboxを添える

### spectrum-axis
両端ラベル付きグラデーション軸。比較・スペクトラム表現に。
```json
{"type": "textbox", "x": 38, "y": 864, "width": 269, "height": 53, "align": "center", "fontSize": 16, "text": "{{bold,#0072E5:EASIER}}"},
{"type": "line", "x": 307, "y": 886, "width": 1306, "height": 0, "lineWidth": 1.5, "dashStyle": "dash", "lineGradient": {"angle": 0, "stops": [{"position": 0, "color": "#0072E5"}, {"position": 0.5, "color": "#C300E0"}, {"position": 1, "color": "#00E500"}]}, "headEnd": "arrow", "tailEnd": "arrow"},
{"type": "textbox", "x": 1613, "y": 864, "width": 269, "height": 53, "align": "center", "fontSize": 16, "text": "{{bold,#00E500:COMPLEX}}"}
```
- 中央ラベルを置く場合: 背景色矩形で線を隠してからテキスト配置

---

## Text Styles（テキスト装飾）

### text-gradient-title
テキストグラデーションの大型タイトル。インパクト重視のアナウンスに。
```json
{"type": "textbox", "x": 58, "y": 238, "width": 806, "height": 189, "fontSize": 36,
  "text": "{{bold:サービス名}}",
  "textGradient": {"angle": 0, "stops": [{"position": 0, "color": "#FF9900"}, {"position": 1, "color": "#FF5CAA"}]}}
```
- 同系色・隣接色相で自然なグラデーション
- AWS風: #FF9900→#FBD332、クール: #00E500→#41B3FF

### highlight-text-item
アクセントカラーキーワード付きテキスト。ポイント列挙に。
```json
{"type": "textbox", "x": 38, "y": 410, "width": 518, "height": 111, "align": "center", "fontSize": 20,
  "text": "{{#FF9900:グローバルに展開}}される\nインフラストラクチャ"}
```
- キーワード1〜2語をアクセント色に
- 残りは通常色で読みやすく

---

## Decorations（装飾・区切り）

### divider
区切り線。セクション間やコンテンツの分離に。
```json
{"type": "line", "x": 96, "y": 500, "width": 1728, "height": 0, "lineWidth": 1, "color": "#8FA7C4"}
```
- **フェード**: `"lineGradient": {"angle": 0, "stops": [{"position": 0, "color": "#FFFFFF", "opacity": 0}, {"position": 0.3, "color": "#FFFFFF", "opacity": 1}, {"position": 0.7, "color": "#FFFFFF", "opacity": 1}, {"position": 1, "color": "#FFFFFF", "opacity": 0}]}` で両端フェード
- **グラデーション**: lineGradientで色付き区切り線
- **破線**: `"dashStyle": "dash"` で軽い区切り
- **縦線**: width=0, height=値 で縦方向の区切り

### icon-circle
アイコン背景の色付き円。アイコンを目立たせる装飾。
```json
{"type": "shape", "shape": "oval", "x": 240, "y": 300, "width": 80, "height": 80, "fill": "#FF9900", "opacity": 0.15, "line": "none"},
{"type": "image", "src": "icons:Arch_AWS-Lambda_48", "x": 252, "y": 312, "width": 56, "labelPosition": "none"}
```
- アイコン位置: x=円x+(円width-アイコンwidth)/2, y=同様に中央揃え
- **塗りつぶし**: opacity=1.0でアイコンを白抜きに
- **枠線のみ**: `"fill": "none", "line": "#FF9900", "lineWidth": 2` で軽い装飾
- **角丸四角**: ovalの代わりにrounded_rectangle + adjustments=[0.25]で角丸四角背景

### dot-bullet-list
グラデーション縦線 + ドット + テキスト。リッチな箇条書きに。
```json
{"type": "line", "x": 872, "y": 108, "width": 0, "height": 832, "lineWidth": 2,
  "lineGradient": {"angle": 90, "stops": [
    {"position": 0, "color": "#41B3FF"}, {"position": 0.21, "color": "#AD5CFF"},
    {"position": 0.4, "color": "#FF5C85"}, {"position": 0.64, "color": "#00E500"},
    {"position": 0.85, "color": "#FF693C"}, {"position": 1.0, "color": "#FBD332"}
  ]}},
{"type": "shape", "shape": "oval", "x": 862, "y": 168, "width": 21, "height": 22, "fill": "#FFFFFF", "line": "none"},
{"type": "textbox", "x": 941, "y": 151, "width": 922, "height": 92, "fontSize": 16, "text": "{{bold:項目テキスト}}"}
```
- ドットのy座標 = テキストのy + 数px で垂直揃え
- 項目数に応じて等間隔配置
- **単色縦線**: lineGradientを外してシンプルに
- **ドットなし**: 縦線 + テキストのみで控えめなリスト

---

## Techniques（テクニック）

### progressive-overlay
半透明オーバーレイ + フォーカス要素の再描画。段階的説明に。
```json
{"type": "shape", "shape": "rectangle", "x": 0, "y": 130, "width": 1920, "height": 821, "fill": "#000000", "opacity": 0.85, "line": "none"}
```
- overrideと組み合わせて使う
- オーバーレイの上にフォーカス要素を再配置
- opacity 0.8-0.9が見やすい
- **fill色はスライド背景色に合わせる**（content=#171D25, title_only=#000000）。背景色と異なると色味がずれる
- オーバーレイのサイズは隠す要素より上下左右に余裕を持たせる（枠線がはみ出さないように）
- 強調枠（line=#FF9900, lineWidth=2-3）を追加するとさらに明確

### callout
吹き出し注釈。要素を指し示して補足説明に。
```json
{"type": "line", "x": 750, "y": 320, "width": 0, "height": 40, "color": "#FF9900", "lineWidth": 1, "dashStyle": "dash", "tailEnd": "arrow"},
{"type": "shape", "shape": "rounded_rectangle", "x": 600, "y": 200, "width": 300, "height": 80, "fill": "#FFFFFF", "opacity": 0.1, "line": "#FF9900", "lineWidth": 1.5, "adjustments": [0.15]},
{"type": "textbox", "x": 610, "y": 210, "width": 280, "height": 60, "fontSize": 12, "verticalAnchor": 1, "marginLeft": 0, "marginRight": 0, "marginTop": 0, "marginBottom": 0, "text": "補足説明テキスト"}
```
- 接続線の向き: width/heightの正負で上下左右を制御（width=50,height=0で右向き等）
- **実線接続**: dashStyleを外して強い関連を示す
- **elbow接続**: `"connectorType": "elbow"` で折れ線接続
