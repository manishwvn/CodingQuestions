class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
#         n = len(graph)
#         result = []
        
#         def dfs(src, path):
            
#             if src == n - 1 :
#                 result.append(path.copy())
#                 return
            
#             for neigh in graph[src]:
#                 path.append(neigh)
#                 dfs(neigh, path)
#                 path.pop()
                
#         dfs(0, [0])
#         return result


        n = len(graph)
        queue = deque()
        queue.append([0, [0]])
        result = []
        
        while queue:
            node, path = queue.popleft()
            
            if node == n - 1:
                result.append(path.copy())
                      
            for nei in graph[node]:
                # path.append(nei)
                queue.append((nei, path + [nei]))
                      
        return result
                      
                      
        
                
                
                
            
    
    
    
    
        
        
        