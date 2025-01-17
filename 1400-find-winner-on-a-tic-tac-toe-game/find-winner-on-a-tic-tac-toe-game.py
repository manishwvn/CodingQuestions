class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def check_row(row, player):
            for col in range(n):
                if board[row][col] != player:
                    return False
            return True
        
        def check_col(col, player):
            for row in range(n):
                if board[row][col] != player:
                    return False
            return True

        def check_diagonal1(player):
            for row in range(n):
                if board[row][row] != player:
                    return False
            return True

        def check_diagonal2(player):
            for row in range(n):
                if board[row][n-1-row] != player:
                    return False
            return True

        n = 3
        board = [[0] * n for _ in range(n)]

        player = 1

        for move in moves:
            row, col = move
            board[row][col] = player

            if check_row(row, player) \
            or check_col(col, player) \
            or check_diagonal1(player) \
            or check_diagonal2(player):
                return "A" if player == 1 else "B"

            player *= -1

        if len(moves) == n * n:
            return "Draw"
        else:
            return "Pending"

        