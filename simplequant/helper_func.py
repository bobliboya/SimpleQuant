# Import packages and library will be used
import pandas as pd
from typing import List, Any

pd.options.display.float_format = "{:.2f}".format


def ddb_alpha_matrix_to_df(alpha_matrix: Any) -> pd.DataFrame:
    """
    Takes the return result of Alpha Calculations from DolphinDB gtjaAlpha191 Module.

    Args:
        alpha_matrix (List [Any]): The return result from DolphinDB.

    Returns:
        The Pandas Dataframe of the dataset.
    """
    values, dates, tickers = alpha_matrix
    df = pd.DataFrame(values, index=pd.to_datetime(dates), columns=tickers)
    return df


def calculate_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily return for each stock: (close - prev_close) / prev_close

    Assumes:
        - df uses MultiIndex ['Date', 'Symbol']
        - df is already sorted by ['Date', 'Symbol']
        - df contains a 'ClosePrice' column

    Does NOT modify the original DataFrame.

    Args:
        df (pd.DataFrame): MultiIndex DataFrame with 'ClosePrice'

    Returns:
        pd.DataFrame: New DataFrame with same index and two columns:
            - 'ClosePrice': copied from original df
            - 'Return': daily return per stock, grouped by Symbol
    """
    if not isinstance(df.index, pd.MultiIndex) or df.index.names != ["Date", "Symbol"]:
        raise ValueError("Input must have MultiIndex ['Date', 'Symbol']")
    if "ClosePrice" not in df.columns:
        raise ValueError("Missing 'ClosePrice' column in input")

    # 计算收益率（不修改原始 df）
    rtn = df.groupby(level="Symbol")["ClosePrice"].pct_change()

    # 返回新构造的 DataFrame，保留原索引
    return pd.DataFrame({"ClosePrice": df["ClosePrice"], "Return": rtn}, index=df.index)


def get_single_day_info(df: pd.DataFrame, date: str) -> pd.DataFrame:
    """
    Get the return rate of each stock at the given date, ignoring time component.

    Args:
        df (pd.DataFrame): The full DataFrame containing all symbol and date data.
        date (str): Date (YYYY-MM-DD) to filter.

    Returns:
        pd.DataFrame: DataFrame with rows matching the specified date.
    """
    # target_date = pd.to_datetime(date).date()

    if "Date" in df.columns:
        return df[df["Date"] == date]
    elif "TRADE_DATE" in df.columns:
        return df[df["TRADE_DATE"] == date]
    else:
        raise ValueError("No valid date column in DataFrame!")


__all__ = [
    "calculate_daily_return",
    "get_single_day_info",
    "ddb_alpha_matrix_to_df",
]
