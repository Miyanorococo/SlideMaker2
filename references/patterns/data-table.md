---
name: data-table
description: 表形式でデータを整理・比較表示するパターン集
category: pattern
---

# データテーブルレイアウト

## ユースケース
- サービス仕様・制限事項の一覧表示
- ステータスマトリクス（バージョン管理、デプロイ状況）
- 機能比較・認証方式などの複雑な分類表

## デザインポイント
- `tableStyleId` でPowerPoint組み込みスタイルを指定し、ヘッダー色・バンド行・罫線を自動適用
- `tableStyleId` 使用時はセルに明示的なfill/fontColorを指定しない（スタイルが上書きされる）
- ステータス値など一部セルのみ `fontColor` で色を付ける
- 明示的な罫線・セル色が必要な場合は `tableStyleId` なしで全セルに指定

## 調整のコツ
- 列数5以上は幅が窮屈になるため、colWidthsで重要列を広めに
- fontSize 12-14ptが表内テキストの適正範囲
- rowSpan/gridSpanは複雑になりすぎないよう最小限に
- anchor: "ctr" で縦方向中央揃えにすると結合セルが見やすい

### 主要な組み込みテーブルスタイル
| スタイルID | 名前 | 特徴 |
|---|---|---|
| `{3B4B98B0-60AC-42C2-AFA5-B58CD77FA1E5}` | Dark Style 1 - Accent 1 | ダーク背景、accent1ヘッダー |
| `{0E3FDE45-AF77-4B5C-9715-49D594BDF05E}` | Dark Style 1 - Accent 3 | ダーク背景、accent3ヘッダー |
| `{912C8C85-51F0-491E-9774-3900AFEF0FD7}` | No Style, Table Grid | スタイルなし、罫線のみ |

## JSON

### 仕様・制限一覧テーブル

`tableStyleId` でダークスタイルを適用。ステータス列のみ色付きテキスト。

```json
{
  "layout": "title_only",
  "title": "サービス制限事項",
  "elements": [
    {
      "type": "table",
      "x": 100, "y": 200, "width": 1775, "height": 340,
      "colWidths": [474, 508, 186, 607],
      "rowHeights": [45, 50, 50, 50, 50],
      "firstRow": true, "bandRow": true,
      "tableStyleId": "{0E3FDE45-AF77-4B5C-9715-49D594BDF05E}",
      "headers": [
        {"text": "項目名", "align": "center", "fontSize": 13},
        {"text": "デフォルト値", "align": "center", "fontSize": 13},
        {"text": "変更可否", "align": "center", "fontSize": 13},
        {"text": "備考", "align": "center", "fontSize": 13}
      ],
      "rows": [
        [
          {"text": "リクエストタイムアウト", "fontSize": 12},
          {"text": "15分", "fontSize": 12, "align": "center"},
          {"text": "不可", "fontSize": 12, "align": "center", "fontColor": "#FBD332", "bold": true},
          {"text": "同期リクエストの最大時間", "fontSize": 12}
        ],
        [
          {"text": "最大ペイロードサイズ", "fontSize": 12},
          {"text": "100 MB", "fontSize": 12, "align": "center"},
          {"text": "不可", "fontSize": 12, "align": "center", "fontColor": "#FBD332", "bold": true},
          {"text": "リクエスト/レスポンスの最大サイズ", "fontSize": 12}
        ],
        [
          {"text": "最大ストリーミング時間", "fontSize": 12},
          {"text": "60分", "fontSize": 12, "align": "center"},
          {"text": "不可", "fontSize": 12, "align": "center", "fontColor": "#FBD332", "bold": true},
          {"text": "ストリーミング接続の最大時間", "fontSize": 12}
        ],
        [
          {"text": "1秒あたりの呼び出し数", "fontSize": 12},
          {"text": "エンドポイントあたり100", "fontSize": 12, "align": "center"},
          {"text": "可能", "fontSize": 12, "align": "center", "fontColor": "#00E500", "bold": true},
          {"text": "API呼び出しのレート制限", "fontSize": 12}
        ]
      ]
    }
  ]
}
```

### ステータスマトリクステーブル

行ごとにステップ、列ごとに環境を表すマトリクス。変更セルのみ緑で強調。

```json
{
  "layout": "title_only",
  "title": "デプロイメントステータス",
  "elements": [
    {
      "type": "table",
      "x": 109, "y": 200, "width": 1700, "height": 350,
      "colWidths": [500, 400, 400, 400],
      "rowHeights": [50, 50, 50, 50, 50],
      "firstRow": true, "bandRow": true,
      "tableStyleId": "{3B4B98B0-60AC-42C2-AFA5-B58CD77FA1E5}",
      "headers": [
        {"text": "操作", "align": "center", "fontSize": 14, "anchor": "ctr"},
        {"text": "開発環境", "align": "center", "fontSize": 14, "anchor": "ctr"},
        {"text": "ステージング", "align": "center", "fontSize": 14, "anchor": "ctr"},
        {"text": "本番環境", "align": "center", "fontSize": 14, "anchor": "ctr"}
      ],
      "rows": [
        [
          {"text": "初期セットアップ", "fontSize": 12, "anchor": "ctr"},
          {"text": "V1", "align": "center", "fontSize": 12, "anchor": "ctr"},
          {"text": "V1", "align": "center", "fontSize": 12, "anchor": "ctr"},
          {"text": "V1", "align": "center", "fontSize": 12, "anchor": "ctr"}
        ],
        [
          {"text": "機能追加リリース", "fontSize": 12, "anchor": "ctr"},
          {"text": "V2", "align": "center", "fontSize": 13, "fontColor": "#00E500", "bold": true, "anchor": "ctr"},
          {"text": "V1", "align": "center", "fontSize": 12, "anchor": "ctr"},
          {"text": "V1", "align": "center", "fontSize": 12, "anchor": "ctr"}
        ],
        [
          {"text": "設定変更", "fontSize": 12, "anchor": "ctr"},
          {"text": "V2", "align": "center", "fontSize": 12, "anchor": "ctr"},
          {"text": "V2", "align": "center", "fontSize": 13, "fontColor": "#00E500", "bold": true, "anchor": "ctr"},
          {"text": "V1", "align": "center", "fontSize": 12, "anchor": "ctr"}
        ],
        [
          {"text": "全環境更新", "fontSize": 12, "anchor": "ctr"},
          {"text": "V3", "align": "center", "fontSize": 13, "fontColor": "#00E500", "bold": true, "anchor": "ctr"},
          {"text": "V3", "align": "center", "fontSize": 13, "fontColor": "#00E500", "bold": true, "anchor": "ctr"},
          {"text": "V3", "align": "center", "fontSize": 13, "fontColor": "#00E500", "bold": true, "anchor": "ctr"}
        ]
      ]
    }
  ]
}
```

### 複合マトリクステーブル（rowSpan/gridSpan活用）

行・列の結合を使い、カテゴリごとにグループ化した分類表。全セルに明示的な罫線・色を指定。

```json
{
  "layout": "title_only",
  "title": "機能分類マトリクス",
  "elements": [
    {
      "type": "table",
      "x": 64, "y": 201, "width": 1803, "height": 736,
      "colWidths": [80, 431, 431, 431, 431],
      "rowHeights": [95, 125, 125, 125, 208],
      "firstRow": true, "bandRow": false,
      "headers": [
        {"text": "#", "align": "center", "bold": true, "fontSize": 18, "fill": "#161D26", "fontColor": "#FF9900", "borders": {"left": {"width": 1.0, "color": "#FFFFFF"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
        {"text": "カテゴリ A", "fontSize": 18, "fontColor": "#FFFFFF", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
        {"text": "カテゴリ B", "fontSize": 18, "fontColor": "#FFFFFF", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
        {"text": "カテゴリ C", "fontSize": 18, "fontColor": "#FFFFFF", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
        {"text": "カテゴリ D", "fontSize": 18, "fontColor": "#FFFFFF", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#FFFFFF"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}}
      ],
      "rows": [
        [
          {"text": "1", "align": "center", "bold": true, "fontSize": 18, "fontColor": "#FF9900", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#FFFFFF"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"text": "共通項目\n（3行にまたがる）", "rowSpan": 3, "fontSize": 18, "fontColor": "#FFFFFF", "anchor": "ctr", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"text": "方式 A", "bold": true, "fontColor": "#FF693C", "fontSize": 18, "anchor": "ctr", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"text": "実装パターン 1\n（2行にまたがる）", "rowSpan": 2, "fontSize": 18, "fontColor": "#FFFFFF", "anchor": "ctr", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"text": "対象リソース A\n（2行にまたがる）", "rowSpan": 2, "fontSize": 18, "fontColor": "#FFFFFF", "anchor": "ctr", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#FFFFFF"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}}
        ],
        [
          {"text": "2", "align": "center", "bold": true, "fontSize": 18, "fontColor": "#FF9900", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#FFFFFF"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"merged": true, "text": ""},
          {"text": "方式 B", "bold": true, "fontColor": "#FF693C", "fontSize": 18, "rowSpan": 3, "anchor": "ctr", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"merged": true, "text": ""},
          {"merged": true, "text": ""}
        ],
        [
          {"text": "3", "align": "center", "bold": true, "fontSize": 18, "fontColor": "#FF9900", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#FFFFFF"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"merged": true, "text": ""},
          {"merged": true, "text": ""},
          {"text": "実装パターン 2\n（2行にまたがる）", "rowSpan": 2, "fontSize": 18, "fontColor": "#FFFFFF", "anchor": "ctr", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"text": "対象リソース B", "bold": true, "fontColor": "#FF693C", "fontSize": 18, "anchor": "ctr", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#FFFFFF"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}}
        ],
        [
          {"text": "4", "align": "center", "bold": true, "fontSize": 18, "fontColor": "#FF9900", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#FFFFFF"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"text": "個別項目", "bold": true, "fontColor": "#FF693C", "fontSize": 18, "anchor": "ctr", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#161D26"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}},
          {"merged": true, "text": ""},
          {"merged": true, "text": ""},
          {"text": "対象リソース C", "bold": true, "fontColor": "#FF693C", "fontSize": 18, "anchor": "ctr", "fill": "#161D26", "borders": {"left": {"width": 1.0, "color": "#161D26"}, "right": {"width": 1.0, "color": "#FFFFFF"}, "top": {"width": 1.0, "color": "#FFFFFF"}, "bottom": {"width": 1.0, "color": "#FFFFFF"}}, "margins": {"left": 17, "right": 17, "top": 17, "bottom": 17}}
        ]
      ]
    }
  ]
}
```

## バリエーション

### シンプルテーブル（文字列のみ）
プロパティ不要な場合はセルを文字列で記述可能。テーマのデフォルト色が自動適用される。

```json
{
  "type": "table",
  "x": 58, "y": 270, "width": 1804,
  "headers": ["項目", "値", "説明"],
  "rows": [
    ["項目A", "100", "基本設定"],
    ["項目B", "200", "拡張設定"]
  ]
}
```
