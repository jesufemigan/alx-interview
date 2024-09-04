#!/usr/bin/python3
'''prime game
'''


def isWinner(x, nums):
    '''
    define the winner of prime game
    '''
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    player_1 = 0
    player_2 = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        multiples_rem(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            player_1 += 1
        else:
            player_2 += 1
    if player_1 > player_2:
        return "Ben"
    if player_2 > player_1:
        return "Maria"
    return None

def multiple_rem(lis, x):
    '''
    removes prime multiples
    '''
    for i in range(2, len(lis)):
        try:
            lis[i * x] = 0
        except (ValueError, IndexError):
            break
