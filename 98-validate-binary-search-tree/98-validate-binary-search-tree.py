# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        global prev, flag
        prev, flag = None, True
        
        def helper(node):
            global prev, flag
            
            if not node:
                return 
            
            if node.left:
                helper(node.left)
                
            if prev and prev.val >= node.val:
                flag = False
                return
            
            prev = node
            if flag:
                if node.right:
                    helper(node.right)
                
        
        helper(root)
        return flag
    
    
        
        