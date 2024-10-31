#!/usr/bin/python3
"""

UTF-8 validation module
"""


def validUTF8(data):
    """
    Number of bytes left in the current UTF-8 character
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False

    """
    num_bytes = 0

    # Masks for identifying the type of bytes
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Keep only the last 8 bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            elif (byte >> 7):
                return False  # 1-byte character should start with 0
        else:
            # Check that the next byte starts with "10"
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
