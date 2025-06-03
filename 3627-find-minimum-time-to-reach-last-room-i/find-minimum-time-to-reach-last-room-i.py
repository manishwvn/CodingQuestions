class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        queue = []
        heapify(queue)
        heappush(queue, (0, 0, 0))  # (time, row, col)
        visited = {}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            curr_time, r, c = heappop(queue)

            if (r, c) == (n - 1, m - 1):
                return curr_time

            if (r, c) in visited and visited[(r, c)] <= curr_time:
                continue

            visited[(r, c)] = curr_time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    wait_time = max(curr_time, moveTime[nr][nc])
                    new_time = wait_time + 1
                    heappush(queue, (new_time, nr, nc))

        return visited[-1][-1]