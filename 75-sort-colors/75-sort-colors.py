class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, mid, right = 0, 0, len(nums) - 1
    
        while mid <= right:

            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

            else:
                mid += 1
            
                