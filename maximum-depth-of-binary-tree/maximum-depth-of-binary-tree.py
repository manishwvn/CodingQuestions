# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        leftDepth =  self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1
        