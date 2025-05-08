class Solution:
    def equalFrequency(self, word: str) -> bool:

        charset = Counter(word)

        for char in list(charset.keys()):
            charset[char] -= 1

            if charset[char] == 0:
                del charset[char]

            if len(set(charset.values())) == 1:
                return True

            if char in charset:
                charset[char] += 1
            else:
                charset[char] = 1

        return False