#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime Game
    Arguments:
        x {int} -- number of rounds
        nums {list} -- list of integers
    Returns:
        [str] -- name of the player that won the most rounds
    """
    def isPrime(num):
        """ Checks if a number is prime """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize a memoization table to store the results of subproblems
    memo = {}

    # Define the recursive function to determine the winner
    def canWin(n):
        """ Determines the winner of the game """
        if n in memo:
            return memo[n]

        # Base case: If n is 1, the current player loses
        if n == 1:
            memo[n] = False
            return False

        # Check if the current player can make
        # a move leading to a losing position
        for i in range(2, n + 1):
            if isPrime(i) and n % i == 0:
                if not canWin(n - i):
                    memo[n] = True
                    return True

        # If no winning move is found, the current player loses
        memo[n] = False
        return False

    # Initialize counters for Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if canWin(n):
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

    # Logic 2
    # if not nums or x < 1:
    #     return None
    # n = max(nums)
    # nums.sort()
    # m = [False for i in range(n + 1)]
    # for i in range(2, int(sqrt(n)) + 1):
    #     if not m[i]:
    #         for j in range(i, n + 1, i):
    #             m[j] = True
    # m[0] = m[1] = True
    # c = 0
    # for i in range(len(m)):
    #     if not m[i]:
    #         c += 1
    #     m[i] = c
    # p1 = 0
    # for n in nums:
    #     p1 += m[n] % 2 == 1
    # if p1 * 2 == len(nums):
    #     return None
    # if p1 * 2 < len(nums):
    #     return "Ben"
    # return "Maria"
