class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #bfs approach
        
        m, n = len(grid), len(grid[0])
        queue = deque()
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        perimeter = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    grid[i][j] = -1
                    
        while queue:
            r, c = queue.popleft()
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if (nr < 0 or nr >= m or nc < 0 or nc >= n) or (nr>= 0 and nr <m and nc >=0 and nc <n and grid[nr][nc] == 0):
                    perimeter += 1
                    
        return perimeter