# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(node, currSum):
            
            if not node: return False
            
            currSum += node.val
            
            leftSum = pathSum(node.left, currSum)
            
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
                
            rightSum = pathSum(node.right, currSum)
            
            return leftSum or rightSum
            
        return pathSum(root, 0)
        
        