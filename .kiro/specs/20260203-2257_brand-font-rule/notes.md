# Notes: ブランドフォントルール適用

Guidelines:
- **Append-only**: Never edit existing content
- **Capture thought process**: "Initially thought X, but actually Y"
- **Be specific**: Include errors, commands, numbers

## Log

### [2026-02-03 22:57] SPEC作成
- ブランドルール: 全角=メイリオ, 半角=Amazon Ember
- 個別指定は将来拡張として対象外

---
**Created**: 2026-02-03

### [2026-02-03 22:58] 実装完了
- `FONT_FULLWIDTH = "メイリオ"`, `FONT_HALFWIDTH = "Amazon Ember"` 定数追加
- `is_fullwidth()` 関数追加（ord(char) > 127で判定）
- `_split_by_width()` メソッド追加（文字種別でテキストを分割）
- `_apply_styled_text()` を修正し、run単位でフォントを適用
- imageのラベルも `_apply_styled_text()` 経由に変更
- テスト結果: 全角→メイリオ、半角→Amazon Emberで正しく分割・適用される
