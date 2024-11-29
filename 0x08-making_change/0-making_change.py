#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins
    needed to meet a given amount total.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If the total cannot be met, return -1.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a greedy approach
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins += total // coin
            total %= coin

    return num_coins if total == 0 else -1
