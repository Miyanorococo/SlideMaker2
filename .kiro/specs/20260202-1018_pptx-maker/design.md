# Design: PPTX Maker

## Architecture

```
[Agent] → JSON → [pptx_builder.py] → [python-pptx] → PPTX
                        ↓
                 [template.pptx]
```

## Layout Mapping

template.pptxのレイアウトインデックスとlayout名のマッピング：

```python
LAYOUT_MAP = {
    "title": 2,        # Title Slide 1B
    "agenda": 7,       # Agenda Slide 2
    "section": 38,     # Section Header Option 1
    "subsection": 37,  # Section Header Option 2
    "content": 7,      # Agenda Slide 2（汎用）
    "thankyou": 48,    # Thank You Option 3
}
```

## Placeholder Mapping

各レイアウトのプレースホルダー構成：

### title (Title Slide 1B)
- idx=0: タイトル (ctrTitle)
- idx=1: サブタイトル (subTitle)
- idx=10: 事業部
- idx=13: 顧客名

### agenda / content (Agenda Slide 2)
- idx=0: タイトル
- idx=1: 本文/箇条書き

### section / subsection
- idx=0: タイトル

### thankyou
- プレースホルダーなし（固定デザイン）

## Implementation Strategy

### Reusable
- python-pptx ライブラリ

### New Components
- `pptx_builder.py`: メインスクリプト
  - `load_template()`: テンプレート読み込み、既存スライド削除
  - `add_slide(layout, **kwargs)`: スライド追加
  - `generate(slides_json, output_path)`: メイン処理

## Error Handling

- 不明なlayout → エラーメッセージ + 利用可能なlayout一覧を表示
- 必須フィールド欠落 → エラーメッセージ
- テンプレート未発見 → デフォルトパスを案内

---
**Created**: 2026-02-02
