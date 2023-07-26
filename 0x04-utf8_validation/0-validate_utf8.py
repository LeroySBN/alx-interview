#!/usr/bin/env python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list): list of integers

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return
        False
    """
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Number of bytes to check for each UTF-8 character
    bytes_to_check = 0

    for num in data:
        # Check the first byte of each UTF-8 character
        if bytes_to_check == 0:
            if num & mask1 == 0:
                continue
            elif num & (mask1 >> 1) == 0:
                return False
            else:
                # Calculate the number of bytes to check
                while num & mask1:
                    bytes_to_check += 1
                    mask1 >>= 1

                # A UTF-8 character can have 1 to 4 bytes
                if bytes_to_check < 1 or bytes_to_check > 4:
                    return False
        else:
            # Check the following bytes in a UTF-8 character
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the bytes to check for the next character
        bytes_to_check -= 1

    return bytes_to_check == 0