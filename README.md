# CPU_simu

CPU_simuは、ExcelベースのCPU命令セット定義をJSONデータベースに読み込み、ROM命令を実行して簡易CPU動作をシミュレーションするPythonツールです。

## 概要

- `main.py` の `read_settings` コマンドでExcelから命令設定を読み込む
- `main.py` の `run` コマンドでROMファイルを実行し、レジスタの状態を出力する
- `commands.yml` に記述された命令名と式を使ってCPU命令を評価する
- `ROM/ROM.txt` に書かれたビット列（2進数）を命令として読み取り実行する

## 主要機能

- Excelファイルから命令セットを読み込み、`databases/<CPU名>.json` に登録
- 読み込んだ命令セットを用いてROMをステップ実行
- `rich` を使ってデバッグ情報を見やすく表示
- ROMファイルが存在しない場合は自動で `ROM/ROM.txt` を作成

## 依存関係

- Python 3.12+
- pandas
- openpyxl
- pyyaml
- rich
- typer
- ruff

これらは `pyproject.toml` の `dependencies` に記載されています。

## インストール

```bash
python -m pip install -e .
```

または直接依存関係をインストールする場合:

```bash
python -m pip install pandas openpyxl pyyaml rich typer ruff
```

## 使い方

### 1. Excelから命令セットを読み込む

```bash
python main.py read_settings path/to/your_instructions.xlsx --bit 4
```

- `path`: Excelファイルのパス
- `--bit`: ROM上の命令ビット数（デフォルトは `4`）
- `--register`: CPU設定をデータベースに保存するかどうか（デフォルトは `True`）

### 2. ROMを実行する

```bash
python main.py run <CPU名> --path ROM/ROM.txt --debug true
```

- `<CPU名>`: `read_settings` により保存された `databases/<CPU名>.json` の名前
- `--path`: ROMファイルのパス（デフォルトは `ROM/ROM.txt`）
- `--debug`: 実行中の詳細表示を有効にするかどうか

## ファイル構成

- `main.py`: CLIエントリポイント
- `pyproject.toml`: プロジェクト設定と依存関係
- `commands.yml`: 命令名と計算式の対応定義
- `ROM/ROM.txt`: 実行対象のROMデータ
- `databases/`: CPU設定JSONデータを保存するフォルダ
- `modules/initialize.py`: 初期化処理
- `modules/dataframe.py`: ExcelからJSONへの変換処理
- `modules/run.py`: ROM実行ロジック
- `tools/search_command.py`: 命令名のあいまい検索処理
- `tools/file_manager.py`: ファイル生成・状態確認ユーティリティ

## 注意点

- `commands.yml` の命令名と `Excel` の命令名が一致しない場合、命令を解決できないことがあります
- ROMファイルは1行ごとに命令ビット列をスペース区切りで記述します
- 命令の演算は Python の `eval` で評価されるため、式内容には注意してください

## 例

`commands.yml` の例:

```yaml
commands:
  インクリメント: a + 1
  デクリメント: a - b
  無条件ジャンプ: null
```

`ROM/ROM.txt` の例:

```text
0001 0001 0000 0001
```
