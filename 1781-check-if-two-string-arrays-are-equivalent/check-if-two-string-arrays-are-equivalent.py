class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        def builder(word):
            res = ""
            for string in word:
                res += string
            return res

        string1 = builder(word1)
        string2 = builder(word2)

        return string1 == string2
        