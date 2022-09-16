class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid or len(grid) == 0: return 0
        
        m, n = len(grid), len(grid[0])
        fresh, time = 0, 0
        queue = deque()
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    
                if grid[i][j] == 1:
                    fresh += 1
                    
        if not fresh: return 0
        
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                for dir in dirs:
                    r, c = dir[0] + curr[0], dir[1] + curr[1]
                    
                    if (r >= 0 and r < m) and (c >=0 and c < n) and (grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        if fresh == 0:
                            return time + 1
                        queue.append([r, c])
                        
            time += 1
            
            
        if fresh: return -1
        return time - 1
            
        
        