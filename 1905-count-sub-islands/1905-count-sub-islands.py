class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m, n = len(grid1), len(grid1[0])
        visited = set()
        count = 0
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r == m or c == n or grid2[r][c] == 0 or (r, c) in visited:
                return True
            
            visited.add((r,c))
            result = True
            if grid1[r][c] == 0:
                result = False
                
            result = dfs(r-1, c) and result
            result = dfs(r+1, c) and result
            result = dfs(r, c-1) and result
            result = dfs(r, c+1) and result
            
            return result
        
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i, j) not in visited and dfs(i, j):
                    count += 1
                    
        return count
                    
        