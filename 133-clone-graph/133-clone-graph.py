"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        visited = {}
        def clone(node):
            if node in visited:
                return visited[node]
            
            copy_node = Node(node.val)
            visited[node] = copy_node
            
            for neigh in node.neighbors:
                copy_node.neighbors.append(clone(neigh))
                    
            return copy_node
            
        return clone(node)
        