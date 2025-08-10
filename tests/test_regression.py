import pytest
import numpy as np
from simplequant import (
    evaluate_regression_model,
    regress_model,
    compute_correlation_from_covariance,
    neutralize_all_factors,
)


def test_evaluate_regression_model_error_1():
    """
    Number of coefficients and number of features does not match
    """
    y_true = np.array([1, 2, 3, 4, 5])
    beta = np.array([1, 2, 3, 4])
    x = np.ones(shape=(5, 5))
    with pytest.raises(
        ValueError,
        match=r"beta and x must have the same number of features; "
        r"got beta\.shape=\(\d+,\), x\.shape=\(\d+, \d+\)",
    ):
        evaluate_regression_model(y_true, beta, x)


def test_evaluate_regression_model_error_2():
    """
    Number of samples in y_true and x does not match
    """
    y_true = np.array([1, 2, 3, 4])
    beta = np.array([1, 2, 3, 4, 5])
    x = np.ones(shape=(5, 5))
    with pytest.raises(
        ValueError,
        match=r"y_true and x must have the same number of samples; "
        r"got y_true\.shape=\(\d+,\), x\.shape=\(\d+, \d+\)",
    ):
        evaluate_regression_model(y_true, beta, x)


def test_evaluate_regression_model_correct():
    """
    Correct regression model
    """
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
        ValueError, match=r"y_true must be 1-D; got ndim=\d+, shape=\(.+\)\."
    ):
        regress_model(y_true, x)


def test_regress_model_error_2():
    y_true = np.array([1, 2, 3, 4, 5])
    x = np.ones(4)
    with pytest.raises(
        ValueError,
        match=r"x must be 2-D \(n_samples, n_features\); got ndim=\d+, shape=\(.+\)\.",
    ):
        regress_model(y_true, x)


def test_regress_model_error_3():
    y_true = np.array([1, 2, 3, 4, 5])
    x = np.eye(4)
    with pytest.raises(
        ValueError,
        match=r"y_true and x must have the same number of samples; got len\(y_true\)=\d+ vs x\.shape\[0\]=\d+\.",
    ):
        regress_model(y_true, x)


def test_regress_model_correct():
    y_true = np.array([0.7, 2.4, 3.3, 2.1, 4.6])
    x = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 3.0], [4.0, 5.0], [5.0, 4.0]])
    res = regress_model(y_true, x, fit_intercept=True)
    assert res["beta"] == pytest.approx(np.array([1.35, -0.75]), abs=1e-4)
    assert res["intercept"] == pytest.approx(0.8200, abs=1e-4)
    assert res["R2"] == pytest.approx(0.9120, abs=1e-4)
