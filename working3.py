"""
         This script is used to download the data for the ticker TSLA and plot the time series of the adjusted close price.    
"""

import os
from termcolor import cprint
import yfinance as yf
import matplotlib.pyplot as plt

# MAJOR VARIABLES
TICKER = "TSLA"

try:
    cprint(f"Downloading data for {TICKER}...", "cyan")
    data = yf.download(TICKER)
    cprint("Download complete.", "green")
except Exception as e:
    cprint(f"Error downloading data: {e}", "red")
    raise

try:
    cprint("Calculating returns...", "cyan")
    data['Return'] = data['Adj Close'].pct_change()
    cprint("Returns calculated.", "green")
except Exception as e:
    cprint(f"Error calculating returns: {e}", "red")
    raise

try:
    cprint("Plotting time series...", "cyan")
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Adj Close'], label='TSLA Adj Close', color='dodgerblue')
    plt.title('TSLA Adjusted Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()
    cprint("Plot displayed.", "green")
except Exception as e:
    cprint(f"Error plotting time series: {e}", "red")
    raise
