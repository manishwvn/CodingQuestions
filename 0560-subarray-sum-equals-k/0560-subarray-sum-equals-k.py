class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count, sum_ = 0, 0
        hm = defaultdict(int)
        hm[0] = 1
        
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ - k in hm:
                count += hm[sum_ - k]
            # if sum_ in hm:
            #     hm[sum_] += 1
            # else:
            #     hm[sum_] = 1
            hm[sum_] += 1
            
        return count
        
        