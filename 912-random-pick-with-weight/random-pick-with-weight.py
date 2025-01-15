class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        sum_ = 0
        for weight in w:
            sum_ += weight
            self.prefix_sums.append(sum_)
        self.total_sum = sum_
        
    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)

        for i in range(len(self.prefix_sums)):
            if target <= self.prefix_sums[i]:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()