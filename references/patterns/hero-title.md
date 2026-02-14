---
name: hero-title
description: 超大型タイトルでインパクトを出すアナウンス系スライド
category: pattern
---

# ヒーロータイトルレイアウト

## ユースケース
- 新サービス・新機能のアナウンス
- Introducing〜系の導入スライド
- インパクト重視のキービジュアル

## デザインポイント
- リード文（Introducing等）40pt + 超大型メインタイトル72ptの2段構成
- メインタイトルは画面の主役、boldで存在感を出す
- キーワードにアクセントカラー（#FF5CAAなど高コントラストのピンク）で視線誘導
- 縦位置は中央やや上（y=38%〜）で安定感

## 調整のコツ
- メインタイトルが長い場合は60pt程度に調整
- アクセントカラーは1箇所に絞る（複数色は散漫になる）
- リード文は40pt程度で控えめに

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
          "x": 96,
          "y": 410,
          "width": 1728,
          "height": 111,
          "fontSize": 40,
          "text": "Introducing"
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 518,
          "width": 1728,
          "height": 189,
          "fontSize": 72,
          "text": "{{bold:Amazon}} {{bold,#FF5CAA:Nova 2 Models}}"
        }
      ]
    }
  ]
}
```

## バリエーション

### イベントRe:cap版
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
          "x": 96,
          "y": 562,
          "width": 1152,
          "fontSize": 36,
          "text": "{{bold:re:Invent 2025 Re:cap}}"
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 691,
          "width": 1152,
          "fontSize": 24,
          "text": "{{#FF9900:AWS 生成AI・エージェント活用}}"
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 821,
          "width": 1152,
          "fontSize": 16,
          "text": "アマゾン ウェブ サービス ジャパン合同会社"
        },
        {
          "type": "textbox",
          "x": 96,
          "y": 886,
          "width": 1152,
          "fontSize": 16,
          "text": "{{italic:Your Name}}"
        }
      ]
    }
  ]
}
```
