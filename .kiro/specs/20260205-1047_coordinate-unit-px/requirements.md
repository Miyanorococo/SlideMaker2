# Requirements: 座標単位を%からpxに変更

## Background & Context

### User Problems
- 現在の%指定は縦横で基準が異なる（横1%=121,920 EMU、縦1%=68,580 EMU）
- `width: 10, height: 10` が正方形にならない
- 同じ%でも縦横で実際の長さが約1.78倍異なる

### 根本原因
- スライドが16:9（12192000 x 6858000 EMU）のため、縦横の1%が異なる長さになる

## Objectives

- 座標・サイズ指定をpx（1920x1080基準）に統一
- 同じ数値で正方形が作れるようにする
- 普遍的な単位で直感的に扱えるようにする

## Scope

### In Scope
- pptx_builder.py: `_pct_to_emu()` → `_px_to_emu()` 変換
- pptx_to_json.py: EMU → px 逆変換
- examples/*.md: JSON内の座標をpxに変換
- demo.json, showcase.json: 座標をpxに変換
- tech.md, SKILL.md: ドキュメント更新
- マイグレーション用スクリプト（使い捨て）

### Out of Scope
- 後方互換性（%指定のサポート継続）
- 単位の自動判定

## Detailed Requirements

### 変換仕様
```
1920px = 12192000 EMU（横）
1080px = 6858000 EMU（縦）

x_emu = x_px * 12192000 / 1920 = x_px * 6350
y_emu = y_px * 6858000 / 1080 = y_px * 6350
```

### JSON形式
```json
{
  "x": 100,      // px (0-1920)
  "y": 100,      // px (0-1080)
  "width": 200,  // px
  "height": 200  // px → 正方形
}
```

### マイグレーション
```
x_px = x_pct * 1920 / 100
y_px = y_pct * 1080 / 100
width_px = width_pct * 1920 / 100
height_px = height_pct * 1080 / 100
```

---
**Created**: 2026-02-05
