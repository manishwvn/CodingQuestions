class Solution:
    def findLHS(self, nums: List[int]) -> int:

        counts = Counter(nums)
        max_len = 0
        
        for num in counts:
            if num + 1 in counts:
                max_len = max(max_len, counts[num] + counts[num+1])
        
        return max_len
        