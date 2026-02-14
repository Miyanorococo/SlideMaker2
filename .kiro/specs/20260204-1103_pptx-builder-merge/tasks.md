# Tasks: pptx_builder機能マージ

## Implementation Checklist
- [x] `_add_group`関数を追加
- [x] `_add_freeform_shape`関数を追加
- [x] `_apply_shape_formatting`関数を追加
- [x] `build_slide`に`_add_group`呼び出しを追加
- [x] `_add_shape`にadjustments対応を追加（既存）
- [x] `_add_shape`のグラデーションにopacity対応を追加
- [x] テキストフレームにmargin/verticalAnchor対応を追加
- [x] `_add_image`にimagePath/rotation対応を追加

## Validation
- [x] 既存のサンプルJSONが正常に生成できる
- [ ] グループ要素を含むJSONが生成できる
- [ ] フリーフォーム図形が生成できる

---
**Created**: 2026-02-04
