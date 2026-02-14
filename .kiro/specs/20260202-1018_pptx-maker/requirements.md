# Requirements: PPTX Maker

## Background & Context

### User Problems
- AWS SAとして顧客向け提案資料や社内勉強会資料を頻繁に作成する
- AIエージェントと対話しながら資料を作成したいが、既存ツールでは社内テンプレートを活用できない

### Related Issues
- 社内テンプレート（template.pptx）には57種類のレイアウトが定義済み
- python-pptxで動作検証済み

## Objectives

AIエージェントがツールとして使用できるPPTX生成スクリプトを作成する。
社内テンプレートのデザインを活かしつつ、JSON入力からスライドを生成する。

## Scope

### In Scope
- JSON形式でスライド定義を受け取り、PPTXを生成
- 社内テンプレートのレイアウトを活用
- Phase 1: テキストベースのスライド（タイトル、箇条書き、セクション）
- Skillとして実装（SKILL.md + scripts/）

### Out of Scope
- 画像挿入（Phase 2）
- 図形描画・アーキテクチャ図（Phase 3）
- MCP化（将来検討）

## Detailed Requirements

### 対応レイアウト（Phase 1）

| layout名 | テンプレートレイアウト | 用途 |
|----------|----------------------|------|
| title | Title Slide 1B | 表紙 |
| agenda | Agenda Slide 2 | アジェンダ/箇条書き |
| section | Section Header Option 1 | セクション区切り |
| subsection | Section Header Option 2 | サブセクション |
| content | Agenda Slide 2 | 通常スライド |
| thankyou | Thank You Option 3 | 締め |

### JSON Schema

```json
{
  "slides": [
    {
      "layout": "title",
      "title": "タイトル",
      "subtitle": "サブタイトル",
      "department": "事業部名"
    },
    {
      "layout": "agenda",
      "title": "アジェンダ",
      "items": ["項目1", "項目2", "項目3"]
    },
    {
      "layout": "section",
      "title": "セクション名"
    },
    {
      "layout": "content",
      "title": "スライドタイトル",
      "body": "本文テキスト"
    },
    {
      "layout": "thankyou"
    }
  ]
}
```

### CLI Interface

```bash
# ファイルから
pptx_builder.py generate slides.json -o output.pptx

# 標準入力から
echo '{"slides": [...]}' | pptx_builder.py generate -o output.pptx

# テンプレート指定（オプション）
pptx_builder.py generate slides.json -o output.pptx -t custom_template.pptx
```

### ファイル構成

```
~/.q-spec/repos/internal/pptx-maker/
├── SKILL.md           # 使い方 + 良いAWS資料の作り方
├── scripts/
│   └── pptx_builder.py
└── template.pptx      # 社内テンプレート
```

---
**Created**: 2026-02-02
