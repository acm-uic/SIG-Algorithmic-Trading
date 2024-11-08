import yfinance as yf
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np

# price_series = [3, 4, 4, 5, 6, 7, 6, 6, 7, 8, 9, 12, 10]

# test = adfuller(price_series)
# test_statistic = test[0]
# p_value = test[1]

# Get tickers from S&P 500 and return them as a list
def get_sp500_tickers():
    sp500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].to_list()
    return sp500_tickers

# This function downloads the stock data for a given ticker and performs the ADF test
def stationaryTest(ticker, start_date, end_date):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        print("Downloading data for: ", ticker)
        close_prices = stock_data['Close'].dropna().to_numpy()

        if len(close_prices) < 2:
            return {'ticker': ticker, 'test_stat': None, 'p_value': None, 'Is_Stationary: ': None}

        test = adfuller(close_prices)
        test_statistic = test[0]
        p_value = test[1]

        isStationary = p_value < 0.05

        return{
            'ticker': ticker,
            'test_stat': test_statistic,
            'p_value': p_value,
            "Is_Stationary: ": isStationary
        }
    except Exception as e:
        return {'ticker': ticker, 'error': str(e)}

tickers = get_sp500_tickers() 

# This function goes through the first 100 stocks in the S&P 500 and performs the ADF test on each stock
def test_stationary(tickers): 
    for ticker in tickers[:100]:
        result = stationaryTest(ticker, '2023-01-01', '2024-01-01')
        
        if 'error' in result:
            print(f"Error for {result['ticker']}: {result['error']}")
        else:
            print(f"{result['ticker']} ADF Test statistic: {result ['test_stat']}")
            if result['p_value'] is not None:
                print(f"P-value: {result ['p_value']}")
            else:
                print("P-value: N/A")

        ifStationary = "False" if result ['Is_Stationary: '] == np.False_ else "True"
        print("Is Stationary: " + ifStationary)

# This function goes through all the stocks in the S&P 500 and returns a list of all the stocks that are stationary
# start_date and end_date are the dates for which the ADF test is performed
# Looks like '2023-01-01' or '2024-01-01'
# tickers is an array of tickers
def find_stationary_tickers_SandP500(tickers, start_date, end_date):
    stationary_tickers = []
    for ticker in tickers:
        result = stationaryTest(ticker, start_date, end_date)
        if result['Is_Stationary: ']:
            stationary_tickers.append(result['ticker'])
    return stationary_tickers






















#print(f'Test statistic: {test_statistic} \nP-value: {p_value}')

# null hypothesis of ADF test means that the mean of the time series is not stationary
# if p-value is less than 0.05, we reject the null hypothesis and conclude that the time series is stationary
# if p-value is greater than 0.05, we fail to reject the null hypothesis and conclude that the time series is not stationary

# Historical data sources from NASDAQ 
# https://www.nasdaq.com/market-activity/stocks/qcom/historical?page=1&rows_per_page=10&timeline=y1
# historical_prices_SBUX_1YEAR = pd.read_csv('MeanReversion/HistoricalData_SBUX_1YEAR.csv')
# historical_prices_QCOM_1YEAR = pd.read_csv('MeanReversion/HistoricalData_QCOM_1YEAR.csv')

# price_df_SBUX = historical_prices_SBUX_1YEAR
# price_df_QCOM = historical_prices_QCOM_1YEAR

# price_series_SBUX = np.array(price_df_SBUX["Close/Last"].to_numpy())
# price_series_QCOM = np.array(price_df_QCOM["Close/Last"].to_numpy())


# for i in range(len(price_series_SBUX)):
#     price_series_SBUX[i] = float(price_series_SBUX[i].replace('$', ''))
#     price_series_QCOM[i] = float(price_series_QCOM[i].replace('$', ''))

# print("Price Series data for Starbucks (Close price by day):")
# print(price_series_SBUX, "\n")
# print("Price Series data for Qualcomm (Close price by day):")
# print(price_series_QCOM, "\n")

# ADF_Test_SBUX = adfuller(price_series_SBUX)
# ADF_Test_QCOM = adfuller(price_series_QCOM)

# test_statistic_SBUX = ADF_Test_SBUX[0]
# p_value_SBUX = ADF_Test_SBUX[1]

# test_statistic_QCOM = ADF_Test_QCOM[0]
# p_value_QCOM = ADF_Test_QCOM[1]

# print(f'Starbucks ADF Test statistic: {test_statistic_SBUX} \nP-value: {p_value_SBUX}')
# print(f'Qualcomm ADF Test statistic: {test_statistic_QCOM} \nP-value: {p_value_QCOM}')