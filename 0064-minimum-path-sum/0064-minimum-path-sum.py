class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        for r in range(0, m):
            for c in range(0, n):

                if r == 0 and c != 0:
                    grid[r][c] = grid[r][c] + grid[r][c-1]

                elif c == 0 and r != 0:
                    grid[r][c] = grid[r][c] + grid[r-1][c]

                elif r != 0 and c != 0:
                    grid[r][c] = min(grid[r-1][c], grid[r][c-1]) + grid[r][c]

        return grid[m-1][n-1]
        