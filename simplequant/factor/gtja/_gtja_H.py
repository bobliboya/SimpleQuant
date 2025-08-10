import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_085(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_085 factor using the formula published by Guotai Junan Securities.

    (TSRANK((VOLUME/MEAN(VOLUME,20)),20)*TSRANK((-1*DELTA(CLOSE,7)),8))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_085 factor value of the last trading day in the series.
    """
    return -888


def alpha_086(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_086 factor using the formula published by Guotai Junan Securities.

    ((0.25<(((DELAY(CLOSE,20)-DELAY(CLOSE,10))/10)-((DELAY(CLOSE,10)-CLOSE)/10)))?(-1*1):(((((DELAY(CLOSE,20)-DELAY(CLOSE,10))/10)-((DELAY(CLOSE,10)-CLOSE)/10))\<0)?1:((-1*1)*(CLOSE-DELAY(CLOSE,1)))))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_086 factor value of the last trading day in the series.
    """
    return -888


def alpha_087(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_087 factor using the formula published by Guotai Junan Securities.

    ((RANK(DECAYLINEAR(DELTA(VWAP,4),7))+TSRANK(DECAYLINEAR(((((LOW*0.9)+(LOW*0.1))-VWAP)/(OPEN-((HIGH+LOW)/2))),11),7))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_087 factor value of the last trading day in the series.
    """
    return -888


def alpha_088(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_088 factor using the formula published by Guotai Junan Securities.

    (CLOSE-DELAY(CLOSE,20))/DELAY(CLOSE,20)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_088 factor value of the last trading day in the series.
    """
    return -888


def alpha_089(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_089 factor using the formula published by Guotai Junan Securities.

    2*(SMA(CLOSE,13,2)-SMA(CLOSE,27,2)-SMA(SMA(CLOSE,13,2)-SMA(CLOSE,27,2),10,2))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_089 factor value of the last trading day in the series.
    """
    return -888


def alpha_090(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_090 factor using the formula published by Guotai Junan Securities.

    (RANK(CORR(RANK(VWAP),RANK(VOLUME),5))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_090 factor value of the last trading day in the series.
    """
    return -888


def alpha_091(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_091 factor using the formula published by Guotai Junan Securities.

    ((RANK((CLOSE-MAX(CLOSE,5)))RANK(CORR((MEAN(VOLUME,40)),LOW,5)))-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_091 factor value of the last trading day in the series.
    """
    return -888


def alpha_092(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_092 factor using the formula published by Guotai Junan Securities.

    (MAX(RANK(DECAYLINEAR(DELTA(((CLOSE*0.35)+(VWAP*0.65)),2),3)),TSRANK(DECAYLINEAR(ABS(CORR((MEAN(VOLUME,180)),CLOSE,13)),5),15))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_092 factor value of the last trading day in the series.
    """
    return -888


def alpha_093(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_093 factor using the formula published by Guotai Junan Securities.

    SUM((OPEN>=DELAY(OPEN,1)?0:MAX((OPEN-LOW),(OPEN-DELAY(OPEN,1)))),20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_093 factor value of the last trading day in the series.
    """
    return -888


def alpha_094(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_094 factor using the formula published by Guotai Junan Securities.

    SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),30)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_094 factor value of the last trading day in the series.
    """
    return -888


def alpha_095(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_095 factor using the formula published by Guotai Junan Securities.

    STD(AMOUNT,20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_095 factor value of the last trading day in the series.
    """
    return -888


def alpha_096(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_096 factor using the formula published by Guotai Junan Securities.

    SMA(SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1),3,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_096 factor value of the last trading day in the series.
    """
    return -888
