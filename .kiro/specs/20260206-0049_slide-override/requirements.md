# Requirements: Slide Override

## Background & Context

### User Problems
- プレゼンで同じ図を使いながら「段階的開示」や「強調箇所の変更」をしたい
- 現状は同じスライドをコピペして微修正する必要があり、ベース変更時に全派生スライドを手動更新する必要がある

### Use Cases
1. **アジェンダのセクションハイライト**: 進行に合わせて現在セクションをアクセントカラーで強調
2. **段階的開示（Progressive Disclosure）**: 複雑な図を段階的に見せる（白矩形で隠す→順次表示）
3. **紙芝居的な強調枠**: 同じ図に対して「ここに注目」の枠線を重ねる

## Objectives

- スライドの継承・オーバーライド機能により、差分のみの記述で派生スライドを生成
- ベーススライド変更時に全派生スライドへ自動反映

## Scope

### In Scope
- `id`キーによるスライド識別
- `override`キーによる継承元指定
- override側のelementsをベースの上に追加（z-index上位）

### Out of Scope
- title/notes/layoutの継承（override側で完全制御）
- ベースelementsの削除・変更
- ベーススライドの出力抑制オプション（将来検討）

## Detailed Requirements

### JSON Schema拡張

```json
// ベーススライド（id指定）
{
  "id": "agenda-base",
  "layout": "content",
  "title": "Agenda",
  "elements": [...]
}

// 派生スライド（override指定）
{
  "override": "agenda-base",
  "elements": [
    {"type": "textbox", "text": "{{#FF9900:Section 1}}", ...}
  ]
}
```

### 処理仕様
1. `id`を持つスライドは通常通り出力
2. `override`を持つスライドは、指定idのelementsをコピーし、その上にoverride側のelementsを追加
3. title/notes/layoutは継承しない（override側で指定がなければ空/デフォルト）

### 制約
- `id`は全スライドでユニーク
- 存在しない`id`へのoverrideはエラー
- 循環参照は禁止（override先がさらにoverrideを持つ場合も解決するが、循環はエラー）

---
**Created**: 2026-02-06
