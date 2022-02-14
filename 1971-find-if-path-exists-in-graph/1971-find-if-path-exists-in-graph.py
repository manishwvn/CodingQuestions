class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            
        stack = []
        stack.append(source)
        visited = set()
        
        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            if node in visited:
                continue
                
            else:
                visited.add(node)
                
            for neighbor in graph[node]:
                stack.append(neighbor)
        
        return False
                
            