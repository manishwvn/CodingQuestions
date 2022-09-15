# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            x_, y_ = False, False
            
            for i in range(size):
                node = queue.popleft()
                if node.val == x:
                    x_ = True
                    
                if node.val == y:
                    y_ = True
                    
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    
                    if node.left.val == y and node.right.val == x:
                        return False
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            if x_ and y_:
                return True
            
            if x_ or y_:
                return False
            
        return False