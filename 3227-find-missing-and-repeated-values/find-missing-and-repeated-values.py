class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        freq = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] in freq:
                    freq[grid[i][j]] += 1
                else:
                    freq[grid[i][j]] = 1
        
        miss, repeat = -1, -1

        for num in range(1, n*n + 1):
            if num not in freq:
                miss = num
            elif freq[num] == 2:
                repeat = num
        
        return [repeat, miss]