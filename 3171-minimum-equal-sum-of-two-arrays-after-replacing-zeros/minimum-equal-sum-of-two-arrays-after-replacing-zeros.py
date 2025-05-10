class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        sum_1, sum_2, c1, c2 = 0, 0, 0, 0

        for val in nums1:
            if val == 0:
                c1 += 1
                sum_1 += 1
            else:
                sum_1 += val

        for val in nums2:
            if val == 0:
                c2 += 1
                sum_2 += 1
            else:
                sum_2 += val

        print(sum_1, sum_2, c1, c2)

        if c1 == 0 and sum_2 > sum_1:
            return -1

        if c2 == 0 and sum_1 > sum_2:
            return -1

        return max(sum_1, sum_2)
        