class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        def find_left(l, r, nums, target):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return r

        left = find_left(0, len(nums) -1, nums, target) + 1
        right = left + (len(nums) // 2)
        
        if right < len(nums) and nums[right] == target:
            return True

        return False