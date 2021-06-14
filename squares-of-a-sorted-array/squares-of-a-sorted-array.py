class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        
        start, end = 0, len(nums) - 1
        last = len(result) - 1
        
        while(start <= end):
            if abs(nums[start]) > abs(nums[end]):
                result[last] = nums[start] ** 2
                start += 1
                last -= 1
                
            else:
                result[last] = nums[end] ** 2
                end -= 1
                last -= 1
        return result
                
        