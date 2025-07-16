#!/usr/bin/python3
"""0-prime_game.py
"""

# Initialize a memoization table to store the results of subproblems
memo = {}

def isPrime(num):
        """Checks if a number is prime
        """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def canWin(n):
    """Determines the winner of the game recursively
    """
    winner = False

    if n == 1:
        return winner

    if n in memo:
        return memo[n]

    for i in range(2, n + 1):
        if isPrime(i):
            if winner:
                winner = memo[i] = False
            else:
                winner = memo[i] = True

    return winner


def isWinner(x, nums):
    maria_wins = ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1
        print(f"{memo} -> Maria: {maria_wins} vs Ben: {ben_wins}")

    if ben_wins > maria_wins:
        return "Ben"
    else:
        return "Maria"
