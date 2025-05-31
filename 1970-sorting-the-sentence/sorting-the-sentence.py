class Solution:
    def sortSentence(self, s: str) -> str:

        words = s.split(' ')
        hm = {}

        for word in words:
            k, v = int(word[-1]) - 1, word[:-1]
            hm[k] = v
        
        sorted_hm = sorted(hm.items())
        
        result = ""
        for k, v in sorted_hm:
            result = result + v
            if k != len(words) - 1:
                result += ' '
        return result
        