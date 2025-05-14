from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        def find_left():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l  # First position >= target

        def find_right():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r  # Last position <= target

        left = find_left()
        right = find_right()

        # If target doesn't exist
        if left > right:
            return []

        # All indices from left to right are target
        return list(x for x in range(left, right+1))