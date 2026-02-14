# Requirements: examples MD移行

## Background & Context
### User Problems
- 現状のexamplesはJSONのみで、デザインパターンの意図や調整方法が伝わらない
- AIエージェントがパターンを参照する際、なぜその値なのかを理解できない

### Related Issues
- `pptx_builder.py example` コマンドでJSONを標準出力している

## Objectives
- examplesをMarkdown形式に移行し、解説とJSONを1ファイルで管理
- YAML frontmatterで一覧表示時にdescriptionを表示

## Scope
### In Scope
- `examples/*.json` → `examples/*.md` への移行
- `cmd_examples()` のmd対応改修
- YAML frontmatter（name, description）の追加

### Out of Scope
- タグ/カテゴリ分類
- 新規パターンの追加

## Detailed Requirements
### frontmatter構造
```yaml
---
name: pattern-name
description: パターンの説明
---
```

### 一覧表示形式
```
# Design Patterns
# Path: /path/to/examples

  four-column-comparison    4つの選択肢を横並びで比較表示
  five-points-deepdive      5つのポイントを深掘り解説
```

### 移行対象
- four-column-comparison.json
- five-points-deepdive.json
- progressive-highlight.json

---
**Created**: 2026-02-04
