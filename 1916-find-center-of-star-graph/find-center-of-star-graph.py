class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = {}
        for u, v in edges:
            graph[u] = graph.get(u, 0) + 1
            graph[v] = graph.get(v, 0) + 1

        print(graph)
        for node, count in graph.items():
            if count == len(edges):
                return node