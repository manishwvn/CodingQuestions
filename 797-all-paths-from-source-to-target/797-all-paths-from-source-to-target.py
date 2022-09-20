class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph) - 1
        paths = []
        
        def helper(src, path):
            if src == target:
                paths.append(path.copy())
                return
            
            
            for node in graph[src]:
                path.append(node)
                helper(node, path)
                path.pop()
        
        helper(0, [0])
        return paths
        