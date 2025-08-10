import pandas as _pd
import numpy as _np
from scipy.stats import rankdata as _rankdata


def alpha_181(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_181 factor using the formula published by Guotai Junan Securities.

    SUM(((CLOSE/DELAY(CLOSE,1)-1)-MEAN((CLOSE/DELAY(CLOSE,1)-1),20))-(BANCHMARKINDEXCLOSE-MEAN(BANCHMARKINDEXCLOSE,20))^2,20)/SUM((BANCHMARKINDEXCLOSE-MEAN(BANCHMARKINDEXCLOSE,20))^3)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_181 factor value of the last trading day in the series.
    """
    return -888


def alpha_182(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_182 factor using the formula published by Guotai Junan Securities.

    COUNT((CLOSE>OPEN&BANCHMARKINDEXCLOSE>BANCHMARKINDEXOPEN)OR(CLOSE<OPEN&BANCHMARKINDEXCLOSE<BANCHMARKINDEXOPEN),20)/20

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_182 factor value of the last trading day in the series.
    """
    return -888


def alpha_183(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_183 factor using the formula published by Guotai Junan Securities.

    MAX(SUMAC(CLOSE-MEAN(CLOSE,24)))-MIN(SUMAC(CLOSE-MEAN(CLOSE,24)))/STD(CLOSE,24)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_183 factor value of the last trading day in the series.
    """
    return -888


def alpha_184(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_184 factor using the formula published by Guotai Junan Securities.

    (RANK(CORR(DELAY((OPEN-CLOSE),1),CLOSE,200))+RANK((OPEN-CLOSE)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_184 factor value of the last trading day in the series.
    """
    return -888


def alpha_185(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_185 factor using the formula published by Guotai Junan Securities.

    RANK((-1*((1-(OPEN/CLOSE))^2)))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_185 factor value of the last trading day in the series.
    """
    return -888


def alpha_186(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_186 factor using the formula published by Guotai Junan Securities.

    (MEAN(ABS(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6)+DELAY(MEAN(ABS(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6),6))/2

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_186 factor value of the last trading day in the series.
    """
    return -888


def alpha_187(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_187 factor using the formula published by Guotai Junan Securities.

    SUM((OPEN<=DELAY(OPEN,1)?0:MAX((HIGH-OPEN),(OPEN-DELAY(OPEN,1)))),20)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_187 factor value of the last trading day in the series.
    """
    return -888


def alpha_188(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_188 factor using the formula published by Guotai Junan Securities.

    ((HIGH-LOW–SMA(HIGH-LOW,11,2))/SMA(HIGH-LOW,11,2))*100

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_188 factor value of the last trading day in the series.
    """
    return -888


def alpha_189(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_189 factor using the formula published by Guotai Junan Securities.

    MEAN(ABS(CLOSE-MEAN(CLOSE,6)),6)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_189 factor value of the last trading day in the series.
    """
    return -888


def alpha_190(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_190 factor using the formula published by Guotai Junan Securities.

    （公式有部分缺失 有调整） 原公式: LOG((COUNT(CLOSE/DELAY(CLOSE)-1>((CLOSE/DELAY(CLOSE,19))^(1/20)-1),20)-1)(SUMIF(((CLOSE/DELAY(CLOSE)-1-(CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)-1))/((COUNT((CLOSE/DELAY(CLOSE)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)-1),20))(SUMIF((CLOSE/DELAY(CLOSE)-1-((CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE)-1>(CLOSE/DELAY(CLOSE,19))^(1/20)-1)))) 修改后公式: LOG((COUNT(CLOSE/DELAY(CLOSE,1)-1>((CLOSE/DELAY(CLOSE,19))^(1/20)-1),20)-1)(SUMIF(((CLOSE/DELAY(CLOSE,1)-1-(CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE,1)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)-1))/((COUNT((CLOSE/DELAY(CLOSE,1)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)-1),20))(SUMIF((CLOSE/DELAY(CLOSE,1)-1-((CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE,1)-1>(CLOSE/DELAY(CLOSE,19))^(1/20)-1))))

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_190 factor value of the last trading day in the series.
    """
    return -888


def alpha_191(sub_df: _pd.DataFrame) -> float:
    """
    Compute the ALPHA_191 factor using the formula published by Guotai Junan Securities.

    ((CORR(MEAN(VOLUME,20),LOW,5)+((HIGH+LOW)/2))-CLOSE)

    Args:
        sub_df (_pd.DataFrame): Dataframe of parameters of a series of trading dates one a single security.

    Returns:
        float: The ALPHA_191 factor value of the last trading day in the series.
    """
    return -888
