class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        queue = deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    queue.append([i, j, 0])
                    visited.add((i, j))
                    break
                    
        while queue:
            r, c, steps = queue.popleft()
            
            if grid[r][c] == "#":
                return steps
            
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != "X":
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append([nr, nc, steps + 1])
                        
        return -1
            
                    
        
        