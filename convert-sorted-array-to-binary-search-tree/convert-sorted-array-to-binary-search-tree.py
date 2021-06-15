# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        leftNode = self.sortedArrayToBST(nums[0:mid])
        rightNode = self.sortedArrayToBST(nums[mid+1:])
        
        root.left = leftNode
        root.right = rightNode
        
        return root