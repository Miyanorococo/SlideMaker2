# PPTX Maker

社内テンプレートを使用してJSONからPowerPointを生成するツール。オーケストレーター + サブエージェント構成で、デザインパターンに基づく高品質なスライドを自動生成する。

## 特徴

- **Component + Pattern 2層設計**: 部品カタログ（組み合わせ自由）+ レイアウトパターン（配置骨格）
- **サブエージェント委譲**: 最大4並列でスライド構築を委譲
- **デザインパターン準拠**: lineGradient枠線、大アイコン、fade line等のプロフェッショナルデザイン
- **Slide Override**: 段階的開示・強調変更の継承機構

## 実行フロー

```
Step 1: 全体設計 ─ ソース読み込み → アジェンダ → 各スライドの設計書
  ↓
Step 2: パターン確認 ─ components/ + patterns/ を読み込み
  ↓
Step 3: サブエージェント委譲 ─ 最大4並列でJSON構築
  ↓
Step 4: マージ & 生成 ─ 複数JSONを結合 → PPTX生成
  ↓
Step 5: レビュー & 調整
```

## セットアップ

### 前提条件

- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### インストール

```bash
cd ~/.q-spec/repos/internal/pptx-maker
uv sync
```

### サブエージェント配置

```bash
cp ~/.q-spec/repos/internal/pptx-maker/agents/slide-builder.json ~/.kiro/agents/
```

## ディレクトリ構成

```
pptx-maker/
├── README.md                     # このファイル
├── SKILL.md                      # オーケストレーター向けSOP
├── agents/
│   ├── slide-builder.json        # サブエージェント設定
│   └── slide-builder-prompt.md   # サブエージェントプロンプト
├── references/
│   ├── json-schema.md            # Element仕様・Styled Text
│   ├── design-rules.md           # 色・フォント・グラデーション
│   ├── components/               # 部品カタログ
│   │   ├── component-catalog.md
│   │   └── component-recipe.md
│   └── patterns/                 # レイアウトパターン
│       ├── three-column-cards.md
│       ├── four-column-comparison.md
│       └── ...
├── scripts/
│   ├── pptx_builder.py           # JSON → PPTX
│   ├── pptx_to_json.py           # PPTX → JSON
│   └── download_icons.py         # アイコンDL
└── template_2026.pptx            # 社内テンプレート
```

## 使い方

```bash
# 生成
uv run python3 scripts/pptx_builder.py generate slides.json -o output.pptx

# プレビュー
uv run python3 scripts/pptx_builder.py preview output.pptx

# アイコン検索
uv run python3 scripts/pptx_builder.py icon-search "lambda api"

# パターン一覧
uv run python3 scripts/pptx_builder.py examples

# PPTX → JSON逆変換
uv run python3 scripts/pptx_to_json.py input.pptx -o output.json
```

kiro-cli chat でプレゼン作成を依頼すると、SKILL.md のワークフローに従って自動生成される。
