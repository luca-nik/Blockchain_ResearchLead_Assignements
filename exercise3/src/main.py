import math
import numpy as np

import constants
from helper import compute_dx_for_dy, compute_profit
from plotters import plot_dx_dy, plot_price, plot_profit


# Compute and plot dx as a function of dy 
dy = np.arange(0.01, 6, 0.01).tolist() 
dx_results = compute_dx_for_dy(dy, L0=constants.L0, y0 = constants.y0, x0 = constants.x0)
dx1 = [result if result is not None and result <= constants.x0 else np.nan for result in dx_results]
dx_value = dx1[dy.index(constants.dy_value)]
print(f"For {constants.dy_value} ETH sold to the pool, we receive {dx_value} USDC")
plot_dx_dy(dy, dx1)

# Compute and plot the LP's USDC/ETH price function
price = [dx/dy for dx,dy in zip(dx1, dy)]
# Find the limiting ETH sold to the LP such that the corresponding price is less than my_degen_friend_price
limit_dy = next((dy for ddx, dy in zip(price, dy) if ddx <= constants.my_degen_friend_price), None)
print(f"For ETH values < {limit_dy}, the price of the LP is more advantageous than the one of my friend")
plot_price(dy, price)

# Compute, maximize, and plot the profit function
profit = compute_profit(dx1, dy, constants.my_degen_friend_price)
best_dx = max(profit) 
best_dy = dy[profit.index(max(profit))] 
print(f"The values that maximize the profit are dx={best_dx} and dy={best_dy}")
plot_profit(dy, profit)