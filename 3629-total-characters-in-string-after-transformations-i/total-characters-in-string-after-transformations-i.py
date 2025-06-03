class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        while t:
            new_freq = [0] * 26

            for i in range(26):
                if i == 25:
                    new_freq[0] += freq[25]
                    new_freq[1] += freq[25]
                else:
                    new_freq[i+1] += freq[i]
            freq = new_freq
            t -= 1
        return sum(freq) % mod