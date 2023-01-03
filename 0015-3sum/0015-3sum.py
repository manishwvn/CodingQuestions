class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #edge case
        if not nums or len(nums) < 3: return []
        
        #sort
        nums.sort()
        
        result = []
        
        for i in range(len(nums)):
            a = nums[i]
            l, r = i+1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while l < r:
                b, c = nums[l], nums[r]
                sum_ = a + b + c
                if sum_ == 0: 
                    result.append([a, b, c])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
                elif sum_ < 0:
                    l += 1
                    
                else:
                    r -= 1
                    
        return result
                
                    
                
                
                
        
        