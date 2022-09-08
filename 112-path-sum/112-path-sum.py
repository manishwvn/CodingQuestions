# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, targetSum, currSum):
            if not node:
                return False
            
            currSum += node.val
            left = helper(node.left, targetSum, currSum)
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
            right = helper(node.right, targetSum, currSum )
            
            return left or right
            
                
        
        if not root:
            return False
        
        return helper(root, targetSum, 0)
            
        