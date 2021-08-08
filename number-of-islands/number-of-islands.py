class Solution:
    def dfs(self, grid, row, col):
    
        rows, cols = len(grid), len(grid[0])

        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col]=='0':
            # print("DID NOTHING!!")
            return

        grid[row][col] = '0'
        # print(f"Making grid[{row}, {col}]=0", grid)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    numIslands += 1
                    #grid[row][col] = '0'
                    # print("Before:", grid)
                    self.dfs(grid, row, col)
                    # print("After:", grid)
                    
                    
        return numIslands
                    
        