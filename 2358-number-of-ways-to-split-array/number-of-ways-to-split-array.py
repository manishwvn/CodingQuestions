class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        n = len(nums)
        prefix_sums = [0] * n

        prefix_sums[0] = nums[0]
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i-1] + nums[i]

        print(prefix_sums)
        counts = 0

        for i in range(n-1):
            if prefix_sums[i] >= prefix_sums[n-1] - prefix_sums[i]:
                counts += 1
        
        return counts
