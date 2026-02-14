# Design: uv パッケージ管理導入

## 新規ファイル
- `pyproject.toml` - プロジェクトルートに配置、依存定義

## 更新ファイル
- `references/setup.md` - uv前提のセットアップ手順に書き換え
- `SKILL.md` - CLIコマンドを `uv run` 形式に更新
- `.kiro/steering/tech.md` - Commandsセクションを更新
- `README.md` - セットアップ・使い方を更新

## Implementation Strategy
- pyproject.tomlはminimal構成（build-system不要、スクリプトツールのため）
- 各ドキュメントの `python3 scripts/...` を `uv run python3 scripts/...` に置換
- setup.mdは全面書き換え（uv sync中心のフローに）

---
**Created**: 2026-02-09
