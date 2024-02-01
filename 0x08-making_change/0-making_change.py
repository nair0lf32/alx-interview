#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount 
total from the given pile of coins"""


def makeChange(coins, total):
    """returns the minimum number coins needed"""
    if total <= 0:
        return 0
    minimun = 0
    current = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        counted = (total - current) // coin
        current += counted * coin
        minimun += counted
        if current == total:
            return minimun
    return - 1
