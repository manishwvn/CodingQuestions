class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) < 3: return []
        
        nums.sort()
        
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]: continue
            
            a = nums[i]
            l, r = i+1, n-1
            
            while l < r:
                
                b, c = nums[l], nums[r]
                sum_ = a + b + c
                
                if sum_ == 0:
                    result.append([a, b, c])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l-1] == nums[l]: l+= 1
                    while l < r and nums[r] == nums[r+1]: r-= 1
                        
                elif sum_ < 0: l += 1
                    
                else: r -= 1
        
        return result

                
                
            
            