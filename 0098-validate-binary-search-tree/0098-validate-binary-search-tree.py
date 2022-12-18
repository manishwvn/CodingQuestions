# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
    
        stack = []
        min, max = float('-inf'), float('inf')
    
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= min or root.val >= max:
                return False

            min = root.val
            root = root.right

        return True
        