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

        l = 0
        r = len(self.prefix_sums)

        while l <= r:
            mid = (l + r) // 2

            if self.prefix_sums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()