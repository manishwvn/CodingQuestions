class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return 0

            grid[i][j] = '0'

            for d in dirs:
                dfs(i+d[0], j+d[1])

            return 1



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += dfs(i,j)

        return count
        