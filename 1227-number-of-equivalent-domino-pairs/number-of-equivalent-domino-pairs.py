class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        count = 0

        for a, b in dominoes:
            # Step 1: canonicalize
            key = (a, b) if a <= b else (b, a)

            # Step 2: every already‐seen copy of key forms a new pair
            count += freq.get(key, 0)

            # Step 3: record this domino
            freq[key] = freq.get(key, 0) + 1

        return count