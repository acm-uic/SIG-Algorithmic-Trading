
In the finance world, minimum variance portfolio optimization is key. 
It helps to manage risk and choose assets wisely. This way, we get a mix 
of investments that lowers the ups and downs. It matches the risk someone is willing to take, being very important today.

  Key Takeaways
Minimum variance portfolio optimization aims to reduce risk while maintaining potential returns.
It involves creating a diverse portfolio that minimizes volatility.
Leverages modern portfolio theory for asset allocation decisions.
Focuses on risk-adjusted returns and correlates with investor risk tolerance.

#--------------------------------------
from pylab import *
import quantpy as qp

# Get portfolio.
P = qp.Portfolio(['IBM','GOOG','MSFT','AAPL','INTC']) 

# Calculate the returns buying 1 share of everything.
bb = P.ret_for_w(ones(5))
cumsum(bb).plot(color='r',label='Buy and Hold Equally.')
mm = cumsum(bb)[-1]

# Find the optimal weighting that yields the same return with minimum variance.
w = P.min_var_w_ret(mm)
aa = P.ret_for_w(w)
cumsum(aa).plot(label='Same return but min variance.')
legend(loc='best',shadow=True, fancybox=True)
show()
