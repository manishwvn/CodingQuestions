class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        n = len(nums)

        # Track max digit from the right
        max_idx = n - 1
        left, right = -1, -1

        for i in range(n - 2, -1, -1):
            if nums[i] > nums[max_idx]:
                max_idx = i
            elif nums[i] < nums[max_idx]:
                left = i
                right = max_idx

        if left != -1:
            nums[left], nums[right] = nums[right], nums[left]

        return int(''.join(str(x) for x in nums))