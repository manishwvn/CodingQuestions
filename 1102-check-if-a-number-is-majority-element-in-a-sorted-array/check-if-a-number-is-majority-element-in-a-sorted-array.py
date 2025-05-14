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

        def find_right(l, r, nums, target):
            while l <=r :
                mid = (l + r) // 2

                if nums[mid] <= target:
                    l = mid + 1

                else:
                    r = mid - 1
            return l

        print(find_left(0, len(nums) -1, nums, target))
        print(find_right(0, len(nums) -1, nums, target))

        left = find_left(0, len(nums) -1, nums, target) + 1
        right = find_right(0, len(nums) -1, nums, target)

        if right - left > len(nums) // 2:
            return True

        return False