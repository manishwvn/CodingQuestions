# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            value = nums[mid]
            node = TreeNode(value)
            
            node.left = helper(start, mid-1)
            node.right = helper(mid +1, end)
            return node
        
        # hm = {v:i for i, v in enumerate(nums)}
        return helper(0, len(nums) - 1)
        
        
        
        