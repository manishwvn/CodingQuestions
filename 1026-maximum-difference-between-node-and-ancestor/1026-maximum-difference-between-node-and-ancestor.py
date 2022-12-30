# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        global result 
        result = 0
        minm, maxm = 10**6, -1
        
        def helper(root, minm, maxm):
            global result

            if not root:
                result = max(result, abs(maxm - minm))
                return
            
            result = max(result, maxm - minm)
            minm = min(minm, root.val)
            maxm = max(maxm, root.val)
            
            helper(root.left, minm , maxm)
            helper(root.right, minm, maxm)        
            
            
        helper(root, minm, maxm)
        return result
        
        