"""
複利計算モジュールのテスト
"""

import pytest
import math
from fintools.compound_interest import (
    annual_to_monthly_rate,
    monthly_to_annual_rate,
    compound_interest,
    future_value,
    present_value,
    effective_annual_rate,
    continuous_compounding,
)


class TestAnnualToMonthlyRate:
    """年利から月利への変換テスト"""

    def test_annual_to_monthly_rate_basic(self):
        """基本的な年利から月利への変換"""
        # 年利12%の場合
        annual_rate = 0.12
        expected_monthly = (1.12 ** (1/12)) - 1
        result = annual_to_monthly_rate(annual_rate)
        assert abs(result - expected_monthly) < 1e-10

    def test_annual_to_monthly_rate_zero(self):
        """年利0%の場合"""
        result = annual_to_monthly_rate(0.0)
        assert result == 0.0

    def test_annual_to_monthly_rate_small(self):
        """小さな年利の場合"""
        annual_rate = 0.01  # 1%
        result = annual_to_monthly_rate(annual_rate)
        assert 0 < result < annual_rate / 12

    def test_annual_to_monthly_rate_negative(self):
        """負の年利でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            annual_to_monthly_rate(-0.05)


class TestMonthlyToAnnualRate:
    """月利から年利への変換テスト"""

    def test_monthly_to_annual_rate_basic(self):
        """基本的な月利から年利への変換"""
        # 月利1%の場合
        monthly_rate = 0.01
        expected_annual = (1.01 ** 12) - 1
        result = monthly_to_annual_rate(monthly_rate)
        assert abs(result - expected_annual) < 1e-10

    def test_monthly_to_annual_rate_zero(self):
        """月利0%の場合"""
        result = monthly_to_annual_rate(0.0)
        assert result == 0.0

    def test_monthly_to_annual_rate_negative(self):
        """負の月利でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            monthly_to_annual_rate(-0.01)

    def test_roundtrip_conversion(self):
        """年利→月利→年利の変換で元に戻ることを確認"""
        original_annual = 0.05
        monthly = annual_to_monthly_rate(original_annual)
        back_to_annual = monthly_to_annual_rate(monthly)
        assert abs(back_to_annual - original_annual) < 1e-10


class TestCompoundInterest:
    """複利計算テスト"""

    def test_compound_interest_annual(self):
        """年次複利計算"""
        principal = 1000000
        annual_rate = 0.05
        years = 10
        
        expected = principal * (1.05 ** 10)
        result = compound_interest(principal, annual_rate, years)
        assert abs(result - expected) < 1e-6

    def test_compound_interest_monthly(self):
        """月次複利計算"""
        principal = 1000000
        annual_rate = 0.12
        years = 5
        frequency = 12
        
        expected = principal * (1 + 0.12/12) ** (12 * 5)
        result = compound_interest(principal, annual_rate, years, frequency)
        assert abs(result - expected) < 1e-6

    def test_compound_interest_zero_rate(self):
        """利率0%の場合"""
        principal = 1000000
        result = compound_interest(principal, 0.0, 10)
        assert result == principal

    def test_compound_interest_zero_years(self):
        """期間0年の場合"""
        principal = 1000000
        result = compound_interest(principal, 0.05, 0)
        assert result == principal

    def test_compound_interest_negative_principal(self):
        """負の元本でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            compound_interest(-1000000, 0.05, 10)

    def test_compound_interest_negative_rate(self):
        """負の利率でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            compound_interest(1000000, -0.05, 10)

    def test_compound_interest_negative_years(self):
        """負の期間でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            compound_interest(1000000, 0.05, -10)

    def test_compound_interest_zero_frequency(self):
        """複利回数0でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            compound_interest(1000000, 0.05, 10, 0)


class TestFutureValue:
    """将来価値計算テスト"""

    def test_future_value_equals_compound_interest(self):
        """future_valueがcompound_interestと同じ結果を返すことを確認"""
        principal = 1000000
        annual_rate = 0.05
        years = 10
        frequency = 4
        
        result1 = future_value(principal, annual_rate, years, frequency)
        result2 = compound_interest(principal, annual_rate, years, frequency)
        assert result1 == result2


class TestPresentValue:
    """現在価値計算テスト"""

    def test_present_value_basic(self):
        """基本的な現在価値計算"""
        future_val = 1628894.63
        annual_rate = 0.05
        years = 10
        
        result = present_value(future_val, annual_rate, years)
        # 複利計算の逆なので、元本に近い値になることを確認
        assert abs(result - 1000000) < 1

    def test_present_value_roundtrip(self):
        """現在価値→将来価値→現在価値で元に戻ることを確認"""
        original_pv = 1000000
        annual_rate = 0.05
        years = 10
        
        fv = compound_interest(original_pv, annual_rate, years)
        back_to_pv = present_value(fv, annual_rate, years)
        assert abs(back_to_pv - original_pv) < 1e-6

    def test_present_value_negative_future_value(self):
        """負の将来価値でエラーが発生することを確認"""
        with pytest.raises(ValueError):
            present_value(-1000000, 0.05, 10)


class TestEffectiveAnnualRate:
    """実効年利計算テスト"""

    def test_effective_annual_rate_annual(self):
        """年次複利の場合、名目利率と実効利率が同じ"""
        nominal_rate = 0.05
        result = effective_annual_rate(nominal_rate, 1)
        assert abs(result - nominal_rate) < 1e-10

    def test_effective_annual_rate_monthly(self):
        """月次複利の場合、実効利率が名目利率より高い"""
        nominal_rate = 0.12
        result = effective_annual_rate(nominal_rate, 12)
        assert result > nominal_rate

    def test_effective_annual_rate_continuous_approximation(self):
        """複利回数が多い場合、連続複利に近づく"""
        nominal_rate = 0.05
        result_daily = effective_annual_rate(nominal_rate, 365)
        continuous_result = math.exp(nominal_rate) - 1
        assert abs(result_daily - continuous_result) < 0.001


class TestContinuousCompounding:
    """連続複利計算テスト"""

    def test_continuous_compounding_basic(self):
        """基本的な連続複利計算"""
        principal = 1000000
        annual_rate = 0.05
        years = 10
        
        expected = principal * math.exp(annual_rate * years)
        result = continuous_compounding(principal, annual_rate, years)
        assert abs(result - expected) < 1e-6

    def test_continuous_compounding_zero_rate(self):
        """利率0%の場合"""
        principal = 1000000
        result = continuous_compounding(principal, 0.0, 10)
        assert result == principal

    def test_continuous_compounding_zero_years(self):
        """期間0年の場合"""
        principal = 1000000
        result = continuous_compounding(principal, 0.05, 0)
        assert result == principal


class TestEdgeCases:
    """エッジケーステスト"""

    def test_very_small_rates(self):
        """非常に小さな利率での計算"""
        principal = 1000000
        annual_rate = 0.0001  # 0.01%
        years = 1
        
        result = compound_interest(principal, annual_rate, years)
        assert result > principal
        assert result < principal * 1.001

    def test_very_large_rates(self):
        """非常に大きな利率での計算"""
        principal = 1000
        annual_rate = 1.0  # 100%
        years = 1
        
        result = compound_interest(principal, annual_rate, years)
        assert result == 2000

    def test_fractional_years(self):
        """小数点の期間での計算"""
        principal = 1000000
        annual_rate = 0.05
        years = 2.5
        
        result = compound_interest(principal, annual_rate, years)
        expected = principal * (1.05 ** 2.5)
        assert abs(result - expected) < 1e-6