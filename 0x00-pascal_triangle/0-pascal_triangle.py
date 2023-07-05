#!/usr/bin/python3
"""
module pascal_triangle
"""


def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    visited[0] = True
    return unlockBoxes(0, boxes, visited)


def unlockBoxes(box, boxes, visited):
    if all(visited):
        return True

    keys = boxes[box]
    for key in keys:
        if key < len(boxes) and not visited[key]:
            visited[key] = True
            if unlockBoxes(key, boxes, visited):
                return True

    return False
