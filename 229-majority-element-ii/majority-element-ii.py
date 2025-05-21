class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        counts = Counter(nums)
        n = len(nums)

        res = []
        for num in counts:
            if counts[num] > n // 3:
                res.append(num)

        return res
        