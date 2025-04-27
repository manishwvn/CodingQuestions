class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        counts = 0

        for i in range(len(words)):
            str1 = words[i]

            for j in range(i+1, len(words)):
                str2 = words[j]

                if len(str1) > len(str2):
                    continue
                prefix = str2[:len(str1)]
                suffix = str2[-len(str1):]

                if prefix == str1 and suffix == str1:
                    counts += 1

        return counts
        