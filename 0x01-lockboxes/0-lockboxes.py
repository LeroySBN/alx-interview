#!/usr/bin/python3
"""
module 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes in a list of boxes can be opened
    """
    # Create a list to track visited boxes, initially all set to False
    visited = [False] * len(boxes)
    # Mark the first box as visited (the starting box)
    visited[0] = True
    # Call the helper function to explore and unlock boxes
    return unlockBoxes(0, boxes, visited)


def unlockBoxes(box, boxes, visited):
    """
    Helper function to recursively explore and unlock boxes
    """
    if all(visited):
        # If all boxes visited, return True to indicate all boxes can be opened
        return True

    keys = boxes[box]  # Get the keys in the current box
    for key in keys:
        if key < len(boxes) and not visited[key]:
            # if key is within range and
            # the box corresponding to the key has not been visited
            visited[key] = True  # Mark the box as visited
            if unlockBoxes(key, boxes, visited):
                # Recursively call the function with
                # the key as the new starting box index
                # If the recursive call returns True,
                # return True to propagate the result
                return True

    # If no key allows all boxes to be opened, return False
    return False
