PROJECT OBJECTIVE AND DESIGN 

The main aim of this project was to develop a market strategy using previous historical data from the S%P 500 ETF. This strategies aim was to develop a good risk adjusted return compared to the passive method of Buying and holding, which was used as a benchmark over the period i chose, which was 2010 to 2025(current)

MAIN PYTHON STACK

data acquistion - yfinance

data analysis - numpy and pandas

visualisation - matplotlib

STRATEGY LOGIC

For my strategy i used a compound strategy to filter trends, using SMA as a trend comformation indicator, both fast and slow to mimimise exposure to major market drawdowns. My momentumn indicator was the RSI, and it was used to better understand the speed and magnitude of change of price movements. I ensured to calculate the RSI using the exponential weighted moving average which prioritises more recent data for greater responsiveness

Position=1.0 (BUY) if (SMA 10>SMA 50) AND (RSI<70)

DATA INTEGRITY AND BIAS AVOIDANCE

my overall evaluation of my strategy came down to 2 main metrics: Annual sharpe ratio to measure the return per unit of risk, and Maximum Drawdown, which measures the largest peak to trough percentage decline. This is used to represent the worst case scenario loss

FINAL RESULTS AND EVALUATION

The inital strategy, being RSI < 30, was too restrictive, being all the way at a Sharpe ratio of just 0.12. This meant my return was so negligable and not worth the time at all. After i changed the RSI to RSI < 70, meaning i will enter when the stock is not completely overbought. This seemed to work a lot better, the Sharpe ratio actually boosted all the way to 0.78(more profit per unit of risk.) Furthermore, the maximum drawdown rate had a final maximum drawdown rate of around -20%, proving its effectiveness as it often successfully stepped through more extreme market downturns without too much loss, compared to the buy and hold method, which had a maximum drawdown rate of about 50%.

Overall this strategy validates the use of trend and momentum indicators to block out market noise and make performance better on a risk consideration basis.

