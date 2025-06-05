class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]

        new_res = []
        for i in range(len(pos)):
            new_res.append(pos[i])
            new_res.append(neg[i])

        return new_res
