import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Meme strategy (short top 5 highest gainers of the day, hold under end of week, exit trade)
def get_top_gainers(date):
    # This function should return the top 5 gainers for the given date
    # For simplicity, let's assume it returns a list of tickers
    # In a real scenario, you would fetch this data from a reliable source
    return ["MSFT", "GOOGL", "AMZN", "TSLA"]

def backtest_strategy(start_date, end_date):
    current_date = start_date
    results = []

    while current_date <= end_date:
        if current_date.weekday() == 0:  # Monday
            top_gainers = get_top_gainers(current_date - timedelta(days=3))  # Get top gainers of last Friday
            entry_prices = {ticker: yf.download(ticker, start=current_date, end=current_date + timedelta(days=1))['Close'][0] for ticker in top_gainers}
            exit_date = current_date + timedelta(days=4)  # Hold until Friday
            exit_prices = {ticker: yf.download(ticker, start=exit_date, end=exit_date + timedelta(days=1))['Close'][0] for ticker in top_gainers}
            weekly_return = sum((entry_prices[ticker] - exit_prices[ticker]) / entry_prices[ticker] for ticker in top_gainers) / len(top_gainers)
            results.append((current_date, weekly_return))
        current_date += timedelta(days=1)

    return pd.DataFrame(results, columns=["Week Start", "Weekly Return"])

start_date = datetime(2023, 1, 1)
end_date = datetime.today()
backtest_results = backtest_strategy(start_date, end_date)
print(backtest_results)