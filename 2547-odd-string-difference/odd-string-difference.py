class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = {}

        for i, word in enumerate(words):
            diff = []
            for j in range(len(word) - 1):
                diff.append(ord(word[j+1]) - ord(word[j]))
            diff = tuple(diff)

            if diff in diffs:
                diffs[diff][0] += 1
            else:
                diffs[diff] = [1, i]

        for count, idx in diffs.values():
            if count == 1:
                return words[idx]