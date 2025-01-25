class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l <=r:
            mid = (l+r) // 2
            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')

            if left < nums[mid] and nums[mid] > right:
                return mid
            elif left < nums[mid] and nums[mid] < right:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        