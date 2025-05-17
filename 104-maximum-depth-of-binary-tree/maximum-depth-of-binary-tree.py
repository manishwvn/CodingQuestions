# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curr_depth):
            nonlocal depth
            
            if not root:
                return
            
            depth = max(depth, curr_depth)
            dfs(root.left, curr_depth+ 1)
            dfs(root.right, curr_depth + 1)
         
        if not root:
            return 0
        depth = 1
        dfs(root, depth)
        return depth
