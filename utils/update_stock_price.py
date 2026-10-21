"""
Author: Alex
Date: 10-15-2026
Description: Updates stock price
"""
from random import uniform
def update_stock_price(stock, event_diff=0):
    """
    Description: Takes stock, and updates it's price to (100+a number between it's most negative variation, and it's most positive (both inclusive))% of
    the current price

    Parameters: (list) stock: the stock to be updated
    """
    stock[2] = stock[2] * ( 1 + uniform *(  stock[3]+event_diff ) )
