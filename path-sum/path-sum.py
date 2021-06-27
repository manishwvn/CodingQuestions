# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
    
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        
        #only check sum if it is a leaf node
        if root.left == None and root.right == None:
            if targetSum == 0:
                return True
            return False

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        