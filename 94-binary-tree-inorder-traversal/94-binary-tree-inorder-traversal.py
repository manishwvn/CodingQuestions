# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(node, res):
            if not node:
                return
            
            if node.left:
                helper(node.left, res)
            res.append(node.val)
            if node.right:
                helper(node.right, res)
            return res
            
        
        if not root:
            return []
        
        res = []
        helper(root, res)
        return res
        