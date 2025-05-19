from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            board[r][c] = 'T'  # temporary mark

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        board[nx][ny] = 'T'
                        queue.append((nx, ny))

        # Start BFS from border 'O's
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    bfs(i, j)
        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    bfs(i, j)

        # Flip and restore
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # surrounded
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # restore