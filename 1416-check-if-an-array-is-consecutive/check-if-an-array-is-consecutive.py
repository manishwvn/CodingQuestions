class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        if len(nums) == 1: return True

        min_num = min(nums)
        num_set = set(nums)

        for num in range(min_num, min_num + len(nums)):
            if num not in num_set:
                return False

        return True

        