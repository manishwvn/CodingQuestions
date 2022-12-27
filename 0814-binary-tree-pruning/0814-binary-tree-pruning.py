# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root):
            
            if not root: return False
            
            leftNode = helper(root.left)  
            rightNode = helper(root.right) 
            
            if not leftNode: 
                root.left = None
                
            if not rightNode:
                root.right = None
                
            if not leftNode and not rightNode and root.val != 1:
                return False
            
            return True
        
        if not helper(root): return None
        return root
        
        
        
        