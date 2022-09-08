# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, target):
            if not node:
                return False
            
            if not node.left and not node.right:
                if node.val == target:
                    return True
                
            return helper(node.left, target - node.val) or helper(node.right, target - node.val)
                
            
            
    
        
        return helper(root, targetSum)
        
        