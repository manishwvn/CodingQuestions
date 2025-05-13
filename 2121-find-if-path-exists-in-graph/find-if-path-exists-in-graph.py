class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = [[] for _ in range(n)]
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            return False
        return dfs(source)
        

