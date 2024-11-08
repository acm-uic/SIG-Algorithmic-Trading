# Follows trends set by candles
# If there are four red candles in a row, the next candle is likely to be green
# If there are four green candles in a row, the next candle is likely to be red
# Because we assume the security is mean reverting


# Therefore if there are four red candles in a row, we should buy
# If there are four green candles in a row, we should sell

# We can use the ADF test to determine if the time series is stationary

# If the time series is stationary, we can assume that the security is mean reverting

# If the security is mean reverting, we can assume that the security will revert to the mean after a period of time

from adf_test import get_sp500_tickers, find_stationary_tickers_SandP500
import yfinance as yf

tickers = get_sp500_tickers() 

# null hypothesis of ADF test means that the mean of the time series is not stationary
# if p-value is less than 0.05, we reject the null hypothesis and conclude that the time series is stationary
# if p-value is greater than 0.05, we fail to reject the null hypothesis and conclude that the time series is not stationary
stationary_stocks_in_SandP500 = find_stationary_tickers_SandP500(tickers, '2023-01-01', '2024-01-01')
print(stationary_stocks_in_SandP500)

# Entry
# If there are four red candles in a row, we should buy
# If there are four green candles in a row, we should sell

def get_candles(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']
