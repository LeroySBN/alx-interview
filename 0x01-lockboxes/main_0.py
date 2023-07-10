#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []] # True
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # True
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]] # False
print(canUnlockAll(boxes))

boxes = [[], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # False
print(canUnlockAll(boxes))

boxes = [[0], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # False
print(canUnlockAll(boxes))

boxes = [[7], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]  # False
print(canUnlockAll(boxes))

boxes = [[1, 3, 7], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # True
print(canUnlockAll(boxes))

boxes = [[]]
print(canUnlockAll(boxes))  # True

boxes = [[1], [0, 2], [3]] # True
print(canUnlockAll(boxes))
