---
name: agenda-highlight
description: アジェンダのセクションハイライト（override活用）
category: pattern
---

# アジェンダハイライト

## ユースケース
- プレゼン進行に合わせて現在のセクションを強調
- 同じアジェンダを複数回表示し、どこにいるか視覚的に示す

## デザインポイント
- ベーススライドに全アジェンダ項目を配置
- 派生スライドでハイライトしたい項目をアクセントカラーで上書き
- override機能でベース変更時に全派生スライドへ自動反映

## 調整のコツ
- ハイライトは`{{#FF9900,bold:...}}`で目立たせる
- 非ハイライト項目は薄いグレー（`#8FA7C4`）で控えめに
- セクション番号の前に矢印アイコンを追加するとより明確

## 注意: テキスト重ね合わせのズレ
overrideでテキストを重ねる場合、**boldの有無でフォント描画位置が微妙にズレる**ことがある。

**対処方法**:
1. **両方boldにする**: ベースもoverride側も同じスタイルにして揃える（推奨）
2. **背景矩形で隠す**: override側で背景色の矩形を先に配置し、その上にテキストを描画

## JSON

```json
{
  "theme": "dark",
  "slides": [
    {
      "id": "agenda-base",
      "layout": "agenda",
      "title": "Agenda",
      "elements": [
        {"type": "textbox", "x": 100, "y": 250, "width": 1200, "fontSize": 32, "text": "{{bold,#8FA7C4:1. Introduction}}"},
        {"type": "textbox", "x": 100, "y": 330, "width": 1200, "fontSize": 32, "text": "{{bold,#8FA7C4:2. Architecture Overview}}"},
        {"type": "textbox", "x": 100, "y": 410, "width": 1200, "fontSize": 32, "text": "{{bold,#8FA7C4:3. Demo}}"},
        {"type": "textbox", "x": 100, "y": 490, "width": 1200, "fontSize": 32, "text": "{{bold,#8FA7C4:4. Q&A}}"}
      ]
    },
    {
      "override": "agenda-base",
      "layout": "agenda",
      "title": "Agenda",
      "elements": [
        {"type": "textbox", "x": 100, "y": 250, "width": 1200, "fontSize": 32, "text": "{{bold,#FF9900:1. Introduction}}"}
      ]
    },
    {
      "override": "agenda-base",
      "layout": "agenda",
      "title": "Agenda",
      "elements": [
        {"type": "textbox", "x": 100, "y": 330, "width": 1200, "fontSize": 32, "text": "{{bold,#FF9900:2. Architecture Overview}}"}
      ]
    },
    {
      "override": "agenda-base",
      "layout": "agenda",
      "title": "Agenda",
      "elements": [
        {"type": "textbox", "x": 100, "y": 410, "width": 1200, "fontSize": 32, "text": "{{bold,#FF9900:3. Demo}}"}
      ]
    },
    {
      "override": "agenda-base",
      "layout": "agenda",
      "title": "Agenda",
      "elements": [
        {"type": "textbox", "x": 100, "y": 490, "width": 1200, "fontSize": 32, "text": "{{bold,#FF9900:4. Q&A}}"}
      ]
    }
  ]
}
```
