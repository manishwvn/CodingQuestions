class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()
        count = 0
        max_w = 0

        for w in weight:
            max_w += w
            if max_w > 5000:
                break
            count += 1
        return count