# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        result, queue = [], deque()
        queue.append(root)
        
        while queue:
            count = len(queue)           
            nodes = []
            for i in range(0, count):
                node = queue.popleft()
                nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            result.append(nodes)
                
        return result