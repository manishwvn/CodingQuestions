class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        j_set = set(jewels)
        s_count = Counter(stones)
        
        result = 0
        
        for j in j_set:
            if j in s_count:
                result += s_count[j]
                
        return result
        