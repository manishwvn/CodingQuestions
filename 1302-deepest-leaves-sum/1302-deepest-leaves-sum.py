# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:
            return root.val
        
        queue = collections.deque()
        queue.append(root)
        result = 0
        
        while queue:
            curr = 0
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                
                #leaf
                if not node.left and not node.right:
                    curr += node.val
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            if not queue and curr > result:
                result = curr
                
        return result
                    
            
        