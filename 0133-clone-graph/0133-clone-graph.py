"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return None
        
        graph = {}
        queue = deque()
        
        newNode = Node(node.val)
        queue.append(node)
        graph[node] = newNode
        
        while queue:
            current = queue.popleft()
            neighbors = current.neighbors
            for n in neighbors:
                if n not in graph:
                    n_copy = Node(n.val)
                    graph[n] = n_copy
                    queue.append(n)
                    
                graph[current].neighbors.append(graph[n])
                
        return newNode
        
        