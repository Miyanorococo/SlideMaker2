# Design: pptx_builder機能マージ

## マージ戦略
現在版をベースに、Downloads版から機能を選択的に追加

## 追加する関数

### _add_group
```python
def _add_group(self, slide, elem):
    """グループ要素を展開して追加（python-pptxはグループ作成非対応）"""
```
- Downloads版をそのまま採用
- 再帰的にサブ要素を処理

### _add_freeform_shape
```python
def _add_freeform_shape(self, slide, elem):
    """カスタムジオメトリの図形を追加"""
```
- Downloads版をベースに、現在版の`_set_fill_opacity`を活用

### _apply_shape_formatting
```python
def _apply_shape_formatting(self, shape, elem):
    """図形のfill/line書式を適用（共通処理）"""
```
- Downloads版から追加
- freeform_shapeと通常shapeで共用

## 修正する関数

### _add_shape
- `adjustments`対応を追加（Downloads版から）
- グラデーションのopacity対応を追加

### _add_textbox / shape内テキスト
- `marginLeft/Top/Right/Bottom`対応を追加
- `verticalAnchor`対応を追加

### _add_image
- `imagePath`対応を追加（抽出画像の再利用）
- `rotation`対応を追加

### build_slide
- `_add_group`の呼び出しを追加

---
**Created**: 2026-02-04
