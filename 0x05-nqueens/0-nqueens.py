#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False
        # Check the diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    """Use backtracking to find all solutions."""
    if row == n:
        # Convert the board representation into the expected output format
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            # Backtrack by removing the queen
            board[row] = -1

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board and solutions list
    board = [-1] * n
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(n, 0, board, solutions)

    # Print all the solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
