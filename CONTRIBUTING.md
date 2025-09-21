# FinToolsへの貢献

FinToolsプロジェクトへの貢献を歓迎します！このドキュメントでは、プロジェクトに貢献する方法について説明します。

## 貢献の方法

### Issues（問題報告・機能要求）

- バグを発見した場合や新機能のアイデアがある場合は、[Issues](https://github.com/aozk/fintools/issues)で報告してください
- 既存のIssueを確認して、重複を避けてください
- 明確で詳細な説明を提供してください

### Pull Requests（プルリクエスト）

1. **フォーク**: リポジトリをフォークしてください
2. **ブランチ作成**: 機能ブランチを作成してください (`git checkout -b feature/amazing-feature`)
3. **変更**: 変更を加えてください
4. **テスト**: テストを追加・実行してください
5. **コミット**: 変更をコミットしてください (`git commit -m 'Add amazing feature'`)
6. **プッシュ**: ブランチにプッシュしてください (`git push origin feature/amazing-feature`)
7. **プルリクエスト**: プルリクエストを作成してください

## 開発環境のセットアップ

### 必要なソフトウェア

- Python 3.8以上
- Git

### セットアップ手順

```bash
# リポジトリをクローン
git clone https://github.com/aozk/fintools.git
cd fintools

# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 開発依存関係をインストール
pip install -r requirements-dev.txt

# パッケージを開発モードでインストール
pip install -e .
```

## コーディング規約

### Pythonコーディングスタイル

- [PEP 8](https://pep8.org/)に従ってください
- [Black](https://black.readthedocs.io/)でコードフォーマットを行ってください
- [flake8](https://flake8.pycqa.org/)でリンターチェックを行ってください
- [mypy](https://mypy.readthedocs.io/)で型チェックを行ってください

### コードフォーマット

```bash
# Black でフォーマット
black src/ tests/

# flake8 でリンターチェック
flake8 src/ tests/

# mypy で型チェック
mypy src/
```

## テスト

### テストの実行

```bash
# すべてのテストを実行
pytest

# カバレッジ付きでテストを実行
pytest --cov=fintools

# 特定のテストファイルを実行
pytest tests/test_compound_interest.py
```

### テストの書き方

- すべての新機能に対してテストを書いてください
- テストファイルは `tests/` ディレクトリに配置してください
- テストファイル名は `test_*.py` の形式にしてください
- テスト関数名は `test_*` の形式にしてください

例:
```python
def test_annual_to_monthly_rate():
    """年利から月利への変換テスト"""
    annual_rate = 0.12  # 12%
    expected_monthly = 0.009488792934582118  # 約0.949%
    result = annual_to_monthly_rate(annual_rate)
    assert abs(result - expected_monthly) < 1e-10
```

## ドキュメント

- 新機能にはdocstringを追加してください
- READMEを更新してください（必要に応じて）
- 型ヒントを使用してください

例:
```python
def compound_interest(
    principal: float,
    annual_rate: float,
    years: int,
    compounding_frequency: int = 1
) -> float:
    """
    複利計算を行います。

    Args:
        principal: 元本
        annual_rate: 年利（小数表記、例：0.05 = 5%）
        years: 投資期間（年）
        compounding_frequency: 年間複利回数（デフォルト：1）

    Returns:
        複利計算後の金額

    Examples:
        >>> compound_interest(1000000, 0.05, 10)
        1628894.6267749023
    """
```

## コミットメッセージ

明確で説明的なコミットメッセージを書いてください：

```
feat: 複利計算に月次複利オプションを追加

- monthly_compound_interest関数を追加
- 月次複利計算のテストを追加
- READMEに使用例を追加
```

## Issue とプルリクエストのテンプレート

### バグレポート

```markdown
## バグの説明
バグの明確で簡潔な説明

## 再現手順
1. '...'に移動
2. '...'をクリック
3. '...'までスクロール
4. エラーを確認

## 期待される動作
何が起こるべきかの明確で簡潔な説明

## 実際の動作
実際に何が起こったかの説明

## 環境
- OS: [例: Windows 10, macOS Big Sur, Ubuntu 20.04]
- Python バージョン: [例: 3.9.5]
- fintools バージョン: [例: 0.1.0]
```

### 機能要求

```markdown
## 機能の説明
提案する機能の明確で簡潔な説明

## 動機
この機能が必要な理由を説明してください

## 提案する解決策
実装したい機能の明確で簡潔な説明

## 代替案
検討した代替解決策や機能の説明
```

## プルリクエストのチェックリスト

- [ ] コードはPEP 8に準拠している
- [ ] テストが追加されており、すべて通過している
- [ ] ドキュメントが更新されている（必要に応じて）
- [ ] 変更がREADMEに記載されている（必要に応じて）
- [ ] 型ヒントが追加されている
- [ ] コミットメッセージが明確である

## 質問やヘルプ

質問がある場合は、以下の方法でお気軽にお問い合わせください：

- [Issues](https://github.com/your-username/fintools/issues)で質問を投稿
- [Discussions](https://github.com/your-username/fintools/discussions)で議論を開始

## ライセンス

貢献することで、あなたの貢献が [MIT License](LICENSE) の下でライセンスされることに同意するものとします。
