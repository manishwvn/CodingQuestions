class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0 if nums[0] == 0 else 1

        ops = set()
        for num in nums:
            if num != 0:
                ops.add(num)
        return len(ops)


        
        