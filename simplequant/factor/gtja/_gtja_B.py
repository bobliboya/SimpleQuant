import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata

def alpha_013(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 12:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-12:]
    return _np.std(close) / (_np.mean(close) + 1e-9)


def alpha_014(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 6:
        return _np.nan
    high = sub_df["HighPrice"].to_numpy()[-6:]
    low = sub_df["LowPrice"].to_numpy()[-6:]
    return (_np.max(high) - _np.min(low)) / (_np.mean(high) + 1e-9)


def alpha_015(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 5:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-5:]
    return -1 * (close[-1] - close[-5])


def alpha_016(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 10:
        return _np.nan
    return _np.mean(sub_df["ClosePrice"].to_numpy()[-10:])


def alpha_017(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 5:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-5:]
    return _np.std(close)


def alpha_018(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 9:
        return _np.nan
    high = sub_df["HighPrice"].to_numpy()[-9:]
    return _rankdata(high)[-1]


def alpha_019(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 12:
        return _np.nan
    low = sub_df["LowPrice"].to_numpy()[-12:]
    return _np.min(low)


def alpha_020(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 20:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-20:]
    return _np.max(close)


def alpha_021(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 5:
        return _np.nan
    open_ = sub_df["OpenPrice"].to_numpy()[-5:]
    return _np.mean(open_)


def alpha_022(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 10:
        return _np.nan
    high = sub_df["HighPrice"].to_numpy()[-10:]
    return _np.std(high)


def alpha_023(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 6:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-6:]
    return _np.mean(close[-3:]) - _np.mean(close[:3])


def alpha_024(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 8:
        return _np.nan
    volume = sub_df["Volume"].to_numpy()[-8:]
    return _np.corrcoef(_np.arange(8), volume)[0, 1]
