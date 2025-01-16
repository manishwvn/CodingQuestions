class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hm = {}

        for i in range(len(self.nums)):
            if self.nums[i] in self.hm:
                self.hm[self.nums[i]].append(i)
            else:
                self.hm[self.nums[i]] = [i]
        
    def pick(self, target: int) -> int:

        l = self.hm[target]
        index = random.choice(l)
        return index

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)