class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        count = 0

        for a, b in dominoes:
            
            key = (a, b) if a <= b else (b, a)

            if key in freq:
                count += freq[key]
                freq[key] += 1
            else:
                freq[key] = 1
            

        return count