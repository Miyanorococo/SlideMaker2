# Notes: PPTX Maker

## Log

### [2026-02-02 10:00] 調査開始
- FlowScriberのpptx_generator.rsを参考に調査
- テンプレート展開方式でPPTX生成する方針

### [2026-02-02 10:08] 既存ツール調査
- python-pptx: Python定番ライブラリ
- Marp: Markdown→PPTX変換
- 既存MCP: Plus AI, SlideSpeak等

### [2026-02-02 10:11] python-pptx検証
- template.pptxに57種類のレイアウトあり
- python-pptxでテンプレートのレイアウトを活用可能
- 既存スライド削除→新規追加の方式で動作確認

### [2026-02-02 10:16] 設計決定
- Skillとして実装（SKILL.md + scripts/）
- ~/.q-spec/repos/internal/pptx-maker/ に配置
- JSON形式でスライド定義を受け取る
- Phase 1はテキストベースのみ

### [2026-02-02 10:19] 実装完了
- pptx_builder.py作成
- プレースホルダーidx修正（department: 10→11, body: 1→10）
- SKILL.md作成

### [2026-02-02 15:47] テーマ対応
- template_2026.pptx追加（ライト/ダークテーマ）
- 2つのスライドマスター対応
- JSON `theme` フィールド追加
- `date` フィールド追加
- `title_only` レイアウト追加

### [2026-02-02 15:55] 表・テキストボックス対応
- `elements` で自由配置（table, textbox）
- テーマ別カラーパレット（THEME_COLORS）で色を統一管理
- 表: ヘッダー色、交互行色、テキスト色を自動適用
- テキストボックス: テーマに応じたテキスト色

### [2026-02-02 16:18] スタイル付きテキスト対応
- `{{attrs:text}}` 記法でインラインスタイル
- 対応属性: bold, italic, #RRGGBB（色）, NNpt（フォントサイズ）
- 複数属性はカンマ区切り: `{{bold,#FF9900:text}}`

### [2026-02-02 16:46] 位置指定の改善
- EMU → パーセント指定に変更
- 推奨描画エリア: x=3%〜97%, y=16%〜88%
- align（left/center/right）で位置基準を変更
- 全レイアウトでelements使用可能に

### [2026-02-02 17:06] 箇条書き対応
- agenda/contentのitemsに箇条書きマーク（•）を適用
- XMLレベルでbuChar設定

---
**Created**: 2026-02-02
