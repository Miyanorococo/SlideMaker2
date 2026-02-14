---
name: three-column-cards
description: 3カラムのカードレイアウト、グラデーション枠線とアイコン
category: pattern
---

# 3カラムカードレイアウト

## ユースケース
- 機能や特徴を3つ並列で紹介
- サービスの主要コンポーネント説明
- 比較や選択肢の提示

## デザインポイント
- 各カード幅28%、間隔3%で均等配置
- グラデーション枠線で視覚的な区別
- アイコン + フェード線 + タイトルの縦構成
- フェード線は両端が透明になるグラデーション

## 調整のコツ
- カード内のアイコンはgeneralアイコンが汎用的
- フェード線のopacityで両端のフェード具合を調整
- 4カラム以上は視認性が下がるため避ける

## JSON

```json
{
  "theme": "dark",
  "slides": [
    {
      "layout": "title_only",
      "title": "高度なエージェントを\n安全かつ大規模に実行するための機能を持つ",
      "elements": [
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 96,
          "y": 346,
          "width": 538,
          "height": 540,
          "adjustments": [
            0.05
          ],
          "lineGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#00E500"
              },
              {
                "position": 1,
                "color": "#41B3FF"
              }
            ]
          },
          "lineWidth": 1.5
        },
        {
          "type": "image",
          "src": "icons:security_analysis_dark",
          "x": 269,
          "y": 410,
          "width": 192,
          "labelPosition": "none"
        },
        {
          "type": "line",
          "x": 192,
          "y": 616,
          "width": 346,
          "height": 0,
          "lineWidth": 1.5,
          "lineGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#FFFFFF",
                "opacity": 0
              },
              {
                "position": 0.3,
                "color": "#FFFFFF",
                "opacity": 1
              },
              {
                "position": 0.7,
                "color": "#FFFFFF",
                "opacity": 1
              },
              {
                "position": 1,
                "color": "#FFFFFF",
                "opacity": 0
              }
            ]
          }
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 702,
          "width": 538,
          "height": 102,
          "align": "center",
          "fontSize": 18,
          "text": "安全かつ\n大規模に展開"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 691,
          "y": 346,
          "width": 538,
          "height": 540,
          "adjustments": [
            0.05
          ],
          "lineGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#41B3FF"
              },
              {
                "position": 1,
                "color": "#AD5CFF"
              }
            ]
          },
          "lineWidth": 1.5
        },
        {
          "type": "image",
          "src": "icons:build_tools_dark",
          "x": 864,
          "y": 410,
          "width": 192,
          "labelPosition": "none"
        },
        {
          "type": "line",
          "x": 787,
          "y": 616,
          "width": 346,
          "height": 0,
          "lineWidth": 1.5,
          "lineGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#FFFFFF",
                "opacity": 0
              },
              {
                "position": 0.3,
                "color": "#FFFFFF",
                "opacity": 1
              },
              {
                "position": 0.7,
                "color": "#FFFFFF",
                "opacity": 1
              },
              {
                "position": 1,
                "color": "#FFFFFF",
                "opacity": 0
              }
            ]
          }
        },
        {
          "type": "textbox",
          "x": 691,
          "y": 702,
          "width": 538,
          "height": 102,
          "align": "center",
          "fontSize": 18,
          "text": "ツールとメモリ\nによる強化"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 1286,
          "y": 346,
          "width": 538,
          "height": 540,
          "adjustments": [
            0.05
          ],
          "lineGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#FBD332"
              },
              {
                "position": 1,
                "color": "#00E500"
              }
            ]
          },
          "lineWidth": 1.5
        },
        {
          "type": "image",
          "src": "icons:infrastructure_monitoring_dark",
          "x": 1459,
          "y": 410,
          "width": 192,
          "labelPosition": "none"
        },
        {
          "type": "line",
          "x": 1382,
          "y": 616,
          "width": 346,
          "height": 0,
          "lineWidth": 1.5,
          "lineGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#FFFFFF",
                "opacity": 0
              },
              {
                "position": 0.3,
                "color": "#FFFFFF",
                "opacity": 1
              },
              {
                "position": 0.7,
                "color": "#FFFFFF",
                "opacity": 1
              },
              {
                "position": 1,
                "color": "#FFFFFF",
                "opacity": 0
              }
            ]
          }
        },
        {
          "type": "textbox",
          "x": 1286,
          "y": 702,
          "width": 538,
          "height": 58,
          "align": "center",
          "fontSize": 18,
          "text": "監視"
        }
      ]
    }
  ]
}
```

## フェード線の仕組み

```json
{
  "type": "line",
  "lineGradient": {
    "angle": 0,
    "stops": [
      {
        "position": 0,
        "color": "#FFFFFF",
        "opacity": 0
      },
      {
        "position": 0.3,
        "color": "#FFFFFF",
        "opacity": 1
      },
      {
        "position": 0.7,
        "color": "#FFFFFF",
        "opacity": 1
      },
      {
        "position": 1,
        "color": "#FFFFFF",
        "opacity": 0
      }
    ]
  }
}
```
- `opacity: 0` で透明、`opacity: 1` で不透明
- position 0〜0.3 と 0.7〜1 でフェードイン/アウト

## バリエーション

### 横行比較（アイコン+箇条書き）
3つの選択肢を横行で比較。左にアイコン+ラベル、右にparagraphs箇条書き、線で区切り。

```json
{
  "layout": "content",
  "title": "タイトル",
  "elements": [
    {
      "type": "textbox",
      "x": 64, "y": 141, "width": 1731, "height": 48,
      "fill": "none", "line": "none",
      "text": "{{bold,#0EEDAF:サブタイトル}}",
      "fontSize": 14
    },
    {
      "type": "image",
      "x": 133, "y": 302, "width": 90, "height": 93,
      "src": "icons:Arch_Amazon-Simple-Storage-Service_48"
    },
    {
      "type": "textbox",
      "x": 8, "y": 419, "width": 347, "height": 44,
      "line": "none", "fontSize": 12, "align": "center",
      "text": "{{#FFFFFF:ラベル 1}}"
    },
    {
      "type": "textbox",
      "x": 326, "y": 302, "width": 1515, "height": 189,
      "line": "none",
      "paragraphs": [
        { "text": "{{#FFFFFF:説明文 1-1}}", "bullet": true },
        { "text": "{{#FFFFFF:説明文 1-2}}", "bullet": true },
        { "text": "{{#FFFFFF:説明文 1-3}}", "bullet": true },
        { "text": "{{#FFFFFF:説明文 1-4}}", "bullet": true }
      ]
    },
    {
      "type": "line",
      "x": 57, "y": 504, "width": 1784, "height": 0,
      "flipH": true, "preset": "line", "color": "#FFFFFF", "lineWidth": 2.2
    },
    {
      "type": "image",
      "x": 136, "y": 556, "width": 94, "height": 104,
      "src": "icons:Res_Amazon-Simple-Storage-Service_S3-Tables_48"
    },
    {
      "type": "textbox",
      "x": 64, "y": 667, "width": 235, "height": 44,
      "line": "none", "fontSize": 12, "align": "center",
      "text": "{{#FFFFFF:ラベル 2}}"
    },
    {
      "type": "textbox",
      "x": 326, "y": 556, "width": 1515, "height": 197,
      "line": "none",
      "paragraphs": [
        { "text": "{{#FFFFFF:説明文 2-1}}", "bullet": true },
        { "text": "{{#FFFFFF:説明文 2-2}}", "bullet": true },
        { "text": "{{#FFFFFF:説明文 2-3}}", "bullet": true }
      ]
    },
    {
      "type": "line",
      "x": 61, "y": 766, "width": 1780, "height": 0,
      "flipH": true, "preset": "line", "color": "#FFFFFF", "lineWidth": 2.2
    },
    {
      "type": "image",
      "x": 138, "y": 806, "width": 96, "height": 99,
      "src": "icons:Arch_Amazon-Redshift_48"
    },
    {
      "type": "textbox",
      "x": 82, "y": 919, "width": 217, "height": 73,
      "line": "none", "fontSize": 12, "align": "center",
      "text": "{{#FFFFFF:ラベル 3}}"
    },
    {
      "type": "textbox",
      "x": 326, "y": 795, "width": 1515, "height": 193,
      "line": "none",
      "paragraphs": [
        { "text": "{{#FFFFFF:説明文 3-1}}", "bullet": true },
        { "text": "{{#FFFFFF:説明文 3-2}}", "bullet": true }
      ]
    }
  ]
}
```

---

## バリアント: カテゴリ別ツール一覧（アイコン＋説明）

横線で区切った3セクション構成。左にアイコン群を配置したボックス、右にツール名＋説明テキスト。

**構成**:
- 3セクション（横線で区切り）
- 左: 背景付き矩形内にアイコン＋ラベル
- 右: ツール名（bold, fs=18）＋ 紫アクセントバー付き説明テキスト（fs=16）
- セクション見出し（bold, fs=20）

**ポイント**:
- 左ボックスは統一サイズ（w=426, h=116）、fill=#324358
- アクセントバー（w=14, fill=#7C59ED）で説明文を強調
- アイコンは `icons:` で指定（サードパーティ含む: nodejs, python, java等）
- セクション2のように1ボックスに複数アイコンを並べることも可能

```json
{
  "layout": "title_only",
  "title": "AWS CDK の開発に必要なもの",
  "elements": [
    {
      "type": "shape",
      "x": 126,
      "y": 623,
      "width": 426,
      "height": 116,
      "shape": "rectangle",
      "line": "none"
    },
    {
      "type": "shape",
      "x": 126,
      "y": 822,
      "width": 426,
      "height": 116,
      "shape": "rectangle",
      "fill": "#324358",
      "line": "none"
    },
    {
      "type": "shape",
      "x": 126,
      "y": 496,
      "width": 426,
      "height": 116,
      "shape": "rectangle",
      "fill": "#324358",
      "line": "none"
    },
    {
      "type": "shape",
      "x": 126,
      "y": 273,
      "width": 426,
      "height": 116,
      "shape": "rectangle",
      "fill": "#324358",
      "line": "none"
    },
    {
      "type": "textbox",
      "x": 274,
      "y": 344,
      "width": 130,
      "height": 40,
      "line": "none",
      "text": "{{#FFFFFF:ツール}}{{#FFFFFF: 1}}",
      "fontSize": 12,
      "align": "center"
    },
    {
      "type": "image",
      "x": 307,
      "y": 276,
      "width": 65,
      "height": 65,
      "src": "icons:git_repository_dark"
    },
    {
      "type": "image",
      "x": 469,
      "y": 511,
      "width": 60,
      "height": 60,
      "src": "icons:nodejs"
    },
    {
      "type": "textbox",
      "x": 438,
      "y": 576,
      "width": 110,
      "height": 40,
      "line": "none",
      "text": "{{#FFFFFF:ツール}}{{#FFFFFF: 2-3}}",
      "fontSize": 12,
      "align": "center"
    },
    {
      "type": "image",
      "x": 148,
      "y": 511,
      "width": 60,
      "height": 60,
      "src": "icons:Arch_AWS-Command-Line-Interface_48"
    },
    {
      "type": "textbox",
      "x": 119,
      "y": 576,
      "width": 121,
      "height": 40,
      "line": "none",
      "text": "{{#FFFFFF:ツール}}{{#FFFFFF: 2-1}}",
      "fontSize": 12,
      "align": "center"
    },
    {
      "type": "image",
      "x": 311,
      "y": 836,
      "width": 60,
      "height": 60,
      "src": "icons:code_dark"
    },
    {
      "type": "textbox",
      "x": 280,
      "y": 898,
      "width": 120,
      "height": 40,
      "line": "none",
      "text": "{{#FFFFFF:ツール}}{{#FFFFFF: 3}}",
      "fontSize": 12,
      "align": "center"
    },
    {
      "type": "image",
      "x": 311,
      "y": 511,
      "width": 60,
      "height": 60,
      "src": "icons:Arch_AWS-Cloud-Development-Kit_48"
    },
    {
      "type": "textbox",
      "x": 235,
      "y": 576,
      "width": 217,
      "height": 40,
      "line": "none",
      "text": "{{#FFFFFF:ツール}}{{#FFFFFF: 2-2}}",
      "fontSize": 12,
      "align": "center"
    },
    {
      "type": "textbox",
      "x": 104,
      "y": 200,
      "width": 493,
      "height": 63,
      "line": "none",
      "text": "{{bold,#FFFFFF:カテゴリ}}{{bold,#FFFFFF: 1}}",
      "fontSize": 20
    },
    {
      "type": "textbox",
      "x": 104,
      "y": 422,
      "width": 493,
      "height": 63,
      "line": "none",
      "text": "{{bold,#FFFFFF:カテゴリ}}{{bold,#FFFFFF: 2}}",
      "fontSize": 20
    },
    {
      "type": "textbox",
      "x": 104,
      "y": 750,
      "width": 493,
      "height": 63,
      "line": "none",
      "text": "{{bold,#FFFFFF:カテゴリ}}{{bold,#FFFFFF: 3}}",
      "fontSize": 20
    },
    {
      "type": "line",
      "x": 104,
      "y": 409,
      "width": 1665,
      "height": 0,
      "preset": "line",
      "color": "#FFFFFF",
      "lineWidth": 0.8
    },
    {
      "type": "line",
      "x": 104,
      "y": 741,
      "width": 1665,
      "height": 0,
      "preset": "line",
      "color": "#FFFFFF",
      "lineWidth": 0.8
    },
    {
      "type": "textbox",
      "x": 411,
      "y": 876,
      "width": 93,
      "height": 48,
      "line": "none",
      "text": "{{#FFFFFF:など}}",
      "fontSize": 14
    },
    {
      "type": "textbox",
      "x": 601,
      "y": 275,
      "width": 1200,
      "height": 50,
      "line": "none",
      "text": "{{bold,#FFFFFF:ツール名}}{{bold,#FFFFFF: 1}}{{#FFFFFF: }}{{#FFFFFF:説明リンク}}"
    },
    {
      "type": "textbox",
      "x": 601,
      "y": 496,
      "width": 1200,
      "height": 110,
      "line": "none",
      "paragraphs": [
        {
          "text": "{{bold,#FFFFFF:ツール名}}{{bold,#FFFFFF: 2-1}}{{#FFFFFF: }}{{#FFFFFF:説明リンク}}"
        },
        {
          "text": "{{bold,#FFFFFF:ツール名}}{{bold,#FFFFFF: 2-2}}{{#FFFFFF: }}{{#FFFFFF:説明リンク}}"
        }
      ]
    },
    {
      "type": "textbox",
      "x": 601,
      "y": 825,
      "width": 1200,
      "height": 50,
      "line": "none",
      "text": "{{bold,#FFFFFF:ツール名}}{{bold,#FFFFFF: 3}}{{#FFFFFF: }}{{#FFFFFF:説明リンク}}"
    },
    {
      "type": "image",
      "x": 411,
      "y": 656,
      "width": 60,
      "height": 60,
      "src": "icons:go"
    },
    {
      "type": "image",
      "x": 332,
      "y": 656,
      "width": 60,
      "height": 60,
      "src": "icons:csharp"
    },
    {
      "type": "image",
      "x": 253,
      "y": 656,
      "width": 60,
      "height": 60,
      "src": "icons:java"
    },
    {
      "type": "image",
      "x": 175,
      "y": 656,
      "width": 60,
      "height": 60,
      "src": "icons:python"
    },
    {
      "type": "textbox",
      "x": 687,
      "y": 351,
      "width": 1120,
      "height": 55,
      "line": "none",
      "text": "{{#FFFFFF:説明文}}{{#FFFFFF: 4-1}}",
      "fontSize": 16
    },
    {
      "type": "textbox",
      "x": 687,
      "y": 626,
      "width": 1120,
      "height": 90,
      "line": "none",
      "text": "{{#FFFFFF:説明文}}{{#FFFFFF: 4-2}}",
      "fontSize": 16
    },
    {
      "type": "shape",
      "x": 656,
      "y": 351,
      "width": 14,
      "height": 55,
      "shape": "rectangle",
      "fill": "#7C59ED",
      "line": "none"
    },
    {
      "type": "shape",
      "x": 656,
      "y": 626,
      "width": 14,
      "height": 90,
      "shape": "rectangle",
      "fill": "#7C59ED",
      "line": "none"
    },
    {
      "type": "textbox",
      "x": 687,
      "y": 891,
      "width": 1120,
      "height": 55,
      "line": "none",
      "text": "{{#FFFFFF:説明文}}{{#FFFFFF: 4-3}}",
      "fontSize": 16
    },
    {
      "type": "shape",
      "x": 656,
      "y": 891,
      "width": 14,
      "height": 55,
      "shape": "rectangle",
      "fill": "#7C59ED",
      "line": "none"
    }
  ]
}
```

---

## バリアント: グラデーション帯＋3カラム箇条書き

上部にグラデーション帯（角丸・adjustments=0.5で完全丸端）、その下に3カラムでラベル＋タイトル＋箇条書き。フェーズ進行やカテゴリ別説明に適する。

**構成**:
- グラデーション帯: 紺→紫→赤の3色グラデーション
- 各カラム: ラベル（fs=11）＋ タイトル（fs=24）＋ 箇条書き（fs=14, items）
- 3カラム均等配置（x=181, 750, 1316 / width=431）
- 説明文は `verticalAnchor: 1`（上寄せ）

```json
{
  "layout": "title_only",
  "elements": [
    {
      "type": "shape",
      "x": 82, "y": 253, "width": 1727, "height": 214,
      "shape": "rounded_rectangle",
      "adjustments": [0.5],
      "gradient": {
        "stops": [
          {"position": 0.0, "color": "#002060"},
          {"position": 0.46, "color": "#8105FF"},
          {"position": 0.99, "color": "#FF0544"}
        ],
        "angle": 0.0
      },
      "line": "none"
    },
    {
      "type": "shape", "x": 181, "y": 310, "width": 431, "height": 41,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "ラベル1", "fontSize": 11, "textAlign": "left"
    },
    {
      "type": "shape", "x": 181, "y": 340, "width": 431, "height": 73,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "カテゴリ A", "fontSize": 24, "textAlign": "left"
    },
    {
      "type": "shape", "x": 181, "y": 497, "width": 431, "height": 378,
      "shape": "rectangle", "fill": "none", "line": "none",
      "verticalAnchor": 1,
      "items": ["説明文1-1", "説明文1-2", "説明文1-3"],
      "fontSize": 14, "textAlign": "left"
    },
    {
      "type": "shape", "x": 750, "y": 310, "width": 431, "height": 41,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "ラベル2", "fontSize": 11, "textAlign": "left"
    },
    {
      "type": "shape", "x": 750, "y": 340, "width": 431, "height": 73,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "カテゴリ B", "fontSize": 24, "textAlign": "left"
    },
    {
      "type": "shape", "x": 750, "y": 497, "width": 431, "height": 378,
      "shape": "rectangle", "fill": "none", "line": "none",
      "verticalAnchor": 1,
      "items": ["説明文2-1", "説明文2-2"],
      "fontSize": 14, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1316, "y": 310, "width": 431, "height": 41,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "ラベル3", "fontSize": 11, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1316, "y": 340, "width": 431, "height": 73,
      "shape": "rectangle", "fill": "none", "line": "none",
      "text": "カテゴリ C", "fontSize": 24, "textAlign": "left"
    },
    {
      "type": "shape", "x": 1316, "y": 497, "width": 431, "height": 378,
      "shape": "rectangle", "fill": "none", "line": "none",
      "verticalAnchor": 1,
      "items": ["説明文3-1", "説明文3-2", "説明文3-3"],
      "fontSize": 14, "textAlign": "left"
    }
  ]
}
```
