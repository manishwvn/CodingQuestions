class Solution:
    def maximumSwap(self, num: int) -> int:

        nums = [int(x) for x in str(num)]
        max_num = num
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):                
                nums[i], nums[j] = nums[j], nums[i]
                curr = int(''.join(str(x) for x in nums))
                max_num = max(max_num, curr)
                nums[i], nums[j] = nums[j], nums[i]
        return max_num