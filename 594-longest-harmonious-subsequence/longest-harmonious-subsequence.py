class Solution:
    def findLHS(self, nums: List[int]) -> int:

        counts = {}
        max_len = 0

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if num - 1 in counts:
                max_len = max(max_len, counts[num] + counts[num - 1])

            if num + 1 in counts:
                max_len = max(max_len, counts[num] + counts[num+1])

        return max_len
        