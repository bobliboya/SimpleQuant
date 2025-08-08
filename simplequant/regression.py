import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression


def evaluate_regression_model(
    y_true: np.ndarray, beta: np.ndarray, x: np.ndarray, plot: bool = False
) -> dict[str, float]:
    """
    Evaluate a linear regression model's performance given coefficients and features.

    This computes key error metrics between predicted and actual values.
    Ensure that the shape of `x` matches `beta`, especially regarding intercept terms.

    Args:
        y_true (np.ndarray): True target values, shape (n_samples,).
        beta (np.ndarray): Regression coefficients, shape (n_features,) or (1, n_features).
        x (np.ndarray): Feature matrix, shape (n_samples, n_features).
            If beta includes an intercept term, x should already be augmented with a column of ones.
        plot (bool): Whether to display a diagnostic plot. (Currently unimplemented)

    Returns:
        dict[str, float]: Dictionary containing:

            - "MSE": Mean Squared Error
            - "RMSE": Root Mean Squared Error
            - "MAE": Mean Absolute Error
            - "R2": R-squared score

    Raises:
        AssertionError: If x.shape[1] != beta.shape[-1]

    Notes:
        **Intercept Warning**: Ensure intercept is handled correctly. This function does not add intercept implicitly.
    """

    if not (x.shape[1] == beta.shape[-1]):
        raise ValueError(
            f"Invalid input Shape: beta and x must have the same number of features."
        )

    if not (x.shape[0] == y_true.shape[-1]):
        raise ValueError(
            f"Invalid input Shape: y_true and x must have the same number of samples."
        )

    y_pred = x @ beta.T
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    results = {"MSE": mse, "RMSE": rmse, "MAE": mae, "R2": r2}

    if plot:
        print("I will plot!")

    return results


def regress_model(
    y_true: np.ndarray, x: np.ndarray, fit_intercept: bool = False
) -> dict[str, float | np.ndarray]:
    """
    Fit a linear regression model and return coefficients, intercept, residuals, and metrics.

    Args:
        y_true (np.ndarray): Target values, shape (n_samples,).
        x (np.ndarray): Feature matrix, shape (n_samples, n_features).
        fit_intercept (bool): Whether to include an intercept term.

    Returns:
        dict[str, float | np.ndarray]: Dictionary containing:

            - "beta": Estimated regression coefficients
            - "intercept": Estimated intercept (0.0 if not used)
            - "residual": Vector of residuals (y_true - y_pred)
            - "MSE", "RMSE", "MAE", "R2": Standard regression metrics. See documentation for `evaluate_regression_model`.

    Notes:
        **Intercept Warning**: If `fit_intercept=True`, x will be augmented internally.
    """

    if not y_true.ndim == 1:
        raise ValueError(
            f"Invalid input Shape: y_true must be 1D array."
        )

    if not y_true.shape[-1] == x.shape[0]:
        raise ValueError(
            f"Invalid input Shape: y_true and x must have the same number of samples."
        )

    model = LinearRegression(fit_intercept=fit_intercept)
    model.fit(x, y_true)
    A = model.coef_
    c = model.intercept_ if fit_intercept else 0.0

    if fit_intercept:
        x_aug = np.hstack([x, np.ones((x.shape[0], 1))])
        y_pred = x_aug @ np.hstack([A, [c]])
    else:
        x_aug = x
        y_pred = x @ A

    residual = y_true - y_pred
    res = evaluate_regression_model(
        y_true=y_true,
        beta=A if not fit_intercept else np.hstack([A, [c]]),
        x=x_aug,
    )

    return {"beta": A, "intercept": c, "residual": residual} | res


def compute_correlation_from_covariance(df_cov: pd.DataFrame) -> pd.DataFrame:
    """
    Convert a covariance matrix to its corresponding correlation matrix.

    Args:
        df_cov (pd.DataFrame): Square covariance matrix with factor names
            as both index and columns. Must be symmetric and aligned.

    Returns:
        pd.DataFrame: Correlation matrix of same shape and labels (or smaller if dropped).

    Raises:
        ValueError: If input is not square with matching index and columns.

    Notes:
        - Zero variance entries (σ²=0) lead to correlation = 0 unless dropped.
        - Diagonal values are forcibly set to 1.0 for stability.
    """
    if not isinstance(df_cov, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if not df_cov.index.equals(df_cov.columns):
        print(df_cov)
        raise ValueError(
            "Covariance matrix must be square with identical index and columns."
        )

    # Compute standard deviations
    stddev = np.sqrt(np.diag(df_cov.values))  # shape: (n,)

    # Outer product of stddev for correlation denominator
    denominator = np.outer(stddev, stddev)

    # Suppress warnings for divide-by-zero; will handle manually
    with np.errstate(divide="ignore", invalid="ignore"):
        corr_values = df_cov.values / denominator

    # Construct DataFrame
    corr = pd.DataFrame(corr_values, index=df_cov.index, columns=df_cov.columns)

    # Fill undefined values with 0, then set diagonal to 1
    corr = corr.fillna(0.0)
    np.fill_diagonal(corr.values, 1.0)

    return corr


def neutralize_all_factors(
    factor_array: np.ndarray,
    exposure_matrix: np.ndarray,
    fit_intercept: bool = False,
    factor_names: list[str] | None = None,
    date_str: str | None = None,
    verbose: bool = False,
) -> np.ndarray:
    """
    Neutralize all factors in a matrix against the same exposure matrix, with robust handling.

    Args:
        factor_array (np.ndarray): Raw factor values, shape (n_samples, n_factors).
        exposure_matrix (np.ndarray): Exposure matrix (industry + style), shape (n_samples, n_features).
        fit_intercept (bool): Whether to include intercept in the regression.
        factor_names (list[str], optional): Names of the factors (for debugging).
        date_str (str, optional): Date string to include in logs.
        verbose (bool): Whether to print diagnostic logs.

    Returns:
        np.ndarray: Neutralized factor values (residuals), same shape as input.
    """
    n_samples, n_factors = factor_array.shape
    neutralized = np.empty_like(factor_array)

    for j in range(n_factors):
        y = factor_array[:, j]
        fname = factor_names[j] if factor_names else f"Factor{j}"

        # Handle NaN or Inf
        if np.isnan(y).any() or np.isinf(y).any():
            if verbose:
                print(
                    f"[Skip] {date_str or ''} {fname}: contains NaN or Inf → set to 0."
                )
            neutralized[:, j] = 0.0
            continue

        # Handle constant values (std = 0): keep as-is
        if np.allclose(y, y[0]):
            if verbose:
                print(
                    f"[Constant] {date_str or ''} {fname}: constant ({y[0]:.4f}) → residual = original value."
                )
            neutralized[:, j] = y  # retain original, since unexplainable by X
            continue

        # Handle extremely large values (overflow risk)
        if np.abs(y).max() > 1e10:
            if verbose:
                print(
                    f"[Clip] {date_str or ''} {fname}: max={np.max(np.abs(y)):.2e} → set to 0."
                )
            neutralized[:, j] = 0.0
            continue

        # Try standard regression
        try:
            res = regress_model(
                y_true=y, x=exposure_matrix, fit_intercept=fit_intercept
            )
            neutralized[:, j] = res["residual"]
        except Exception as e:
            if verbose:
                print(
                    f"[Error] {date_str or ''} {fname}: regression failed: {e} → set to 0."
                )
            neutralized[:, j] = 0.0

    return neutralized


__all__ = [
    "evaluate_regression_model",
    "regress_model",
    "compute_correlation_from_covariance",
    "neutralize_all_factors",
]
