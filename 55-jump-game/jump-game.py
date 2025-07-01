class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # can't reach this index
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return True