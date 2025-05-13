class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        result = list(word)
        l = 0

        for r in range(len(word)):
            if result[r] == ch:
                while l < r:
                    result[l], result[r] = result[r], result[l]
                    l += 1
                    r -= 1
                return "".join(result)

        return word
        