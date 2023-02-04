# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        def depth(root):
            
            d = 0
            
            while root.left:
                d += 1
                root = root.left
                
            return d
        
        def check(idx, d, node):
            left, right = 0, 2**d - 1
            
            for _ in range(d):
                mid = (left + right) // 2
                
                if idx <= mid:
                    node = node.left
                    right = mid
                    
                else:
                    node = node.right
                    left = mid + 1
                    
            return node 
        
        
        d = depth(root)
        if d == 0: return 1
        
        left, right = 1, 2**d - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid, d, root):
                left = mid + 1
                
            else:
                right = mid - 1
                
        return (2 ** d - 1) + left
        
                
        
        