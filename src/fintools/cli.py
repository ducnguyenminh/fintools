"""
FinTools コマンドラインインターフェース

コマンドラインから金融計算を実行するためのツールです。
"""

import argparse
import sys
from typing import Optional

from .compound_interest import (
    annual_to_monthly_rate,
    monthly_to_annual_rate,
    compound_interest,
    present_value,
    effective_annual_rate,
    continuous_compounding,
)


def format_percentage(rate: float, decimal_places: int = 4) -> str:
    """利率を%表記でフォーマットします"""
    return f"{rate * 100:.{decimal_places}f}%"


def format_currency(amount: float, currency: str = "¥") -> str:
    """金額を通貨表記でフォーマットします"""
    return f"{currency}{amount:,.0f}"


def cmd_annual_to_monthly(args) -> None:
    """年利から月利への変換コマンド"""
    try:
        monthly_rate = annual_to_monthly_rate(args.annual_rate / 100)
        print(f"年利: {format_percentage(args.annual_rate / 100, 2)}")
        print(f"月利: {format_percentage(monthly_rate, 4)}")
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_monthly_to_annual(args) -> None:
    """月利から年利への変換コマンド"""
    try:
        annual_rate = monthly_to_annual_rate(args.monthly_rate / 100)
        print(f"月利: {format_percentage(args.monthly_rate / 100, 4)}")
        print(f"年利: {format_percentage(annual_rate, 2)}")
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_compound_interest(args) -> None:
    """複利計算コマンド"""
    try:
        result = compound_interest(
            args.principal,
            args.annual_rate / 100,
            args.years,
            args.frequency
        )
        
        print(f"元本: {format_currency(args.principal)}")
        print(f"年利: {format_percentage(args.annual_rate / 100, 2)}")
        print(f"期間: {args.years}年")
        print(f"複利回数: 年{args.frequency}回")
        print(f"将来価値: {format_currency(result)}")
        print(f"利息: {format_currency(result - args.principal)}")
        
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_present_value(args) -> None:
    """現在価値計算コマンド"""
    try:
        result = present_value(
            args.future_value,
            args.annual_rate / 100,
            args.years,
            args.frequency
        )
        
        print(f"将来価値: {format_currency(args.future_value)}")
        print(f"年利: {format_percentage(args.annual_rate / 100, 2)}")
        print(f"期間: {args.years}年")
        print(f"複利回数: 年{args.frequency}回")
        print(f"現在価値: {format_currency(result)}")
        
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


def create_parser() -> argparse.ArgumentParser:
    """コマンドライン引数パーサーを作成します"""
    parser = argparse.ArgumentParser(
        description="FinTools - 金融計算コマンドラインツール",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  fintools annual-to-monthly 5.0        # 年利5%を月利に変換
  fintools compound 1000000 5.0 10      # 100万円、年利5%、10年の複利計算
  fintools compound 1000000 5.0 10 -f 12  # 月次複利で計算
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='利用可能なコマンド')
    
    # 年利→月利変換
    parser_a2m = subparsers.add_parser(
        'annual-to-monthly',
        help='年利から月利に変換'
    )
    parser_a2m.add_argument(
        'annual_rate',
        type=float,
        help='年利（%表記、例：5.0）'
    )
    parser_a2m.set_defaults(func=cmd_annual_to_monthly)
    
    # 月利→年利変換
    parser_m2a = subparsers.add_parser(
        'monthly-to-annual',
        help='月利から年利に変換'
    )
    parser_m2a.add_argument(
        'monthly_rate',
        type=float,
        help='月利（%表記、例：0.4）'
    )
    parser_m2a.set_defaults(func=cmd_monthly_to_annual)
    
    # 複利計算
    parser_compound = subparsers.add_parser(
        'compound',
        help='複利計算'
    )
    parser_compound.add_argument(
        'principal',
        type=float,
        help='元本（円）'
    )
    parser_compound.add_argument(
        'annual_rate',
        type=float,
        help='年利（%表記、例：5.0）'
    )
    parser_compound.add_argument(
        'years',
        type=float,
        help='期間（年）'
    )
    parser_compound.add_argument(
        '-f', '--frequency',
        type=int,
        default=1,
        help='年間複利回数（デフォルト：1）'
    )
    parser_compound.set_defaults(func=cmd_compound_interest)
    
    # 現在価値計算
    parser_pv = subparsers.add_parser(
        'present-value',
        help='現在価値計算'
    )
    parser_pv.add_argument(
        'future_value',
        type=float,
        help='将来価値（円）'
    )
    parser_pv.add_argument(
        'annual_rate',
        type=float,
        help='年利（%表記、例：5.0）'
    )
    parser_pv.add_argument(
        'years',
        type=float,
        help='期間（年）'
    )
    parser_pv.add_argument(
        '-f', '--frequency',
        type=int,
        default=1,
        help='年間複利回数（デフォルト：1）'
    )
    parser_pv.set_defaults(func=cmd_present_value)
    
    return parser


def main() -> None:
    """メイン実行関数"""
    parser = create_parser()
    args = parser.parse_args()
    
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()