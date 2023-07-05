#!/usr/bin/python3
"""
module 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Returns: True if all boxes can be opened, else False
    """
    # Set to keep track of opened boxes
    opened_boxes = set([0])

    # Recursive function to open boxes
    def openBoxes(box_number):
        for key in boxes[box_number]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                openBoxes(key)

    # Start opening boxes from the first box (box 0)
    openBoxes(0)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
