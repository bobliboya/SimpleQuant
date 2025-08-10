import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_157(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_157 factor using the formula published by Guotai Junan Securities.

    (MIN(PROD(RANK(RANK(LOG(SUM(TSMIN(RANK(RANK((-1*RANK(DELTA((CLOSE-1),5))))),2),1)))),1),5) +TSRANK(DELAY((-1*RET),6),5))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_157 factor value of the last trading day in the series.
    """
    return -888


def alpha_158(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_158 factor using the formula published by Guotai Junan Securities.

    ((HIGH-SMA(CLOSE,15,2))-(LOW-SMA(CLOSE,15,2)))/CLOSE

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_158 factor value of the last trading day in the series.
    """
    return -888


def alpha_159(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_159 factor using the formula published by Guotai Junan Securities.

    ((CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),6))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,DELAY(CLOSE,1)),6)*12*24+(CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),12))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,DELAY(CL OSE,1)),12)*6*24+(CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),24))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,D ELAY(CLOSE,1)),24)*6*24)*100/(6*12+6*24+12*24)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_159 factor value of the last trading day in the series.
    """
    return -888


def alpha_160(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_160 factor using the formula published by Guotai Junan Securities.

    SMA((CLOSE<=DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_160 factor value of the last trading day in the series.
    """
    return -888


def alpha_161(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_161 factor using the formula published by Guotai Junan Securities.

    MEAN(MAX(MAX((HIGH-LOW),ABS(DELAY(CLOSE,1)-HIGH)),ABS(DELAY(CLOSE,1)-LOW)),12)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_161 factor value of the last trading day in the series.
    """
    return -888


def alpha_162(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_162 factor using the formula published by Guotai Junan Securities.

    (SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100-MIN(SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12))/(MAX(SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12)-MIN(SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12, 1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_162 factor value of the last trading day in the series.
    """
    return -888


def alpha_163(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_163 factor using the formula published by Guotai Junan Securities.

    RANK(((((-1*RET)MEAN(VOLUME,20))*VWAP)(HIGH-CLOSE)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_163 factor value of the last trading day in the series.
    """
    return -888


def alpha_164(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_164 factor using the formula published by Guotai Junan Securities.

    SMA((((CLOSE>DELAY(CLOSE,1))?1/(CLOSE-DELAY(CLOSE,1)):1)-MIN(((CLOSE>DELAY(CLOSE,1))?1/(CLOSE-D ELAY(CLOSE,1)):1),12))/(HIGH-LOW)*100,13,2)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_164 factor value of the last trading day in the series.
    """
    return -888


def alpha_165(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_165 factor using the formula published by Guotai Junan Securities.

    MAX(SUMAC(CLOSE-MEAN(CLOSE,48)))-MIN(SUMAC(CLOSE-MEAN(CLOSE,48)))/STD(CLOSE,48)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_165 factor value of the last trading day in the series.
    """
    return -888


def alpha_166(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_166 factor using the formula published by Guotai Junan Securities.

    -20*(20-1)^1.5*SUM(CLOSE/DELAY(CLOSE,1)-1-MEAN(CLOSE/DELAY(CLOSE,1)-1,20),20)/((20-1)*(20-2)(SUM((CLOSE/DELAY(CLOSE,1),20)^2,20))^1.5)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_166 factor value of the last trading day in the series.
    """
    return -888


def alpha_167(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_167 factor using the formula published by Guotai Junan Securities.

    SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_167 factor value of the last trading day in the series.
    """
    return -888


def alpha_168(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_168 factor using the formula published by Guotai Junan Securities.

    (-1*VOLUME/MEAN(VOLUME,20))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_168 factor value of the last trading day in the series.
    """
    return -888
