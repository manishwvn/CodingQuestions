class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        n = len(nums)
        ranges = []

        if n == 0:
            return [[lower, upper]]
        
        if lower < nums[0]:
            ranges.append([lower, nums[0] - 1])

        for i in range(n-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            ranges.append([nums[i] + 1, nums[i+1] - 1])

        if upper > nums[-1]:
            ranges.append([nums[-1]+1, upper])

        return ranges
        