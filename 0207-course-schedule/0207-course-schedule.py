class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            graph[i].append(j)

        visited = [0] * numCourses


        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True

            visited[node] = -1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 1

            return True

        for node in range(numCourses):
            if not dfs(node):
                return False

        return True