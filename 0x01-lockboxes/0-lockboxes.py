#!/usr/bin/python3
"""0-lockboxes.py
"""

def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    return unlockRecursive(0, boxes, unlocked)

def unlockRecursive(idx, boxes, unlocked):
    if all(unlocked):
        return True
    for key in boxes[idx]:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            if unlockRecursive(key, boxes, unlocked):
                return True
    return False
