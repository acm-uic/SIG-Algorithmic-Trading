from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np

price_series = [3, 4, 4, 5, 6, 7, 6, 6, 7, 8, 9, 12, 10]

test = adfuller(price_series)


test_statistic = test[0]
p_value = test[1]

#print(f'Test statistic: {test_statistic} \nP-value: {p_value}')

# null hypothesis of ADF test means that the mean of the time series is not stationary
# if p-value is less than 0.05, we reject the null hypothesis and conclude that the time series is stationary
# if p-value is greater than 0.05, we fail to reject the null hypothesis and conclude that the time series is not stationary

# Historical data sources from NASDAQ 
# https://www.nasdaq.com/market-activity/stocks/qcom/historical?page=1&rows_per_page=10&timeline=y1
historical_prices_SBUX_1YEAR = pd.read_csv('MeanReversion/HistoricalData_SBUX_1YEAR.csv')
historical_prices_QCOM_1YEAR = pd.read_csv('MeanReversion/HistoricalData_QCOM_1YEAR.csv')

price_df_SBUX = historical_prices_SBUX_1YEAR
price_df_QCOM = historical_prices_QCOM_1YEAR

price_series_SBUX = np.array(price_df_SBUX["Close/Last"].to_numpy())
price_series_QCOM = np.array(price_df_QCOM["Close/Last"].to_numpy())


for i in range(len(price_series_SBUX)):
    price_series_SBUX[i] = float(price_series_SBUX[i].replace('$', ''))
    price_series_QCOM[i] = float(price_series_QCOM[i].replace('$', ''))

print("Price Series data for Starbucks (Close price by day):")
print(price_series_SBUX, "\n")
print("Price Series data for Qualcomm (Close price by day):")
print(price_series_QCOM, "\n")

ADF_Test_SBUX = adfuller(price_series_SBUX)
ADF_Test_QCOM = adfuller(price_series_QCOM)

test_statistic_SBUX = ADF_Test_SBUX[0]
p_value_SBUX = ADF_Test_SBUX[1]

test_statistic_QCOM = ADF_Test_QCOM[0]
p_value_QCOM = ADF_Test_QCOM[1]

print(f'Starbucks ADF Test statistic: {test_statistic_SBUX} \nP-value: {p_value_SBUX}')
print(f'Qualcomm ADF Test statistic: {test_statistic_QCOM} \nP-value: {p_value_QCOM}')