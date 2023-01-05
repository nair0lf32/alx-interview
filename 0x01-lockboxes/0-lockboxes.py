#!/usr/bin/python3

"""
Lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Boxes is a list of lists
    (boxes containing keys of other boxes or not)
    Returns True or False for either all lockboxes
    can be opened or not
    """
    unlocked_boxes = [0]
    for i in unlocked_boxes:
        for j in boxes[i]:
            if j not in unlocked_boxes:
                unlocked_boxes.append(j)

    if len(unlocked_boxes) == len(boxes):
        return True
    else:
        return False
