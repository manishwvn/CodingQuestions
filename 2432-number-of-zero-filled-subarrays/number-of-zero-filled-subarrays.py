class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        result = count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                count = 0

            result += count

        return result
        