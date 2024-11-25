import numpy as np
import math
from matplotlib import pyplot as plt
from typing import List, Tuple, Optional

def compute_dx_for_dy(
    dy_values: List[float], 
    L0: float = 10, 
    y0: float = 42, 
    x0: float =  0.005668169284575697
) -> List[Tuple[float, Optional[float], Optional[float]]]:
    """
    Computes dx for a range of dy values using constants L0, y0, and x0.
    
    Parameters:
        dy_values (List[float]): List of dy values (ETH being sold).
        L0 (float): The initial liquidity level (default is 10).
        y0 (float): Initial ETH reserve (default is 42).
        x0 (float): Initial USDC reserve (default is 0.005668169284575697).
    
    Returns:
        List[float]: A list of floats representing the computed dx as a function of dy
    """
    results: List[Tuple[float, Optional[float], Optional[float]]] = []
    
    for dy in dy_values:
        # Define coefficients for the quadratic equation
        b: float = -(2 * x0 + y0 + dy)
        c: float = (-L0 / (y0 + dy)) + x0 * (x0 + y0 + dy)
        
        # Calculate the discriminant
        discriminant: float = b ** 2 - 4 * c
        
        # Check if discriminant is non-negative for real solutions
        if discriminant >= 0:
            sqrt_discriminant: float = math.sqrt(discriminant)
            dx1: float = (-b - sqrt_discriminant) / 2
        else:
            dx1 = None  # No real solutions for dx

        # Append the results as a tuple
        results.append(dx1)

    
    return results

def compute_profit(
    dx_list: List[float], 
    dy_list: List[float], 
    my_degen_friend_price: float
) -> Tuple[float, float]:
    """
    Computes the expression (dx - my_degen_friend_price * dy) given lists of dx and dy values.

    Parameters:
        dx_list (List[float]): List of dx values.
        dy_list (List[float]): List of dy values corresponding to dx values.
        my_degen_friend_price (float): The fixed price used in the expression.

    Returns:
        List[float]: A list containing the profit
    """
    
    # Calculate the expression for each pair of dx and dy
    profit: List[float] = [
        dx - my_degen_friend_price * dy for dx, dy in zip(dx_list, dy_list)
    ]
    
    # Return the dx and dy values that maximize the expression
    return profit