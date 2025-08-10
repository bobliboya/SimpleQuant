import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_121(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_121 factor using the formula published by Guotai Junan Securities.

    ((RANK((VWAP-MIN(VWAP,12)))^TSRANK(CORR(TSRANK(VWAP,20),TSRANK(MEAN(VOLUME,60),2),18),3))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_121 factor value of the last trading day in the series.
    """
    return -888


def alpha_122(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_122 factor using the formula published by Guotai Junan Securities.

    (SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2)-DELAY(SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2),1))/DELAY(SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2),1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_122 factor value of the last trading day in the series.
    """
    return -888


def alpha_123(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_123 factor using the formula published by Guotai Junan Securities.

    ((RANK(CORR(SUM(((HIGH+LOW)/2),20),SUM(MEAN(VOLUME,60),20),9))\

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_123 factor value of the last trading day in the series.
    """
    return -888


def alpha_124(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_124 factor using the formula published by Guotai Junan Securities.

    (CLOSE-VWAP)/DECAYLINEAR(RANK(TSMAX(CLOSE,30)),2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_124 factor value of the last trading day in the series.
    """
    return -888


def alpha_125(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_125 factor using the formula published by Guotai Junan Securities.

    (RANK(DECAYLINEAR(CORR((VWAP),MEAN(VOLUME,80),17),20))/RANK(DECAYLINEAR(DELTA(((CLOSE*0.5)+(VWAP*0.5)),3),16)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_125 factor value of the last trading day in the series.
    """
    return -888


def alpha_126(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_126 factor using the formula published by Guotai Junan Securities.

    (CLOSE+HIGH+LOW)/3

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_126 factor value of the last trading day in the series.
    """
    return -888


def alpha_127(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_127 factor using the formula published by Guotai Junan Securities.

    (MEAN((100*(CLOSE-MAX(CLOSE,12))/(MAX(CLOSE,12)))^2))^(1/2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_127 factor value of the last trading day in the series.
    """
    return -888


def alpha_128(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_128 factor using the formula published by Guotai Junan Securities.

    100-(100/(1+SUM(((HIGH+LOW+CLOSE)/3>DELAY((HIGH+LOW+CLOSE)/3,1)?(HIGH+LOW+CLOSE)/3*VOLUM E:0),14)/SUM(((HIGH+LOW+CLOSE)/3\

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_128 factor value of the last trading day in the series.
    """
    return -888


def alpha_129(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_129 factor using the formula published by Guotai Junan Securities.

    SUM((CLOSE-DELAY(CLOSE,1)\<0?ABS(CLOSE-DELAY(CLOSE,1)):0),12)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_129 factor value of the last trading day in the series.
    """
    return -888


def alpha_130(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_130 factor using the formula published by Guotai Junan Securities.

    (RANK(DECAYLINEAR(CORR(((HIGH+LOW)/2),MEAN(VOLUME,40),9),10))/RANK(DECAYLINEAR(CORR(RANK(VWAP),RANK(VOLUME),7),3)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_130 factor value of the last trading day in the series.
    """
    return -888


def alpha_131(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_131 factor using the formula published by Guotai Junan Securities.

    (RANK(DELAT(VWAP,1))^TSRANK(CORR(CLOSE,MEAN(VOLUME,50),18),18))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_131 factor value of the last trading day in the series.
    """
    return -888


def alpha_132(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_132 factor using the formula published by Guotai Junan Securities.

    MEAN(AMOUNT,20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_132 factor value of the last trading day in the series.
    """
    return -888
