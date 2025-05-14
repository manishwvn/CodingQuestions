class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_num = -1
        max_num_i = -1

        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_num_i = i

        max_sec = -1
        for i, num in enumerate(nums):
            if num > max_sec and num <= max_num and i != max_num_i:
                max_sec = num

        return (max_num - 1) * (max_sec -1)

        