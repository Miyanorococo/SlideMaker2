# Design: examples MD移行

## 実装方針
- 既存の `cmd_examples()` を最小限の変更でmd対応
- PyYAMLを使わず、シンプルな正規表現でfrontmatterをパース

## コード変更

### cmd_examples() 改修
```python
def cmd_examples(args):
    script_dir = Path(__file__).parent.parent
    examples_dir = script_dir / "examples"
    
    if not examples_dir.exists():
        print(f"Examples directory not found: {examples_dir}", file=sys.stderr)
        return
    
    # .json → .md
    patterns = sorted(f.stem for f in examples_dir.glob("*.md"))
    
    if args.names:
        for name in args.names:
            pattern_file = examples_dir / f"{name}.md"
            if not pattern_file.exists():
                print(f"# Pattern not found: {name}", file=sys.stderr)
                print(f"# Available: {', '.join(patterns)}", file=sys.stderr)
                continue
            print(f"# {pattern_file}")
            print(pattern_file.read_text())
            print()
    else:
        # 一覧表示（frontmatterからdescription取得）
        print("# Design Patterns")
        print(f"# Path: {examples_dir}")
        print()
        for name in patterns:
            desc = _get_frontmatter_description(examples_dir / f"{name}.md")
            print(f"  {name:<30} {desc}")

def _get_frontmatter_description(path: Path) -> str:
    """Extract description from YAML frontmatter."""
    import re
    content = path.read_text()
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        fm = match.group(1)
        desc_match = re.search(r'^description:\s*(.+)$', fm, re.MULTILINE)
        if desc_match:
            return desc_match.group(1).strip().strip('"\'')
    return ""
```

## MDファイル構造
```markdown
---
name: pattern-name
description: パターンの説明
---

# パターン名

## ユースケース
...

## デザインポイント
...

## JSON
```json
{...}
```　
```

---
**Created**: 2026-02-04
