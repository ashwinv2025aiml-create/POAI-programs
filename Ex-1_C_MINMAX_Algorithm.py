# To Implement Minimax Algorithm

import math

#Minimax for Tic-Tac-Toe

def minimax_tictactoe():
    PLAYER_X = 1
    PLAYER_O = -1
    EMPTY = 0

    def evaluate(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return board[i][0]
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != EMPTY:
                return board[0][j]
        if board[0][0] == board[1][1] == board[2][2] != EMPTY:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != EMPTY:
            return board[0][2]
        return 0

    def is_moves_left(board):
        return any(cell == EMPTY for row in board for cell in row)

    def minimax(board, is_max):
        score = evaluate(board)
        if score != 0:
            return score
        if not is_moves_left(board):
            return 0

        if is_max:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_X
                        best = max(best, minimax(board, False))
                        board[i][j] = EMPTY
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_O
                        best = min(best, minimax(board, True))
                        board[i][j] = EMPTY
            return best

    def find_best_move(board):
        best_value = -math.inf
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    value = minimax(board, False)
                    board[i][j] = EMPTY
                    if value > best_value:
                        best_value = value
                        best_move = (i, j)
        return best_move

    def print_board(board):
        for row in board:
            print(" ".join("X" if c == PLAYER_X else "O" if c == PLAYER_O else "."
                           for c in row))

    board = [
        [EMPTY, PLAYER_X, PLAYER_O],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, PLAYER_O, PLAYER_X]
    ]

    print("Current Board\n")
    print_board(board)

    move = find_best_move(board)
    print("\nBest Move (row, col):", move)

    board[move[0]][move[1]] = PLAYER_X
    print("\nBoard After AI Move\n")
    print_board(board)

# Part B: Minimax on a Game Tree

def minimax_tree():
    def minimax(depth, node_index, is_max, scores, height):
        if depth == height:
            return scores[node_index]

        left = minimax(depth + 1, node_index * 2, not is_max, scores, height)
        right = minimax(depth + 1, node_index * 2 + 1, not is_max, scores, height)

        return max(left, right) if is_max else min(left, right)

    scores = list(map(int, input("Enter 8 terminal node values: ").split()))
    height = int(math.log2(len(scores)))

    print("Optimal Value:", minimax(0, 0, True, scores, height))

# Main
if __name__ == "__main__":
    print("===== Minimax: Tic-Tac-Toe =====\n")
    minimax_tictactoe()

    print("\n===== Minimax: Game Tree =====\n")
    minimax_tree()


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   Part A: None (the board is fixed in the code)
#   Part B: Enter 8 terminal node values: 3 5 2 9 12 5 23 23
#
# Output:
#   ===== Minimax: Tic-Tac-Toe =====
#
#   Current Board
#
#   . X O
#   . . .
#   . O X
#
#   Best Move (row, col): (0, 0)
#
#   Board After AI Move
#
#   X X O
#   . . .
#   . O X
#
#   ===== Minimax: Game Tree =====
#
#   Enter 8 terminal node values: 3 5 2 9 12 5 23 23
#   Optimal Value: 12
