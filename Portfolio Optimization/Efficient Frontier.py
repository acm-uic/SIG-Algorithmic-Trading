'''
Explanation of Efficient Frontier:
    - The efficient frontier, also known as the portfolio frontier, is a set of ideal or optimal portfolios that are expected to give 
    the highest return for a minimal level of return12. It is formed by plotting the expected return on the y-axis and the standard 
    deviation as a measure of risk on the x-axis1. 
    - Portfolios that lie below the efficient frontier are sub-optimal because they do not provide enough return for the level of risk.
    - Great video to visualize this--> https://www.youtube.com/watch?v=AGjsvdDMyhE&t=1s

Explanation of code:
    1. Plots Efficient Frontier (to visualize portfolio asset distribution)
    2. Calculates optiomal portfolio weights
    3. Comuptes expected retuns + volatility + sharpe ratio (=expected returns/volatility)
    4. Prints allocation of different asset classes (using data from 3)
    note: allows users to type in their preferred stocks using get-user_ticker() func

Pre-requisite:
    -------------------------
    |  pip install quantpy |
    -------------------------
'''
#---------------------------

import quantpy as qp
import numpy as np

def get_user_tickers():
    tickers = []
    while True:
        ticker = input("Enter a stock ticker (or press Enter to finish): ").strip().upper()
        if ticker == "":
            if len(tickers) < 2:
                print("Please enter at least two tickers.")
            else:
                break
        else:
            tickers.append(ticker)
    return tickers

def main():
    print("Welcome to the Portfolio Analysis Tool!")
    tickers = get_user_tickers()

    try:
        # Create portfolio
        P = qp.Portfolio(tickers)

        # Plot efficient frontier
        P.efficient_frontier_plot()

        # Get optimal portfolio
        weights = P.optimal_portfolio()

        # Calculate expected return and volatility
        exp_return = np.sum(P.exp_returns * weights)
        volatility = np.sqrt(np.dot(weights.T, np.dot(P.cov_matrix, weights)))

        # Print results
        print("\nOptimal Portfolio Allocation:")
        for ticker, weight in zip(tickers, weights):
            print(f"{ticker}: {weight*100:.2f}%")

        print(f"\nExpected Annual Return: {exp_return*100:.2f}%")
        print(f"Expected Annual Volatility (Risk): {volatility*100:.2f}%")
        print(f"Sharpe Ratio: {exp_return/volatility:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("This might be due to invalid tickers or data availability issues.")

if __name__ == "__main__":
    main()
