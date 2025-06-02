class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        if len(nums) == 3:
            if 2 * (nums[0] + nums[2]) == nums[1]:
                return 1
            else:
                return 0

        count = 0

        for i in range(len(nums)-2):
            if 2 * (nums[i] + nums[i+2]) == nums[i+1]:
                count += 1

        return count

        