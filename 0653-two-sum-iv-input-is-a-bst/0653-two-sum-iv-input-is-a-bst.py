# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        queue = deque()
        queue.append(root)
        seen = set()
        
        while queue:
            p = queue.popleft()
            
            if k - p.val in seen: return True
            seen.add(p.val)
            
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
                    
        return False
                
            
        