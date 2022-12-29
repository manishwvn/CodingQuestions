class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        result = []
        
        def dfs(src, path):
            
            if src == n - 1 :
                result.append(path)
                return
            
            for neigh in graph[src]:
                # path.append(neigh)
                dfs(neigh, path + [neigh])
                # path.pop(neigh)
                
                
            # path.pop()
                
        dfs(0, [0])
        return result
        
        
        