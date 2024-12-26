class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        total = sum(nums)
        counts = collections.Counter(nums)
        outlier = -1001

        for num in nums:
            total -= num
            counts[num] -= 1

            if total % 2 == 0 and counts.get(total // 2, 0) > 0:
                outlier = max(outlier, num)

            total += num
            counts[num] += 1

        return outlier
        