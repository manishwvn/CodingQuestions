class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        def is_increase(arr):
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    return False
            return True

        result = 0

        for l in range(len(nums)):
            for r in range(l, len(nums)):
                rem = nums[:l] + nums[r+1:]

                if is_increase(rem):
                    result += 1

        return result

        