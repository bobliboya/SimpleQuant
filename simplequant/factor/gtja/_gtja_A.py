import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


# Alpha001 to Alpha012: each function assumes sub_df is already filtered by symbol and date window


def alpha_001(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 001 factor using the formula published by Guotai Junan Securities.

    (-1 * CORR(RANK(DELTA(LOG(VOLUME),1)),RANK(((CLOSE-OPEN)/OPEN)),6)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The Alpha 001 factor value of the last trading day in the series.
    """
    if len(sub_df) < 7:
        return _np.nan
    open_price = sub_df["OpenPrice"].to_numpy()[-6:]
    close_price = sub_df["ClosePrice"].to_numpy()[-6:]
    volume = sub_df["Volume"].to_numpy()[-7:]
    delta_log_volume = _np.diff(_np.log(volume))
    daily_change = (close_price - open_price) / open_price
    return -1 * _np.corrcoef(_rankdata(delta_log_volume), _rankdata(daily_change))[0, 1]


def alpha_002(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 002 factor using the formula published by Guotai Junan Securities.

    -1 * delta((((close-low)-(high-close))/((high-low)),1))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The Alpha 002 factor value of the last trading day in the series.
    """
    if len(sub_df) < 2:
        return _np.nan
    h1, h2 = sub_df["HighPrice"].iloc[-2], sub_df["HighPrice"].iloc[-1]
    l1, l2 = sub_df["LowPrice"].iloc[-2], sub_df["LowPrice"].iloc[-1]
    c1, c2 = sub_df["ClosePrice"].iloc[-2], sub_df["ClosePrice"].iloc[-1]
    if h1 == l1 or h2 == l2:
        return _np.nan
    return -1 * ((2 * c2 - l2 - h2) / (h2 - l2) - (2 * c1 - l1 - h1) / (h1 - l1))


def alpha_003(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 7:
        return _np.nan
    high = sub_df["HighPrice"].to_numpy()
    low = sub_df["LowPrice"].to_numpy()
    close = sub_df["ClosePrice"].to_numpy()
    alpha = 0
    for i in range(-6, 0):
        prev = close[i - 1]
        curr = close[i]
        if curr == prev:
            continue
        elif curr < prev:
            alpha += curr - max(high[i], prev)
        else:
            alpha += curr - min(low[i], prev)
    return alpha


def alpha_004(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 20:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()
    volume = sub_df["Volume"].to_numpy()
    avg_8 = _np.mean(close[-8:])
    std_8 = _np.std(close[-8:])
    avg_2 = _np.mean(close[-2:])
    mean_volume_20 = _np.mean(volume[-20:])
    if avg_8 + std_8 < avg_2:
        return -1
    elif avg_2 < avg_8 - std_8:
        return 1
    elif volume[-1] / mean_volume_20 >= 1:
        return 1
    else:
        return -1


def alpha_005(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 7:
        return _np.nan
    ts_high = _pd.Series(sub_df["HighPrice"].to_numpy()[-7:]).rank(pct=True)
    ts_volume = _pd.Series(sub_df["Volume"].to_numpy()[-7:]).rank(pct=True)
    ts_df = _pd.DataFrame({"high": ts_high, "volume": ts_volume})
    corr_series = ts_df["high"].rolling(window=5).corr(ts_df["volume"])
    corr_clean = corr_series.replace([_np.inf, -_np.inf], _np.nan).dropna()
    return -1 * corr_clean.max() if not corr_clean.empty else _np.nan


def alpha_006(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 10:
        return _np.nan
    return (
        -1
        * _np.corrcoef(
            sub_df["OpenPrice"].to_numpy()[-10:], sub_df["Volume"].to_numpy()[-10:]
        )[0, 1]
    )


def alpha_007(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 20:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()
    volume = sub_df["Volume"].to_numpy()
    adv20 = _np.mean(volume[-20:])
    diff = close[-1] - adv20
    return -1 * _np.cbrt(diff * abs(diff))


def alpha_008(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 10:
        return _np.nan
    return (
        -1
        * _np.corrcoef(
            sub_df["OpenPrice"].to_numpy()[-10:], sub_df["Volume"].to_numpy()[-10:]
        )[0, 1]
    )


def alpha_009(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 5:
        return _np.nan
    volume = sub_df["Volume"].to_numpy()[-5:]
    return _np.max(volume) / (_np.mean(volume) + 1e-9)


def alpha_010(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 6:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-6:]
    return -1 * _rankdata(close)[-1]


def alpha_011(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 9:
        return _np.nan
    close = sub_df["ClosePrice"].to_numpy()[-9:]
    return close[-1] - close.mean()


def alpha_012(sub_df: _pd.DataFrame) -> float:
    if len(sub_df) < 7:
        return _np.nan
    volume = sub_df["Volume"].to_numpy()[-7:]
    return _rankdata(volume)[-1] / 7.0
