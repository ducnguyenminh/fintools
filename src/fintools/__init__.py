"""
FinTools - 金融計算に特化したPythonツールライブラリ

このライブラリは、複利計算、利回り計算、投資リターン分析など、
金融関連の計算を簡単に行うことができます。
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .compound_interest import (
    annual_to_monthly_rate,
    monthly_to_annual_rate,
    compound_interest,
    future_value,
    present_value,
)

__all__ = [
    "annual_to_monthly_rate",
    "monthly_to_annual_rate",
    "compound_interest",
    "future_value",
    "present_value",
]
