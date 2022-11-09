class NumArray:

    def __init__(self, nums: List[int]):
        
        self.prefix_nums = [None] *(len(nums))
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            self.prefix_nums[i] = sum_
        

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0: return self.prefix_nums[right]
        return self.prefix_nums[right] - self.prefix_nums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)