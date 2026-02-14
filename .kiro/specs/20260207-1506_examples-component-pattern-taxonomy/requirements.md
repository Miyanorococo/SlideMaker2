# Requirements: examples体系の再設計（Component + Pattern 2層構造）

## Background & Context
### User Problems
- 現状のexamplesはスライド全体のレイアウトパターン（Pattern層）のみ
- パターンをそのまま使うときれいだがワンパターンになる
- エージェントが部品を組み合わせて応用する力が不足している

### Related Issues
- examplesの有無でスライドのクオリティが格段に変わるため、体系設計は重要

## Objectives
- Component（部品）+ Pattern（全体レイアウト）の2層構造を導入
- エージェントがComponentを組み合わせて多様なスライドを自作できるようにする

## Scope
### In Scope
- frontmatterへの `category: component | pattern` 追加
- 一覧表示のカテゴリ別グルーピング
- 既存examplesへのcategory付与
- 初期Componentの作成（数個）
- SKILL.mdへの使い分け説明追記

### Out of Scope
- 全Componentの網羅（段階的に追加）
- ディレクトリ構造の変更（examples/のまま）
- コマンドインターフェースの変更（--typeオプション等）

## Detailed Requirements
### Component層
- 再利用可能な部品単位のexample
- 1つのComponentは1つの役割（KPIカード、アイコン+説明、フロー矢印など）
- Patternの中でどう使われるかの文脈も記載

### Pattern層（既存）
- スライド全体のレイアウトパターン
- どのComponentを組み合わせているかを明示（応用のヒント）

### 一覧表示
- カテゴリ別にグルーピングして表示
- 既存コマンドの使い方は変わらない

---
**Created**: 2026-02-07
