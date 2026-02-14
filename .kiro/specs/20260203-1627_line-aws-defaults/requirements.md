# Requirements: line要素のAWS推奨デフォルト値

## Background & Context
### User Problems
- アーキテクチャ図を作成する際、毎回色や線幅を指定する必要がある
- AWS公式の推奨スタイルに合わせたい

### Related Issues
- aws-icons-raycastプロジェクトで使用しているAWS推奨矢印スタイルを参考

## Objectives
- line要素のデフォルト値をAWS推奨スタイルに変更
- SKILL.mdにアーキテクチャ図の推奨パターンを記載

## Scope
### In Scope
- line要素のデフォルト色・線幅の変更
- SKILL.md / tech.mdの更新

### Out of Scope
- `type: "arrow"`の新規追加（lineで対応可能）

## Detailed Requirements
### AWS推奨デフォルト値
| 設定 | Light | Dark |
|------|-------|------|
| color | `#000000` | `#8FA7C4` |
| lineWidth | `1.25` | `1.25` |

### 矢印の指定
tailEnd/headEndは明示的に指定（デフォルト変更なし）
```json
{"type": "line", "tailEnd": "arrow"}
```

---
**Created**: 2026-02-03
