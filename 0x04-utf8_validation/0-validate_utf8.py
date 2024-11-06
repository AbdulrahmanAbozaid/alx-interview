#!/usr/bin/python3
"""UTF-8 Validation

understanding of the UTF-8 encoding scheme,
and Python programming skills to validate whether a given
dataset represents a valid UTF-8 encoding.
Here’s a list of concepts and resources that will be helpful:
"""
from typing import List


def mask(byte: int) -> tuple | None:
    """Mask the byte to define if it a ascii, bytes' header or cont. bit"""
    byte_utf = {
        0x80: (0x00, 0),
        0xC0: (0x80, 0),
        0xE0: (0xC0, 1),
        0xF0: (0xE0, 2),
        0xF9: (0xF0, 3),
    }

    for mask, end in byte_utf.items():
        if byte & mask == end[0]:
            return end
    return None


def validUTF8(data: List[int]) -> bool:
    """determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): data to test
    """
    ctr = 0
    for ele in data:
        end = mask(ele)

        if end is None:
            return False

        if ctr and end[1] == 0x80:
            ctr -= 1
        elif ctr:
            return False
        else:
            ctr = end[1]
    return True
