import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_061(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_061 factor using the formula published by Guotai Junan Securities.

    (MAX(RANK(DECAYLINEAR(DELTA(VWAP,1),12)),RANK(DECAYLINEAR(RANK(CORR((LOW),MEAN(VOLUME,80),8)),17)))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_061 factor value of the last trading day in the series.
    """
    return -888


def alpha_062(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_062 factor using the formula published by Guotai Junan Securities.

    (-1*CORR(HIGH,RANK(VOLUME),5))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_062 factor value of the last trading day in the series.
    """
    return -888


def alpha_063(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_063 factor using the formula published by Guotai Junan Securities.

    SMA(MAX(CLOSE-DELAY(CLOSE,1),0),6,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),6,1)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_063 factor value of the last trading day in the series.
    """
    return -888


def alpha_064(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_064 factor using the formula published by Guotai Junan Securities.

    (MAX(RANK(DECAYLINEAR(CORR(RANK(VWAP),RANK(VOLUME),4),4)),RANK(DECAYLINEAR(MAX(CORR(RANK(CLOSE),RANK(MEAN(VOLUME,60)),4),13),14)))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_064 factor value of the last trading day in the series.
    """
    return -888


def alpha_065(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_065 factor using the formula published by Guotai Junan Securities.

    MEAN(CLOSE,6)/CLOSE

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_065 factor value of the last trading day in the series.
    """
    return -888


def alpha_066(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_066 factor using the formula published by Guotai Junan Securities.

    (CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_066 factor value of the last trading day in the series.
    """
    return -888


def alpha_067(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_067 factor using the formula published by Guotai Junan Securities.

    SMA(MAX(CLOSE-DELAY(CLOSE,1),0),24,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),24,1)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_067 factor value of the last trading day in the series.
    """
    return -888


def alpha_068(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_068 factor using the formula published by Guotai Junan Securities.

    SMA(((HIGH+LOW)/2-(DELAY(HIGH,1)+DELAY(LOW,1))/2)*(HIGH-LOW)/VOLUME,15,2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_068 factor value of the last trading day in the series.
    """
    return -888


def alpha_069(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_069 factor using the formula published by Guotai Junan Securities.

    (SUM(DTM,20)>SUM(DBM,20)?(SUM(DTM,20)-SUM(DBM,20))/SUM(DTM,20):(SUM(DTM,20)=SUM(DBM,20)?0:(SUM(DTM,20)-SUM(DBM,20))/SUM(DBM,20)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_069 factor value of the last trading day in the series.
    """
    return -888


def alpha_070(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_070 factor using the formula published by Guotai Junan Securities.

    STD(AMOUNT,6)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_070 factor value of the last trading day in the series.
    """
    return -888


def alpha_071(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_071 factor using the formula published by Guotai Junan Securities.

    (CLOSE-MEAN(CLOSE,24))/MEAN(CLOSE,24)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_071 factor value of the last trading day in the series.
    """
    return -888


def alpha_072(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_072 factor using the formula published by Guotai Junan Securities.

    SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,15,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_072 factor value of the last trading day in the series.
    """
    return -888
