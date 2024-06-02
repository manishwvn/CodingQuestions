from copy import deepcopy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * (n * 2)
        flag = False
        for i in range(n*2):
            j = i % n 
            ans[i] = nums[j]

        print(ans)
        return ans
            
        