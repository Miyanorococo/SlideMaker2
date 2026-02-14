---
name: five-points-deepdive
description: 5つのポイント + プログレッシブハイライトで深掘り
category: pattern
---

# 5ポイント深掘りレイアウト

## ユースケース
- メリットや特徴を5つ程度列挙
- 各ポイントを順番に深掘り説明
- プレゼンで1つずつフォーカスしながら解説

## デザインポイント
- 上段3つ、下段2つの配置でバランス
- アイコン + キーワードのシンプルな構成
- 2枚目以降で半透明オーバーレイ + 深掘りテキスト

## プログレッシブハイライト技法
1. 1枚目: 全体像を表示（`id`でベース定義）
2. 2枚目以降: `override`でベースを継承
3. 半透明の黒オーバーレイ（opacity: 0.85）で背景を暗く
4. フォーカスする要素だけ再描画して前面に
5. 中央に大きく深掘り説明を配置

**override活用のメリット**:
- ベースの5ポイント配置を変更 → 全派生スライドに自動反映
- 各深掘りスライドは「追加要素のみ」で記述量削減

## 調整のコツ
- オーバーレイのopacityは0.8-0.9が見やすい
- フォーカス要素は元の位置に再配置
- 深掘りテキストは32pt程度で視認性確保

## JSON

```json
{
  "theme": "dark",
  "slides": [
    {
      "id": "five-points-base",
      "layout": "title_only",
      "title": "AWS 活用のメリット",
      "elements": [
        {"type": "image", "src": "icons:aws_global_dark", "x": 230, "y": 270, "width": 134, "labelPosition": "none"},
        {"type": "textbox", "x": 38, "y": 410, "width": 518, "height": 111, "align": "center", "fontSize": 20, "text": "{{#FF9900:グローバルに展開}}される\nインフラストラクチャ"},
        {"type": "image", "src": "icons:shield_dark", "x": 883, "y": 270, "width": 134, "labelPosition": "none"},
        {"type": "textbox", "x": 634, "y": 410, "width": 634, "height": 111, "align": "center", "fontSize": 20, "text": "{{#FF9900:セキュリティ}}機能と\n{{#FF9900:コンプライアンス}}認証の取得"},
        {"type": "image", "src": "icons:fast_applications_dark", "x": 1536, "y": 270, "width": 134, "labelPosition": "none"},
        {"type": "textbox", "x": 1306, "y": 410, "width": 576, "height": 111, "align": "center", "fontSize": 20, "text": "すぐに ITリソースを\n利用できる{{#FF9900:俊敏性}}"},
        {"type": "image", "src": "icons:scale_dark", "x": 576, "y": 648, "width": 134, "labelPosition": "none"},
        {"type": "textbox", "x": 346, "y": 788, "width": 576, "height": 111, "align": "center", "fontSize": 20, "text": "{{#FF9900:弾力性}}で\n必要な時に必要なだけ"},
        {"type": "image", "src": "icons:aws_products_services_dark", "x": 1210, "y": 648, "width": 134, "labelPosition": "none"},
        {"type": "textbox", "x": 960, "y": 788, "width": 634, "height": 63, "align": "center", "fontSize": 20, "text": "{{#FF9900:240}}を超える豊富なサービス"}
      ]
    },
    {
      "override": "five-points-base",
      "layout": "title_only",
      "title": "AWS 活用のメリット",
      "elements": [
        {"type": "shape", "shape": "rectangle", "x": 0, "y": 130, "width": 1920, "height": 821, "fill": "#000000", "opacity": 0.85, "line": "none"},
        {"type": "image", "src": "icons:aws_global_dark", "x": 230, "y": 270, "width": 134, "labelPosition": "none"},
        {"type": "textbox", "x": 38, "y": 410, "width": 518, "height": 111, "align": "center", "fontSize": 20, "text": "{{#FF9900:グローバルに展開}}される\nインフラストラクチャ"},
        {"type": "textbox", "x": 154, "y": 648, "width": 1613, "height": 170, "align": "center", "fontSize": 32, "text": "AWS グローバルインフラストラクチャによって\n{{#FF9900:高い可用性}}、{{#FF9900:耐障害性}}を実現"}
      ]
    }
  ]
}
```
