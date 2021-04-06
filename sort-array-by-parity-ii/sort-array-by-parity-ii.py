class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
                
            else:
                odd.append(nums[i])
                
        idx = 0
        i = 0
        while(idx < len(nums)):
            nums[idx] = even[i]
            idx += 2
            i += 1
            
        idx = 1
        i = 0
        while(idx < len(nums)):
            nums[idx] = odd[i]
            idx += 2
            i += 1
            
        return nums