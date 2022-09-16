class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        perimeter = 0
        
        def dfs(grid, i, j, m, n):
            nonlocal perimeter        
            if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0):
                perimeter += 1
                return 
            
            
            grid[i][j] = -1
        
            for dir in dirs:
                nr, nc = i + dir[0], j + dir[1]
                if nr < 0 or nr >= m:
                    perimeter += 1
                
                if nc < 0 or nc >= n:
                    perimeter += 1
                
                if nr>= 0 and nr < m and nc >=0 and nc < n and grid[nr][nc] == 0:
                    dfs(grid, nr, nc, m, n)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(grid, i, j, m, n)
                    
        return perimeter