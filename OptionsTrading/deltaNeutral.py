'''
Delta Neutral Options Trading Strategy

What is delta? It's a greek letter but in options and finance it is 
The change in price of an option contract due to the change in the underlying price

Delta is a percentage measure and represents some movement of the underlying security. Remember,
options are based off of other financial instruments (stocks, futures, etc.)
Source: https://www.cmegroup.com/education/courses/option-greeks/options-delta-the-greeks.html

TO DO: Caluclate the delta value for DJT (Trump Media: Stock) in any way you see fit. Be sure 
to make it clear what time horizon your delta is based off of.

The formula of delta = Change in the Price of Option / Change in the Price of Underlying.
'''
#--------------------------------------------------------------
#pip install yoptions
import yoptions as yo
from datetime import datetime, timedelta

def get_time_horizon(expiration_date):
    today = datetime.now().date()
    expiry = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    return (expiry - today).days

# Chain of all DJT (Trump Media) call options for next expiration date + IV + Greeks (including delta ofc)
chain = yo.get_chain_greeks(stock_ticker='DJT', dividend_yield=0, option_type='c', risk_free_rate=None)
chain['Time_Horizon'] = chain['expiration_date'].apply(get_time_horizon)
print("DJT Call Options:")
print(chain[['strike', 'bid', 'ask', 'expiration_date', 'Time_Horizon', 'delta', 'gamma', 'theta', 'vega', 'rho', 'implied_volatility']].head().to_string())

# Chain of all DJT (Trump Media) put options that expire on a specific date
specific_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
chain = yo.get_chain_greeks_date(stock_ticker='DJT', dividend_yield=0, option_type='p', 
                                 expiration_date=specific_date, risk_free_rate=None)
chain['Time_Horizon'] = chain['expiration_date'].apply(get_time_horizon)
print("\nDJT Put Options:")
print(chain[['strike', 'bid', 'ask', 'expiration_date', 'Time_Horizon', 'delta', 'gamma', 'theta', 'vega', 'rho', 'implied_volatility']].head().to_string())

# Get specific option details for DJT
expiry_date = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d')
strike_price = 50  # Adjust based on current DJT stock price
option_data = yo.get_option_greeks('DJT', expiry_date, 'c', strike_price, dividend_yield=0, risk_free_rate=0.05)
option_data['Time_Horizon'] = get_time_horizon(expiry_date)
print("\nSpecific DJT Option Details:")
print(option_data.to_string())
