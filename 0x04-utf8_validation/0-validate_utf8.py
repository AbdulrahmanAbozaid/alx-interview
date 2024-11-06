#!/usr/bin/python3
"""
Function to validate if a dataset represents a valid UTF-8 encoding
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first few bits of each byte
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Only need to examine the last 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the byte count for the current character
        num_bytes -= 1

    return num_bytes == 0
