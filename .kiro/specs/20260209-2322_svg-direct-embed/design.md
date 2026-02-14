# Design: SVG直接埋め込み

## 新規関数
- `add_svg_to_slide(slide, svg_path, x, y, width, height, icon_color=None)` - SVGをOpenXML経由で直接埋め込み
- `get_svg_dimensions(svg_path)` - viewBoxからアスペクト比を取得

## 変更関数
- `PPTXBuilder._add_image()` - SVGの場合は `add_svg_to_slide` を呼ぶ分岐を追加
- `_recolor_svg()` - 既存のまま流用（lxmlベース、cairosvg非依存）

## 削除
- `convert_to_png_if_needed()` - 不要
- `cairosvg` import箇所すべて
- `ICON_CACHE_DIR` 関連（PNGキャッシュ不要）
- `scripts/poc_svg_direct.py` - PoC完了

## 更新ファイル
- `scripts/pptx_builder.py` - 上記変更
- `pyproject.toml` - cairosvg削除
- `references/setup.md` - cairo記載削除
- `README.md` - cairo前提条件削除
- `.kiro/steering/tech.md` - cairosvg削除

## SVG埋め込みのOpenXML構造
```xml
<p:pic>
  <p:blipFill>
    <a:blip r:embed="{rId}">
      <a:extLst>
        <a:ext uri="{96DAC541-7B7A-43D3-8B79-37D633B846F1}">
          <asvg:svgBlip r:embed="{rId}"/>
        </a:ext>
      </a:extLst>
    </a:blip>
  </p:blipFill>
</p:pic>
```

---
**Created**: 2026-02-09
