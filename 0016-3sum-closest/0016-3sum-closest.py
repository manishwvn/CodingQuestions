class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        
        nums.sort()
        min_diff = float('inf')
        
        for i in range(len(nums)):
            a = nums[i]
            l, r = i+1, len(nums) - 1

            while l < r:
                b, c = nums[l], nums[r]
                total = a + b + c

                if total == target:
                    return total
                
                if abs(target - total) < abs(min_diff):
                    min_diff = target - total
                
                
                
                if total < target:
                    l += 1
                    
                else:
                    r -= 1
                
                    
        return target - min_diff
                


