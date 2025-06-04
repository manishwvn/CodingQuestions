class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for data in times:
            src, dest, time = data
            graph[src].append([dest, time])

        queue = []
        heappush(queue, [0, k])
        t = 0
        visited = set()

        while queue:
            time_1, node = heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            
            t = max(time_1, t)
            for neighbor, time_2 in graph[node]:
                if neighbor not in visited:
                    heappush(queue, [time_1 + time_2, neighbor])

        return t if len(visited) == n else -1


        