class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        target = [m-1, n-1]
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        if k >= m + n - 2:
            return m + n - 2
        
        
        count = 0
        cell = (0, 0, k)
        queue = deque()
        queue.append([count, cell])
        visited = set(cell)
        
        while queue:
            count, cell = queue.popleft()
            
            r, c, k = cell
            
            if r == target[0] and c == target[1]:
                return count
            
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                
                if (0 <= nr < m) and (0 <= nc < n):
                    nk = k - grid[nr][nc]
                    ncell = (nr, nc, nk)
                    
                    
                    if nk >= 0 and ncell not in visited:
                        queue.append([count+1, ncell])
                        visited.add(ncell)
                        
        return -1                
        
                    
            
            
        
        