# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        

        def traverse(root):
            nonlocal nums
            if not root:
                return
            traverse(root.left)
            nums.append(root.val)
            traverse(root.right)

        nums = []
        traverse(root)
        print(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == k:
                return True
            elif sum_ > k:
                r -= 1
            else:
                l += 1
        return False

            