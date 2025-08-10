import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_097(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_097 factor using the formula published by Guotai Junan Securities.

    STD(VOLUME,10)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_097 factor value of the last trading day in the series.
    """
    return -888


def alpha_098(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_098 factor using the formula published by Guotai Junan Securities.

    ((((DELTA((SUM(CLOSE,100)/100),100)/DELAY(CLOSE,100))\<0.05)||((DELTA((SUM(CLOSE,100)/100),100)/DELAY(CLOSE,100))==0.05))?(-1*(CLOSE-TSMIN(CLOSE,100))):(-1*DELTA(CLOSE,3)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_098 factor value of the last trading day in the series.
    """
    return -888


def alpha_099(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_099 factor using the formula published by Guotai Junan Securities.

    (-1*RANK(COVIANCE(RANK(CLOSE),RANK(VOLUME),5)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_099 factor value of the last trading day in the series.
    """
    return -888


def alpha_100(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_100 factor using the formula published by Guotai Junan Securities.

    STD(VOLUME,20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_100 factor value of the last trading day in the series.
    """
    return -888


def alpha_101(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_101 factor using the formula published by Guotai Junan Securities.

    ((RANK(CORR(CLOSE,SUM(MEAN(VOLUME,30),37),15))\

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_101 factor value of the last trading day in the series.
    """
    return -888


def alpha_102(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_102 factor using the formula published by Guotai Junan Securities.

    SMA(MAX(VOLUME-DELAY(VOLUME,1),0),6,1)/SMA(ABS(VOLUME-DELAY(VOLUME,1)),6,1)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_102 factor value of the last trading day in the series.
    """
    return -888


def alpha_103(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_103 factor using the formula published by Guotai Junan Securities.

    ((20-LOWDAY(LOW,20))/20)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_103 factor value of the last trading day in the series.
    """
    return -888


def alpha_104(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_104 factor using the formula published by Guotai Junan Securities.

    (-1*(DELTA(CORR(HIGH,VOLUME,5),5)*RANK(STD(CLOSE,20))))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_104 factor value of the last trading day in the series.
    """
    return -888


def alpha_105(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_105 factor using the formula published by Guotai Junan Securities.

    (-1*CORR(RANK(OPEN),RANK(VOLUME),10))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_105 factor value of the last trading day in the series.
    """
    return -888


def alpha_106(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_106 factor using the formula published by Guotai Junan Securities.

    CLOSE-DELAY(CLOSE,20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_106 factor value of the last trading day in the series.
    """
    return -888


def alpha_107(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_107 factor using the formula published by Guotai Junan Securities.

    (((-1*RANK((OPEN-DELAY(HIGH,1))))*RANK((OPEN-DELAY(CLOSE,1))))*RANK((OPEN-DELAY(LOW,1))))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_107 factor value of the last trading day in the series.
    """
    return -888


def alpha_108(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_108 factor using the formula published by Guotai Junan Securities.

    ((RANK((HIGH-MIN(HIGH,2)))^RANK(CORR((VWAP),(MEAN(VOLUME,120)),6)))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_108 factor value of the last trading day in the series.
    """
    return -888
