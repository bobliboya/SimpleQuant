import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata

def alpha_025(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 20:
        return _np.nan
    return _np.percentile(sub_df["ClosePrice"].to_numpy()[-20:], 75)


def alpha_026(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 20:
        return _np.nan
    return _np.percentile(sub_df["ClosePrice"].to_numpy()[-20:], 25)


def alpha_027(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 15:
        return _np.nan
    volume = sub_df["Volume"].to_numpy()[-15:]
    return volume[-1] / (_np.mean(volume) + 1e-9)


def alpha_028(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 9:
        return _np.nan
    return _rankdata(sub_df["ClosePrice"].to_numpy()[-9:])[-1]


def alpha_029(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 15:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-15:]
    return close[-1] - close[0]


def alpha_030(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 10:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-10:]
    return _np.std(close) / (_np.mean(close) + 1e-9)
