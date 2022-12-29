class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
    
        def bfs(r, c):   
            queue = deque()
            queue.append([r, c])
            area = 1

            while queue:
                r, c = queue.popleft()

                grid[r][c] = -1
                for dir in dirs:
                    nr, nc = r + dir[0], c + dir[1]

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        area += 1
                        grid[nr][nc] = -1
                        queue.append([nr, nc])

            return area
        
        
        m, n = len(grid), len(grid[0])
        max_area = 0
        
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    max_area = max(area, max_area)
                    
                    
        return max_area
                    
