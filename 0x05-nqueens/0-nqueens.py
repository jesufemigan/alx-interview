#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board, col):
    """Solves the N-queens problem recursively."""
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res |= solve_n_queens(board, col + 1)
            board[i][col] = 0
    return res


def print_solutions(solutions):
    """Prints the solutions in the required format."""
    for solution in solutions:
        print(solution)


def main():
    """Main function to handle arguments and solve the problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    global solutions
    solutions = []
    board = [[0] * N for _ in range(N)]
    solve_n_queens(board, 0)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
