# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,root,ancestors):
        if not root:
            return None
        
        if root.right:
            ancestors[root.right] = root
            
        if root.left:
            ancestors[root.left] = root
            
            
        self.dfs(root.left,ancestors)
        self.dfs(root.right,ancestors)
        
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1 = p
        ancestors = collections.defaultdict(None)
        ancestors[root] = None
        self.dfs(root,ancestors)
        
        ancestors_p = set()
        
        while p:
            ancestors_p.add(p)
            p = ancestors[p]
               
        ans = None
        
        while q:
           
            if q in ancestors_p:

                
                return q
                
            q = ancestors[q]
            
            
        return ans
            
        
            
            