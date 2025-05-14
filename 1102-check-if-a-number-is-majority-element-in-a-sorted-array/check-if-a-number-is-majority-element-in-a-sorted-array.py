class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        def find_left(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return r

        def find_right(nums, target):
            l, r = 0, len(nums) - 1

            while l <=r :
                mid = (l + r) // 2

                if nums[mid] <= target:
                    l = mid + 1

                else:
                    r = mid - 1
            return l

        print(find_left(nums, target))
        print(find_right(nums, target))

        left = find_left(nums, target) + 1
        right = find_right(nums, target)

        if right - left > len(nums) // 2:
            return True

        return False