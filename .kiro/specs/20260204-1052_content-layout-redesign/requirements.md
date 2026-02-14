# Requirements: contentレイアウト再設計

## Background & Context
### User Problems
- 既存のcontentレイアウト（masterIndex=15）は本文エリアが固定で自由度が低い
- agendaレイアウトの背景（ダークブルー＋左ライン）は見た目が良く使いやすいが、本文エリアが固定

### Related Issues
- agendaの見た目で自由配置したいニーズがある

## Objectives
- contentレイアウトをagendaの見た目＋自由配置に変更
- 通常のスライド作成で使いやすいレイアウトを提供

## Scope
### In Scope
- contentレイアウトのmasterIndex変更（15→7）
- contentレイアウトの動作変更（title_onlyと同じ自由配置）
- tech.mdのドキュメント更新

### Out of Scope
- agendaレイアウトの変更
- title_onlyレイアウトの変更

## Detailed Requirements

| layout | masterIndex | ユースケース |
|--------|-------------|-------------|
| content（変更） | 7 | 通常のスライド作成。ダークブルー背景で統一感のある資料に |
| title_only（既存） | 9 | 画面全体を使いたい時。図解やダイアグラムの配置に |

---
**Created**: 2026-02-04
