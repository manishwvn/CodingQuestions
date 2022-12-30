class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            
            node = queue.pop(0)
            print(node)
            result.append(node)
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == numCourses else []