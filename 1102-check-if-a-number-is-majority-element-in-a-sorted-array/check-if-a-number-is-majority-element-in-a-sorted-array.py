class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        n = len(nums)
        l, r = 0, len(nums) - 1
        freq = Counter(nums)

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target and freq[nums[mid]] > n // 2:
                return True

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False