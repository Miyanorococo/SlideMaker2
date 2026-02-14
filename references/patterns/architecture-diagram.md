---
name: architecture-diagram
description: AWSアーキテクチャ図の設計ガイドライン
category: pattern
---

# アーキテクチャ図 設計ガイド

## 基本原則

1. **グリッド思考**: 要素を仮想グリッドに沿って配置
2. **対称性**: 分岐する矢印は中心から対称に
3. **余白の一貫性**: 同じ種類の余白は同じ値を使う
4. **階層の明示**: グループ化で論理構造を視覚化

---

## スケール設計

アーキテクチャの複雑さに応じてスケールを選択:

| 複雑さ | アイコンサイズ | アイコン間隔 | 矢印分岐幅 | 用途 |
|--------|---------------|-------------|-----------|------|
| シンプル（3-5個） | 120px | 200px | ±15px | 概要図、単一フロー |
| 標準（6-10個） | 100px | 160px | ±12px | 一般的な構成図 |
| 複雑（11-15個） | 80px | 120px | ±10px | 詳細アーキテクチャ |
| 高密度（16個以上） | 60px | 100px | ±8px | 全体俯瞰図 |

**計算式**:
- アイコン間隔 ≈ アイコンサイズ × 1.6〜2.0
- 矢印分岐幅 ≈ アイコンサイズ × 0.1〜0.15
- ラベルフォント ≈ アイコンサイズ × 0.1（最小10px、最大14px）

---

## レイアウト構造

### 描画エリア
```
スライド: 1920 x 1080px
推奨エリア: x=60〜1860, y=200〜900（title_onlyレイアウト）
```

### AWS Cloud境界
```json
{
  "type": "shape",
  "shape": "rectangle",
  "x": [左マージン],
  "y": [上マージン],
  "width": [右端 - 左マージン],
  "height": [下端 - 上マージン],
  "fill": "none",
  "line": "#FFFFFF",
  "lineWidth": 2
}
```

### AWS Cloudロゴ配置
```
ロゴ位置 = 境界位置 + 枠線幅
例: 境界(420, 200) + 枠線2px → ロゴ(422, 202)
```

---

## アイコン配置

### 水平フロー（左→右）
```
アイコン中心Y = 描画エリア中央
アイコンX = 開始位置 + (インデックス × 間隔)
```

例（120pxアイコン、200px間隔）:
```
CloudFront: x=500  (中心=560)
API Gateway: x=700 (中心=760)
Lambda: x=900      (中心=960)
```

### 垂直配置
同じX座標で、Y座標を間隔分ずらす:
```
上段: y=340
下段: y=480（間隔140px）
```

### グループ化
関連サービスを角丸矩形でグループ化:
```json
{
  "type": "shape",
  "shape": "rounded_rectangle",
  "fill": "#1A242F",
  "line": "#5A6B7D",
  "adjustments": [0.1]
}
```

グループ内アイコン配置:
- グループ上部にラベル（fontSize: 12）
- アイコンはラベルの下に等間隔配置
- グループ内間隔 ≈ アイコンサイズ × 1.4

---

## 矢印設計

### 基本ルール
- **水平・垂直のみ**: 斜め矢印は使わない
- **始点**: アイコン右端（または下端）
- **終点**: 次のアイコン左端（または上端）の手前

### 単一矢印
```
始点X = アイコンX + アイコンサイズ
終点X = 次のアイコンX
矢印Y = アイコン中心Y
```

例:
```json
{
  "type": "line",
  "x": 620,
  "y": 540,
  "width": 80,
  "height": 0,
  "tailEnd": "arrow"
}
```

### 分岐矢印（1つのアイコンから複数方向）

**対称配置が重要**:
```
上向き矢印Y = アイコン中心Y - 分岐幅
下向き矢印Y = アイコン中心Y + 分岐幅
```

**⚠️ ラベルとの重なり回避**:
`labelPosition: "bottom"` を使用している場合、アイコンの下にラベルが配置される。
分岐矢印の始点Yは、ラベルと重ならないように設定する必要がある。

```
アイコン下端 = アイコンY + アイコンサイズ
ラベル領域 = アイコン下端 〜 アイコン下端 + 約30px
矢印始点Y = ラベル領域を避けて設定
```

**推奨パターン**:
1. **ラベルなし（labelPosition: "none"）**: 矢印をアイコン中心から自由に配置可能
2. **ラベルあり（labelPosition: "bottom"）**: 
   - 水平矢印: アイコン中心Y（ラベルより上）から開始
   - 下向き分岐: ラベル下端より下から開始、または別途textboxでラベル配置

例（中心540、分岐幅±15px）:
```json
// 上向き（データストアへ）
{"type": "line", "x": 1020, "y": 525, "width": 320, "height": -135, "connectorType": "elbow", "tailEnd": "arrow"}

// 下向き（セキュリティへ）
{"type": "line", "x": 1020, "y": 555, "width": 320, "height": 155, "connectorType": "elbow", "tailEnd": "arrow"}
```

### 折れ線矢印（elbow）
水平→垂直または垂直→水平に曲がる:
```json
{
  "connectorType": "elbow",
  "width": [水平距離],
  "height": [垂直距離（負=上、正=下）]
}
```

### 矢印の種類選択

| パターン | connectorType | 用途 |
|----------|---------------|------|
| 直線 | straight（デフォルト） | 隣接アイコン間 |
| L字 | elbow | 異なる行/列への接続 |
| 曲線 | curved | 複雑な経路（非推奨） |

---

## テキスト配置

### ラベル位置の原則
- **矢印の上には置かない**: 重なって読みにくい
- **矢印の下または横に配置**

### 水平矢印のラベル
```
ラベルY = 矢印Y + 10〜15px（矢印の下）
ラベルX = 矢印X（左揃え）または中央揃え
```

例:
```json
{"type": "line", "x": 340, "y": 540, "width": 160, "height": 0, "tailEnd": "arrow"},
{"type": "textbox", "x": 340, "y": 555, "width": 160, "align": "center", "fontSize": 11, "text": "{{#8FA7C4:HTTPS}}"}
```

### 折れ線矢印のラベル
折れ曲がり部分の近くに配置:
```
上向きelbow → ラベルは折れ曲がりの右側
下向きelbow → ラベルは折れ曲がりの右側
```

### フォントサイズ目安

| 用途 | サイズ | 色 |
|------|--------|-----|
| グループタイトル | 12-14px | #8FA7C4 |
| 矢印ラベル | 10-11px | #8FA7C4 |
| アイコンラベル | 自動（labelPosition使用） | デフォルト |

---

## 色設計

### ダークテーマ推奨色

| 用途 | 色 |
|------|-----|
| AWS Cloud境界 | #FFFFFF |
| サブグループ境界 | #5A6B7D |
| サブグループ背景 | #1A242F |
| テキスト（補助） | #8FA7C4 |
| 矢印 | デフォルト（#8FA7C4） |

---

## 複雑なアーキテクチャのコツ

### 1. レイヤー分け
```
左 → 右: データフロー方向
上 → 下: レイヤー（フロントエンド → バックエンド → データ）
```

### 2. グループ活用
- 同じ役割のサービスをグループ化
- グループ間の矢印で全体フローを明示

### 3. 密度調整
要素が多い場合:
- アイコンサイズを小さく
- グループ内は密に、グループ間は疎に
- 重要でない接続は省略

### 4. 双方向通信
```json
// 2本の矢印を近接配置
{"type": "line", "x": 500, "y": 538, "width": 100, "height": 0, "tailEnd": "arrow"},
{"type": "line", "x": 600, "y": 542, "width": -100, "height": 0, "tailEnd": "arrow"}
```

---

## チェックリスト

- [ ] アイコンサイズは複雑さに合っているか
- [ ] 同じ行のアイコンはY座標が揃っているか
- [ ] 分岐矢印は中心から対称か
- [ ] 矢印ラベルは矢印と重なっていないか
- [ ] **分岐矢印がアイコンラベル（labelPosition: bottom）と重なっていないか**
- [ ] AWS Cloudロゴは枠線にピッタリ配置されているか
- [ ] グループの背景色で階層が明確か

---

## サンプル: サーバーレス Web アプリケーション

override機能を使って、全体像→部分フォーカスの段階的説明を実現。

```json
{
  "theme": "dark",
  "slides": [
    {
      "id": "arch-base",
      "layout": "title_only",
      "title": "サーバーレス Web アプリケーション",
      "elements": [
        {
          "type": "shape",
          "shape": "rectangle",
          "x": 420,
          "y": 200,
          "width": 1440,
          "height": 700,
          "fill": "none",
          "line": "#FFFFFF",
          "lineWidth": 2
        },
        {
          "type": "image",
          "src": "icons:AWS-Cloud-logo_32",
          "x": 422,
          "y": 202,
          "width": 80,
          "labelPosition": "none"
        },
        {
          "type": "shape",
          "shape": "rectangle",
          "x": 60,
          "y": 350,
          "width": 280,
          "height": 450,
          "fill": "none",
          "line": "#5A6B7D",
          "lineWidth": 1
        },
        {
          "type": "textbox",
          "x": 60,
          "y": 360,
          "width": 280,
          "height": 48,
          "fontSize": 14,
          "align": "center",
          "text": "{{bold:クライアント}}"
        },
        {
          "type": "image",
          "src": "icons:web_mobile_applications_dark",
          "x": 140,
          "y": 420,
          "width": 120,
          "labelPosition": "none"
        },
        {
          "type": "textbox",
          "x": 60,
          "y": 550,
          "width": 280,
          "height": 44,
          "fontSize": 12,
          "align": "center",
          "text": "モバイル / Web"
        },
        {
          "type": "image",
          "src": "icons:desktop_laptop_dark",
          "x": 140,
          "y": 600,
          "width": 120,
          "labelPosition": "none"
        },
        {
          "type": "textbox",
          "x": 60,
          "y": 730,
          "width": 280,
          "height": 44,
          "fontSize": 12,
          "align": "center",
          "text": "デスクトップ"
        },
        {
          "type": "image",
          "src": "icons:Arch_Amazon-CloudFront_48",
          "x": 500,
          "y": 480,
          "width": 120,
          "label": "CloudFront",
          "labelPosition": "bottom"
        },
        {
          "type": "image",
          "src": "icons:Arch_Amazon-API-Gateway_48",
          "x": 700,
          "y": 480,
          "width": 120,
          "label": "API Gateway",
          "labelPosition": "bottom"
        },
        {
          "type": "image",
          "src": "icons:Arch_AWS-Lambda_48",
          "x": 900,
          "y": 480,
          "width": 120,
          "label": "Lambda",
          "labelPosition": "bottom"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 1340,
          "y": 260,
          "width": 460,
          "height": 260,
          "fill": "#1A242F",
          "line": "#5A6B7D",
          "lineWidth": 1,
          "adjustments": [0.1]
        },
        {
          "type": "textbox",
          "x": 1340,
          "y": 270,
          "width": 460,
          "height": 44,
          "fontSize": 12,
          "align": "center",
          "text": "{{#8FA7C4:データストア}}"
        },
        {
          "type": "image",
          "src": "icons:Arch_Amazon-DynamoDB_48",
          "x": 1380,
          "y": 340,
          "width": 100,
          "label": "DynamoDB",
          "labelPosition": "bottom"
        },
        {
          "type": "image",
          "src": "icons:Res_Amazon-Simple-Storage-Service_Bucket_48",
          "x": 1520,
          "y": 340,
          "width": 100,
          "label": "S3",
          "labelPosition": "bottom"
        },
        {
          "type": "image",
          "src": "icons:Arch_Amazon-ElastiCache_48",
          "x": 1660,
          "y": 340,
          "width": 100,
          "label": "ElastiCache",
          "labelPosition": "bottom"
        },
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 1340,
          "y": 580,
          "width": 460,
          "height": 260,
          "fill": "#1A242F",
          "line": "#5A6B7D",
          "lineWidth": 1,
          "adjustments": [0.1]
        },
        {
          "type": "textbox",
          "x": 1340,
          "y": 590,
          "width": 460,
          "height": 44,
          "fontSize": 12,
          "align": "center",
          "text": "{{#8FA7C4:セキュリティ & 監視}}"
        },
        {
          "type": "image",
          "src": "icons:Arch_Amazon-Cognito_48",
          "x": 1380,
          "y": 660,
          "width": 100,
          "label": "Cognito",
          "labelPosition": "bottom"
        },
        {
          "type": "image",
          "src": "icons:Arch_Amazon-CloudWatch_48",
          "x": 1520,
          "y": 660,
          "width": 100,
          "label": "CloudWatch",
          "labelPosition": "bottom"
        },
        {
          "type": "image",
          "src": "icons:Arch_AWS-X-Ray_48",
          "x": 1660,
          "y": 660,
          "width": 100,
          "label": "X-Ray",
          "labelPosition": "bottom"
        },
        {
          "type": "line",
          "x": 340,
          "y": 540,
          "width": 160,
          "height": 0,
          "tailEnd": "arrow"
        },
        {
          "type": "textbox",
          "x": 340,
          "y": 550,
          "width": 160,
          "height": 41,
          "fontSize": 11,
          "align": "center",
          "text": "{{#8FA7C4:HTTPS}}"
        },
        {
          "type": "line",
          "x": 620,
          "y": 540,
          "width": 80,
          "height": 0,
          "tailEnd": "arrow"
        },
        {
          "type": "line",
          "x": 820,
          "y": 540,
          "width": 80,
          "height": 0,
          "tailEnd": "arrow"
        },
        {
          "type": "line",
          "x": 1020,
          "y": 525,
          "width": 320,
          "height": -135,
          "connectorType": "elbow",
          "tailEnd": "arrow"
        },
        {
          "type": "textbox",
          "x": 1100,
          "y": 360,
          "width": 80,
          "height": 39,
          "fontSize": 10,
          "text": "{{#8FA7C4:R/W}}"
        },
        {
          "type": "line",
          "x": 1020,
          "y": 555,
          "width": 320,
          "height": 155,
          "connectorType": "elbow",
          "tailEnd": "arrow"
        },
        {
          "type": "textbox",
          "x": 1100,
          "y": 680,
          "width": 80,
          "height": 39,
          "fontSize": 10,
          "text": "{{#8FA7C4:認証}}"
        }
      ]
    },
    {
      "override": "arch-base",
      "layout": "title_only",
      "title": "サーバーレス Web アプリケーション",
      "elements": [
        {"type": "shape", "shape": "rectangle", "x": 0, "y": 130, "width": 1920, "height": 821, "fill": "#000000", "opacity": 0.8, "line": "none"},
        {"type": "shape", "shape": "rounded_rectangle", "x": 450, "y": 430, "width": 620, "height": 240, "fill": "none", "line": "#FF9900", "lineWidth": 2, "adjustments": [0.06]},
        {"type": "image", "src": "icons:Arch_Amazon-CloudFront_48", "x": 500, "y": 480, "width": 120, "label": "CloudFront", "labelPosition": "bottom"},
        {"type": "image", "src": "icons:Arch_Amazon-API-Gateway_48", "x": 700, "y": 480, "width": 120, "label": "API Gateway", "labelPosition": "bottom"},
        {"type": "image", "src": "icons:Arch_AWS-Lambda_48", "x": 900, "y": 480, "width": 120, "label": "Lambda", "labelPosition": "bottom"},
        {"type": "line", "x": 620, "y": 540, "width": 80, "height": 0, "tailEnd": "arrow"},
        {"type": "line", "x": 820, "y": 540, "width": 80, "height": 0, "tailEnd": "arrow"},
        {"type": "textbox", "x": 100, "y": 700, "width": 1300, "height": 131, "align": "center", "fontSize": 24, "text": "CloudFront → API Gateway → Lambda で\n{{#FF9900:サーバーレスなリクエスト処理}}を実現"}
      ]
    }
  ]
}
```

**override活用ポイント**:
- 1枚目（id: arch-base）: 全体像
- 2枚目以降: overrideでベースを継承し、オーバーレイ + 強調枠 + フォーカス要素を追加
- 同様に「データストア」「セキュリティ」フォーカスの派生スライドを追加可能

---
**Updated**: 2026-02-06

---

## バリアント: 図解＋説明テキスト分割（Zero-ETL）

左にアーキテクチャ図、右に説明テキスト3つ、中央にグラデーション区切り線。
データフロー図と要点説明を1枚に収めるレイアウト。

**構成**:
- 左半分: 白枠内にアイコン + ラベル + コネクタ矢印で構成した図解
- 中央: lineGradient付き縦線（accent6→accent4→accent2）
- 右半分: 説明テキスト3つ（等間隔配置）

**ポイント**:
- データソースは左列にアイコン+ラベルを縦並び
- ZERO-ETLラベル（accent6, bold）で変換ステップを明示
- 右下2x2グリッドで関連サービスを小さく配置
- 図タイトル（"Unified Data"）は背景色fillで枠線上に重ねる

```json
{
  "layout": "content",
  "title": "Zero-ETL 統合",
  "elements": [
    {
      "type": "textbox",
      "x": 48,
      "y": 158,
      "width": 1824,
      "height": 48,
      "line": "none",
      "text": "{{bold,#FFFFFF:説明サブタイトル}}",
      "fontSize": 14
    },
    {
      "type": "line",
      "x": 1007,
      "y": 298,
      "width": 0,
      "height": 515,
      "preset": "line",
      "headEnd": "none",
      "tailEnd": "none",
      "lineGradient": {
        "stops": [
          {
            "position": 0.0,
            "color": "#FBD332"
          },
          {
            "position": 0.628,
            "color": "#FF5C85"
          },
          {
            "position": 1.0,
            "color": "#AD5CFF"
          }
        ],
        "angle": 270.0
      },
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 46,
      "y": 317,
      "width": 911,
      "height": 491,
      "shape": "rectangle",
      "line": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 876,
      "y": 594,
      "width": 36,
      "height": 38,
      "shape": "rounded_rectangle",
      "adjustments": [
        0.16667
      ],
      "line": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 835,
      "y": 553,
      "width": 36,
      "height": 38,
      "shape": "rounded_rectangle",
      "adjustments": [
        0.16667
      ],
      "line": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 876,
      "y": 553,
      "width": 36,
      "height": 38,
      "shape": "rounded_rectangle",
      "adjustments": [
        0.16667
      ],
      "line": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 835,
      "y": 594,
      "width": 36,
      "height": 38,
      "shape": "rounded_rectangle",
      "adjustments": [
        0.16667
      ],
      "line": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 368,
      "y": 294,
      "width": 268,
      "height": 53,
      "shape": "rectangle",
      "fill": "#171D25",
      "line": "none",
      "verticalAnchor": 3,
      "text": "{{bold,#00E500:Unified Data}}",
      "fontSize": 16,
      "textAlign": "center"
    },
    {
      "type": "shape",
      "x": 390,
      "y": 380,
      "width": 538,
      "height": 89,
      "shape": "rectangle",
      "line": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "image",
      "x": 413,
      "y": 398,
      "width": 50,
      "height": 50,
      "src": "icons:embedded_analytics_dark"
    },
    {
      "type": "textbox",
      "x": 129,
      "y": 718,
      "width": 119,
      "height": 48,
      "line": "none",
      "text": "{{#FFFFFF: }}{{#FFFFFF:アプリケーション}}",
      "fontSize": 10
    },
    {
      "type": "textbox",
      "x": 347,
      "y": 629,
      "width": 218,
      "height": 143,
      "line": "none",
      "paragraphs": [
        {
          "text": "{{bold,#FBD332:Lakehouse}}"
        },
        {
          "text": "{{#FFFFFF: (Redshift Managed }}"
        },
        {
          "text": "{{#FFFFFF:Storage/}}{{#FFFFFF:オープンフォーマット）}}{{#FFFFFF: }}"
        }
      ],
      "fontSize": 10,
      "align": "center"
    },
    {
      "type": "image",
      "x": 598,
      "y": 577,
      "width": 39,
      "height": 39,
      "src": "icons:Arch_Amazon-SageMaker-AI_48"
    },
    {
      "type": "image",
      "x": 664,
      "y": 577,
      "width": 39,
      "height": 39,
      "src": "icons:Arch_Amazon-Athena_48"
    },
    {
      "type": "textbox",
      "x": 585,
      "y": 632,
      "width": 129,
      "height": 62,
      "line": "none",
      "text": "{{#FFFFFF:レコメンドエンジン}}",
      "fontSize": 10,
      "align": "center"
    },
    {
      "type": "shape",
      "x": 484,
      "y": 393,
      "width": 434,
      "height": 64,
      "shape": "rectangle",
      "line": "none",
      "verticalAnchor": 3,
      "text": "{{bold,#FF5C85:BI /}}{{bold,#FF5C85:分析アプリケーション}}{{#FFFFFF:\n}}{{#FFFFFF:分析と可視化のためにデータを連携する}}",
      "fontSize": 10,
      "textAlign": "left"
    },
    {
      "type": "textbox",
      "x": 724,
      "y": 627,
      "width": 91,
      "height": 48,
      "line": "none",
      "text": "{{bold,#FF5C85:AI/ML}}",
      "fontSize": 10
    },
    {
      "type": "textbox",
      "x": 725,
      "y": 529,
      "width": 91,
      "height": 44,
      "line": "none",
      "text": "{{bold,#FF5C85:Spark}}",
      "fontSize": 10
    },
    {
      "type": "textbox",
      "x": 129,
      "y": 562,
      "width": 128,
      "height": 48,
      "line": "none",
      "text": "{{#FFFFFF:NoSQL databases}}",
      "fontSize": 10
    },
    {
      "type": "image",
      "x": 83,
      "y": 567,
      "width": 34,
      "height": 34,
      "src": "icons:Arch_Amazon-DynamoDB_48"
    },
    {
      "type": "textbox",
      "x": 135,
      "y": 399,
      "width": 128,
      "height": 48,
      "line": "none",
      "paragraphs": [
        {
          "text": "{{#FFFFFF:Relational}}"
        },
        {
          "text": "{{#FFFFFF:databases }}"
        }
      ],
      "fontSize": 10
    },
    {
      "type": "image",
      "x": 79,
      "y": 407,
      "width": 39,
      "height": 39,
      "src": "icons:Arch_Amazon-Aurora_48"
    },
    {
      "type": "image",
      "x": 76,
      "y": 718,
      "width": 37,
      "height": 37,
      "src": "icons:applications_dark"
    },
    {
      "type": "line",
      "x": 617,
      "y": 484,
      "width": 0,
      "height": 69,
      "rotation": 180.0,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "headEnd": "none",
      "tailEnd": "arrow",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "line",
      "x": 683,
      "y": 484,
      "width": 0,
      "height": 69,
      "rotation": 180.0,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "headEnd": "arrow",
      "tailEnd": "none",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "line",
      "x": 731,
      "y": 580,
      "width": 72,
      "height": 0,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "headEnd": "arrow",
      "tailEnd": "arrow",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "line",
      "x": 731,
      "y": 610,
      "width": 72,
      "height": 0,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "headEnd": "arrow",
      "tailEnd": "arrow",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "textbox",
      "x": 252,
      "y": 554,
      "width": 126,
      "height": 67,
      "line": "none",
      "text": "{{bold,#FBD332:ZERO-ETL}}",
      "fontSize": 10
    },
    {
      "type": "line",
      "x": 257,
      "y": 595,
      "width": 151,
      "height": 0,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "headEnd": "none",
      "tailEnd": "arrow",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "line",
      "x": 241,
      "y": 441,
      "width": 93,
      "height": 31,
      "preset": "line",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "line",
      "x": 258,
      "y": 684,
      "width": 95,
      "height": 59,
      "flipH": true,
      "preset": "line",
      "headEnd": "none",
      "tailEnd": "triangle",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "line",
      "x": 534,
      "y": 560,
      "width": 0,
      "height": 69,
      "rotation": 270.0,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "headEnd": "none",
      "tailEnd": "arrow",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "textbox",
      "x": 1055,
      "y": 480,
      "width": 810,
      "height": 130,
      "line": "none",
      "fontSize": 18,
      "paragraphs": [
        {
          "text": "{{#FFFFFF:説明文}}{{#FFFFFF: 3-2}}",
          "bullet": true
        }
      ]
    },
    {
      "type": "textbox",
      "x": 1055,
      "y": 650,
      "width": 810,
      "height": 130,
      "line": "none",
      "fontSize": 18,
      "paragraphs": [
        {
          "text": "{{#FFFFFF:説明文}}{{#FFFFFF: 3-3}}",
          "bullet": true
        }
      ]
    },
    {
      "type": "image",
      "x": 434,
      "y": 578,
      "width": 43,
      "height": 43,
      "src": "icons:Arch_AWS-Glue_48"
    },
    {
      "type": "textbox",
      "x": 64,
      "y": 508,
      "width": 505,
      "height": 44,
      "line": "none",
      "paragraphs": [
        {
          "text": "{{#FFFFFF:Amazon}}"
        },
        {
          "text": "{{#FFFFFF:Redshift}}"
        }
      ],
      "fontSize": 9,
      "align": "center"
    },
    {
      "type": "image",
      "x": 286,
      "y": 449,
      "width": 54,
      "height": 54,
      "src": "icons:Arch_Amazon-Redshift_48"
    },
    {
      "type": "textbox",
      "x": 249,
      "y": 406,
      "width": 128,
      "height": 48,
      "line": "none",
      "text": "{{bold,#FBD332:ZERO-ETL}}",
      "fontSize": 10
    },
    {
      "type": "line",
      "x": 340,
      "y": 477,
      "width": 91,
      "height": 83,
      "preset": "straightConnector1",
      "connectorType": "straight",
      "tailEnd": "triangle",
      "color": "#FFFFFF",
      "lineWidth": 1.0
    },
    {
      "type": "shape",
      "x": 347,
      "y": 491,
      "width": 226,
      "height": 58,
      "shape": "rectangle",
      "line": "none",
      "verticalAnchor": 3,
      "text": "{{#FFFFFF:Federated\nCatalog}}",
      "fontSize": 9,
      "textAlign": "center"
    },
    {
      "type": "textbox",
      "x": 1055,
      "y": 310,
      "width": 810,
      "height": 130,
      "line": "none",
      "fontSize": 18,
      "paragraphs": [
        {
          "text": "{{#FFFFFF:説明文}}{{#FFFFFF: 3-1}}",
          "bullet": true
        }
      ]
    }
  ]
}
```
