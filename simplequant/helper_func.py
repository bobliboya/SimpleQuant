# Import packages and library will be used
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from typing import List
from . import factor

pd.options.display.float_format = '{:.2f}'.format

def select_single_col_from_df(
        df: pd.DataFrame,
        symbol: int,
        end_date: str,
        col_name: str,
) -> np.ndarray:
    df['Date'] = pd.to_datetime(df['Date'])
    df_symbol = df[df['Symbol'] == symbol]
    df_symbol = df_symbol[df_symbol['Date'] <= end_date]
    return np.array(df_symbol[col_name])

def extract_symbol_window(df: pd.DataFrame, symbol: int, end_date: str, window: int = 250) -> pd.DataFrame:
    sub_df = df[(df['Symbol'] == symbol) & (df['Date'] <= end_date)]
    sub_df = sub_df.sort_values('Date').tail(window).reset_index(drop=True)
    return sub_df

def run_parallel_alpha(df: pd.DataFrame, symbols: List[int], dates: List[pd.Timestamp], n_jobs: int = 8) -> pd.DataFrame:
    tasks = [(symbol, date) for symbol in symbols for date in dates]
    results = Parallel(n_jobs=n_jobs)(
        delayed(compute_alphas_for_one)(df, symbol, date) for symbol, date in tasks
    )
    return pd.DataFrame(results)


def compute_alphas_for_one(df: pd.DataFrame, symbol: int, date: pd.Timestamp) -> dict:
    """
    Compute Alpha001 to Alpha030 for a given stock symbol and date.

    Args:
        df (pd.DataFrame): The full DataFrame containing all symbol and date data.
        symbol (int): The stock code.
        date (pd.Timestamp): The target date.

    Returns:
        dict: A dictionary containing the date, symbol, and all 30 alpha values.
    """
    try:
        date_str = date.strftime('%Y-%m-%d')
        sub_df = extract_symbol_window(df, symbol, date_str)

        return {
            'Date': date,
            'Symbol': symbol,
            'Alpha1': factor.gtja.alpha_001(sub_df),
            'Alpha2': factor.gtja.alpha_002(sub_df),
            'Alpha3': factor.gtja.alpha_003(sub_df),
            'Alpha4': factor.gtja.alpha_004(sub_df),
            'Alpha5': factor.gtja.alpha_005(sub_df),
            'Alpha6': factor.gtja.alpha_006(sub_df),
            'Alpha7': factor.gtja.alpha_007(sub_df),
            'Alpha8': factor.gtja.alpha_008(sub_df),
            'Alpha9': factor.gtja.alpha_009(sub_df),
            'Alpha10': factor.gtja.alpha_010(sub_df),
            'Alpha11': factor.gtja.alpha_011(sub_df),
            'Alpha12': factor.gtja.alpha_012(sub_df),
            'Alpha13': factor.gtja.alpha_013(sub_df),
            'Alpha14': factor.gtja.alpha_014(sub_df),
            'Alpha15': factor.gtja.alpha_015(sub_df),
            'Alpha16': factor.gtja.alpha_016(sub_df),
            'Alpha17': factor.gtja.alpha_017(sub_df),
            'Alpha18': factor.gtja.alpha_018(sub_df),
            'Alpha19': factor.gtja.alpha_019(sub_df),
            'Alpha20': factor.gtja.alpha_020(sub_df),
            'Alpha21': factor.gtja.alpha_021(sub_df),
            'Alpha22': factor.gtja.alpha_022(sub_df),
            'Alpha23': factor.gtja.alpha_023(sub_df),
            'Alpha24': factor.gtja.alpha_024(sub_df),
            'Alpha25': factor.gtja.alpha_025(sub_df),
            'Alpha26': factor.gtja.alpha_026(sub_df),
            'Alpha27': factor.gtja.alpha_027(sub_df),
            'Alpha28': factor.gtja.alpha_028(sub_df),
            'Alpha29': factor.gtja.alpha_029(sub_df),
            'Alpha30': factor.gtja.alpha_030(sub_df),
        }
    except Exception as e:
        print(f"Error on {symbol} {date}: {e}")
        return {
            'Date': date,
            'Symbol': symbol,
            **{f'Alpha{i}': np.nan for i in range(1, 31)}
        }


__all__ = ['run_parallel_alpha']