class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return [nums[0]]
        
        
        counts = collections.Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        result = []
        
        for num, count in counts.items():
            freq[count].append(num)
            
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                
                if len(result) == k:
                    return result
            
            
        