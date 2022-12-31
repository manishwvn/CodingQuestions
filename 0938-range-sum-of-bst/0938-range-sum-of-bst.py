# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        sum_ = 0
        
        def helper(root):
            nonlocal sum_
            
            if not root:
                return
            
            
                
            if low <= root.val and high >= root.val:
                sum_ += root.val

            if low < root.val:
                helper(root.left)

            if root.val < high:
                helper(root.right)
            
            
        helper(root)
        return sum_
        