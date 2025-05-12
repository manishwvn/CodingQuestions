class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            if nums[0] < nums[1] and nums[2] < nums[1]:
                return sum(nums)
            else:
                return -1

        n = len(nums)
        left_min = [float('inf')] * n
        right_min = [float('inf')] * n

        # Fill left_min
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i-1])

        # Fill right_min
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i+1])

        print(left_min)
        print(right_min)

        min_sum = float('inf')
        for j in range(1, n-1):
            if left_min[j] < nums[j] and right_min[j] < nums[j]:
                curr_sum = left_min[j] + nums[j] + right_min[j]
                min_sum = min(min_sum, curr_sum)

        return min_sum if min_sum != float('inf') else -1
