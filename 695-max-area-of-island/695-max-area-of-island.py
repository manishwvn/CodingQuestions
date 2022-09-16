class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(grid, i, j):
            dirs = [[-1,0], [0,-1], [1,0],[0,1]]
            queue = deque()
            queue.append([i,j])
            grid[i][j] = -1
            count = 1
            
            while queue:
                r, c = queue.popleft()
                
                for dir in dirs:
                    nr, nc = r + dir[0], c + dir[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc <n and grid[nr][nc] == 1:
                        count += 1
                        grid[nr][nc] = -1
                        queue.append([nr, nc])
            
            return count
                
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = bfs(grid, i, j)
                    max_area = max(curr, max_area)
        
        return max_area
                    