#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []] # True
print(f"boxList 1 (Expected - True) -> {canUnlockAll(boxes)}")

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # True
print(f"boxList 2 (Expected - True) -> {canUnlockAll(boxes)}")

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]] # False
print(f"boxList 3 (Expected - False) -> {canUnlockAll(boxes)}")

boxes = [[], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # False
print(f"boxList 4 (Expected - False) -> {canUnlockAll(boxes)}")

boxes = [[0], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # False
print(f"boxList 5 (Expected - False) -> {canUnlockAll(boxes)}")

boxes = [[7], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]  # False
print(f"boxList 6 (Expected - False) -> {canUnlockAll(boxes)}")

boxes = [[1, 3, 7], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] # True
print(f"boxList 7 (Expected - True) -> {canUnlockAll(boxes)}")

boxes = [[]]
print(f"boxList 8 (Expected - True) -> {canUnlockAll(boxes)}")  # True

boxes = [[1], [0, 2], [3]] # True
print(f"boxList 9 (Expected - True) -> {canUnlockAll(boxes)}")  # True
