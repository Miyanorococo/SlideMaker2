---
name: customer-case-study
description: 顧客事例を引用付きで紹介するレイアウト
category: pattern
---

# 顧客事例レイアウト

## ユースケース
- 顧客の成功事例紹介
- ユースケース・ソリューション・結果の3カラム構成
- 顧客の声（引用）を強調表示

## デザインポイント
- 左上: 顧客名 + サブタイトル（プロジェクト名など）
- 右上: 顧客ロゴ/画像（虹色グラデーション枠）
- 中央: Use Case / Solution / Result の3カラム
- 下部: 引用ボックス（ダークグレー背景、ピンク引用符、青色ハイライト）

## 調整のコツ
- 引用文の強調部分は青色（#41B3FF）でハイライト
- 3カラムの区切り線は太線+細線の組み合わせで視覚的階層を表現
- 画像枠のグラデーションは虹色で華やかさを演出

## JSON

```json
{
  "theme": "dark",
  "slides": [
    {
      "layout": "title_only",
      "title": "",
      "elements": [
        {
          "type": "textbox",
          "x": 77,
          "y": 86,
          "width": 1248,
          "height": 102,
          "fontSize": 36,
          "text": "{{bold:顧客名}}"
        },
        {
          "type": "textbox",
          "x": 77,
          "y": 184,
          "width": 1248,
          "height": 58,
          "fontSize": 18,
          "text": "{{#FF5C85:プロジェクト名 / サブタイトル}}"
        },
        {
          "type": "textbox",
          "x": 1459,
          "y": 216,
          "width": 326,
          "height": 82,
          "align": "center",
          "fontSize": 14,
          "text": "{{#666666:企業ロゴ /}}\n{{#666666:写真}}"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 1421,
          "y": 65,
          "width": 403,
          "height": 400,
          "fill": "none",
          "lineWidth": 2,
          "adjustments": [
            0.05
          ],
          "lineGradient": {
            "angle": 135,
            "stops": [
              {
                "position": 0,
                "color": "#AD5CFF"
              },
              {
                "position": 0.25,
                "color": "#FF5C85"
              },
              {
                "position": 0.5,
                "color": "#00E500"
              },
              {
                "position": 0.75,
                "color": "#FF693C"
              },
              {
                "position": 1.0,
                "color": "#FBD332"
              }
            ]
          }
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 77,
          "y": 292,
          "width": 1190,
          "height": 65,
          "fill": "#FFFFFF",
          "opacity": 0.15,
          "line": "none",
          "adjustments": [
            0.35
          ]
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 302,
          "width": 288,
          "height": 53,
          "fontSize": 16,
          "text": "Use Case"
        },
        {
          "type": "textbox",
          "x": 461,
          "y": 302,
          "width": 288,
          "height": 53,
          "fontSize": 16,
          "text": "Solution"
        },
        {
          "type": "textbox",
          "x": 883,
          "y": 302,
          "width": 288,
          "height": 53,
          "fontSize": 16,
          "text": "Result"
        },
        {
          "type": "line",
          "x": 403,
          "y": 302,
          "width": 0,
          "height": 54,
          "color": "#FFFFFF",
          "lineWidth": 1.5
        },
        {
          "type": "line",
          "x": 403,
          "y": 367,
          "width": 0,
          "height": 151,
          "color": "#FFFFFF",
          "lineWidth": 0.25
        },
        {
          "type": "line",
          "x": 816,
          "y": 302,
          "width": 0,
          "height": 54,
          "color": "#FFFFFF",
          "lineWidth": 1.5
        },
        {
          "type": "line",
          "x": 816,
          "y": 367,
          "width": 0,
          "height": 151,
          "color": "#FFFFFF",
          "lineWidth": 0.25
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 378,
          "width": 288,
          "height": 131,
          "fontSize": 16,
          "text": "ユースケースの\n説明文をここに\n記載"
        },
        {
          "type": "textbox",
          "x": 461,
          "y": 378,
          "width": 326,
          "height": 92,
          "fontSize": 16,
          "text": "ソリューションの\n説明文"
        },
        {
          "type": "textbox",
          "x": 883,
          "y": 378,
          "width": 384,
          "height": 131,
          "fontSize": 16,
          "text": "結果・成果の\n説明文をここに\n記載"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 77,
          "y": 562,
          "width": 1306,
          "height": 259,
          "fill": "#1A1A1A",
          "line": "none",
          "adjustments": [
            0.03
          ]
        },
        {
          "type": "textbox",
          "x": 77,
          "y": 572,
          "width": 96,
          "fontSize": 48,
          "text": "{{#AB0071:\"}}"
        },
        {
          "type": "textbox",
          "x": 154,
          "y": 626,
          "width": 1229,
          "height": 116,
          "fontSize": 14,
          "paragraphs": [
            {
              "text": "{{italic:\"顧客の声をここに記載します。}}{{italic,#41B3FF:強調したい部分は青色}}{{italic:でハイライトします。引用文が長い場合は複数行になります。\"}}"
            },
            {
              "text": "{{italic:– 氏名, }}役職、部署名"
            }
          ]
        }
      ]
    }
  ]
}
```
