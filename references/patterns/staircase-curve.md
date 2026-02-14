---
name: staircase-curve
description: グラデーション階段カーブ＋ドット＋ラベルによるフェーズ進行レイアウト
category: pattern
---

# 階段カーブレイアウト

## ユースケース
- フェーズ進行・ステップアップの視覚表現
- ロードマップや成長段階の提示
- プロセスの段階的な進展を曲線で表現

## デザインポイント
- freeform のベジェ曲線（`C`コマンド）で階段状のカーブを描画
- lineGradient で段階に応じた色の変化
- 各段の中央にドット（oval）、その下にラベル＋説明文
- 段の高さは均等配置が基本

## 調整のコツ
- **段数の変更**: path の `C` セグメントを増減し、ドット・ラベルも対応して追加・削除する。各段の y 値を `height / (段数)` で均等に割る
- **lineWidth**: SVG の stroke-width からの変換は `stroke-width × (表示幅 / viewBox幅) / 2` でpt値を算出
- **制御点の考え方**: 各ステップで CP1.y = 始点の y（水平に出る）、CP2.y = 終点の y（水平に入る）でS字遷移になる
- ドットの色は lineGradient の stops に合わせると統一感が出る

## JSON

### 4段階フェーズ進行

```json
{
  "layout": "title_only",
  "elements": [
    {
      "type": "freeform",
      "x": 0, "y": 200, "width": 1930, "height": 600,
      "fill": "none",
      "lineGradient": {
        "angle": 0,
        "stops": [
          {"position": 0, "color": "#295EFF"},
          {"position": 0.33, "color": "#962EFF"},
          {"position": 0.66, "color": "#DB3300"},
          {"position": 1, "color": "#FF693C"}
        ]
      },
      "lineWidth": 41,
      "path": [
        {"cmd": "M", "x": 0, "y": 600},
        {"cmd": "C", "pts": [[80, 600], [160, 600], [300, 600]]},
        {"cmd": "C", "pts": [[440, 600], [420, 420], [560, 420]]},
        {"cmd": "C", "pts": [[700, 420], [680, 420], [820, 420]]},
        {"cmd": "C", "pts": [[960, 420], [940, 240], [1080, 240]]},
        {"cmd": "C", "pts": [[1220, 240], [1200, 240], [1340, 240]]},
        {"cmd": "C", "pts": [[1480, 240], [1460, 60], [1600, 60]]},
        {"cmd": "C", "pts": [[1740, 60], [1840, 60], [1930, 60]]}
      ]
    },
    {
      "type": "shape", "x": 109, "y": 759, "width": 82, "height": 82,
      "shape": "oval", "fill": "#7598FF", "line": "none"
    },
    {
      "type": "shape", "x": 649, "y": 579, "width": 82, "height": 82,
      "shape": "oval", "fill": "#BF80FF", "line": "none"
    },
    {
      "type": "shape", "x": 1169, "y": 399, "width": 82, "height": 82,
      "shape": "oval", "fill": "#FF6A3D", "line": "none"
    },
    {
      "type": "shape", "x": 1724, "y": 219, "width": 82, "height": 82,
      "shape": "oval", "fill": "#FBD332", "line": "none"
    },
    {
      "type": "shape", "x": 20, "y": 860, "width": 260, "height": 53,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "{{#41B3FF:Phase One}}", "fontSize": 16, "textAlign": "left"
    },
    {
      "type": "shape", "x": 20, "y": 910, "width": 340, "height": 80,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "説明文テキスト", "fontSize": 12, "textAlign": "left"
    },
    {
      "type": "shape", "x": 560, "y": 680, "width": 260, "height": 53,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "{{#AD5CFF:Phase Two}}", "fontSize": 16, "textAlign": "left"
    },
    {
      "type": "shape", "x": 560, "y": 730, "width": 340, "height": 80,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "説明文テキスト", "fontSize": 12, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1080, "y": 500, "width": 260, "height": 53,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "{{#FF693C:Phase Three}}", "fontSize": 16, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1080, "y": 550, "width": 340, "height": 80,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "説明文テキスト", "fontSize": 12, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1620, "y": 320, "width": 260, "height": 53,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "{{#FBD332:Phase Four}}", "fontSize": 16, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1620, "y": 370, "width": 340, "height": 80,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "説明文テキスト", "fontSize": 12, "textAlign": "left"
    }
  ]
}
```

<!-- 段数を変更する場合:
  1. path の C セグメントを増減（水平区間 + 遷移カーブ で1段）
  2. 各段の y 値を height/(段数) で均等に割る（例: 3段なら 600,300,0）
  3. ドット(oval)とラベル(rectangle×2)のセットを段数分用意
  4. lineGradient の stops を段数に合わせて調整
  5. ドットの fill 色を gradient stops に合わせる
-->
