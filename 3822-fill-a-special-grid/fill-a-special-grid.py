from typing import List

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size = 1 << n  # 2^n
        grid = [[0] * size for _ in range(size)]

        def dfs(r: int, c: int, length: int, start: int) -> int:
            if length == 1:
                grid[r][c] = start
                return start + 1

            half = length // 2

            # Fill in quadrants in the correct DFS order:
            # Top-right
            next_val = dfs(r, c + half, half, start)
            # Bottom-right
            next_val = dfs(r + half, c + half, half, next_val)
            # Bottom-left
            next_val = dfs(r + half, c, half, next_val)
            # Top-left
            next_val = dfs(r, c, half, next_val)

            return next_val

        dfs(0, 0, size, 0)
        return grid