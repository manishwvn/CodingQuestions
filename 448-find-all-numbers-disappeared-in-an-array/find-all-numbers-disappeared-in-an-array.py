class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        num_set = set(nums)
   
        result = []
        for num in range(1, n+1):
            if num not in num_set:
                result.append(num)
                
        return result
        