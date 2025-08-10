import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_133(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_133 factor using the formula published by Guotai Junan Securities.

    ((20-HIGHDAY(HIGH,20))/20)*100-((20-LOWDAY(LOW,20))/20)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_133 factor value of the last trading day in the series.
    """
    return -888


def alpha_134(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_134 factor using the formula published by Guotai Junan Securities.

    (CLOSE-DELAY(CLOSE,12))/DELAY(CLOSE,12)*VOLUME

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_134 factor value of the last trading day in the series.
    """
    return -888


def alpha_135(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_135 factor using the formula published by Guotai Junan Securities.

    -SMA(DELAY(CLOSE/DELAY(CLOSE,20),1),20,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_135 factor value of the last trading day in the series.
    """
    return -888


def alpha_136(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_136 factor using the formula published by Guotai Junan Securities.

    ((-1*RANK(DELTA(RET,3)))*CORR(OPEN,VOLUME,10))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_136 factor value of the last trading day in the series.
    """
    return -888


def alpha_137(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_137 factor using the formula published by Guotai Junan Securities.

    16*(CLOSE-DELAY(CLOSE,1)+(CLOSE-OPEN)/2+DELAY(CLOSE,1)-DELAY(OPEN,1))/((ABS(HIGH-DELAY(CLOSE,1))>ABS(LOW-DELAY(CLOSE,1)) &ABS(HIGH-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))?ABS(HIGH-DELAY(CLOSE,1))+ABS(LOW-DELAY(CLOSE,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:(ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1)) & ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(CLOSE,1))?ABS(LOW-DELAY(CLOSE,1))+ABS(HIGH-DELAY(CLOSE,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:ABS(HIGH-DELAY(LOW,1))+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4)))*MAX(ABS(HIGH-DELAY(CLOSE,1)),ABS(LOW-DELAY(CLOSE,1)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_137 factor value of the last trading day in the series.
    """
    return -888


def alpha_138(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_138 factor using the formula published by Guotai Junan Securities.

    ((RANK(DECAYLINEAR(DELTA((((LOW*0.7)+(VWAP*0.3))),3),20))-TSRANK(DECAYLINEAR(TSRANK(CORR(TSRANK(LOW,8),TSRANK(MEAN(VOLUME,60),17),5),19),16),7))* -1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_138 factor value of the last trading day in the series.
    """
    return -888


def alpha_139(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_139 factor using the formula published by Guotai Junan Securities.

    (-1*CORR(OPEN,VOLUME,10))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_139 factor value of the last trading day in the series.
    """
    return -888


def alpha_140(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_140 factor using the formula published by Guotai Junan Securities.

    MIN(RANK(DECAYLINEAR(((RANK(OPEN)+RANK(LOW))-(RANK(HIGH)+RANK(CLOSE))),8)),TSRANK(DECAYLINEAR(CORR(TSRANK(CLOSE,8),TSRANK(MEAN(VOLUME,60),20),8),7),3))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_140 factor value of the last trading day in the series.
    """
    return -888


def alpha_141(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_141 factor using the formula published by Guotai Junan Securities.

    (RANK(CORR(RANK(HIGH),RANK(MEAN(VOLUME,15)),9))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_141 factor value of the last trading day in the series.
    """
    return -888


def alpha_142(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_142 factor using the formula published by Guotai Junan Securities.

    (((-1*RANK(TSRANK(CLOSE,10)))*RANK(DELTA(DELTA(CLOSE,1),1)))*RANK(TSRANK((VOLUME/MEAN(VOLUME,20)),5)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_142 factor value of the last trading day in the series.
    """
    return -888


def alpha_143(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_143 factor using the formula published by Guotai Junan Securities.

    CLOSE>DELAY(CLOSE,1)?(CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)*SELF:SELF

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_143 factor value of the last trading day in the series.
    """
    return -888


def alpha_144(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_144 factor using the formula published by Guotai Junan Securities.

    SUMIF(ABS(CLOSE/DELAY(CLOSE,1)-1)/AMOUNT,20,CLOSE<DELAY(CLOSE,1))/COUNT(CLOSE<DELAY(CLOSE,1),20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_144 factor value of the last trading day in the series.
    """
    return -888
