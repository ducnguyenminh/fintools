"""
FinTools 使用例

このスクリプトは、FinToolsライブラリの基本的な使用方法を示します。
"""

import os
import sys

# パッケージのパスを追加（開発用）
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fintools.compound_interest import (  # noqa: E402
    annual_to_monthly_rate,
    compound_interest,
    continuous_compounding,
    effective_annual_rate,
    monthly_to_annual_rate,
    present_value,
)


def format_percentage(rate: float, decimal_places: int = 4) -> str:
    """利率を%表記でフォーマット"""
    return f"{rate * 100:.{decimal_places}f}%"


def format_currency(amount: float, currency: str = "¥") -> str:
    """金額を通貨表記でフォーマット"""
    return f"{currency}{amount:,.0f}"


def example_1_rate_conversion() -> None:
    """例1: 年利⇔月利変換"""
    print("=" * 50)
    print("例1: 年利⇔月利変換")
    print("=" * 50)

    # 年利5%を月利に変換
    annual_rate = 0.05
    monthly_rate = annual_to_monthly_rate(annual_rate)

    print(
        f"年利 {format_percentage(annual_rate, 2)}"
        f" → 月利 {format_percentage(monthly_rate, 4)}"
    )

    # 確認のため月利から年利に戻す
    back_to_annual = monthly_to_annual_rate(monthly_rate)
    print(
        f"月利 {format_percentage(monthly_rate, 4)}"
        f" → 年利 {format_percentage(back_to_annual, 2)}"
    )

    print(
        f"\n注意: 単純に12で割った場合の月利は"
        f" {format_percentage(annual_rate/12, 4)} となり、"
    )
    print("複利効果を考慮した実効月利とは異なります。")
    print()


def example_2_compound_interest() -> None:
    """例2: 複利計算比較"""
    print("=" * 50)
    print("例2: 複利計算（複利回数による違い）")
    print("=" * 50)

    principal = 1000000  # 100万円
    annual_rate = 0.05  # 年利5%
    years = 10  # 10年間

    print(f"元本: {format_currency(principal)}")
    print(f"年利: {format_percentage(annual_rate, 1)}")
    print(f"期間: {years}年\n")

    # 異なる複利回数での計算
    frequencies = [
        (1, "年1回（年次複利）"),
        (2, "年2回（半年複利）"),
        (4, "年4回（四半期複利）"),
        (12, "年12回（月次複利）"),
        (365, "年365回（日次複利）"),
    ]

    results = []
    for freq, description in frequencies:
        result = compound_interest(principal, annual_rate, years, freq)
        results.append((freq, result, description))
        print(
            f"{description:20}: {format_currency(result)}"
            f" (利息: {format_currency(result - principal)})"
        )

    # 連続複利
    continuous_result = continuous_compounding(principal, annual_rate, years)
    print(
        f"{'連続複利':20}: {format_currency(continuous_result)}"
        f" (利息: {format_currency(continuous_result - principal)})"
    )

    print("\n複利回数が多いほど将来価値が大きくなることがわかります。")
    print()


def example_3_investment_scenarios() -> None:
    """例3: 投資シナリオ比較"""
    print("=" * 50)
    print("例3: 投資シナリオ比較")
    print("=" * 50)

    principal = 1000000  # 100万円
    years = 20  # 20年間

    scenarios = [
        (0.02, "低リスク（年利2%）"),
        (0.05, "中リスク（年利5%）"),
        (0.08, "高リスク（年利8%）"),
    ]

    print(f"初期投資額: {format_currency(principal)}")
    print(f"投資期間: {years}年\n")

    for rate, description in scenarios:
        # 年次複利
        result_annual = compound_interest(principal, rate, years, 1)
        # 月次複利
        result_monthly = compound_interest(principal, rate, years, 12)

        print(f"{description}")
        print(
            f"  年次複利: {format_currency(result_annual)}"
            f" (利息: {format_currency(result_annual - principal)})"
        )
        print(
            f"  月次複利: {format_currency(result_monthly)}"
            f" (利息: {format_currency(result_monthly - principal)})"
        )
        print(f"  実効年利: {format_percentage(effective_annual_rate(rate, 12), 2)}")
        print()


def example_4_present_value() -> None:
    """例4: 現在価値計算"""
    print("=" * 50)
    print("例4: 現在価値計算")
    print("=" * 50)

    # 10年後に200万円欲しい場合、今いくら投資すれば良いか？
    target_amount = 2000000  # 200万円
    annual_rate = 0.05  # 年利5%
    years = 10  # 10年後

    required_investment = present_value(target_amount, annual_rate, years)

    print(f"目標金額: {format_currency(target_amount)}")
    print(f"年利: {format_percentage(annual_rate, 1)}")
    print(f"期間: {years}年")
    print(f"必要な初期投資額: {format_currency(required_investment)}")

    # 確認計算
    check_amount = compound_interest(required_investment, annual_rate, years)
    print(
        f"確認: {format_currency(required_investment)}"
        f" を年利{format_percentage(annual_rate, 1)}で{years}年運用すると"
    )
    print(f"      {format_currency(check_amount)} になります。")
    print()


def example_5_monthly_investment() -> None:
    """例5: 毎月積立投資シミュレーション"""
    print("=" * 50)
    print("例5: 毎月積立投資シミュレーション")
    print("=" * 50)

    monthly_investment = 50000  # 月5万円
    annual_rate = 0.06  # 年利6%
    years = 20  # 20年間

    # 毎月の実効利率
    monthly_rate = annual_to_monthly_rate(annual_rate)
    total_months = years * 12

    # 年金現価計算（毎月定額投資の場合）
    # PMT * [((1+r)^n - 1) / r] の公式を使用
    total_amount = monthly_investment * (
        ((1 + monthly_rate) ** total_months - 1) / monthly_rate
    )
    total_invested = monthly_investment * total_months
    total_return = total_amount - total_invested

    print(f"毎月の投資額: {format_currency(monthly_investment)}")
    print(f"年利: {format_percentage(annual_rate, 1)}")
    print(f"月利（実効）: {format_percentage(monthly_rate, 4)}")
    print(f"投資期間: {years}年（{total_months}回）")
    print()
    print(f"総投資額: {format_currency(total_invested)}")
    print(f"最終金額: {format_currency(total_amount)}")
    print(f"運用益: {format_currency(total_return)}")
    print(f"運用益率: {format_percentage(total_return / total_invested, 1)}")
    print()


def main() -> None:
    """メイン実行関数"""
    print("FinTools 使用例デモンストレーション")
    print("このスクリプトは、FinToolsライブラリの主要機能を紹介します。\n")

    # 各例を実行
    example_1_rate_conversion()
    example_2_compound_interest()
    example_3_investment_scenarios()
    example_4_present_value()
    example_5_monthly_investment()

    print("=" * 50)
    print("デモンストレーション終了")
    print("=" * 50)
    print("詳細な使用方法については、READMEやドキュメントを参照してください。")


if __name__ == "__main__":
    main()
