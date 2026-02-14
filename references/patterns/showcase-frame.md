---
name: showcase-frame
description: レインボーグラデーション枠でスクリーンショットやデモ動画を展示
category: pattern
---

# ショーケースフレームレイアウト

## ユースケース
- デモ動画やGIFアニメーションの展示
- スクリーンショットの強調表示
- 製品UIのショーケース

## デザインポイント
- 中央に大きな角丸フレーム（70%幅）
- レインボーグラデーションの枠線で視線を引きつける
- 半透明の黒背景（opacity: 0.3）で画像を引き立てる
- 画像はフレーム内に配置

## 調整のコツ
- グラデーションの色順はstopsのpositionで調整
- 枠線の太さはlineWidthで調整（1-3pt推奨）
- 画像サイズはフレームより少し小さく（1-2%マージン）

## JSON

```json
{
  "theme": "dark",
  "slides": [
    {
      "layout": "content",
      "title": "デモタイトル",
      "elements": [
        {
          "type": "shape",
          "shape": "rounded_rectangle",
          "x": 288,
          "y": 194,
          "width": 1344,
          "height": 767,
          "adjustments": [
            0.04
          ],
          "fill": "#000000",
          "opacity": 0.3,
          "lineGradient": {
            "angle": 0,
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
          },
          "lineWidth": 2
        },
        {
          "type": "image",
          "src": "path/to/screenshot.png",
          "x": 307,
          "y": 216,
          "width": 1306
        }
      ]
    }
  ]
}
```

## バリエーション

### 青系グラデーション（クール）
```json
{
  "lineGradient": {
    "angle": 0,
    "stops": [
      {
        "position": 0,
        "color": "#00BFFF"
      },
      {
        "position": 0.5,
        "color": "#0072E5"
      },
      {
        "position": 1.0,
        "color": "#AD5CFF"
      }
    ]
  }
}
```

### オレンジ系グラデーション（AWS風）
```json
{
  "lineGradient": {
    "angle": 0,
    "stops": [
      {
        "position": 0,
        "color": "#FF9900"
      },
      {
        "position": 0.5,
        "color": "#FF693C"
      },
      {
        "position": 1.0,
        "color": "#FBD332"
      }
    ]
  }
}
```
