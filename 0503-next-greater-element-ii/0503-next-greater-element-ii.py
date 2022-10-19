class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = [-1] * len(nums)
        stack = []
        
        n = len(nums)
        
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                res[idx] = nums[i % n]
            
            
            if i < n:
                stack.append(i)
                
        return res
            
        
        