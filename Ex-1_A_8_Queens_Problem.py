#To Implement Eight Queens Problem using backtracking 


N = 8  # Size of the chessboard (N x N)

def print_solution(board):
    """Print the board with Q for a queen and . for an empty square."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    # Check the column above
    for i in range(row):
        if board[i][col]:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False

    return True


def solve(board, row, solutions):
    """Place queens row by row using backtracking."""
    if row == N:
        solutions.append([r[:] for r in board])  # save a copy of this solution
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1                # Place queen
            solve(board, row + 1, solutions)   # Move to next row
            board[row][col] = 0                # Backtrack (remove queen)


def eight_queens():
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)

    if not solutions:
        print("Solution does not exist")
        return

    print(f"Total solutions: {len(solutions)}\n")
    print("One of the possible solutions:\n")
    print_solution(solutions[0])


if __name__ == "__main__":
    eight_queens()


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   None
#
# Output:
#   Total solutions: 92
#
#   One of the possible solutions:
#
#   Q . . . . . . .
#   . . . . Q . . .
#   . . . . . . . Q
#   . . . . . Q . .
#   . . Q . . . . .
#   . . . . . . Q .
#   . Q . . . . . .
#   . . . Q . . . .
