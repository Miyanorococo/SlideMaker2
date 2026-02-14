# Design: icon-search manifest活用改善

## Implementation Strategy

### manifest読み込み
```python
MANIFEST_PATH = ICON_DIR.parent / "manifest.json"

def load_manifest():
    with open(MANIFEST_PATH) as f:
        return json.load(f)["icons"]
```

### 検索ロジック
- name(小文字)にクエリが含まれるかチェック
- `--type`指定時はtypeでフィルタ
- スコア: 名前が短いほど優先（現行維持）

### 出力形式
```
# lambda
  AWS Lambda [Compute/service]                      (w:10%, h:10.0%)
  AWS Lambda Lambda Function [Compute/resource]    (w:10%, h:10.0%)
```

---
**Created**: 2026-02-04
