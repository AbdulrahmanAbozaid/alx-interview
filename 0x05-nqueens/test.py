#!/usr/bin/python3
"""
NQueens
"""


def is_safe(r: int, c: int, n: int, mat: list) -> bool:
    """Check the ability to put a queen here"""
    i = r
    j = c

    for x in range(c):
        if mat[r][x] == 1:
            return False

    while i >= 0 and j >= 0:
        if mat[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = r, c

    while i < n and j >= 0:
        if mat[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def nqueens(col: int, n: int, mat: list, ans: list) -> None:
    """Solve nqueens problem recusively"""
    if col == n:
        ans.append([[i, j] for i in range(n) for j in range(n) if mat[i][j]])
        return

    for i in range(n):
        if is_safe(i, col, n, mat):
            mat[i][col] = 1
            nqueens(col + 1, n, mat, ans)
            mat[i][col] = 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    mat = [[0 for i in range(n)] for _ in range(n)]
    ans = []
    nqueens(0, n, mat, ans)

    for row in ans:
        print(row)
