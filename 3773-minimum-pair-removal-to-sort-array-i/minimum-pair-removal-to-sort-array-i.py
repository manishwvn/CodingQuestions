class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        def is_sorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        while not is_sorted(nums):
            min_sum = float("inf")
            min_idx = -1

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    min_idx = i

            merged = nums[min_idx] + nums[min_idx + 1]
            nums = nums[:min_idx] + [merged] + nums[min_idx + 2:]
            ops += 1

        return ops



        