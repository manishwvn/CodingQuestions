class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
    
        graph = {}
        for i in range(n):
            graph[i] = []
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)

        print(graph)

        visited = set()
        stack = []
        provinces = 0

        for i in range(n):
            if i not in visited:
                stack.append(i)
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        stack.extend(graph[node])
                provinces += 1

        return provinces
        