#!/usr/bin/python3
"""To create a chessboard of N x N size"""


import sys
"""Sys module imported"""

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N: int = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

except ValueError:
    print("N must be a number")
    sys.exit(1)


def create_chessboard(N):
    """Creates an N x N chessboard with empty cells"""

    board = [["."] * N for _ in range(N)]
    return (board)


def is_safe(board, row, col):
    """To check if a Queen can be safely placed at
    board[row][col].
    """

    # Check for Queens in the same row
    for i in range(col):
        if board[row][i] == "Q":
            return (False)

    # Check for Queens in the upper diagonal
    for i, j in zip(
            range(row, -1, -1),
            range(col, -1, -1) if col else range(0, 0),
    ):
        if board[i][j] == "Q":
            return (False)

    # Check for Queens in the lower diagonal
    for i, j in zip(
            range(row, N, 1),
            range(col, -1, -1) if col else range(0, 0),
    ):
        if board[i][j] == "Q":
            return (False)

    # If no conflicts found, the position is safe.
    return (True)


solutions = []
board = create_chessboard(N)


def solve_nqueens(N, board, row):
    """My Backtracking algorithm using recursion"""

    if row == N:
        solutions.append(board.copy())
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            solve_nqueens(N, board, row + 1)
            board[row][col] = "."


def print_solution(solutions):
    """To print the solutions gotten from the
    backtracking algorithm"""

    for solution in solutions:
        queens = [[row, col.index("Q")] for row,
                  col in enumerate(solution) if "Q" in col]
        print(queens)
        print()


solve_nqueens(N, board, 0)
print_solution(solutions)
