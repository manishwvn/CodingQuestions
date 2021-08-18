class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node, visited):
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    dfs(adjacent, visited)
        
        #create an adjacency list
        graph = collections.defaultdict(list)
        visited = set()
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                components += 1
                
        return components
                
            
            