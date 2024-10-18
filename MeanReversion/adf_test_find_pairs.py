import yfinance as yf
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Function to download stock data
def download_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Function to perform ADF test
def adf_test(series):
    result = adfuller(series)
    return result[1]  # Return p-value

# Function to find pairs
def find_pairs(data, p_value_threshold=0.05):
    pairs = []
    # Iterate through all pairs of stocks
    # For each pair, perform ADF test on the difference of the stock prices
    # If p-value is less than threshold, the pair is a potential pair
    return pairs

# Download S&P 500 data
sp500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist()
# Remove tickers that yf cannot download
tickers_to_remove = ['BF.B', 'BRK.B', 'KVUE', 'VLTO', 'SOLV', 'SW', 'AMTM', 'GEV', 'GEHC', 'CEG']
print("Removing faulty data from S&P 500")
sp500_tickers = [ticker for ticker in sp500_tickers if ticker not in tickers_to_remove]
print("Successfully removed faulty data from S&P 500")
data = download_data(sp500_tickers, '2020-01-01', '2021-01-01')



# Find pairs
print(data)
# pairs = find_pairs(data)
# print(pairs)

# null hypothesis of ADF test means that the mean of the time series is not stationary
# if p-value is less than 0.05, we reject the null hypothesis and conclude that the time series is stationary
# if p-value is greater than 0.05, we fail to reject the null hypothesis and conclude that the time series is not stationary