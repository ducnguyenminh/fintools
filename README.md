# FinTools 📊

[![CI/CD Pipeline](https://github.com/aozk/fintools/actions/workflows/ci.yml/badge.svg)](https://github.com/aozk/fintools/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/aozk/fintools/branch/main/graph/badge.svg)](https://codecov.io/gh/aozk/fintools)
[![PyPI version](https://badge.fury.io/py/fintools.svg)](https://badge.fury.io/py/fintools)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

金融計算に特化したPythonツールライブラリです。複利計算、利回り計算、投資リターン分析など、金融関連の計算を簡単に行うことができます。

## 特徴

- 🧮 複利計算ツール（年利→月利変換）
- 📈 投資リターン分析
- 💰 金融計算の実用的なユーティリティ
- 🐍 Pure Python実装
- 📖 充実したドキュメントと使用例

## インストール

```bash
# GitHubから直接インストール
pip install git+https://github.com/aozk/fintools.git

# または、ソースコードをクローンしてインストール
git clone https://github.com/aozk/fintools.git
cd fintools
pip install -e .
```

## 使用方法

### 複利計算ツール

年利から月利への変換を行います：

```python
from fintools.compound_interest import annual_to_monthly_rate

# 年利5%を月利に変換
annual_rate = 0.05  # 5%
monthly_rate = annual_to_monthly_rate(annual_rate)
print(f"年利 {annual_rate*100:.2f}% → 月利 {monthly_rate*100:.4f}%")
```

### 基本的な複利計算

```python
from fintools.compound_interest import compound_interest

# 初期投資額100万円、年利5%、10年間の複利計算
principal = 1000000  # 100万円
rate = 0.05         # 年利5%
years = 10          # 10年間

final_amount = compound_interest(principal, rate, years)
print(f"10年後の元利合計: {final_amount:,.0f}円")
```

## API リファレンス

### `compound_interest` モジュール

#### `annual_to_monthly_rate(annual_rate)`
年利を月利に変換します。

**パラメータ:**
- `annual_rate` (float): 年利（小数表記、例：0.05 = 5%）

**戻り値:**
- float: 月利（小数表記）

#### `compound_interest(principal, annual_rate, years, compounding_frequency=1)`
複利計算を行います。

**パラメータ:**
- `principal` (float): 元本
- `annual_rate` (float): 年利（小数表記）
- `years` (int): 投資期間（年）
- `compounding_frequency` (int): 年間複利回数（デフォルト：1）

**戻り値:**
- float: 複利計算後の金額

## 開発について

### 開発環境のセットアップ

```bash
# リポジトリをクローン
git clone https://github.com/your-username/fintools.git
cd fintools

# 仮想環境を作成
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate

# 開発依存関係をインストール
pip install -r requirements-dev.txt
```

### テストの実行

```bash
# すべてのテストを実行
python -m pytest

# カバレッジ付きでテストを実行
python -m pytest --cov=fintools
```

## 貢献について

プロジェクトへの貢献を歓迎します！詳細については [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。

## 作者

- aozk - [@aozk](https://github.com/aozk)

## 謝辞

- 金融計算のアルゴリズムについて参考にした資料やライブラリがあれば記載

## 今後の予定

- [ ] 投資ポートフォリオ分析ツール
- [ ] リスク計算機能
- [ ] 税金計算ユーティリティ
- [ ] Webインターフェースの追加
- [ ] より多くの金融指標の計算機能

---

⭐ このプロジェクトが役に立ったら、ぜひスターをつけてください！