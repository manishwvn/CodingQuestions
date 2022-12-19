class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        degree = max(counts.values())
        
        left, right = {}, {}
        
        for i, num in enumerate(nums):
            if num not in left: left[num] = i
            right[num] = i
            
        result = len(nums)
        
        for num in counts:
            if counts[num] == degree:
                result = min(result, right[num] - left[num] + 1)
                
        return result
                