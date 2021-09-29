class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        hm = {0:1}
        sum_ = 0
        for i in range(0, len(nums)):
            sum_ += nums[i]
            remSum = sum_ - k
            
            if remSum in hm:
                ans += hm[remSum]
                
            if sum_ in hm:
                hm[sum_] += 1
            else:
                hm[sum_]  = 1
            
        return ans
        