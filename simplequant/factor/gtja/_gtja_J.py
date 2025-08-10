import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_109(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_109 factor using the formula published by Guotai Junan Securities.

    SMA(HIGH-LOW,10,2)/SMA(SMA(HIGH-LOW,10,2),10,2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_109 factor value of the last trading day in the series.
    """
    return -888


def alpha_110(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_110 factor using the formula published by Guotai Junan Securities.

    SUM(MAX(0,HIGH-DELAY(CLOSE,1)),20)/SUM(MAX(0,DELAY(CLOSE,1)-LOW),20)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_110 factor value of the last trading day in the series.
    """
    return -888


def alpha_111(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_111 factor using the formula published by Guotai Junan Securities.

    SMA(VOL*((CLOSE-LOW)-(HIGH-CLOSE))/(HIGH-LOW),11,2)-SMA(VOL*((CLOSE-LOW)-(HIGH-CLOSE))/(HIGH-LOW),4,2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_111 factor value of the last trading day in the series.
    """
    return -888


def alpha_112(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_112 factor using the formula published by Guotai Junan Securities.

    (SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)-SUM((CLOSE-DELAY(CLOSE,1)\<0?ABS(CLOS E-DELAY(CLOSE,1)):0),12))/(SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)+SUM((CLOSE-DE LAY(CLOSE,1)\<0?ABS(CLOSE-DELAY(CLOSE,1)):0),12))*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_112 factor value of the last trading day in the series.
    """
    return -888


def alpha_113(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_113 factor using the formula published by Guotai Junan Securities.

    (-1*((RANK((SUM(DELAY(CLOSE,5),20)/20))*CORR(CLOSE,VOLUME,2))*RANK(CORR(SUM(CLOSE,5),SUM(CLOSE,20),2))))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_113 factor value of the last trading day in the series.
    """
    return -888


def alpha_114(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_114 factor using the formula published by Guotai Junan Securities.

    ((RANK(DELAY(((HIGH-LOW)/(SUM(CLOSE,5)/5)),2))*RANK(RANK(VOLUME)))/(((HIGH-LOW)/(SUM(CLOSE,5)/5))/(VWAP-CLOSE)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_114 factor value of the last trading day in the series.
    """
    return -888


def alpha_115(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_115 factor using the formula published by Guotai Junan Securities.

    (RANK(CORR(((HIGH*0.9)+(CLOSE*0.1)),MEAN(VOLUME,30),10))^RANK(CORR(TSRANK(((HIGH+LOW)/2),4),TSRANK(VOLUME,10),7)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_115 factor value of the last trading day in the series.
    """
    return -888


def alpha_116(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_116 factor using the formula published by Guotai Junan Securities.

    REGBETA(CLOSE,SEQUENCE,20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_116 factor value of the last trading day in the series.
    """
    return -888


def alpha_117(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_117 factor using the formula published by Guotai Junan Securities.

    ((TSRANK(VOLUME,32)(1-TSRANK(((CLOSE+HIGH)-LOW),16)))(1-TSRANK(RET,32)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_117 factor value of the last trading day in the series.
    """
    return -888


def alpha_118(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_118 factor using the formula published by Guotai Junan Securities.

    SUM(HIGH-OPEN,20)/SUM(OPEN-LOW,20)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_118 factor value of the last trading day in the series.
    """
    return -888


def alpha_119(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_119 factor using the formula published by Guotai Junan Securities.

    (RANK(DECAYLINEAR(CORR(VWAP,SUM(MEAN(VOLUME,5),26),5),7))-RANK(DECAYLINEAR(TSRANK(MIN(CORR(RANK(OPEN),RANK(MEAN(VOLUME,15)),21),9),7),8)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_119 factor value of the last trading day in the series.
    """
    return -888


def alpha_120(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_120 factor using the formula published by Guotai Junan Securities.

    (RANK((VWAP-CLOSE))/RANK((VWAP+CLOSE)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_120 factor value of the last trading day in the series.
    """
    return -888
