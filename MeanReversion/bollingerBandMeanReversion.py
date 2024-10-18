import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

place_holder_tickers = ['KO', 'PEP']

def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

def calculate_bollinger_bands(data, window=20):
    rolling_mean = data.rolling(window).mean()
    rolling_std = data.rolling(window).std()
    upper_band = rolling_mean + (rolling_std * 2) # 2 standard deviations above the mean -> 2 sigma
    lower_band = rolling_mean - (rolling_std * 2) # 2 standard deviations below the mean
    return rolling_mean, upper_band, lower_band

def plot_bollinger_bands(data, rolling_mean, upper_band, lower_band, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data, label=f'{ticker} Price')
    plt.plot(rolling_mean, label='Rolling Mean')
    plt.plot(upper_band, label='Upper Band')
    plt.plot(lower_band, label='Lower Band')
    plt.fill_between(data.index, lower_band, upper_band, color='gray', alpha=0.2)
    plt.title(f'Bollinger Bands for {ticker}')
    plt.legend()
    plt.show()

start_date = '2020-01-01'
end_date = '2021-01-01'

data = get_data(place_holder_tickers, start_date, end_date)

for ticker in place_holder_tickers:
    ticker_data = data[ticker]
    rolling_mean, upper_band, lower_band = calculate_bollinger_bands(ticker_data)
    plot_bollinger_bands(ticker_data, rolling_mean, upper_band, lower_band, ticker)