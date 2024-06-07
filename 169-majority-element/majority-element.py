class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # O(n) Time and O(1) Space
        # Boyer-Moore Algorithm
        if len(nums) == 1:
            return nums[0]

        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1

        return res
