import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_169(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_169 factor using the formula published by Guotai Junan Securities.

    SMA(MEAN(DELAY(SMA(CLOSE-DELAY(CLOSE,1),9,1),1),12)-MEAN(DELAY(SMA(CLOSE-DELAY(CLOSE,1),9,1),1), 26),10,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_169 factor value of the last trading day in the series.
    """
    return -888


def alpha_170(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_170 factor using the formula published by Guotai Junan Securities.

    ((((RANK((1/CLOSE))VOLUME)/MEAN(VOLUME,20))((HIGH*RANK((HIGH-CLOSE)))/(SUM(HIGH,5)/5)))-RANK((VWAP-DELAY(VWAP,5))))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_170 factor value of the last trading day in the series.
    """
    return -888


def alpha_171(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_171 factor using the formula published by Guotai Junan Securities.

    ((-1*((LOW-CLOSE)(OPEN^5)))/((CLOSE-HIGH)(CLOSE^5)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_171 factor value of the last trading day in the series.
    """
    return -888


def alpha_172(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_172 factor using the formula published by Guotai Junan Securities.

    MEAN(ABS(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_172 factor value of the last trading day in the series.
    """
    return -888


def alpha_173(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_173 factor using the formula published by Guotai Junan Securities.

    3*SMA(CLOSE,13,2)-2*SMA(SMA(CLOSE,13,2),13,2)+SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2);

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_173 factor value of the last trading day in the series.
    """
    return -888


def alpha_174(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_174 factor using the formula published by Guotai Junan Securities.

    SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_174 factor value of the last trading day in the series.
    """
    return -888


def alpha_175(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_175 factor using the formula published by Guotai Junan Securities.

    MEAN(MAX(MAX((HIGH-LOW),ABS(DELAY(CLOSE,1)-HIGH)),ABS(DELAY(CLOSE,1)-LOW)),6)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_175 factor value of the last trading day in the series.
    """
    return -888


def alpha_176(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_176 factor using the formula published by Guotai Junan Securities.

    CORR(RANK(((CLOSE-TSMIN(LOW,12))/(TSMAX(HIGH,12)-TSMIN(LOW,12)))),RANK(VOLUME),6)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_176 factor value of the last trading day in the series.
    """
    return -888


def alpha_177(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_177 factor using the formula published by Guotai Junan Securities.

    ((20-HIGHDAY(HIGH,20))/20)*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_177 factor value of the last trading day in the series.
    """
    return -888


def alpha_178(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_178 factor using the formula published by Guotai Junan Securities.

    (CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)*VOLUME

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_178 factor value of the last trading day in the series.
    """
    return -888


def alpha_179(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_179 factor using the formula published by Guotai Junan Securities.

    (RANK(CORR(VWAP,VOLUME,4))*RANK(CORR(RANK(LOW),RANK(MEAN(VOLUME,50)),12)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_179 factor value of the last trading day in the series.
    """
    return -888


def alpha_180(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_180 factor using the formula published by Guotai Junan Securities.

    ((MEAN(VOLUME,20)<VOLUME)?((-1*TSRANK(ABS(DELTA(CLOSE,7)),60))*SIGN(DELTA(CLOSE,7)):(-1*VOLUME)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_180 factor value of the last trading day in the series.
    """
    return -888
