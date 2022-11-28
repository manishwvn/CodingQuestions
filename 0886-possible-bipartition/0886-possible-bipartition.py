class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        for node in range(1, n+1):
            if node not in color:
                color[node] = 0
                queue = deque([node])
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = color[node] ^ 1
                            queue.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True
        