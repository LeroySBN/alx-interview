#!/usr/bin/python3
""" N Queens """

import sys


def printBoard(board):
    """ print the board """
    print([list(i) for i in board])


def isSafe(board, row, col, n) -> bool:
    """ check if a queen can be placed on board[row]
    Args:
        board: board
        row: row
        col: column
        n: number of queens
    Returns:
        True or False
    """
    #
    for i in range(col):
        if board[row][i] == 1:
            return False
    #
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    #
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col, n) -> bool:
    """ solve the N Queen problem
    Args:
        board: board
        col: column
        n: number of queens
    Returns:
        True or False
    """
    #
    if col == n:
        printBoard(board)
        return True
    #
    res = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res


def main():
    """ main function """
    pass


if __name__ == "__main__":
    main()
