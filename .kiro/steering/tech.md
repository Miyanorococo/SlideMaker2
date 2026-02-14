# Tech

## Stack

- Python 3.x
- python-pptx
- lxml（XML操作）
- Pillow（プレビュー画像生成）
- uv（パッケージ管理）

## Architecture

```
pptx-maker/
├── SKILL.md              # エージェント向けワークフロー
├── references/
│   ├── json-schema.md    # JSON仕様
│   ├── design-rules.md   # デザインルール
│   ├── setup.md          # セットアップ手順
│   ├── components/       # 部品・レイアウト座標カタログ
│   └── patterns/         # デザインパターン（JSON付き完成形）
├── scripts/
│   ├── pptx_builder.py   # JSON → PPTX + CLI
│   └── pptx_to_json.py   # PPTX → JSON（逆変換）
├── template_2026.pptx    # 社内テンプレート
└── .kiro/
    ├── steering/         # 開発ガイド
    └── specs/            # SPEC履歴
```

## Commands

```bash
# 作業ディレクトリ初期化
uv run python3 scripts/pptx_builder.py init --theme dark

# 生成
uv run python3 scripts/pptx_builder.py generate slides.json -o output.pptx

# プレビュー（5%グリッド付き）
uv run python3 scripts/pptx_builder.py preview output.pptx
uv run python3 scripts/pptx_builder.py preview output.pptx -p 1,3,5 --no-grid

# アイコン検索
uv run python3 scripts/pptx_builder.py icon-search "lambda api"

# パターン一覧・詳細
uv run python3 scripts/pptx_builder.py examples
uv run python3 scripts/pptx_builder.py examples pattern-name

# PPTX → JSON変換
uv run python3 scripts/pptx_to_json.py input.pptx -o output.json
```

## ワークフロー

メインエージェントが一貫してスライド生成を担当：
1. Phase 1: 全体設計（アジェンダ合意）
2. Phase 2: 1枚ずつJSON構築（fs_write）
3. Phase 3: PPTX生成（全スライド完成後に1回）
4. Phase 4: プレビューPNGをレビュー
5. Phase 5: レビュー結果に基づき修正・再生成

## JSON概要

詳細は [references/json-schema.md](../references/json-schema.md) を参照。

- 座標: px（1920×1080基準）
- テキスト内`\n`は改行（paragraph分割）
- Styled Text: `{{bold:太字}}` `{{#FF9900:色}}` `{{link:URL:テキスト}}`
- Slide Override: `id`/`override`で要素継承

---
**Updated**: 2026-02-09
