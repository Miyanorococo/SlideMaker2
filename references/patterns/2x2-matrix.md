---
name: 2x2-matrix
description: 2軸で4象限に分類する意思決定マトリクス
category: pattern
---

# 2x2マトリクス 設計ガイド

## ユースケース

- 意思決定フレームワーク（重要度×緊急度など）
- ポジショニングマップ（価格×品質など）
- 分類・比較（複雑さ×頻度など）
- 戦略マトリクス（成長率×市場シェアなど）

---

## レイアウト設計

### 描画エリア
```
スライド: 1920 x 1080px
コンテンツ: y=160〜1000
軸の中心: x=960, y=560
```

### 象限の座標

| 象限 | 位置 | X範囲 | Y範囲 |
|------|------|-------|-------|
| A（左上） | 高×低 | 200-940 | 200-540 |
| B（右上） | 高×高 | 980-1720 | 200-540 |
| C（左下） | 低×低 | 200-940 | 580-920 |
| D（右下） | 低×高 | 980-1720 | 580-920 |

---

## 要素配置

### 軸ラベル
```
上: y=180, align=center
下: y=900, align=center
左: x=80, y=550
右: x=1750, y=550
```

### 象限コンテンツ
各象限に配置する要素:
1. **アイコン**（オプション）: 象限の上部
2. **タイトル**: 太字、下線付き
3. **説明文**: 2-3行程度
4. **ユースケース**: 具体例

---

## カスタマイズガイド

### カスタマイズ推奨要素
- **軸ラベル**: 用途に応じた軸の意味を設定
- **象限コンテンツ**: アイコン・タイトル・説明・ユースケースを自由に
- **アイコン**: 象限ごとに異なるアイコンで視覚的に区別

### 軸の意味を変える
| 軸パターン | 縦軸 | 横軸 | 用途 |
|------------|------|------|------|
| 優先度 | 重要度 | 緊急度 | タスク管理 |
| 市場分析 | 成長率 | シェア | BCGマトリクス |
| 技術選定 | 複雑さ | 価値 | 投資判断 |
| 業務分類 | 複雑さ | 頻度 | 自動化判断 |

### テーマ切り替え時の調整ポイント
darkテーマに変更する場合、以下の要素も合わせて調整を検討:
- 軸線の色（背景に対して視認性を確保）
- 象限タイトルの色（背景とのコントラスト）
- ユースケース等の補助テキストの色
- 軸ラベルの色

### 象限の強調
特定の象限を強調したい場合:
```json
{
  "type": "shape",
  "shape": "rectangle",
  "x": 980,
  "y": 200,
  "width": 740,
  "height": 340,
  "fill": "#FF9900",
  "opacity": 0.1,
  "line": "none"
}
```

### アイコンの選択
象限の内容に合わせてAWSアイコンまたは汎用アイコンを選択:
```bash
python3 scripts/pptx_builder.py icon-search "research automation"
```

---

## デザインバリエーション

### 1. シンプル（テキストのみ）
- アイコンなし
- タイトル＋説明のみ
- 軸ラベルを強調

### 2. アイコン付き
- 各象限にアイコン配置
- タイトル＋説明＋ユースケース
- 視覚的に分かりやすい

### 3. カード型
- 各象限を角丸矩形で囲む
- 背景色で象限を区別
- より構造化された印象

---

## チェックリスト

- [ ] 軸の意味が明確か（ラベルで伝わるか）
- [ ] 4象限のバランスが取れているか
- [ ] 各象限の内容量が均等か
- [ ] 軸線が中央に配置されているか
- [ ] ヘッダーのタイトルが内容を表しているか

---

## サンプル: 業務自動化マトリクス

```json
{
  "theme": "light",
  "slides": [
    {
      "layout": "title_only",
      "title": "業務自動化の判断マトリクス",
      "elements": [
        {
          "type": "line",
          "x": 960,
          "y": 200,
          "width": 0,
          "height": 720,
          "color": "#5F6368",
          "lineWidth": 1.5,
          "headEnd": "triangle",
          "tailEnd": "triangle"
        },
        {
          "type": "line",
          "x": 120,
          "y": 560,
          "width": 1680,
          "height": 0,
          "color": "#5F6368",
          "lineWidth": 1.5,
          "headEnd": "triangle",
          "tailEnd": "triangle"
        },
        {
          "type": "textbox",
          "x": 860,
          "y": 170,
          "width": 200,
          "height": 48,
          "align": "center",
          "fontSize": 14,
          "text": "{{#5F6368:複雑なタスク}}"
        },
        {
          "type": "textbox",
          "x": 860,
          "y": 930,
          "width": 200,
          "height": 48,
          "align": "center",
          "fontSize": 14,
          "text": "{{#5F6368:単純なタスク}}"
        },
        {
          "type": "textbox",
          "x": 58,
          "y": 520,
          "width": 60,
          "height": 184,
          "align": "center",
          "fontSize": 14,
          "text": "{{#5F6368:アド\nホック}}"
        },
        {
          "type": "textbox",
          "x": 1802,
          "y": 520,
          "width": 60,
          "height": 184,
          "align": "center",
          "fontSize": 14,
          "text": "{{#5F6368:定期\nタスク}}"
        },
        {
          "type": "image",
          "src": "icons:Quick_Suite_Research",
          "x": 280,
          "y": 240,
          "width": 64,
          "labelPosition": "none"
        },
        {
          "type": "textbox",
          "x": 360,
          "y": 250,
          "width": 500,
          "height": 63,
          "fontSize": 20,
          "text": "{{bold,#232F3E:Research}}"
        },
        {
          "type": "textbox",
          "x": 280,
          "y": 320,
          "width": 580,
          "height": 82,
          "fontSize": 14,
          "text": "重要で深い分析が必要だが\n速度は求めないし回数は少ない"
        },
        {
          "type": "textbox",
          "x": 280,
          "y": 420,
          "width": 580,
          "height": 48,
          "fontSize": 14,
          "text": "{{#5F6368:ユースケース: 業界トレンド調査}}"
        },
        {
          "type": "image",
          "src": "icons:Quick_Suite_Automate",
          "x": 1040,
          "y": 240,
          "width": 64,
          "labelPosition": "none"
        },
        {
          "type": "textbox",
          "x": 1120,
          "y": 250,
          "width": 500,
          "height": 63,
          "fontSize": 20,
          "text": "{{bold,#232F3E:Automation}}"
        },
        {
          "type": "textbox",
          "x": 1040,
          "y": 320,
          "width": 580,
          "height": 82,
          "fontSize": 14,
          "text": "頻度は多くAIに任せる部分は広げたいが、\nリスクもあるので着実に進めていきたい"
        },
        {
          "type": "textbox",
          "x": 1040,
          "y": 420,
          "width": 580,
          "height": 48,
          "fontSize": 14,
          "text": "{{#5F6368:ユースケース: 毎週のレポートチェック}}"
        },
        {
          "type": "image",
          "src": "icons:Quick_Suite_Chat_Agents",
          "x": 280,
          "y": 600,
          "width": 64,
          "labelPosition": "none"
        },
        {
          "type": "textbox",
          "x": 360,
          "y": 610,
          "width": 500,
          "height": 63,
          "fontSize": 20,
          "text": "{{bold,#232F3E:Chat agents (Spaces)}}"
        },
        {
          "type": "textbox",
          "x": 280,
          "y": 680,
          "width": 580,
          "height": 82,
          "fontSize": 14,
          "text": "アドホックで探索的に\nやり取りしながら進めたい"
        },
        {
          "type": "textbox",
          "x": 280,
          "y": 780,
          "width": 580,
          "height": 82,
          "fontSize": 14,
          "text": "{{#5F6368:ユースケース: 自前のドキュメントを}}\n{{#5F6368:エージェントのナレッジにして分析(RAG)}}"
        },
        {
          "type": "image",
          "src": "icons:Quick_Suite_Flows",
          "x": 1040,
          "y": 600,
          "width": 64,
          "labelPosition": "none"
        },
        {
          "type": "textbox",
          "x": 1120,
          "y": 610,
          "width": 500,
          "height": 63,
          "fontSize": 20,
          "text": "{{bold,#232F3E:Flows}}"
        },
        {
          "type": "textbox",
          "x": 1040,
          "y": 680,
          "width": 580,
          "height": 82,
          "fontSize": 14,
          "text": "よくある業務なので、\npromptや分析手順を使いまわしたい"
        },
        {
          "type": "textbox",
          "x": 1040,
          "y": 780,
          "width": 580,
          "height": 48,
          "fontSize": 14,
          "text": "{{#5F6368:ユースケース: キャッチコピーの作成}}"
        }
      ]
    }
  ]
}
```
