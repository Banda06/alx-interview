#!/usr/bin/python3
"""
N quenns finds all posible solutions.

"""
import sys

def validate_input():
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
    
    return N

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            board[row] = -1

def print_solutions(solutions, N):
    for solution in solutions:
        result = []
        for row in range(N):
            result.append([row, solution[row]])
        print(result)

def main():
    N = validate_input()
    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions, N)

if __name__ == "__main__":
    main()
