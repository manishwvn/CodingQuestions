class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        is_inc = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                is_inc = False
                break
        
        if not is_inc:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i+1]:
                    return False
        return True

        