# セットアップガイド

pptx-maker Skillを別環境で使用するためのセットアップ手順。

## 前提条件

- kiro-cli インストール済み
- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) インストール済み

## 1. 依存インストール

```bash
cd ~/.q-spec/repos/internal/pptx-maker
uv sync
```

## 2. サブエージェント配置

```bash
cp agents/design-reviewer.json ~/.kiro/agents/
kiro-cli agent list | grep design-reviewer
```

## 3. 動作確認

```bash
# pptx_builder.pyが動作するか確認
uv run python3 scripts/pptx_builder.py examples

# アイコン検索が動作するか確認
uv run python3 scripts/pptx_builder.py icon-search "lambda"

# init が動作するか確認
uv run python3 scripts/pptx_builder.py init --theme dark -o /tmp/test-pptx && rm -rf /tmp/test-pptx
```

## トラブルシューティング

### uvが未インストール
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### "design-reviewer agent not found"
```bash
cp agents/design-reviewer.json ~/.kiro/agents/
```

### "Missing icons" エラー
```bash
uv run python3 scripts/download_icons.py
```
