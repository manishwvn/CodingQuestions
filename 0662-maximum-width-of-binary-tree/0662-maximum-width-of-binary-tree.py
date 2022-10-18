# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque()
        queue.append((root, 0))
        
        max_width = 0
        
        while queue:
            size = len(queue)
            node, level_index = queue[0]
            for i in range(size):
                node, index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2 * index))
                    
                if node.right:
                    queue.append((node.right, 2 * index + 1))
                    
            max_width = max(max_width, index - level_index+1)
            
        return max_width
        
        