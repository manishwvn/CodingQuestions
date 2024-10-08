class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []

        for i in range(2*n):
            result.append(nums[i % n])

        return result

        