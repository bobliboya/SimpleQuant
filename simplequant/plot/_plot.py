import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Plot stock prices over time
def plot_stock_price(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # Step 3: Pivot the data to wide format (Date as index, each Symbol as column)
    pivot_df = df.pivot(index='Date', columns='Symbol', values='ClosePrice')

    # Step 4: Plot the daily close prices
    plt.figure(figsize=(14, 7))

    for col in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[col], label=str(col))

    plt.title('Daily Close Prices of Each Stock')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend(title='Symbol', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.ylim(ymin=0)
    plt.tight_layout()
    plt.show()


# Plot variables over time
def plot_variables_over_time(M, title, y_label, series_name):
    assert len(series_name) == np.shape(M)[0], "series_name should have the same size of M!!"
    n = np.shape(M)[1]
    dates = np.arange(n)
    plt.figure(figsize=(14, 7))
    a = 0
    for i in M:
        plt.plot(dates, i, label=series_name[a])
        a += 1
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(y_label)
    plt.legend(title='Series', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.xlim(xmin=0)
    plt.tight_layout()
    plt.show()

__all__ = ['plot_stock_price', 'plot_variables_over_time']