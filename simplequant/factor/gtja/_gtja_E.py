import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_049(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 049 factor.

    Formula:
        SUM(((HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) / (SUM(((HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) + SUM(((HIGH+LOW) <= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'HighPrice', 'LowPrice' columns

    Returns:
        float: Alpha 049 value
    """
    if len(sub_df) < 12:
        return 0.0
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]

    high_prev = high.shift(1)
    low_prev = low.shift(1)

    # Condition: (HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1))
    condition1 = (high + low) >= (high_prev + low_prev)
    condition2 = (high + low) <= (high_prev + low_prev)

    # MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))
    abs_high_diff = _np.abs(high - high_prev)
    abs_low_diff = _np.abs(low - low_prev)
    max_diff = _np.maximum(abs_high_diff, abs_low_diff)

    # Apply conditions
    term1 = _pd.Series(0.0, index=sub_df.index)
    term2 = _pd.Series(0.0, index=sub_df.index)

    term1[~condition1] = max_diff[~condition1]
    term2[~condition2] = max_diff[~condition2]

    sum1 = term1.rolling(12).sum()
    sum2 = term2.rolling(12).sum()

    result = sum1 / (sum1 + sum2)
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_050(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 050 factor.

    Formula:
        SUM(((HIGH+LOW) <= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) / (SUM(((HIGH+LOW) <= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) + SUM(((HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12)) - SUM(((HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) / (SUM(((HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) + SUM(((HIGH+LOW) <= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'HighPrice', 'LowPrice' columns

    Returns:
        float: Alpha 050 value
    """
    if len(sub_df) < 12:
        return 0.0
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]

    high_prev = high.shift(1)
    low_prev = low.shift(1)

    condition1 = (high + low) <= (high_prev + low_prev)
    condition2 = (high + low) >= (high_prev + low_prev)

    abs_high_diff = _np.abs(high - high_prev)
    abs_low_diff = _np.abs(low - low_prev)
    max_diff = _np.maximum(abs_high_diff, abs_low_diff)

    term1 = _pd.Series(0.0, index=sub_df.index)
    term2 = _pd.Series(0.0, index=sub_df.index)

    term1[~condition1] = max_diff[~condition1]
    term2[~condition2] = max_diff[~condition2]

    sum1 = term1.rolling(12).sum()
    sum2 = term2.rolling(12).sum()

    result = sum1 / (sum1 + sum2) - sum2 / (sum1 + sum2)
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_051(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 051 factor.

    Formula:
        SUM(((HIGH+LOW) <= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) / (SUM(((HIGH+LOW) <= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12) + SUM(((HIGH+LOW) >= (DELAY(HIGH,1)+DELAY(LOW,1)) ? 0 : MAX(ABS(HIGH-DELAY(HIGH,1)), ABS(LOW-DELAY(LOW,1)))), 12))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'HighPrice', 'LowPrice' columns

    Returns:
        float: Alpha 051 value
    """
    if len(sub_df) < 12:
        return 0.0
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]

    high_prev = high.shift(1)
    low_prev = low.shift(1)

    condition1 = (high + low) <= (high_prev + low_prev)
    condition2 = (high + low) >= (high_prev + low_prev)

    abs_high_diff = _np.abs(high - high_prev)
    abs_low_diff = _np.abs(low - low_prev)
    max_diff = _np.maximum(abs_high_diff, abs_low_diff)

    term1 = _pd.Series(0.0, index=sub_df.index)
    term2 = _pd.Series(0.0, index=sub_df.index)

    term1[~condition1] = max_diff[~condition1]
    term2[~condition2] = max_diff[~condition2]

    sum1 = term1.rolling(12).sum()
    sum2 = term2.rolling(12).sum()

    result = sum1 / (sum1 + sum2)
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_052(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 052 factor.

    Formula:
        SUM(MAX(0, HIGH - DELAY((HIGH + LOW + CLOSE) / 3, 1)), 26) / SUM(MAX(0, DELAY((HIGH + LOW + CLOSE) / 3, 1) - LOW), 26) * 100

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'HighPrice', 'LowPrice', 'ClosePrice' columns

    Returns:
        float: Alpha 052 value
    """
    if len(sub_df) < 26:
        return 0.0
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]
    close = sub_df["ClosePrice"]

    # (HIGH + LOW + CLOSE) / 3
    typical_price = (high + low + close) / 3
    typical_price_prev = typical_price.shift(1)

    # MAX(0, HIGH - DELAY((HIGH + LOW + CLOSE) / 3, 1))
    term1 = _np.maximum(0, high - typical_price_prev)

    # MAX(0, DELAY((HIGH + LOW + CLOSE) / 3, 1) - LOW)
    term2 = _np.maximum(0, typical_price_prev - low)

    sum1 = term1.rolling(26).sum()
    sum2 = term2.rolling(26).sum()

    result = sum1 / sum2 * 100
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_053(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 053 factor.

    Formula:
        COUNT(CLOSE > DELAY(CLOSE, 1), 12)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice' column

    Returns:
        float: Alpha 053 value
    """
    if len(sub_df) < 12:
        return 0.0
    close = sub_df["ClosePrice"]

    close_prev = close.shift(1)
    up_condition = close > close_prev

    result = up_condition.rolling(12).sum()
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_054(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 054 factor.

    Formula:
        (-1 * RANK(STD(ABS(CLOSE - OPEN), 10)) + CORR(CLOSE, OPEN, 10))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'OpenPrice' columns

    Returns:
        float: Alpha 054 value
    """
    if len(sub_df) < 10:
        return 0.0
    close = sub_df["ClosePrice"]
    open_price = sub_df["OpenPrice"]

    abs_diff = _np.abs(close - open_price)
    std_abs = abs_diff.rolling(10).std()
    rank_std = std_abs.rank(pct=True)

    corr_close_open = close.rolling(10).corr(open_price)

    result = -rank_std + corr_close_open
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_055(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 055 factor.

    Formula:
        SUM(16 * (CLOSE - DELAY(CLOSE, 1) + (CLOSE - OPEN) / 2 + DELAY(CLOSE, 1) - DELAY(OPEN, 1)) / ((ABS(HIGH - DELAY(CLOSE, 1)) > ABS(LOW - DELAY(CLOSE, 1)) & ABS(HIGH - DELAY(CLOSE, 1)) > ABS(HIGH - DELAY(LOW, 1)) ? ABS(HIGH - DELAY(CLOSE, 1)) + ABS(LOW - DELAY(CLOSE, 1)) / 2 + ABS(DELAY(CLOSE, 1) - DELAY(OPEN, 1)) / 4 : (ABS(LOW - DELAY(CLOSE, 1)) > ABS(HIGH - DELAY(LOW, 1)) & ABS(LOW - DELAY(CLOSE, 1)) > ABS(HIGH - DELAY(CLOSE, 1)) ? ABS(LOW - DELAY(CLOSE, 1)) + ABS(HIGH - DELAY(CLOSE, 1)) / 2 + ABS(DELAY(CLOSE, 1) - DELAY(OPEN, 1)) / 4 : ABS(HIGH - DELAY(LOW, 1)) + ABS(DELAY(CLOSE, 1) - DELAY(OPEN, 1)) / 4))) * MAX(ABS(HIGH - DELAY(CLOSE, 1)), ABS(LOW - DELAY(CLOSE, 1))), 20)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'OpenPrice', 'HighPrice', 'LowPrice' columns

    Returns:
        float: Alpha 055 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]
    open_price = sub_df["OpenPrice"]
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]

    close_prev = close.shift(1)
    open_prev = open_price.shift(1)
    low_prev = low.shift(1)

    # Numerator
    num = 16 * (close - close_prev + (close - open_price) / 2 + close_prev - open_prev)

    # Denominator conditions
    abs_high_close_prev = _np.abs(high - close_prev)
    abs_low_close_prev = _np.abs(low - close_prev)
    abs_high_low_prev = _np.abs(high - low_prev)
    abs_close_prev_open_prev = _np.abs(close_prev - open_prev)

    condition1 = (abs_high_close_prev > abs_low_close_prev) & (
        abs_high_close_prev > abs_high_low_prev
    )
    condition2 = (abs_low_close_prev > abs_high_low_prev) & (
        abs_low_close_prev > abs_high_close_prev
    )

    denom = _pd.Series(0.0, index=sub_df.index)
    denom[condition1] = (
        abs_high_close_prev[condition1]
        + abs_low_close_prev[condition1] / 2
        + abs_close_prev_open_prev[condition1] / 4
    )
    denom[condition2] = (
        abs_low_close_prev[condition2]
        + abs_high_close_prev[condition2] / 2
        + abs_close_prev_open_prev[condition2] / 4
    )
    denom[~(condition1 | condition2)] = (
        abs_high_low_prev[~(condition1 | condition2)]
        + abs_close_prev_open_prev[~(condition1 | condition2)] / 4
    )

    # MAX(ABS(HIGH - DELAY(CLOSE, 1)), ABS(LOW - DELAY(CLOSE, 1)))
    max_abs = _np.maximum(abs_high_close_prev, abs_low_close_prev)

    temp = num / denom * max_abs
    result = temp.rolling(20).sum()

    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_056(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 056 factor.

    Formula:
        RANK((OPEN - TSMIN(OPEN, 12))) < RANK((RANK(CORR(SUM(((HIGH + LOW) / 2), 19), SUM(MEAN(VOLUME, 40), 19), 13)) ^ 5))

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'OpenPrice', 'HighPrice', 'LowPrice', 'Volume' columns

    Returns:
        float: Alpha 056 value
    """
    if len(sub_df) < 40:
        return 0.0
    open_price = sub_df["OpenPrice"]
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]
    volume = sub_df["Volume"]

    # TSMIN(OPEN, 12)
    tsmin_open = open_price.rolling(12).min()
    rank_open = (open_price - tsmin_open).rank(pct=True)

    # SUM(((HIGH + LOW) / 2), 19)
    hl_avg = (high + low) / 2
    sum_hl = hl_avg.rolling(19).sum()

    # SUM(MEAN(VOLUME, 40), 19)
    mean_vol = volume.rolling(40).mean()
    sum_mean_vol = mean_vol.rolling(19).sum()

    # CORR(SUM(((HIGH + LOW) / 2), 19), SUM(MEAN(VOLUME, 40), 19), 13)
    corr_sum = sum_hl.rolling(13).corr(sum_mean_vol)
    rank_corr = corr_sum.rank(pct=True)
    rank_corr_pow = rank_corr**5

    result = rank_open < rank_corr_pow
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_057(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 057 factor.

    Formula:
        SMA((CLOSE - TSMIN(LOW, 12)) / (TSMAX(HIGH, 12) - TSMIN(LOW, 12)) * 100, 9, 1)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'HighPrice', 'LowPrice' columns

    Returns:
        float: Alpha 057 value
    """
    if len(sub_df) < 12:
        return 0.0
    close = sub_df["ClosePrice"]
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]

    tsmin_low = low.rolling(12).min()
    tsmax_high = high.rolling(12).max()

    temp = (close - tsmin_low) / (tsmax_high - tsmin_low) * 100
    sma_result = temp.ewm(alpha=1 / 9, adjust=False).mean()

    return sma_result.iloc[-1] if _np.isfinite(sma_result.iloc[-1]) else 0.0


def alpha_058(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 058 factor.

    Formula:
        COUNT(CLOSE > DELAY(CLOSE, 1), 20) / 20 * 100

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice' column

    Returns:
        float: Alpha 058 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]

    close_prev = close.shift(1)
    up_condition = close > close_prev

    count_up = up_condition.rolling(20).sum()
    result = count_up / 20 * 100

    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_059(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 059 factor.

    Formula:
        SUM((CLOSE = DELAY(CLOSE, 1) ? 0 : CLOSE - (CLOSE > DELAY(CLOSE, 1) ? MIN(LOW, DELAY(CLOSE, 1)) : MAX(HIGH, DELAY(CLOSE, 1)))), 20)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'HighPrice', 'LowPrice' columns

    Returns:
        float: Alpha 059 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]

    close_prev = close.shift(1)

    # CLOSE = DELAY(CLOSE, 1)
    equal_condition = close == close_prev

    # CLOSE > DELAY(CLOSE, 1)
    up_condition = close > close_prev

    # MIN(LOW, DELAY(CLOSE, 1))
    min_low_close_prev = _np.minimum(low, close_prev)

    # MAX(HIGH, DELAY(CLOSE, 1))
    max_high_close_prev = _np.maximum(high, close_prev)

    # Conditional calculation
    temp = _pd.Series(0.0, index=sub_df.index)
    temp[~equal_condition & up_condition] = (
        close[~equal_condition & up_condition]
        - min_low_close_prev[~equal_condition & up_condition]
    )
    temp[~equal_condition & ~up_condition] = (
        close[~equal_condition & ~up_condition]
        - max_high_close_prev[~equal_condition & ~up_condition]
    )

    result = temp.rolling(20).sum()
    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0


def alpha_060(sub_df: _pd.DataFrame) -> float:
    """
    Compute the Alpha 060 factor.

    Formula:
        SUM(((CLOSE - LOW) - (HIGH - CLOSE)) / (HIGH - LOW) * VOLUME, 20)

    Args:
        sub_df (_pd.DataFrame): DataFrame with 'ClosePrice', 'HighPrice', 'LowPrice', 'Volume' columns

    Returns:
        float: Alpha 060 value
    """
    if len(sub_df) < 20:
        return 0.0
    close = sub_df["ClosePrice"]
    high = sub_df["HighPrice"]
    low = sub_df["LowPrice"]
    volume = sub_df["Volume"]

    temp = ((close - low) - (high - close)) / (high - low) * volume
    result = temp.rolling(20).sum()

    return result.iloc[-1] if _np.isfinite(result.iloc[-1]) else 0.0
