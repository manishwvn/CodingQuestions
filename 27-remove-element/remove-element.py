class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0: return 0
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        