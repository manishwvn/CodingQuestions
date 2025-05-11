class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        last = {x: i for i, x in enumerate(nums)}
        
        for i in range(len(nums)):
            for d in range(9, nums[i], -1):
                if last.get(d, -1) > i:
                    nums[i], nums[last[d]] = nums[last[d]], nums[i]
                    return int(''.join(map(str, nums)))
        return num