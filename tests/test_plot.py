import pytest
import pandas as pd
import numpy as np

from simplequant import plot_factor_matrix, plot_model_comparison


# ------------------------
# plot_factor_matrix tests
# ------------------------


def test_invalid_matrix_type():
    matrix = pd.DataFrame(np.eye(3), index=["A", "B", "C"], columns=["A", "B", "C"])
    with pytest.raises(ValueError, match="Invalid matrix_type"):
        plot_factor_matrix(matrix, "bad_type", "2025-08-01")


def test_non_square_matrix():
    matrix = pd.DataFrame(
        np.random.rand(2, 3), index=["A", "B"], columns=["A", "B", "C"]
    )
    with pytest.raises(ValueError, match="Matrix must be square"):
        plot_factor_matrix(matrix, "cov", "2025-08-01")


def test_index_column_mismatch():
    matrix = pd.DataFrame(np.eye(2), index=["X", "Y"], columns=["A", "B"])
    with pytest.raises(ValueError, match="Matrix index and columns must match"):
        plot_factor_matrix(matrix, "cov", "2025-08-01")


# ----------------------------
# plot_model_comparison tests
# ----------------------------


def test_invalid_metric_name():
    df = pd.DataFrame(
        {"Date": pd.date_range("2025-01-01", periods=3), "Model 1": [0.1, 0.2, 0.3]}
    ).set_index("Date")

    with pytest.raises(ValueError, match="Invalid metric 'bad_metric'"):
        plot_model_comparison(df, metric="bad_metric")
