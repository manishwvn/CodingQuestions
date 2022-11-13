class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bs(array, num):
            l, r = 0, len(array) - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if array[mid] == num:
                    return mid
                
                elif array[mid] <= num:
                    l = mid + 1
                    
                else:
                    r = mid - 1
                    
            return l
        
        
        result = [nums[0]]
        
        for i in range(len(nums)):
            if nums[i] > result[-1]:
                result.append(nums[i])
                
            else:
                j = bs(result, nums[i])
                result[j] = nums[i]
                
        return len(result)
    