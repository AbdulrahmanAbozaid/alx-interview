#!/usr/bin/env python3
"""Test Module"""
minOperations = __import__("test").minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Not Correct pass n")
        exit(0)
    n = int(sys.argv[1])
    result = minOperations(n)
    print(result)
