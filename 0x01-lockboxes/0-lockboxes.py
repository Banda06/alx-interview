#!/usr/bin/python3

"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else False.
    """
    # Start with the first key to box 0 (which is always unlocked)
    number_of_keys = [0]
    # Get the total number of boxes
    number_of_boxes = len(boxes)

    # Loop through the list of available keys
    for keys in number_of_keys:
        # Iterate through the keys in the current box
        for box in boxes[keys]:
            # If the key opens a valid box that hasn't been unlocked yet
            if box < number_of_boxes and box not in number_of_keys:
                # Add this new box to the list of unlocked boxes
                number_of_keys.append(box)

    if len(number_of_keys) == number_of_boxes:
        return True

    return False
