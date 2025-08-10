import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, Tuple, Optional, Literal, List
import os

GLOBAL_DPI = 120
MARKERS = ["o"]
COLORS = plt.get_cmap("Set1").colors


def plot_factor_matrix(
    matrix: pd.DataFrame,
    matrix_type: Literal["cov", "corr"],
    date: Union[str, pd.Timestamp],
    figsize: Optional[Tuple[int, int]] = (12, 10),
    save_path: Optional[str] = None,
) -> None:
    """
    Plots a covariance or correlation matrix as a heatmap, with optional image export.

    Args:
        matrix (pd.DataFrame): A square DataFrame with factor names as index and columns.
        matrix_type (Literal["cov", "corr"]): Type of the matrix, controls color scale and annotations.
        date (Union[str, pd.Timestamp]): Date to show in title.
        figsize (Optional[Tuple[int, int]]): Size of figure.
        save_path (Optional[str]): If provided, saves the plot to this path.

    Returns:
        None
    """
    if matrix_type not in {"cov", "corr"}:
        raise ValueError(
            f"Invalid matrix_type: {matrix_type}. Must be 'cov' or 'corr'."
        )

    # Ensure square matrix with matching index and columns
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square (same number of rows and columns).")
    if not matrix.index.equals(matrix.columns):
        raise ValueError(
            "Matrix index and columns must match (i.e., square and aligned)."
        )

    if isinstance(date, pd.Timestamp):
        date = date.strftime("%Y-%m-%d")

    plt.figure(figsize=figsize)

    if matrix_type == "cov":
        sns.heatmap(
            matrix,
            annot=False,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
            xticklabels=True,
            yticklabels=True,
            cbar_kws={"label": "Covariance"},
        )
    elif matrix_type == "corr":
        sns.heatmap(
            matrix,
            cmap="coolwarm",
            center=0,
            vmin=-1,
            vmax=1,
            annot=True,
            fmt=".2f",
            annot_kws={"size": 5},
            xticklabels=True,
            yticklabels=True,
            cbar_kws={"label": "Correlation"},
        )

    title_prefix = "Covariance" if matrix_type == "cov" else "Correlation"
    plt.title(f"{title_prefix} Matrix on {date}", fontsize=16)
    plt.ylabel("Factors")
    plt.xlabel("Factors")
    plt.xticks(rotation=90)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=GLOBAL_DPI, bbox_inches="tight")

    plt.close()


def plot_model_comparison(
    df: pd.DataFrame,
    metric: str,
    figsize: Optional[Tuple[int, int]] = (12, 10),
    save_path: Optional[str] = None,
) -> None:
    """
    Plot a time series scatter plot comparing multiple error metrics over time.

    Each non-"Date" column in the input DataFrame is treated as a separate series
    and plotted as scatter points against the "Date" column. Useful for visually
    comparing different models' performance over time on a chosen error metric
    (e.g. "rmse", "mae", "r2", or "residual").

    Args:
        df (pd.DataFrame): A DataFrame with a "Date" column and one or more columns
            representing the error values (e.g., rmse, r2) for different models.
            Each row corresponds to one date.
        metric (Literal): The name of the error metric to display on the y-axis.
            Must be one of: "rmse", "mse", "mae", "r2", "residual".
        figsize (Optional[Tuple[int, int]], optional): Size of the matplotlib figure as
            (width, height). Defaults to (12, 10).
        save_path (Optional[str], optional): If specified, saves the plot to this path.
            Intermediate directories will be created automatically.

    Returns:
        None

    Example:
        >>> plot_model_comparison(df, metric="r2", save_path="output/r2_comparison.png")
    """
    metric = metric.lower()
    if metric not in {"rmse", "mse", "mae", "r2"}:
        raise ValueError(
            f"Invalid metric '{metric}'. Must be one of: rmse, mse, mae, r2."
        )

    plt.figure(figsize=figsize)
    i = 0

    y_all_values = []

    for col in df.columns:
        if col != "Date":
            y_vals = df[col]
            y_all_values.append(y_vals)

            color = COLORS[i % len(COLORS)]
            marker = MARKERS[i % len(MARKERS)]

            mean_val = y_vals.mean()
            # Original Scatterplot
            plt.scatter(
                df.index,
                y_vals,
                label=f"{col} (mean={mean_val:.4f})",
                marker=marker,
                s=15,
                color=color,
            )

            # Adding Average Horizontal Line
            plt.axhline(
                y=mean_val, linestyle="--", linewidth=2.0, color=color, label=None
            )

            i += 1

    plt.xlabel("Date")
    plt.ylabel(metric.upper())
    plt.grid(
        axis="y",
        linestyle="--",
    )
    plt.axhline(0, color="black", linewidth=1.2, linestyle="-")

    # Set Y-Axis Range Automatically
    if metric == "r2":
        min_y = max(np.floor(df.min().min() * 10) / 10, -0.2)
        plt.ylim(min_y, 1 + 0.05)
        plt.yticks(np.arange(min_y, 1.0 + 0.05, 0.1))
    elif metric in {"rmse", "mse", "mae"}:
        plt.ylim(bottom=0)

    xtick_stride = max(1, len(df) // 10)
    plt.xticks(df.index[::xtick_stride], rotation=45)

    plt.title(f"Model Comparison: {metric.upper()} vs Time")
    plt.legend()
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=GLOBAL_DPI, bbox_inches="tight")

    plt.show()
    plt.close()


__all__ = ["plot_factor_matrix", "plot_model_comparison"]
