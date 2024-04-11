#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed at position (row, col) on the board
    # without attacking any other queens.

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0, N)

def solve_nqueens_util(board, col, N):
    if col >= N:
        # Print the solution when all N queens are placed successfully
        print_solution(board, N)
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_nqueens_util(board, col + 1, N)

            # Backtrack and remove the queen from the current position
            board[i][col] = 0

def print_solution(board, N):
    # Print the board configuration for a valid solution
    solution = []
    for row in board:
        line = ''.join(['Q' if cell == 1 else '.' for cell in row])
        solution.append(line)
    print('\n'.join(solution))
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)
