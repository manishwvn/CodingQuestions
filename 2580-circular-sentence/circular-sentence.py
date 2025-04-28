class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split()

        if len(words) == 1:
            return True if words[0][0] == words[0][-1] else False

        for i in range(1, len(words)):
            if (words[i][0]) != words[i-1][-1]:
                return False

        if words[-1][-1] != words[0][0]:
            return False
        
        return True

        