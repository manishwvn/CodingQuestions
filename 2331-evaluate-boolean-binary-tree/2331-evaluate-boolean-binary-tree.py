# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node.left and not node.right:
                if node.val == 1:
                    return True
                    
                else:
                    return False
                    
        
            left = helper(node.left)
            right = helper(node.right)
            
            if node.val == 2:
                return left or right
                
            if node.val == 3:
                return left and right
        
        return helper(root)
        
        