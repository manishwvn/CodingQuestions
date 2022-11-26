class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        islands = set()
        visited = set()
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        def bfs(r, c, visited, islands):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            path = ""
            
            
            while queue:
                cr, cc = queue.popleft()
                path += str(cr-r) + str(cc-c)
                
                for dir in dirs:
                    nr, nc = cr + dir[0], cc + dir[1]
                    
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                            
            islands.add(path)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j, visited, islands)
                    
        return len(islands)

        
        
        