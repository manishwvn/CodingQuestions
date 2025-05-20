"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_node, q_node = p, q

        while p_node != q_node:
            if p_node:
                p_node = p_node.parent
            else:
                p_node = q

            if q_node:
                q_node = q_node.parent
            else:
                q_node = p

        return p_node
        