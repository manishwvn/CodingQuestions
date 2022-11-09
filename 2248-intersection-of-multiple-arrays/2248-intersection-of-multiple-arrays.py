class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = {}
        
        for arr in nums:
            for x in arr:
                if x in counts:
                    counts[x] += 1
                else:
                    counts[x] = 1
                
        ans = []
        n = len(nums)
        
        for key in counts:
            if counts[key] == n:
                ans.append(key)
                
        return sorted(ans)