import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_037(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 037 factor.

    Formula:
        (-1 * RANK(((SUM(OPEN, 5) * SUM(RET, 5)) - DELAY((SUM(OPEN, 5) * SUM(RET, 5)), 10))))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'OpenPrice', 'ClosePrice' columns

    Returns:
        float: Alpha 037 value
    """
    if len(sub_df) < 15:
        return 0.0
    open_price = sub_df["OpenPrice"]
    close = sub_df["ClosePrice"]

    ret = close.pct_change()
    sum_open5 = open_price.rolling(5).sum()
    sum_ret5 = ret.rolling(5).sum()
    temp = sum_open5 * sum_ret5
    delay_temp = temp.shift(10)
    diff_temp = temp - delay_temp
    rank_result = diff_temp.rank(pct=True)

    return -rank_result.iloc[-1] if _np.isfinite(rank_result.iloc[-1]) else 0.0


def alpha_038(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 038 factor.

    Formula:
        (((SUM(HIGH, 20)/20)<HIGH)?(-1*DELTA(HIGH,2)):0)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_038 factor value of the last trading day in the series.
    """
    if len(sub_df) < 20:
        return 0.0
    high = sub_df["HighPrice"]

    ma_high = high.rolling(20).mean()
    delta_high = high.diff(2)

    condition = ma_high < high
    result = _pd.Series(0.0, index=sub_df.index)
    result[condition] = -delta_high[condition]

    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_039(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 039 factor.

    Formula:
        ((RANK(DECAYLINEAR(DELTA((CLOSE), 2), 8)) - RANK(DECAYLINEAR(CORR(((VWAP * 0.3) + (OPEN * 0.7)), SUM(MEAN(VOLUME, 180), 37), 14), 12))) * -1)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'VWAP', 'OpenPrice', 'Volume' columns

    Returns:
        float: Alpha 039 value
    """
    if len(sub_df) < 37:
        return 0.0
    close = sub_df["ClosePrice"]
    vwap = sub_df["VWAP"]
    open_price = sub_df["OpenPrice"]
    volume = sub_df["Volume"]

    # DELTA(CLOSE, 2)
    delta_close = close.diff(2)

    # DECAYLINEAR with weights [8, 7, 6, ..., 1]
    def decay_linear(x):
        if len(x) < 8:
            return _np.nan
        weights = _np.arange(8, 0, -1)
        return _np.average(x[-8:], weights=weights)

    decay_delta = delta_close.rolling(8).apply(decay_linear, raw=True)
    rank_decay_delta = decay_delta.rank(pct=True)

    # CORR((VWAP * 0.3 + OPEN * 0.7), SUM(MEAN(VOLUME, 180), 37), 14)
    temp_price = vwap * 0.3 + open_price * 0.7
    mean_vol180 = volume.rolling(180).mean()
    sum_mean_vol = mean_vol180.rolling(37).sum()
    corr_temp = temp_price.rolling(14).corr(sum_mean_vol)
    decay_corr = corr_temp.rolling(12).apply(decay_linear, raw=True)
    rank_decay_corr = decay_corr.rank(pct=True)

    result = (rank_decay_delta - rank_decay_corr) * -1
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_040(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 040 factor.

    Formula:
        SUM((CLOSE > DELAY(CLOSE, 1) ? VOLUME : 0), 26) / SUM((CLOSE <= DELAY(CLOSE, 1) ? VOLUME : 0), 26) * 100

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'Volume' columns

    Returns:
        float: Alpha 040 value
    """
    if len(sub_df) < 26:
        return 0.0
    close = sub_df["ClosePrice"]
    volume = sub_df["Volume"]

    close_prev = close.shift(1)
    up_condition = close > close_prev
    down_condition = close <= close_prev

    up_volume = _pd.Series(0.0, index=sub_df.index)
    down_volume = _pd.Series(0.0, index=sub_df.index)

    up_volume[up_condition] = volume[up_condition]
    down_volume[down_condition] = volume[down_condition]

    sum_up = up_volume.rolling(26).sum()
    sum_down = down_volume.rolling(26).sum()

    result = sum_up / sum_down * 100
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_041(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 041 factor.

    Formula:
        (RANK(MAX(DELTA(VWAP, 3), 5)) * -1)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'VWAP' column

    Returns:
        float: Alpha 041 value
    """
    if len(sub_df) < 8:
        return 0.0
    vwap = sub_df["VWAP"]

    delta_vwap = vwap.diff(3)
    max_delta = delta_vwap.rolling(5).max()
    rank_result = max_delta.rank(pct=True)

    return -rank_result.iloc[-1] if _np.isfinite(rank_result.iloc[-1]) else 0.0


def alpha_042(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 042 factor.

    Formula:
        (-1 * RANK(STD(HIGH, 10))) * CORR(HIGH, VOLUME, 10)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'HighPrice', 'Volume' columns

    Returns:
        float: Alpha 042 value
    """
    if len(sub_df) < 10:
        return 0.0
    high = sub_df["HighPrice"]
    volume = sub_df["Volume"]

    std_high = high.rolling(10).std()
    rank_std = std_high.rank(pct=True)
    corr_high_vol = high.rolling(10).corr(volume)

    result = -rank_std * corr_high_vol
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_043(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 043 factor.

    Formula:
        SUM((CLOSE > DELAY(CLOSE, 1) ? VOLUME : (CLOSE < DELAY(CLOSE, 1) ? -VOLUME : 0)), 6)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'Volume' columns

    Returns:
        float: Alpha 043 value
    """
    if len(sub_df) < 6:
        return 0.0
    close = sub_df["ClosePrice"]
    volume = sub_df["Volume"]

    close_prev = close.shift(1)
    up_condition = close > close_prev
    down_condition = close < close_prev

    signed_volume = _pd.Series(0.0, index=sub_df.index)
    signed_volume[up_condition] = volume[up_condition]
    signed_volume[down_condition] = -volume[down_condition]

    result = signed_volume.rolling(6).sum()
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_044(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 044 factor.

    Formula:
        (TSRANK(DECAYLINEAR(CORR(((LOW)), MEAN(VOLUME, 10), 7), 6), 4) + TSRANK(DECAYLINEAR(DELTA((VWAP), 3), 10), 15))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'LowPrice', 'Volume', 'VWAP' columns

    Returns:
        float: Alpha 044 value
    """
    if len(sub_df) < 15:
        return 0.0
    low = sub_df["LowPrice"]
    volume = sub_df["Volume"]
    vwap = sub_df["VWAP"]

    # CORR(LOW, MEAN(VOLUME, 10), 7)
    mean_vol10 = volume.rolling(10).mean()
    corr_low_vol = low.rolling(7).corr(mean_vol10)

    # DECAYLINEAR with weights [6, 5, 4, ..., 1]
    def decay_linear(x):
        if len(x) < 6:
            return _np.nan
        weights = _np.arange(6, 0, -1)
        return _np.average(x[-6:], weights=weights)

    decay_corr = corr_low_vol.rolling(6).apply(decay_linear, raw=True)

    # TSRANK with rank function
    def tsrank(x):
        if len(x) < 4:
            return _np.nan
        return _rankdata(x)[-1] / len(x)

    tsrank1 = decay_corr.rolling(4).apply(tsrank, raw=True)

    # DELTA(VWAP, 3)
    delta_vwap = vwap.diff(3)
    decay_delta = delta_vwap.rolling(10).apply(decay_linear, raw=True)
    tsrank2 = decay_delta.rolling(15).apply(tsrank, raw=True)

    result = tsrank1 + tsrank2
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_045(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 045 factor.

    Formula:
        (-1 * RANK((SUM(DELAY(CLOSE, 5), 20) / 20)) * CORR(CLOSE, VOLUME, 2) * RANK(CORR(SUM(CLOSE, 5), SUM(CLOSE, 20), 2)))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'Volume' columns

    Returns:
        float: Alpha 045 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]
    volume = sub_df["Volume"]

    # SUM(DELAY(CLOSE, 5), 20) / 20
    close_delay5 = close.shift(5)
    sum_delay = close_delay5.rolling(20).sum() / 20
    rank_sum = sum_delay.rank(pct=True)

    # CORR(CLOSE, VOLUME, 2)
    corr_close_vol = close.rolling(2).corr(volume)

    # CORR(SUM(CLOSE, 5), SUM(CLOSE, 20), 2)
    sum_close5 = close.rolling(5).sum()
    sum_close20 = close.rolling(20).sum()
    corr_sum = sum_close5.rolling(2).corr(sum_close20)
    rank_corr_sum = corr_sum.rank(pct=True)

    result = -rank_sum * corr_close_vol * rank_corr_sum
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_046(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 046 factor.

    Formula:
        (RANK((RANK((RANK((RANK(DELTA((((CLOSE * 0.6) + (OPEN * 0.4))), 2)) * -1)) * -1)) * -1)) / COUNT(CLOSE, 60))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'OpenPrice' columns

    Returns:
        float: Alpha 046 value
    """
    if len(sub_df) < 60:
        return 0.0
    close = sub_df["ClosePrice"]
    open_price = sub_df["OpenPrice"]

    # ((CLOSE * 0.6) + (OPEN * 0.4))
    temp_price = close * 0.6 + open_price * 0.4
    delta_temp = temp_price.diff(2)

    rank1 = delta_temp.rank(pct=True)
    rank2 = (-rank1).rank(pct=True)
    rank3 = (-rank2).rank(pct=True)
    rank4 = (-rank3).rank(pct=True)

    count_close = close.rolling(60).count()

    result = rank4 / count_close
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_047(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 047 factor.

    Formula:
        ((RANK((1 / CLOSE))) * VOLUME) / MEAN(VOLUME, 20)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'Volume' columns

    Returns:
        float: Alpha 047 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]
    volume = sub_df["Volume"]

    rank_inv_close = (1 / close).rank(pct=True)
    mean_vol = volume.rolling(20).mean()

    result = rank_inv_close * volume / mean_vol
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_048(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 048 factor.

    Formula:
        (-1 * ((RANK(((SIGN((CLOSE - DELAY(CLOSE, 1))) + SIGN((DELAY(CLOSE, 1) - DELAY(CLOSE, 2)))) + SIGN((DELAY(CLOSE, 2) - DELAY(CLOSE, 3)))))) * SUM(VOLUME, 5)) / SUM(VOLUME, 20)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'Volume' columns

    Returns:
        float: Alpha 048 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]
    volume = sub_df["Volume"]

    close_delay1 = close.shift(1)
    close_delay2 = close.shift(2)
    close_delay3 = close.shift(3)

    sign1 = _np.sign(close - close_delay1)
    sign2 = _np.sign(close_delay1 - close_delay2)
    sign3 = _np.sign(close_delay2 - close_delay3)

    sum_signs = sign1 + sign2 + sign3
    rank_signs = sum_signs.rank(pct=True)

    sum_vol5 = volume.rolling(5).sum()
    sum_vol20 = volume.rolling(20).sum()

    result = -rank_signs * sum_vol5 / sum_vol20
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0
