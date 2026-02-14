---
name: section-label-bullets
description: ラベル見出しとコンテンツを組み合わせた情報整理レイアウト
category: pattern
---

# セクションラベル＋コンテンツレイアウト

## ユースケース
- 情報を明確なセクションに分けて提示
- ラベル付きで視認性の高い構造化スライド
- 提案・報告・比較など幅広い用途

## デザインポイント
- セクションラベル: 矩形やテキストで見出しを明示（色付き・枠線・テキストのみなど自由）
- コンテンツ: 箇条書き、テキスト、強調色の混在が可能
- verticalAnchor でラベルテキストの縦位置を調整

## 調整のコツ
- ラベルのスタイル（fill、枠線、フォントサイズ）でセクションの重要度を表現
- セクション数は2〜3が適切（それ以上は縦スペース不足）
- 強調色は `#41B3FF`（accent1）が標準、他のaccent色も可
- バナー・区切り線など補助要素は用途に応じて追加・省略

## JSON

### パターン1: 色付きラベル＋箇条書き＋下部バナー

```json
{
  "layout": "title_only",
  "title": "タイトル",
  "elements": [
    {
      "type": "shape",
      "x": 64, "y": 172, "width": 381, "height": 67,
      "shape": "rectangle", "fill": "#0060A0", "line": "none",
      "verticalAnchor": 3,
      "text": "{{bold,#FFFFFF:セクション 1}}", "textAlign": "center"
    },
    {
      "type": "textbox",
      "x": 64, "y": 256, "width": 1803, "height": 172,
      "line": "none",
      "paragraphs": [
        {"text": "背景説明文 1", "bullet": true, "spaceAfter": 600},
        {"text": "背景説明文 2", "bullet": true, "spaceAfter": 600}
      ],
      "fontSize": 20
    },
    {
      "type": "shape",
      "x": 64, "y": 431, "width": 381, "height": 67,
      "shape": "rectangle", "fill": "#0060A0", "line": "none",
      "verticalAnchor": 3,
      "text": "{{bold,#FFFFFF:セクション 2}}", "textAlign": "center"
    },
    {
      "type": "textbox",
      "x": 64, "y": 532, "width": 1803, "height": 233,
      "line": "none",
      "paragraphs": [
        {"text": "{{bold,#41B3FF:強調ポイント 1}}{{#FFFFFF:の補足説明文。}}", "bullet": true, "spaceAfter": 600},
        {"text": "{{bold,#41B3FF:強調ポイント 2}}{{#FFFFFF:の補足説明文。}}", "bullet": true, "spaceAfter": 600},
        {"text": "{{#FFFFFF:通常文の中で}}{{bold,#41B3FF:強調ポイント 3}}{{#FFFFFF:を含む説明文。}}", "bullet": true, "spaceAfter": 600}
      ],
      "fontSize": 20
    },
    {
      "type": "shape",
      "x": 64, "y": 836, "width": 1803, "height": 118,
      "shape": "rectangle", "fill": "#0060A0", "line": "none",
      "verticalAnchor": 3,
      "text": "{{bold,#FFFFFF:まとめ・結論メッセージ}}",
      "fontSize": 28, "textAlign": "center"
    }
  ]
}
```

### パターン2: 枠線グリッド＋ラベル＋箇条書き（spaceAfter付き）

左にラベル、右にコンテンツの2行グリッド。枠線のみ（fill なし）で区切り。

```json
{
  "layout": "title_only",
  "title": "タイトル",
  "elements": [
    {
      "type": "shape",
      "x": 83, "y": 201, "width": 346, "height": 208,
      "shape": "rectangle", "fill": "none", "line": "#FCFCFD",
      "verticalAnchor": 3,
      "text": "ラベル 1", "fontSize": 24, "textAlign": "center"
    },
    {
      "type": "shape",
      "x": 451, "y": 201, "width": 1329, "height": 208,
      "shape": "rectangle", "fill": "none", "line": "#FCFCFD",
      "verticalAnchor": 3,
      "items": [
        {"text": "説明文 1-1", "spaceAfter": 800},
        {"text": "説明文 1-2", "spaceAfter": 800}
      ],
      "fontSize": 20, "textAlign": "left"
    },
    {
      "type": "shape",
      "x": 83, "y": 449, "width": 346, "height": 453,
      "shape": "rectangle", "fill": "none", "line": "#FCFCFD",
      "verticalAnchor": 3,
      "text": "ラベル 2", "fontSize": 24, "textAlign": "center"
    },
    {
      "type": "shape",
      "x": 451, "y": 449, "width": 1329, "height": 453,
      "shape": "rectangle", "fill": "none", "line": "#FCFCFD",
      "verticalAnchor": 3,
      "items": [
        {"text": "説明文 2-1", "spaceAfter": 800},
        {"text": "説明文 2-2", "spaceAfter": 800},
        {"text": "説明文 2-3", "spaceAfter": 800},
        {"text": "説明文 2-4", "spaceAfter": 800}
      ],
      "fontSize": 20, "textAlign": "left"
    }
  ]
}
```
