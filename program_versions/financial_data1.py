import yfinance as yf
import pandas as pd
import numpy as np
#download the dataset
data = yf.download("SPY", start="2010-01-10")
data.info()
#removing all rows with missing values
data.dropna(inplace=True)
#calculate 10 day SMA - fast
data["SMA_10"] = data["Close"].rolling(window=10).mean()
#calculate 50 day SMA - slow
data["SMA_50"] = data["Close"].rolling(window=50).mean()
#remove all rows that now come up with missing values
data.dropna(inplace=True)
#SMA crossover rule - determine a bullish trend as fast SMA on average is higher than slower SMA
data["Position"]  = np.where(data["SMA_10"] > data["SMA_50"], 1.0, 0.0)
#calculates the percentage change in close values, today and yesterday
data["daily_returns"] = data["Close"].pct_change()
#avoid look ahead bias - uses current days close value instead of tomorrow's close value
data["strategy_returns"] = (data["daily_returns"] * data["Position"].shift(1))
#calculates compound returns, adds one to create a percentage, like * by 100
data["cumulative_returns"] = (data["strategy_returns"] + 1 ).cumprod()
print(data[0:100].to_string())
