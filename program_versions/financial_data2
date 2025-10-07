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

#GAINS AND LOSSES
#calculate absolute numerical difference between current days closing price and yesterday's closing price
data["Change"] = data["Close"].diff()
#set the gain column to contain positive percentage changes, set negatives to 0
data["Gain"] = np.where(data["Change"] >  0, data["Change"], 0).copy()
#set the loss column to contain negative percentage changes, use absolute neg to avoid minus percentages, if there is no loss sets to 0
data["Loss"] = np.where(data["Change"] < 0, abs(data["Change"]), 0).copy()
data.dropna(inplace=True)
#AVG GAINS AND LOSSES - RSI CALCULATIONS
data["Avg_Gain"] = data["Gain"].ewm(com=13).mean()
data["Avg_Loss"] = data["Loss"].ewm(com=13).mean()
data["RS"] = (data["Avg_Gain"] / data["Avg_Loss"])
data["RSI"] = (100 - (100/(1+data["RS"])))
data.dropna(inplace=True)

#new trading signal using RSI and SMA combined
data["Compound_Position"] = np.where((data["SMA_10"] > data["SMA_50"]) & (data["RSI"] < 30), 1.0, 0.0)
#avoid look ahead bias - uses current days close value instead of tomorrow's close value
data["strategy_returns"] = (data["daily_returns"] * data["Compound_Position"].shift(1))
#calculates compound returns, adds one to create a percentage, like * by 100
data["cumulative_returns"] = (data["strategy_returns"] + 1).cumprod()
print(data[0:100].to_string())
