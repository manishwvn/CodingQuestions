class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = [0] * 100
        count = 0

        for a, b in dominoes:
            if a <= b:
                code = 10 * a + b
            else:
                code = 10 * b + a 

            count += freq[code]
            freq[code] += 1

        return count