# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = None 
        closest_difference = float('inf')
        from collections import deque 
        
        queue = deque([root])    
        while queue:
            node = queue.popleft()
            curr_difference = abs(target - node.val)
            if curr_difference < closest_difference:
                closest_difference = curr_difference
                closest_value = node.val
            elif curr_difference == closest_difference:
                if node.val < closest_value:
                    closest_value = node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return closest_value
        