class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        set_b = set(bobSizes)
        
        for x in aliceSizes:
            if x + (sum_b - sum_a) / 2 in set_b:
                return [x, x + (sum_b - sum_a) / 2]
        
        