class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        areas = {}
        iid = -1
        
        def dfs(grid, r, c):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == 1:
                grid[r][c] = iid
                area = 1
                
                for dir in dirs:
                    nr = r + dir[0]
                    nc = c + dir[1]
                    
                    area += dfs(grid, nr, nc)
                    
                return area
            
            else:
                return 0
                    
                
            
        
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(grid, r, c)
                    
                    areas[iid] = area
                    iid -= 1
        
        max_area = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    area = 1
                    
                    surround = set()
                    
                    for dir in dirs:
                        nr = r + dir[0]
                        nc = c + dir[1]
                        
                        if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and grid[nr][nc] != 0:
                            surround.add(grid[nr][nc])
                            
                    for iid in surround:
                        area += areas[iid]
                        
                    max_area = max(max_area, area)
                    
        return max_area if max_area else (len(grid) ** 2)
                            
                    