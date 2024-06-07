class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #O(n) time - O(n) space
        seen = {}
        n = len(nums)
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:    
                seen[num] = 1
            if seen[num] > n // 2:
                    return num
        