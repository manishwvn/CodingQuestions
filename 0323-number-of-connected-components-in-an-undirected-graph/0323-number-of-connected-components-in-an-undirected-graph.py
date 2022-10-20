class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}
    
        for i in range(n):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
    
        print(graph)
        count = 0
        stack = []
        visited = set()
        #run iterative dfs on each node

        for node in graph:
            if node not in visited:
                count += 1
                stack.append(node)

                while stack:
                    curr = stack.pop()
                    visited.add(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        return count
        
        
        