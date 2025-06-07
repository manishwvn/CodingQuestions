class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = 0

            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    bfs(i, j)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count