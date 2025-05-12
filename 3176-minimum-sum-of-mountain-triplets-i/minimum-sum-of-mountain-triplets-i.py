class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            if nums[0] < nums[1] and nums[2] < nums[1]:
                return sum(nums)
            else:
                return -1


        min_sum = float('inf')
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        curr_sum = nums[i] + nums[j] + nums[k]
                        min_sum = min(curr_sum, min_sum)

        return min_sum if min_sum != float('inf') else -1
