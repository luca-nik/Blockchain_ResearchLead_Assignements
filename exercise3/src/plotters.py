from matplotlib import pyplot as plt
from typing import List, Tuple, Optional

import constants

def plot_dx_dy(dy: List[float], dx: List[float]) -> None:

    # Plotting dx/dy
    plt.figure(figsize=(10, 6))
    plt.hlines(y = constants.x0, xmin=0, xmax = dy[-1], linewidth=2)
    plt.plot(dy, dx, label=r"dx$_1$", color="red", linewidth=2)
    
    # Adding labels and title
    plt.xlabel("dy (ETH sold)", fontsize=14)
    plt.ylabel("dx (USDC received)", fontsize=14)
    plt.legend(loc="lower right", fontsize=12)
    plt.grid(True)
    
    # Adjusting the tick parameters for both axes
    plt.tick_params(axis='both', which='major', labelsize=12, width=1.5, length=7)  # Major ticks
    
    # Save the plot as a file
    plt.tight_layout()
    plt.savefig("images/dx_vs_dy.png")

def plot_price(dy: List[float], price: List[float]) -> None:
    # Plot the LP's price function
    plt.figure(figsize=(10, 6))
    plt.hlines(y = 10, xmin=0, xmax = dy[-1], linewidth=2)
    plt.plot(dy, price, color="red", linewidth=2, label= "LP Price Function")
    plt.yscale('log')
    
    # Adding labels and title
    plt.xlabel("dy (ETH sold)", fontsize=14)
    plt.ylabel("Pool's USDC price (dx/dy)", fontsize=14)
    plt.legend(loc="upper right", fontsize=12)
    plt.grid(True)
    
    # Adjusting the tick parameters for both axes
    plt.tick_params(axis='both', which='major', labelsize=12, width=1.5, length=7)  # Major ticks
    
    # Save the plot as a file
    plt.tight_layout()
    plt.savefig("images/USDC_price.png")

def plot_profit(dy: List[float], profit: List[float]) -> None:
    
    # Plot the expression values
    plt.figure(figsize=(10, 6))
    plt.plot(dy, profit, color='b', label="Profit", linewidth=2)
    plt.axhline(y=max(profit), color='r', linestyle='--', label="Maximized value")

    # Highlight the point where the maximum occurs
    max_index = profit.index(max(profit))
    plt.plot(dy[max_index], max(profit), 'ro')
    
    # Add labels and title
    plt.xlabel("ETH sold to LP", fontsize=14)
    plt.ylabel("Profit in USDC", fontsize=14)
    plt.legend(loc="lower right", fontsize=12)
    plt.grid(True)
    # Adjusting the tick parameters for both axes
    plt.tick_params(axis='both', which='major', labelsize=12, width=1.5, length=7)  # Major ticks
    
    # Show the plot
    plt.tight_layout()
    plt.savefig("images/profit.png")
    