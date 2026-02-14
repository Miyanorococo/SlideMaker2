# Requirements: SKILL.md 構造改革

## 背景

現在のpptx-makerは SKILL.md (629行) + .kiro/steering/tech.md にスキーマ・ワークフロー・デザインルールが混在。sop-creator の SOP形式 + deep-research のサブエージェント構成を参考に、段階的開示・サブエージェント委譲の構造へ移行する。

## 目標構造

```
pptx-maker/
├── README.md                    # NEW: プロジェクト概要（人間向け）
├── SKILL.md                     # REFACTOR: <500行、オーケストレーター向けSOP
├── agents/
│   ├── slide-builder.json       # NEW: サブエージェント設定
│   └── slide-builder-prompt.md  # NEW: サブエージェントプロンプト
├── references/
│   ├── json-schema.md           # MOVE: Element仕様・Styled Text等
│   ├── design-rules.md          # MOVE: 色パレット・height計算等
│   └── workflow-details.md      # MOVE: Phase詳細手順
├── examples/
│   ├── components/              # 部品カタログ（組み合わせて使う）
│   │   ├── component-catalog.md # 既存を移動
│   │   └── component-recipe.md  # 既存を移動
│   └── patterns/                # レイアウトパターン（配置に集中）
│       ├── three-column-cards.md
│       ├── four-column-comparison.md
│       └── ...（既存パターン）
├── scripts/                     # KEEP: 既存スクリプト（変更なし）
└── template_2026.pptx           # KEEP
```

## 機能要件

### FR-1: SKILL.md のSOP形式化（<500行）

現在のSKILL.mdを sop-creator 形式に準拠させる:

- YAML frontmatter（name, description + トリガー条件）
- Overview（役割: オーケストレーター）
- Parameters（ペルソナ、目的、分量、テーマ等）
- Steps（RFC 2119制約付き）
- 詳細はreferences/への動的参照

**SKILL.mdに残すもの**:
- ワークフロー概要（Phase 1-3）
- 各Phaseの要約とRFC 2119制約
- サブエージェント呼び出し方法
- CLIコマンド一覧
- references/への参照リンク

**SKILL.mdから移動するもの**:
- JSON Schema詳細 → references/json-schema.md
- デザインルール（60-30-10、色パレット等）→ references/design-rules.md
- Phase内の詳細手順 → references/workflow-details.md
- height計算ガイドライン → references/design-rules.md

### FR-2: サブエージェント（slide-builder）の導入

deep-research の parallel-searcher パターンに倣い、実際のスライド構築をサブエージェントに委譲:

**オーケストレーター（SKILL.md）の責務**:
- Phase 1: 全体設計（ソース資料読み込み → アジェンダ作成 → 各スライドの設計書作成）
- Phase 2: 各スライドの設計書をサブエージェントに渡して構築を委譲
- Phase 3: 各サブエージェントが出力した個別JSONをマージして最終PPTX生成
- Phase 4: 最終レビュー・調整
- ユーザーとの対話

**サブエージェント（slide-builder）の責務**:
- オーケストレーターから受け取る入力:
  1. **スライド設計書**: 伝えたい内容、使用パターン名、使用コンポーネント名
  2. **コンポーネント参照**: 該当する components/ の内容
  3. **パターン参照**: 該当する patterns/ の内容
- icon-search の実行
- JSON要素の構築（座標計算、色指定等）
- **担当分のJSONファイルを出力**（複数スライドを含む場合あり）

**並列実行**:
- サブエージェントの最大並列数は4
- オーケストレーターはスライドを最大4グループに分割して並列委譲
- 例: 12枚 → 3スライド×4並列

**Phase 3: マージ & 生成（オーケストレーター）**:
```bash
# 各サブエージェントが出力したJSONをまとめて生成
python3 scripts/pptx_builder.py generate batch_a.json batch_b.json batch_c.json batch_d.json -o output.pptx
```
- pptx_builder.py に複数JSON入力のマージ機能を追加（NFR-0）

**agents/slide-builder.json**:
- サブエージェント設定（利用ツール: execute_bash, fs_read, fs_write）
- プロンプトファイルへの参照

**agents/slide-builder-prompt.md**:
- JSON Schema の全量
- デザインルール
- 座標計算・height計算ガイドライン
- 「1スライドのJSON構築 → generate → open」の手順

### FR-3: examples/ の Component / Pattern 分離

**Component（examples/components/）**:
- 再利用可能な部品カタログ（lineGradientカード、fade line、アクセントバー等）
- 組み合わせて使う「引き出し」
- 既存の component-catalog.md, component-recipe.md を移動

**Pattern（examples/patterns/）**:
- スライド全体のレイアウト骨格（three-column-cards, architecture-diagram等）
- 個々の部品はシンプルに、配置・構成に集中
- 部品の詳細はコンポーネントを参照（パターン内では応用形のみ記載）
- 既存のパターンファイルを移動

### FR-4: references/ による段階的開示

SKILL.md本文からの動的参照パターン:

- **references/json-schema.md**: Element仕様、Styled Text、Positioning（現tech.mdの内容）
- **references/design-rules.md**: 60-30-10ルール、色パレット、height計算、lineGradient使用法
- **references/workflow-details.md**: Phase 1-3の詳細手順、チェックリスト

### FR-5: README.md の作成

deep-research の README.md に倣った人間向けドキュメント:
- 特徴
- 実行フロー図
- セットアップ手順（サブエージェント配置含む）
- ディレクトリ構成
- 使い方

## 非機能要件

### NFR-0: pptx_builder.py の複数JSON入力対応
```bash
python3 scripts/pptx_builder.py generate slide01.json slide02.json slide03.json -o output.pptx
```
- 複数JSONファイルを受け取り、slides配列を順番に結合して1つのPPTXを生成
- theme は最初のJSONから取得（または共通オプションで指定）

## 非機能要件（品質）

### NFR-1: SKILL.md 500行以下
sop-creator の推奨に従い、コアワークフローのみ。

### NFR-2: サブエージェントプロンプトの自己完結性
slide-builder-prompt.md は単独で動作可能（SKILL.mdを読まなくてもスライド構築できる）。

### NFR-3: 既存scripts/の非破壊
scripts/ は変更しない。examples/ はディレクトリ構造の再編のみ（内容は変更しない）。

### NFR-4: 後方互換
サブエージェントなしでも SKILL.md + references/ で従来通り動作可能。

## 成功基準

- [ ] SKILL.md が500行以下
- [ ] slide-builder サブエージェントが1スライド生成を完遂できる
- [ ] references/ への動的参照が機能する
- [ ] README.md でセットアップ〜使い方が完結する
