class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        seen = {}
        for node in range(len(graph)):
            if node not in seen:
                seen[node] = 0
                stack = [node]
                
                while stack:
                    currentNode = stack.pop()
                    
                    for neighbor in graph[currentNode]:
                        if neighbor not in seen:
                            stack.append(neighbor)
                            seen[neighbor] = seen[currentNode] ^ 1
                            
                        elif seen[neighbor] == seen[currentNode]:
                            return False
                        
        return True
            
        