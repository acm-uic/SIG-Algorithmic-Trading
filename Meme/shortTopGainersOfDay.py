import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Meme strategy (short top 5 highest gainers of the day, hold under end of week, exit trade)
def get_top_gainers():
    # Fetch the top gainers of the day
    gainers = pd.read_html('https://finance.yahoo.com/markets/stocks/gainers/')
    top_5_gainers = gainers[0].head(5)
    return top_5_gainers

def short_stocks(symbols):
    for symbol in symbols:
        print(f"Shorting stock: {symbol}")

def exit_trades(symbols):
    for symbol in symbols:
        print(f"Exiting trade for: {symbol}")

def main():
    # today = datetime.now()
    # end_of_week = today + timedelta(days=(4 - today.weekday()))

    # top_gainers = get_top_gainers()
    # short_stocks(top_gainers)

    # while datetime.now() < end_of_week:
    #     pass  # Hold until end of week

    # exit_trades(top_gainers)
    print(get_top_gainers())

if __name__ == "__main__":
    main()