class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1

        grid[0][0] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque()
        queue.append([0, 0])
        distance = 1
        while queue:
            r, c = queue.popleft()
            distance = grid[r][c]
            if [r, c] == [m-1, n-1]:
                return distance

            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = distance + 1
                    queue.append([nr, nc])

        return -1
        