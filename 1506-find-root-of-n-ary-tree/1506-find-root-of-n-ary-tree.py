"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        visited = set()
        
        for node in tree:
            for child in node.children:
                visited.add(child.val)
                
        for node in tree:
            if node.val not in visited:
                return node
        