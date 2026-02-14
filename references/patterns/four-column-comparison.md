---
name: four-column-comparison
description: 4つの選択肢を横並びで比較表示
category: pattern
---

# 4カラム比較レイアウト

## ユースケース
- 複数の選択肢やアプローチの比較
- 段階的な難易度・複雑さの表現
- 機能やサービスの並列比較

## デザインポイント
- 各カラム幅22%、間隔2%で均等配置
- 枠線のみのカードでグラデーション軸と色を連動（左から右へ青→紫→ピンク→緑）
- アイコン→タイトル→説明の縦構成
- 下部に難易度軸などの補足情報

## 調整のコツ
- 5カラム以上は視認性が下がるため避ける
- カラム内テキストは13-18pt程度で収める
- 枠線は1pt程度で控えめに、彩度の高い色でもチカチカしない

## JSON

```json
{
  "theme": "dark",
  "slides": [
    {
      "id": "comparison-base",
      "layout": "title_only",
      "title": "生成 AI に独自の知識を取り込む方法",
      "elements": [
        {"type": "shape", "shape": "rounded_rectangle", "x": 58, "y": 173, "width": 422, "height": 648, "fill": "none", "line": "#0072E5", "lineWidth": 1, "adjustments": [0.06]},
        {"type": "image", "src": "icons:gear_dark", "x": 192, "y": 205, "width": 154, "labelPosition": "none"},
        {"type": "textbox", "x": 58, "y": 367, "width": 422, "height": 102, "align": "center", "fontSize": 18, "text": "{{bold,#0072E5:プロンプト}}\n{{bold,#0072E5:エンジニアリング}}"},
        {"type": "textbox", "x": 77, "y": 518, "width": 384, "height": 235, "align": "center", "fontSize": 13, "text": "生成 AI へのプロンプトに直\n接知識を取り込む\n\n外部の知識ベースの\n準備はいらない\n\n基盤モデルは変更しない"},
        {"type": "shape", "shape": "rounded_rectangle", "x": 518, "y": 173, "width": 422, "height": 648, "fill": "none", "line": "#C300E0", "lineWidth": 1, "adjustments": [0.06]},
        {"type": "image", "src": "icons:Arch_Amazon-OpenSearch-Service_48", "x": 653, "y": 205, "width": 154, "labelPosition": "none"},
        {"type": "textbox", "x": 518, "y": 367, "width": 422, "height": 102, "align": "center", "fontSize": 18, "text": "{{bold,#C300E0:RAG}}\n{{bold,#C300E0:(検索拡張生成)}}"},
        {"type": "textbox", "x": 538, "y": 518, "width": 384, "height": 204, "align": "center", "fontSize": 13, "text": "{{#C300E0:外部の知識ベース}}から\n取得したコンテンツを\n{{#C300E0:プロンプトに補完}}して\n知識を与える\n\n基盤モデルは変更しない"},
        {"type": "shape", "shape": "rounded_rectangle", "x": 979, "y": 173, "width": 422, "height": 648, "fill": "none", "line": "#E000A0", "lineWidth": 1, "adjustments": [0.06]},
        {"type": "image", "src": "icons:model_dark", "x": 1114, "y": 205, "width": 154, "labelPosition": "none"},
        {"type": "textbox", "x": 979, "y": 367, "width": 422, "height": 102, "align": "center", "fontSize": 18, "text": "{{bold,#E000A0:ファイン}}\n{{bold,#E000A0:チューニング}}"},
        {"type": "textbox", "x": 998, "y": 518, "width": 384, "height": 267, "align": "center", "fontSize": 13, "text": "特定のタスクに対して特化\nした能力を得る\n\n少量のラベル付き\nサンプルで学習\n\n{{#E000A0:基盤モデルのコピーに対し}}\n{{#E000A0:て変更を加える}}"},
        {"type": "shape", "shape": "rounded_rectangle", "x": 1440, "y": 173, "width": 422, "height": 648, "fill": "none", "line": "#00E500", "lineWidth": 1, "adjustments": [0.06]},
        {"type": "image", "src": "icons:Arch_Amazon-Bedrock_48", "x": 1574, "y": 205, "width": 154, "labelPosition": "none"},
        {"type": "textbox", "x": 1440, "y": 367, "width": 422, "height": 102, "align": "center", "fontSize": 18, "text": "{{bold,#00E500:独自モデル}}\n{{bold,#00E500:の開発}}"},
        {"type": "textbox", "x": 1459, "y": 518, "width": 384, "height": 172, "align": "center", "fontSize": 13, "text": "大量のトレーニング\nデータによる一般知識や専門\n知識の獲得\n\nゼロから新しいモデルを開発"},
        {"type": "textbox", "x": 38, "y": 864, "width": 269, "height": 53, "align": "center", "fontSize": 16, "text": "{{bold,#0072E5:EASIER}}"},
        {"type": "line", "x": 307, "y": 886, "width": 1306, "height": 0, "lineWidth": 1.5, "dashStyle": "dash", "lineGradient": {"angle": 0, "stops": [{"position": 0, "color": "#0072E5"}, {"position": 0.5, "color": "#C300E0"}, {"position": 1, "color": "#00E500"}]}, "headEnd": "arrow", "tailEnd": "arrow"},
        {"type": "shape", "shape": "rectangle", "x": 768, "y": 853, "width": 384, "height": 54, "fill": "#000000", "line": "none"},
        {"type": "textbox", "x": 768, "y": 864, "width": 384, "height": 44, "align": "center", "fontSize": 12, "text": "A D O P T I O N"},
        {"type": "textbox", "x": 1613, "y": 864, "width": 269, "height": 53, "align": "center", "fontSize": 16, "text": "{{bold,#00E500:COMPLEX}}"}
      ]
    },
    {
      "override": "comparison-base",
      "layout": "title_only",
      "title": "生成 AI に独自の知識を取り込む方法",
      "elements": [
        {"type": "shape", "shape": "rectangle", "x": 0, "y": 130, "width": 1920, "height": 750, "fill": "#000000", "opacity": 0.8, "line": "none"},
        {"type": "shape", "shape": "rounded_rectangle", "x": 518, "y": 173, "width": 422, "height": 648, "fill": "none", "line": "#C300E0", "lineWidth": 3, "adjustments": [0.06]},
        {"type": "image", "src": "icons:Arch_Amazon-OpenSearch-Service_48", "x": 653, "y": 205, "width": 154, "labelPosition": "none"},
        {"type": "textbox", "x": 518, "y": 367, "width": 422, "height": 102, "align": "center", "fontSize": 18, "text": "{{bold,#C300E0:RAG}}\n{{bold,#C300E0:(検索拡張生成)}}"},
        {"type": "textbox", "x": 538, "y": 518, "width": 384, "height": 204, "align": "center", "fontSize": 13, "text": "{{#C300E0:外部の知識ベース}}から\n取得したコンテンツを\n{{#C300E0:プロンプトに補完}}して\n知識を与える\n\n基盤モデルは変更しない"}
      ]
    }
  ]
}
```

**override活用ポイント**:
- 1枚目（id: comparison-base）: 4つの選択肢を全体表示
- 2枚目以降: overrideでベースを継承し、オーバーレイ + 1つの選択肢をフォーカス
- 各選択肢を順番に説明する際に、同じベースから派生させることで一貫性を保つ

## バリエーション

### 詳細比較マトリクス（行×属性）
3行×4列の比較表。左にアイコン列、縦グラデーション線で分離、○△で評価、注釈・脚注付き。

```json
{
  "layout": "title_only",
  "title": "タイトル",
  "elements": [
    {
      "type": "textbox",
      "x": 48, "y": 136, "width": 1790, "height": 44,
      "line": "none",
      "text": "{{bold,#0EEDAF:サブタイトル}}"
    },
    {
      "type": "line",
      "x": 327, "y": 245, "width": 0, "height": 680,
      "preset": "line", "headEnd": "none", "tailEnd": "none", "lineWidth": 1.0,
      "lineGradient": {
        "stops": [
          { "position": 0.0, "color": "#F2FF85" },
          { "position": 0.628, "color": "#FF316E" },
          { "position": 1.0, "color": "#2C0152" }
        ],
        "angle": 270.0
      }
    },

    {"_comment": "--- 列ヘッダー (y=245) ---"},
    {
      "type": "textbox",
      "x": 345, "y": 245, "width": 250, "height": 65,
      "line": "none", "fontSize": 13, "align": "center",
      "text": "{{#FFFFFF:列ヘッダー A}}"
    },
    {
      "type": "textbox",
      "x": 620, "y": 245, "width": 220, "height": 65,
      "line": "none", "fontSize": 14, "align": "center",
      "text": "{{#FFFFFF:列ヘッダー B}}"
    },
    {
      "type": "textbox",
      "x": 870, "y": 245, "width": 330, "height": 65,
      "line": "none", "fontSize": 13, "align": "center",
      "text": "{{#FFFFFF:列ヘッダー C}}"
    },
    {
      "type": "textbox",
      "x": 1230, "y": 245, "width": 690, "height": 65,
      "line": "none", "fontSize": 16, "align": "center",
      "text": "{{#FFFFFF:列ヘッダー D}}"
    },

    {"_comment": "--- 行1 (y=340) ---"},
    {
      "type": "image",
      "x": 140, "y": 350, "width": 70, "height": 65,
      "src": "icons:Arch_Amazon-Aurora_48"
    },
    {
      "type": "textbox",
      "x": 80, "y": 425, "width": 190, "height": 40,
      "line": "none", "fontSize": 12, "align": "center",
      "text": "{{#FFFFFF:行ラベル 1}}"
    },
    {
      "type": "textbox",
      "x": 345, "y": 340, "width": 250, "height": 150,
      "line": "none", "fontSize": 18, "align": "center",
      "text": "{{#FFFFFF:セル A1}}"
    },
    {
      "type": "textbox",
      "x": 620, "y": 340, "width": 220, "height": 150,
      "line": "none", "fontSize": 14, "align": "center",
      "paragraphs": [
        { "text": "{{#FFFFFF:ニアリアル}}" },
        { "text": "{{#FFFFFF:タイム}}" }
      ]
    },
    {
      "type": "textbox",
      "x": 870, "y": 340, "width": 80, "height": 150,
      "line": "none", "fontSize": 32, "align": "center",
      "text": "{{#FFFFFF:△}}"
    },
    {
      "type": "textbox",
      "x": 955, "y": 340, "width": 245, "height": 150,
      "line": "none", "fontSize": 11, "align": "center",
      "text": "{{#FFFFFF:(補足説明)}}"
    },
    {
      "type": "textbox",
      "x": 1230, "y": 340, "width": 690, "height": 150,
      "line": "none", "fontSize": 12,
      "paragraphs": [
        { "text": "{{#FFFFFF:注意点 1-1}}", "bullet": true },
        { "text": "{{#FFFFFF:注意点 1-2}}", "bullet": true },
        { "text": "{{#FFFFFF:注意点 1-3}}", "bullet": true },
        { "text": "{{#FFFFFF:注意点 1-4}}", "bullet": true }
      ]
    },

    {"_comment": "--- 行2 (y=530) ---"},
    {
      "type": "image",
      "x": 140, "y": 540, "width": 70, "height": 65,
      "src": "icons:Arch_Amazon-DynamoDB_48"
    },
    {
      "type": "textbox",
      "x": 80, "y": 615, "width": 190, "height": 40,
      "line": "none", "fontSize": 12, "align": "center",
      "text": "{{#FFFFFF:行ラベル 2}}"
    },
    {
      "type": "textbox",
      "x": 345, "y": 530, "width": 250, "height": 150,
      "line": "none", "fontSize": 16, "align": "center",
      "paragraphs": [
        { "text": "{{#FFFFFF:セル A2-1}}" },
        { "text": "{{#FFFFFF:セル A2-2}}" }
      ]
    },
    {
      "type": "textbox",
      "x": 620, "y": 530, "width": 220, "height": 150,
      "line": "none", "fontSize": 16, "align": "center",
      "text": "{{#FFFFFF:15分〜}}"
    },
    {
      "type": "textbox",
      "x": 870, "y": 530, "width": 80, "height": 150,
      "line": "none", "fontSize": 48, "align": "center",
      "text": "{{#FFFFFF:○}}"
    },
    {
      "type": "textbox",
      "x": 1230, "y": 530, "width": 690, "height": 150,
      "line": "none", "fontSize": 12,
      "text": "{{#FFFFFF:注意点 2}}"
    },

    {"_comment": "--- 行3 (y=720) ---"},
    {
      "type": "image",
      "x": 140, "y": 730, "width": 70, "height": 65,
      "src": "icons:applications_dark"
    },
    {
      "type": "textbox",
      "x": 80, "y": 805, "width": 190, "height": 40,
      "line": "none", "fontSize": 12, "align": "center",
      "text": "{{#FFFFFF:行ラベル 3}}"
    },
    {
      "type": "textbox",
      "x": 345, "y": 720, "width": 250, "height": 150,
      "line": "none", "fontSize": 20, "align": "center",
      "text": "{{#FFFFFF:セル A3}}"
    },
    {
      "type": "textbox",
      "x": 620, "y": 720, "width": 220, "height": 150,
      "line": "none", "fontSize": 16, "align": "center",
      "text": "{{#FFFFFF:1時間〜}}"
    },
    {
      "type": "textbox",
      "x": 870, "y": 720, "width": 80, "height": 150,
      "line": "none", "fontSize": 48, "align": "center",
      "text": "{{#FFFFFF:○}}"
    },
    {
      "type": "textbox",
      "x": 1230, "y": 720, "width": 690, "height": 150,
      "line": "none", "fontSize": 12,
      "text": "{{#FFFFFF:注意点 3}}"
    },

    {"_comment": "--- 注釈・脚注 ---"},
    {
      "type": "textbox",
      "x": 830, "y": 237, "width": 22, "height": 32,
      "line": "none", "fontSize": 7, "align": "center",
      "text": "{{#FFFFFF:※1}}"
    },
    {
      "type": "textbox",
      "x": 650, "y": 994, "width": 435, "height": 34,
      "line": "none", "fontSize": 8, "align": "center",
      "text": "{{#FFFFFF:※1) 脚注テキスト}}"
    }
  ]
}
```
