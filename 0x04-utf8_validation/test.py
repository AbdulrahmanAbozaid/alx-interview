#!/usr/bin/python3
"""
Testing
"""

byte_utf = {
    0x80: (0x00, 0),
    0xC0: (0x80, 0),
    0xE0: (0xC0, 1),
    0xF0: (0xE0, 2),
    0xF9: (0xF0, 3),
}

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]

def mask(byte):
    for mask, end in byte_utf.items():
        if byte&mask == end[0]:
            return end

    return None

def validate(data):
    res = []
    ctr = 0
    for ele in data:
        end = mask(ele)

        if end == None:
            return False

        if ctr and end[1] == 0x80:
            ctr-=1
        elif ctr:
            return False
        else:
            ctr = end[1]
    return True


if __name__ == '__main__':
    print(validate([229, 65, 127, 256]))