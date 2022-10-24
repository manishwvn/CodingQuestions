# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        stack = [root]
        sum_ = 0
        
        def isLeaf(node):
            if node and node.left is None and node.right is None:
                return True
            else: 
                return False
        
        while stack:
            node = stack.pop()
            if isLeaf(node.left):
                sum_ += node.left.val
                
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
        
        return sum_
                
        
        