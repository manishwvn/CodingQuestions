class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i):

            if i == len(nums):
                result.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        result = []
        backtrack(0)
        return result



        