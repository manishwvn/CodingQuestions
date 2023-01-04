class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        if len(time) == 1: return 0
        
        pairs = 0
        hm = defaultdict(int)
        
        for num in time:
            diff = (60 - (num % 60)) % 60
            if diff in hm:
                pairs += hm[diff]
                
            hm[num % 60] += 1
            
        print(hm)
        return pairs
        
        
        
        
        