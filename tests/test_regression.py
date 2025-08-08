import pytest
import numpy as np
from simplequant import (
    evaluate_regression_model,
    regress_model,
    compute_correlation_from_covariance,
    neutralize_all_factors,
)


def test_evaluate_regression_model_error_1():
    # Number coefficients and number of features does not match
    y_true = np.array([1, 2, 3, 4, 5])
    beta = np.array([1, 2, 3, 4])
    x = np.ones(shape=(5, 5))
    with pytest.raises(
        ValueError,
        match="Invalid input Shape: beta and x must have the same number of features.",
    ):
        evaluate_regression_model(y_true, beta, x)


def test_evaluate_regression_model_error_2():
    # Number of samples of the sample and training does not match
    y_true = np.array([1, 2, 3, 4])
    beta = np.array([1, 2, 3, 4, 5])
    x = np.ones(shape=(5, 5))
    with pytest.raises(
        ValueError,
        match="Invalid input Shape: y_true and x must have the same number of samples.",
    ):
        evaluate_regression_model(y_true, beta, x)


def test_evaluate_regression_model_correct():
    # Testing the correct evaluation of a regression model
    y_true = np.array([0.7, 2.4, 3.3, 2.1, 4.6])
    beta = np.array([1.5, -0.5])
    x = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 3.0], [4.0, 5.0], [5.0, 4.0]])
    res = evaluate_regression_model(y_true, beta, x)
    assert res["MSE"] == pytest.approx(0.5820, abs=1e-4)
    assert res["RMSE"] == pytest.approx(0.7629, abs=1e-4)
    assert res["MAE"] == pytest.approx(0.5800, abs=1e-4)
    assert res["R2"] == pytest.approx(0.6531, abs=1e-4)


def test_regress_model_error_1():
    y_true = np.array([[1, 2, 3, 4, 5]])
    x = np.eye(5)
    with pytest.raises(
        ValueError,
        match=f"Invalid input Shape: y_true must be 1D array."
    ):
        regress_model(y_true, x)


def test_regress_model_error_2():
    y_true = np.array([1, 2, 3, 4, 5])
    x = np.eye(4)
    with pytest.raises(
        ValueError,
        match=f"Invalid input Shape: y_true and x must have the same number of samples."
    ):
        regress_model(y_true, x)