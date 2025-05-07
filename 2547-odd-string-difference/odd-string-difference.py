class Solution:
    def oddString(self, words: List[str]) -> str:
        
        diffs = {}
        for i in range(len(words)):
            n = len(words[i])
            diff = []
            for j in range(n-1):
                diff.append(ord(words[i][j+1]) - ord(words[i][j]))
            
            key = tuple(diff)
            if key in diffs:
                diffs[key][0] += 1
            else:
                diffs[key] = [1, i]

        for count, idx in diffs.values():
            if count == 1:
                return words[idx]

        