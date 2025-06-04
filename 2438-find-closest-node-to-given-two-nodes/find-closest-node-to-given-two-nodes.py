class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        graph = defaultdict(list)

        for src, dest in enumerate(edges):
            if dest > -1:
                graph[src].append(dest)

        def bfs(src, dists):
            queue = deque()
            queue.append([src, 0])
            dists[src] = 0

            while queue:
                node, dist = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in dists:
                        queue.append([neighbor, dist + 1])
                        dists[neighbor] = dist + 1

        node1_dist = {}
        node2_dist = {}
        bfs(node1, node1_dist)
        bfs(node2, node2_dist)
        print(node1_dist)

        res = -1
        res_dist = float('inf')

        for i in range(len(edges)):
            if i in node1_dist and i in node2_dist:
                dist = max(node1_dist[i], node2_dist[i])
                if dist < res_dist:
                    res = i
                    res_dist = dist

        return res