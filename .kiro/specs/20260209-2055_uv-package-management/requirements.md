# Requirements: uv パッケージ管理導入

## Background & Context
### User Problems
- pptx-makerは社内配布スキルで、初めての人がセットアップする
- 現状 `pip install` でシステムPythonに直接インストールする手順になっている
- 標準環境の汚染を嫌うユーザーがいる
- 依存管理ファイル（pyproject.toml等）が存在しない

### Related Issues
- setup.md の手順が `pip install` 前提
- SKILL.md, tech.md, README.md のコマンドが `python3` 直接実行

## Objectives
- uvによる仮想環境管理で、システムPythonを汚さずに利用可能にする
- 初めての人が最小手順でセットアップ・実行できるようにする

## Scope
### In Scope
- `pyproject.toml` 作成（依存定義）
- `setup.md` をuv前提に更新
- `SKILL.md` のCLIコマンドを `uv run` に更新
- `tech.md` のコマンドセクションを更新
- `README.md` のセットアップ・使い方を更新

### Out of Scope
- スクリプト本体の変更（pptx_builder.py, pptx_to_json.py）
- cairoのインストール方法変更（引き続き `brew install cairo`）
- uv自体のインストール手順（利用者が各自導入済み前提、未導入時の案内のみ記載）

## Detailed Requirements
- `pyproject.toml` に python-pptx, lxml, Pillow, cairosvg を依存として宣言
- Python バージョン要件は `>=3.10` とする
- `uv sync` → `uv run python3 scripts/...` の2ステップで使えること
- 既存の `python3` 直接実行も引き続き動作する（uvは必須ではなく推奨）

---
**Created**: 2026-02-09
