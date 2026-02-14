# Design: 座標単位を%からpxに変更

## 変換定数

```python
SLIDE_WIDTH = 12192000   # EMU
SLIDE_HEIGHT = 6858000   # EMU
PX_WIDTH = 1920
PX_HEIGHT = 1080
EMU_PER_PX = 6350        # 12192000 / 1920 = 6858000 / 1080
```

## API Design

### pptx_builder.py

```python
# Before
def _pct_to_emu(self, value, is_width=True):
    base = self.SLIDE_WIDTH if is_width else self.SLIDE_HEIGHT
    return Emu(int(base * value / 100))

# After
def _px_to_emu(self, px):
    return Emu(int(px * 6350))
```

- `is_width` パラメータ不要になる（縦横同じ変換）
- 全呼び出し箇所を `_px_to_emu()` に置換

### pptx_to_json.py

```python
# Before
"x": round(shape.left * 100 / 12192000, 1)
"y": round(shape.top * 100 / 6858000, 1)

# After
"x": round(shape.left / 6350)
"y": round(shape.top / 6350)
```

## Components

### 変更対象ファイル

| ファイル | 変更内容 |
|---------|---------|
| scripts/pptx_builder.py | `_pct_to_emu` → `_px_to_emu`、呼び出し箇所修正 |
| scripts/pptx_to_json.py | EMU→px変換式を修正 |
| .kiro/steering/tech.md | 座標仕様をpxに更新 |
| SKILL.md | 座標仕様をpxに更新（存在すれば） |

### マイグレーション対象

| ファイル | 形式 |
|---------|------|
| demo.json | JSON |
| showcase.json | JSON |
| examples/*.md | Markdown内のJSONブロック |

## Implementation Strategy

### 新規作成
- `scripts/migrate_pct_to_px.py`: 使い捨てマイグレーションスクリプト

### 修正
- `scripts/pptx_builder.py`: 変換関数と呼び出し箇所
- `scripts/pptx_to_json.py`: 逆変換式
- ドキュメント類

---
**Created**: 2026-02-05
