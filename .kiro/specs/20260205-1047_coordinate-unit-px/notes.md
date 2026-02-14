# Notes: 座標単位を%からpxに変更

Guidelines:
- **Append-only**: Never edit existing content
- **Capture thought process**: "Initially thought X, but actually Y"
- **Be specific**: Include errors, commands, numbers

## Log

### [2026-02-05 10:47] SPEC作成

ヒアリングで決定した内容:
- 問題: %指定は縦横比の違いにより同じ%でも長さが異なる
- 解決策: px（1920x1080基準）に統一
- マイグレーション: 使い捨てスクリプトで対応

検討した代替案:
- 横幅基準%に統一 → 「y:50が中央でなくなる」等、新しい概念導入で複雑化
- EMU直接指定 → 数値が巨大で扱いにくい
- aspect-ratio対応 → 場当たり的

pxを選んだ理由:
- 普遍的な単位、説明不要
- 正方形 = 同じ数値
- Figma等のデザインツールと親和性

---
**Created**: 2026-02-05
