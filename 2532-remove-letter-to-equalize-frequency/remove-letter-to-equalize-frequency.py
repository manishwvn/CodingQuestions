class Solution:
    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):
            charset = Counter(word)
            charset[word[i]] -= 1
            if charset[word[i]] == 0:
                del charset[word[i]]

            if len(set(charset.values())) == 1:
                return True

        return False
        