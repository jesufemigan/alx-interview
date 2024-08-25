#!/usr/bin/python3
'''
changes comes from within
'''

def makeChange(coins, total):
    '''
    determine fewest number of coins
    needed to meet a given amount total
    '''
    if total <= 0:
        return 0
    if not coins or coins or None:
        return -1
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
