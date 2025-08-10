import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_073(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_073 factor using the formula published by Guotai Junan Securities.

    ((TSRANK(DECAYLINEAR(DECAYLINEAR(CORR((CLOSE),VOLUME,10),16),4),5)-RANK(DECAYLINEAR(CORR(VWAP,MEAN(VOLUME,30),4),3)))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_073 factor value of the last trading day in the series.
    """
    return -888


def alpha_074(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_074 factor using the formula published by Guotai Junan Securities.

    (RANK(CORR(SUM(((LOW*0.35)+(VWAP*0.65)),20),SUM(MEAN(VOLUME,40),20),7))+RANK(CORR(RANK(VWAP),RANK(VOLUME),6)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_074 factor value of the last trading day in the series.
    """
    return -888


def alpha_075(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_075 factor using the formula published by Guotai Junan Securities.

    BANCHMARKINDEXCLOSE<BANCHMARKINDEXOPEN,50)/COUNT(BANCHMARKINDEXCLOSE<BANCHMARKIN DEXOPEN,50)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_075 factor value of the last trading day in the series.
    """
    return -888


def alpha_076(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_076 factor using the formula published by Guotai Junan Securities.

    STD(ABS((CLOSE/DELAY(CLOSE,1)-1))/VOLUME,20)/MEAN(ABS((CLOSE/DELAY(CLOSE,1)-1))/VOLUME,20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_076 factor value of the last trading day in the series.
    """
    return -888


def alpha_077(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_077 factor using the formula published by Guotai Junan Securities.

    MIN(RANK(DECAYLINEAR(((((HIGH+LOW)/2)+HIGH)-(VWAP+HIGH)),20)),RANK(DECAYLINEAR(CORR(((HIGH+LOW)/2),MEAN(VOLUME,40),3),6)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_077 factor value of the last trading day in the series.
    """
    return -888


def alpha_078(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_078 factor using the formula published by Guotai Junan Securities.

    ((HIGH+LOW+CLOSE)/3-MA((HIGH+LOW+CLOSE)/3,12))/(0.015*MEAN(ABS(CLOSE-MEAN((HIGH+LOW+CLOSE)/3,12)),12))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_078 factor value of the last trading day in the series.
    """
    return -888


def alpha_079(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_079 factor using the formula published by Guotai Junan Securities.

    SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_079 factor value of the last trading day in the series.
    """
    return -888


def alpha_080(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_080 factor using the formula published by Guotai Junan Securities.

    (VOLUME-DELAY(VOLUME,5))/DELAY(VOLUME,5)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_080 factor value of the last trading day in the series.
    """
    return -888


def alpha_081(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_081 factor using the formula published by Guotai Junan Securities.

    SMA(VOLUME,21,2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_081 factor value of the last trading day in the series.
    """
    return -888


def alpha_082(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_082 factor using the formula published by Guotai Junan Securities.

    SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,20,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_082 factor value of the last trading day in the series.
    """
    return -888


def alpha_083(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_083 factor using the formula published by Guotai Junan Securities.

    (-1*RANK(COVIANCE(RANK(HIGH),RANK(VOLUME),5)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_083 factor value of the last trading day in the series.
    """
    return -888


def alpha_084(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_084 factor using the formula published by Guotai Junan Securities.

    SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_084 factor value of the last trading day in the series.
    """
    return -888
