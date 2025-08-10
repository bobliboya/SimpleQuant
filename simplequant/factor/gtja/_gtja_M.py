import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_145(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_145 factor using the formula published by Guotai Junan Securities.

    (MEAN(VOLUME,9)-MEAN(VOLUME,26))/MEAN(VOLUME,12)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_145 factor value of the last trading day in the series.
    """
    return -888


def alpha_146(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_146 factor using the formula published by Guotai Junan Securities.

    MEAN((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2),20)*(( CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2))/SMA(((CLOS E-DELAY(CLOSE,1))/DELAY(CLOSE,1)-((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2)))^2,60);

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_146 factor value of the last trading day in the series.
    """
    return -888


def alpha_147(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_147 factor using the formula published by Guotai Junan Securities.

    REGBETA(MEAN(CLOSE,12),SEQUENCE(12))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_147 factor value of the last trading day in the series.
    """
    return -888


def alpha_148(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_148 factor using the formula published by Guotai Junan Securities.

    ((RANK(CORR((OPEN),SUM(MEAN(VOLUME,60),9),6))<RANK((OPEN-TSMIN(OPEN,14))))*-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_148 factor value of the last trading day in the series.
    """
    return -888


def alpha_149(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_149 factor using the formula published by Guotai Junan Securities.

    REGBETA(FILTER(CLOSE/DELAY(CLOSE,1)-1,BANCHMARKINDEXCLOSE<DELAY(BANCHMARKINDEXCLOSE,1)),FILTER(BANCHMARKINDEXCLOSE/DELAY(BANCHMARKINDEXCLOSE,1)-1,BANCHMARKINDEXCLOSE<DELAY(BANCHMARKINDEXCLOSE,1)),252)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_149 factor value of the last trading day in the series.
    """
    return -888


def alpha_150(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_150 factor using the formula published by Guotai Junan Securities.

    (CLOSE+HIGH+LOW)/3*VOLUME

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_150 factor value of the last trading day in the series.
    """
    return -888


def alpha_151(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_151 factor using the formula published by Guotai Junan Securities.

    SMA(CLOSE-DELAY(CLOSE,20),20,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_151 factor value of the last trading day in the series.
    """
    return -888


def alpha_152(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_152 factor using the formula published by Guotai Junan Securities.

    SMA(MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,9),1),9,1),1),12)-MEAN(DELAY(SMA(DELAY(CLOSE/DELAY (CLOSE,9),1),9,1),1),26),9,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_152 factor value of the last trading day in the series.
    """
    return -888


def alpha_153(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_153 factor using the formula published by Guotai Junan Securities.

    (MEAN(CLOSE,3)+MEAN(CLOSE,6)+MEAN(CLOSE,12)+MEAN(CLOSE,24))/4

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_153 factor value of the last trading day in the series.
    """
    return -888


def alpha_154(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_154 factor using the formula published by Guotai Junan Securities.

    (((VWAP-MIN(VWAP,16)))<(CORR(VWAP,MEAN(VOLUME,180),18)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_154 factor value of the last trading day in the series.
    """
    return -888


def alpha_155(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_155 factor using the formula published by Guotai Junan Securities.

    SMA(VOLUME,13,2)-SMA(VOLUME,27,2)-SMA(SMA(VOLUME,13,2)-SMA(VOLUME,27,2),10,2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_155 factor value of the last trading day in the series.
    """
    return -888


def alpha_156(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_156 factor using the formula published by Guotai Junan Securities.

    (MAX(RANK(DECAYLINEAR(DELTA(VWAP,5),3)),RANK(DECAYLINEAR(((DELTA(((OPEN*0.15)+(LOW*0.85)),2)/((OPEN*0.15)+(LOW*0.85)))-1),3)))-1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_156 factor value of the last trading day in the series.
    """
    return -888
