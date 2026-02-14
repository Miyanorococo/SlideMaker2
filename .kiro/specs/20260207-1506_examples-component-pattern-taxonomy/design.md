# Design: examples体系の再設計

## 変更対象

### 1. frontmatter拡張
既存の frontmatter に `category` フィールドを追加：
```yaml
---
name: three-column-cards
description: 3カラムのカードレイアウト
category: pattern
---
```
- `category`: `component` | `pattern`（未指定時は `pattern` として扱う＝後方互換）

### 2. `_get_frontmatter_description` → 汎用frontmatterパーサーに変更
- description だけでなく category も取得できるようにする

### 3. `cmd_examples` の一覧表示をカテゴリ別グルーピング
出力イメージ：
```
# Design Examples

## Components
  kpi-card                 数値+ラベルのカード
  icon-with-desc           アイコン+説明文の縦組み

## Patterns
  three-column-cards       3カラムのカードレイアウト
  split-hero-bullets       左右分割レイアウト
```

### 4. 既存examplesに `category: pattern` 追加

### 5. 初期Componentの作成
以下を初期セットとして作成：
- `kpi-card` - 数値+ラベルのカード1枚
- `icon-with-desc` - アイコン+説明テキストの縦組み
- `flow-step` - ステップ間の矢印接続フロー
- `quote-block` - 引用ブロック
- `section-header-bar` - セクション内の小見出しバー

### 6. SKILL.md更新
Component/Patternの使い分け説明を追記

## Implementation Strategy
- Reusable: `_get_frontmatter_description`を拡張
- New: Component用markdownファイル

---
**Created**: 2026-02-07
