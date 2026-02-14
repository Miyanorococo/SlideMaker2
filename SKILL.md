---
name: pptx-maker
description: "Generate PowerPoint presentations from JSON. Use when user wants to create slides, proposals, or presentation materials."
---

# PPTX Maker

社内テンプレートを使用してPowerPointを生成するツール。
このファイル内のパスはすべてこのSKILL.mdからの相対パス。コマンド実行時はこのSKILL.mdのディレクトリに`cd`すること。

## スライド作成ワークフロー

### Phase 1: ナラティブ設計

スライドの構成ではなく、「何を伝えたいか」のストーリーを描く。
**このフェーズがスライドの質を決める。**

1. 資料作成対象について理解する
2. ペルソナ（誰向けか）、目的（何を達成したいか）、発表時間、テーマ（light/dark）を確認
   - 発表時間≠スライド枚数。枚数は情報量と見せ方で決まるので制限しない（段階的開示や紙芝居ではスライド数は多くなる）
3. ナラティブ（ストーリーライン）を作成してユーザーと合意する

ナラティブで書くこと：
- 聴衆に何を言いたいか、何を感じてほしいか、どう行動してほしいかを自然文で記述する
- セクションに分けて流れを整理する（ただしスライド枚数やレイアウトは決めない）
- Phase 2でナラティブを自由に解釈してスライドに落とし込む

**Constraints:**
- You MUST NOT skip to slide building without an agreed agenda

### Phase 2: 個別スライド作成

まずナラティブとexamplesを読み、スライド構成を設計する。
段階的な説明や繰り返しパターンにはoverride（継承）を活用する（スライド送りでアニメーション効果を実現できる）。

1枚ずつ以下を繰り返す：

1. このスライドで何を伝えたいか考える
2. `examples`コマンドでデザインパターンを複数参照し、いいとこ取りする
3. `icon-search`で必要なアイコンを確認
4. fs_writeでスライドを追加

**開始手順**:
```bash
uv run python3 scripts/pptx_builder.py init --theme dark
# → output_json, output_pptx のパスを以降のPhaseで使用する
```

**Constraints:**
- You MUST read before building the first slide:
  - [references/json-schema.md](references/json-schema.md)
  - [references/design-rules.md](references/design-rules.md)
  - 複数パターン（`python3 scripts/pptx_builder.py examples`）
- You MUST use fs_write to edit JSON
- You MUST NOT batch-generate multiple slides simultaneously
  because output truncation, coordinate errors, and breakage on edit
- You MUST NOT run generate until all slides are added to the JSON

### Phase 3: 生成と自動検査

generateコマンドはPPTX生成後にPowerPointのauto-fit計算を実行し、
テキストの可読性を自動検査する。

```bash
uv run python3 scripts/pptx_builder.py generate {output_json} -o {output_pptx}
```

**自動検査の出力:**
- `✅ Readability check: Pass` — 問題なし。Phase 4に進む。
- `⚠️ Readability check (N issues):` — テキストが小さくなりすぎている箇所がある。

**警告が出た場合の対処:**

| 警告タイプ | 意味 | 対処法 |
|-----------|------|--------|
| Text shrunk to Xpt | PowerPointがテキストを自動縮小した結果、最小フォントサイズ(10.5pt)を下回った | テキストを要約して短くする（最優先）。または height を拡張して下の要素も y をずらす |
| Shape extends to y=Npx | テキストボックスが自動拡張してスライド描画エリア(y=950px)を超えた | テキストを削減するか、スライドを2枚に分割する |

**自己修正ループ:**
1. 警告されたスライドのJSONを修正（テキスト要約 or レイアウト調整）
2. 再度 `generate` を実行
3. 警告がなくなるまで繰り返す（最大3回）

**よくある警告パターンと対処法:**

| パターン | 原因 | 対処 |
|---------|------|------|
| oval内テキスト縮小 | ovalは内部余白が大きい | width/height を 56px以上に |
| textbox height不足 | fontSize×3.5 未満の height | height拡大 or 省略（自動拡張） |
| 混合サイズテキスト縮小 | `{{16pt:...}}` が全体縮小に巻き込まれる | 混合サイズを避ける or コンテナ拡大 |
| テーブルセル切れ | auto-fit非対応 | Phase 4で目視確認（自動検知不可） |

**Constraints:**
- You MUST fix readability warnings before proceeding to Phase 4
- You MUST NOT reduce fontSize below design-rules.md minimums to fix warnings — shorten text instead

### Phase 2.5: textbox height 指定ルール（必須）

エージェントのpromptに以下を**必ず含める**:

- textbox には必ず height を指定すること。height なしの textbox は自動拡張して下の要素と重なる
- 1行: fontSize×3.5、複数行: 行数×fontSize×2.7、箇条書き: 項目数×fontSize×3.0 を目安に指定
- height 省略はスライド最下部の要素で下に他の要素がない場合のみ許可
- 関連するテキスト（タイトル+説明、価格+単位など）は1つの textbox にまとめ、\n で改行する

### Phase 4: デザインレビュー

完成PPTXのプレビューPNGを確認し、デザイン品質をレビューする。
Phase 3の自動検査では検知できない視覚的な問題をここで拾う。

```bash
uv run python3 scripts/pptx_builder.py preview {output_pptx} --no-grid
```

プレビュー画像をfs_readのImageモードで読み込み、
`references/design-review-guide.md` に従ってレビューする。

**自動検査でカバーされない項目（Phase 4で確認が必要）:**
- テーブルのセル内テキスト切れ（テーブルはauto-fitが効かないため）
- 要素間の意図しない重なり
- 色のコントラスト不足
- 整列のズレ
- 全体的なバランスと情報密度

**Constraints:**
- You MUST read ALL preview images before reporting
- You MUST check: わかりやすさ、レイアウト、テキスト、デザイン
- Pay special attention to TABLE cells — auto-fit does not apply to tables

### SWARM エージェント向け: バッチ検証手順

**重要**: エージェントは SKILL.md を自動で読まない。メインエージェントがこのセクションの手順を
エージェントの prompt に**直接含める**必要がある。prompt に含めないとバッチ検証はスキップされる。

**元資料の渡し方**: エージェントには**元資料のファイルパス**を渡し、エージェント自身に読ませること。リーダーが要約してプロンプトに書くのではなく、元資料への参照を渡す。要約は情報損失の主因となる。

SWARM並列化で個別スライドを担当するエージェントは、全スライド書き出し後に以下の検証を行うこと。

**手順:**
1. 担当スライドを全て書き出す（slide_XX.json）
2. 担当スライドを結合し、generate + preview で一括検証する:
```bash
python3 -c "
import json, glob
slides = []
for f in sorted(glob.glob('/path/to/slides/slide_*.json')):
    slides.append(json.load(open(f)))
json.dump({'theme':'dark','slides':slides}, open('/tmp/batch_check.json','w'), ensure_ascii=False)
"
uv run python3 scripts/pptx_builder.py generate /tmp/batch_check.json -o /tmp/batch_check.pptx
uv run python3 scripts/pptx_builder.py preview /tmp/batch_check.pptx --no-grid
```
3. generate 時の `⚠️ Readability check` 警告を確認。警告が出たらテキストを短くして再 generate
4. 生成されたプレビューPNGを **1枚ずつ** 読み込んでチェック:
   - テキストがボックスからはみ出していないか
   - 要素同士が重なっていないか
   - テーブルのセル内テキストが切れていないか
   - 情報密度が十分か（スカスカになっていないか）
5. 問題があるスライドのみJSONを修正し、再度バッチ生成+該当PNGのみ再確認
6. 全スライドOKを確認してから完了報告

**よくあるコンテナサイズの問題（promptに含める推奨）:**
- oval（楕円）にテキストを入れる場合: width/height を 56px以上にする（矩形より内部余白が大きい）
- textbox に height 指定時: fontSize×3.5（1行）/ 行数×fontSize×2.7（複数行）を目安に確保
- shape の text は常に自動縮小（TEXT_TO_FIT_SHAPE）。十分なサイズを確保する
- 混合フォントサイズ `{{16pt:...}}` は全体の縮小に巻き込まれるため注意

**Constraints:**
- You MUST run generate and check readability warnings before reporting completion
- You MUST fix all readability warnings before reporting completion
- You MUST visually check ALL preview PNGs (one at a time) before reporting completion

### Phase 5: 仕上げ & 微修正

レビュー結果やユーザーフィードバックに基づいてoutput_jsonを直接編集し、再生成する。

## CLI Commands

```bash
uv run python3 scripts/pptx_builder.py init --theme dark                    # 作業ディレクトリ初期化
uv run python3 scripts/pptx_builder.py generate slides.json -o output.pptx  # PPTX生成 + 可読性自動検査
uv run python3 scripts/pptx_builder.py preview output.pptx                  # プレビューPNG出力
uv run python3 scripts/pptx_builder.py icon-search "keyword"                # アイコン検索
uv run python3 scripts/pptx_builder.py icon-search "keyword" --type general # 一般アイコン検索
uv run python3 scripts/pptx_builder.py examples                             # パターン一覧
uv run python3 scripts/pptx_builder.py examples pattern-name                # パターン詳細+JSON
uv run python3 scripts/pptx_to_json.py input.pptx -o output.json            # PPTX→JSON逆変換
```
