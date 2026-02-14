# Tasks: PPTX Maker

## Implementation Checklist

### Phase 1: Core Script
- [x] pptx_builder.py 作成
  - [x] テンプレート読み込み・既存スライド削除
  - [x] layout mapping 実装
  - [x] title スライド対応
  - [x] agenda スライド対応（箇条書き）
  - [x] section / subsection 対応
  - [x] content スライド対応
  - [x] thankyou スライド対応
  - [x] CLI引数パース（argparse）
  - [x] 標準入力対応

### Phase 2: SKILL.md
- [x] SKILL.md 作成
  - [x] 基本的な使い方
  - [x] JSON Schema説明
  - [x] レイアウト一覧
  - [x] 良いAWS資料の作り方ガイド

### Phase 3: Validation
- [x] 各レイアウトで生成テスト
- [ ] エラーケースのテスト

## Validation
- [x] `pptx_builder.py generate test.json -o test.pptx` が動作する
- [x] 生成されたPPTXがPowerPointで正常に開ける
- [x] テンプレートのデザインが適用されている

---
**Created**: 2026-02-02
