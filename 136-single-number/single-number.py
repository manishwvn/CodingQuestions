class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        for k, v in hm.items():
            if v == 1:
                return k
        