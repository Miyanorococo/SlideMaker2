---
name: split-hero-bullets
description: 左にヒーロータイトル、右に箇条書きの左右分割レイアウト
category: pattern
---

# 左右分割ヒーロー＋箇条書きレイアウト

## ユースケース
- 新サービス・新機能のアナウンス
- サービス紹介で機能を一覧表示
- 左にインパクト、右に詳細の構成

## デザインポイント
- 左40%: サービス名（グラデーション）+ サブタイトル + バッジ
- 中央: グラデーション縦線（angle=90）+ 白ドット装飾
- 右50%: 箇条書き（5項目程度）

## 調整のコツ
- 縦線のlineGradientはangle=90で上から下へ
- textGradientはangle=0で左から右へ
- Previewバッジは省略可能

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
          "x": 58,
          "y": 238,
          "width": 806,
          "height": 189,
          "fontSize": 36,
          "text": "{{bold:Amazon Bedrock\nAgentCore Evaluations}}",
          "textGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#FF9900"
              },
              {
                "position": 1,
                "color": "#FF5CAA"
              }
            ]
          }
        },
        {
          "type": "textbox",
          "x": 58,
          "y": 594,
          "width": 806,
          "height": 131,
          "fontSize": 24,
          "text": "{{bold:本番環境でエージェントの\n品質を継続的に検査・改善}}"
        },
        {
          "type": "line",
          "x": 872,
          "y": 108,
          "width": 0,
          "height": 832,
          "lineWidth": 2,
          "lineGradient": {
            "angle": 90,
            "stops": [
              {
                "position": 0,
                "color": "#41B3FF"
              },
              {
                "position": 0.21,
                "color": "#AD5CFF"
              },
              {
                "position": 0.4,
                "color": "#FF5C85"
              },
              {
                "position": 0.64,
                "color": "#00E500"
              },
              {
                "position": 0.85,
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
          "shape": "oval",
          "x": 862,
          "y": 168,
          "width": 21,
          "height": 22,
          "fill": "#FFFFFF",
          "line": "none"
        },
        {
          "type": "shape",
          "shape": "oval",
          "x": 862,
          "y": 328,
          "width": 21,
          "height": 22,
          "fill": "#FFFFFF",
          "line": "none"
        },
        {
          "type": "shape",
          "shape": "oval",
          "x": 862,
          "y": 486,
          "width": 21,
          "height": 22,
          "fill": "#FFFFFF",
          "line": "none"
        },
        {
          "type": "shape",
          "shape": "oval",
          "x": 862,
          "y": 643,
          "width": 21,
          "height": 22,
          "fill": "#FFFFFF",
          "line": "none"
        },
        {
          "type": "shape",
          "shape": "oval",
          "x": 862,
          "y": 809,
          "width": 21,
          "height": 22,
          "fill": "#FFFFFF",
          "line": "none"
        },
        {
          "type": "textbox",
          "x": 941,
          "y": 151,
          "width": 922,
          "height": 92,
          "fontSize": 16,
          "text": "{{bold:リアルタイムの品質モニタリングと自動リスク評価で、信頼性の高いエージェントを迅速にデプロイ}}"
        },
        {
          "type": "textbox",
          "x": 941,
          "y": 302,
          "width": 922,
          "height": 92,
          "fontSize": 16,
          "text": "{{bold:正確性、有用性、安全性などの品質基準でエージェントの振る舞いを分析}}"
        },
        {
          "type": "textbox",
          "x": 941,
          "y": 454,
          "width": 922,
          "height": 92,
          "fontSize": 16,
          "text": "{{bold:13種類のビルトイン評価機能により、数ヶ月の開発工数とインフラ管理を削減}}"
        },
        {
          "type": "textbox",
          "x": 941,
          "y": 605,
          "width": 922,
          "height": 92,
          "fontSize": 16,
          "text": "{{bold:カスタム評価を作成し、独自のプロンプトやモデルで品質評価をカスタマイズ可能}}"
        },
        {
          "type": "textbox",
          "x": 941,
          "y": 778,
          "width": 922,
          "height": 92,
          "fontSize": 16,
          "text": "{{bold:評価結果はAgentCore Observability経由でCloudWatchに連携し、統合監視が可能}}"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 54,
          "y": 788,
          "width": 211,
          "height": 54,
          "adjustments": [
            0.5
          ],
          "fill": "#AD5CFF",
          "line": "none"
        },
        {
          "type": "textbox",
          "x": 54,
          "y": 788,
          "width": 211,
          "fontSize": 20,
          "align": "center",
          "text": "{{#FFFFFF:Preview}}"
        }
      ]
    }
  ]
}
```

## バリエーション

### シンプル版（アイコン付き、バッジなし）
```json
{
  "theme": "dark",
  "slides": [
    {
      "layout": "content",
      "title": "",
      "elements": [
        {
          "type": "image",
          "src": "icons:Arch_Amazon-Bedrock_48",
          "x": 154,
          "y": 281,
          "width": 173
        },
        {
          "type": "textbox",
          "x": 134,
          "y": 486,
          "width": 730,
          "height": 116,
          "fontSize": 42,
          "text": "{{bold:Amazon Bedrock}}",
          "textGradient": {
            "angle": 0,
            "stops": [
              {
                "position": 0,
                "color": "#7C59ED"
              },
              {
                "position": 1,
                "color": "#9FFCEA"
              }
            ]
          }
        },
        {
          "type": "textbox",
          "x": 134,
          "y": 626,
          "width": 730,
          "height": 82,
          "fontSize": 14,
          "text": "基盤モデルと周辺ツール群で生成 AI アプリケーションを構築"
        },
        {
          "type": "line",
          "x": 952,
          "y": 248,
          "width": 0,
          "height": 637,
          "lineWidth": 1.5
        },
        {
          "type": "textbox",
          "x": 1037,
          "y": 238,
          "width": 826,
          "height": 58,
          "fontSize": 18,
          "text": "最先端の基盤モデルを単一 API で利用"
        },
        {
          "type": "textbox",
          "x": 1037,
          "y": 367,
          "width": 826,
          "height": 58,
          "fontSize": 18,
          "text": "モデルのカスタマイズ"
        },
        {
          "type": "textbox",
          "x": 1037,
          "y": 508,
          "width": 826,
          "height": 58,
          "fontSize": 18,
          "text": "Retrieval Augmented Generation (RAG)"
        },
        {
          "type": "textbox",
          "x": 1037,
          "y": 637,
          "width": 826,
          "height": 58,
          "fontSize": 18,
          "text": "マルチステップタスクのエージェント実行"
        },
        {
          "type": "textbox",
          "x": 1037,
          "y": 778,
          "width": 826,
          "height": 58,
          "fontSize": 18,
          "text": "セキュリティ・プライバシー・統制"
        }
      ]
    }
  ]
}
```
