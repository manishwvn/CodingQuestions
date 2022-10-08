# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        def dfs(root, p, q, path):
            nonlocal path_p, path_q
            
            #base
            if not root:
                return
            
            if root == p:
                path_p = path.copy()
                path_p.append(root)
                path_p.append(root)
                
            if root == q:
                path_q = path.copy()
                path_q.append(root)
                path_q.append(root)
                
            #action
            path.append(root)
            
            #recursion
            dfs(root.left, p, q, path)
            dfs(root.right, p, q, path)
            
            #backtrack
            path.pop()
            
        path_p, path_q = [], []
        dfs(root, p, q, [])
        
        for i in range(len(path_p)):
            if path_p[i] != path_q[i]:
                return path_p[i - 1]
        
        
        