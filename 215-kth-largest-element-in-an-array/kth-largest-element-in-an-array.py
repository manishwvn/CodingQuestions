class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minm, maxm = min(nums), max(nums)

        counts = [0] * (maxm - minm + 1)

        for num in nums:
            counts[num - minm] += 1

        remain = k
        for num in range(len(counts)-1, -1, -1):
            remain -= counts[num]
            if remain <= 0:
                return num + minm

        return -1

        