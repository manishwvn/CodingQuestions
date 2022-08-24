class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        prefixSum = 0
        result = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in hm:
                result += hm[prefixSum - k]
                
            if prefixSum not in hm:
                hm[prefixSum] = 0
            hm[prefixSum] += 1
            
        return result
        