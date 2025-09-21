"""
複利計算モジュール

このモジュールは複利計算、年利⇔月利変換、将来価値・現在価値計算などの
金融計算機能を提供します。
"""

import math
from typing import Union


def annual_to_monthly_rate(annual_rate: float) -> float:
    """
    年利を実効月利に変換します。

    複利効果を考慮して、年利から等価な月利を計算します。
    単純に12で割るのではなく、(1 + 年利)^(1/12) - 1 で計算します。

    Args:
        annual_rate: 年利（小数表記、例：0.05 = 5%）

    Returns:
        月利（小数表記）

    Raises:
        ValueError: 年利が負の値の場合

    Examples:
        >>> annual_to_monthly_rate(0.05)  # 年利5%
        0.004074124340267653
        >>> annual_to_monthly_rate(0.12)  # 年利12%
        0.009488792934582118
    """
    if annual_rate < 0:
        raise ValueError("年利は0以上である必要があります")

    return (1 + annual_rate) ** (1 / 12) - 1


def monthly_to_annual_rate(monthly_rate: float) -> float:
    """
    月利を実効年利に変換します。

    複利効果を考慮して、月利から等価な年利を計算します。
    (1 + 月利)^12 - 1 で計算します。

    Args:
        monthly_rate: 月利（小数表記、例：0.004 = 0.4%）

    Returns:
        年利（小数表記）

    Raises:
        ValueError: 月利が負の値の場合

    Examples:
        >>> monthly_to_annual_rate(0.004074124340267653)  # 月利約0.407%
        0.049999999999999906
        >>> monthly_to_annual_rate(0.01)  # 月利1%
        0.12682503013196972
    """
    if monthly_rate < 0:
        raise ValueError("月利は0以上である必要があります")

    return (1 + monthly_rate) ** 12 - 1


def compound_interest(
    principal: float,
    annual_rate: float,
    years: Union[int, float],
    compounding_frequency: int = 1,
) -> float:
    """
    複利計算を行います。

    元本、年利、期間、複利回数から将来価値を計算します。
    公式: FV = PV * (1 + r/n)^(n*t)

    Args:
        principal: 元本
        annual_rate: 年利（小数表記、例：0.05 = 5%）
        years: 投資期間（年）
        compounding_frequency: 年間複利回数（デフォルト：1）
            1: 年1回, 2: 半年1回, 4: 四半期1回, 12: 月1回, 365: 日1回

    Returns:
        複利計算後の将来価値

    Raises:
        ValueError: 負の値が入力された場合

    Examples:
        >>> compound_interest(1000000, 0.05, 10)  # 100万円、年利5%、10年
        1628894.6267749023
        >>> compound_interest(1000000, 0.05, 10, 12)  # 月次複利
        1643619.463481218
    """
    if principal < 0:
        raise ValueError("元本は0以上である必要があります")
    if annual_rate < 0:
        raise ValueError("年利は0以上である必要があります")
    if years < 0:
        raise ValueError("期間は0以上である必要があります")
    if compounding_frequency <= 0:
        raise ValueError("複利回数は1以上である必要があります")

    rate_per_period = annual_rate / compounding_frequency
    total_periods = compounding_frequency * years

    return principal * (1 + rate_per_period) ** total_periods


def future_value(
    principal: float,
    annual_rate: float,
    years: Union[int, float],
    compounding_frequency: int = 1,
) -> float:
    """
    将来価値を計算します（compound_interestのエイリアス）。

    Args:
        principal: 現在価値（元本）
        annual_rate: 年利（小数表記）
        years: 期間（年）
        compounding_frequency: 年間複利回数（デフォルト：1）

    Returns:
        将来価値
    """
    return compound_interest(principal, annual_rate, years, compounding_frequency)


def present_value(
    future_value_amount: float,
    annual_rate: float,
    years: Union[int, float],
    compounding_frequency: int = 1,
) -> float:
    """
    現在価値を計算します。

    将来の価値から、現在の等価な価値を計算します。
    公式: PV = FV / (1 + r/n)^(n*t)

    Args:
        future_value_amount: 将来価値
        annual_rate: 年利（小数表記、例：0.05 = 5%）
        years: 期間（年）
        compounding_frequency: 年間複利回数（デフォルト：1）

    Returns:
        現在価値

    Raises:
        ValueError: 負の値が入力された場合

    Examples:
        >>> present_value(1628894.63, 0.05, 10)  # 10年後の162万円の現在価値
        1000000.0000061395
        >>> present_value(2000000, 0.03, 5, 12)  # 月次複利での現在価値
        1725518.1320751005
    """
    if future_value_amount < 0:
        raise ValueError("将来価値は0以上である必要があります")
    if annual_rate < 0:
        raise ValueError("年利は0以上である必要があります")
    if years < 0:
        raise ValueError("期間は0以上である必要があります")
    if compounding_frequency <= 0:
        raise ValueError("複利回数は1以上である必要があります")

    rate_per_period = annual_rate / compounding_frequency
    total_periods = compounding_frequency * years

    return future_value_amount / (1 + rate_per_period) ** total_periods


def effective_annual_rate(
    nominal_annual_rate: float, compounding_frequency: int
) -> float:
    """
    名目年利から実効年利を計算します。

    複利回数を考慮して、名目年利から実際の年利を計算します。
    公式: EAR = (1 + r/n)^n - 1

    Args:
        nominal_annual_rate: 名目年利（小数表記）
        compounding_frequency: 年間複利回数

    Returns:
        実効年利（小数表記）

    Examples:
        >>> effective_annual_rate(0.05, 12)  # 名目5%、月次複利
        0.05116189788173683
        >>> effective_annual_rate(0.1, 365)  # 名目10%、日次複利
        0.10515578161654986
    """
    if nominal_annual_rate < 0:
        raise ValueError("名目年利は0以上である必要があります")
    if compounding_frequency <= 0:
        raise ValueError("複利回数は1以上である必要があります")

    return (
        1 + nominal_annual_rate / compounding_frequency
    ) ** compounding_frequency - 1


def continuous_compounding(
    principal: float, annual_rate: float, years: Union[int, float]
) -> float:
    """
    連続複利計算を行います。

    公式: FV = PV * e^(r*t)

    Args:
        principal: 元本
        annual_rate: 年利（小数表記）
        years: 期間（年）

    Returns:
        連続複利での将来価値

    Examples:
        >>> continuous_compounding(1000000, 0.05, 10)
        1648721.270700128
    """
    if principal < 0:
        raise ValueError("元本は0以上である必要があります")
    if annual_rate < 0:
        raise ValueError("年利は0以上である必要があります")
    if years < 0:
        raise ValueError("期間は0以上である必要があります")

    return principal * math.exp(annual_rate * years)
