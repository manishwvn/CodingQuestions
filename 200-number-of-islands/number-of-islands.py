class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(grid, r, c):
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]
            queue = deque()
            queue.append((r, c))
            grid[r][c] = '-1'
            islands = 1

            while queue:
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = '-1'
                        queue.append((nr, nc))
            
            return islands





        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    curr_count = bfs(grid, i, j)
                    count += curr_count
                
        return count
        