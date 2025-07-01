class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces += 1

        return provinces