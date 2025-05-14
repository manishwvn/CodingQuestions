class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for index, num in enumerate(nums):
            heappush(heap, (num, index))
            if len(heap) > k:
                heappop(heap)

        while heap:
            num, index = heappop(heap)
            res.append(index)

        res.sort()
        return [nums[index] for index in res]