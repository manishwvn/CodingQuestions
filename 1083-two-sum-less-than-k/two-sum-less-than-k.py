class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()

        max_sum = -1
        for i in range(len(nums) - 1):
            target = k - nums[i]
            l, r = i + 1, len(nums) - 1
            curr = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    curr = nums[mid]
                    l = mid + 1
                else:
                    r = mid - 1
            if curr != -1:
                max_sum = max(max_sum, nums[i] + curr)

        return max_sum