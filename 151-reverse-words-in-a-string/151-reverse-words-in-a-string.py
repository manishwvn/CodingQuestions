class Solution:
    def reverseWords(self, S: str) -> str:
        s = []
        temp = ''
        for i in (S + ' '):
            if i == ' ':
                if temp != '':
                    s.append(temp)
                    temp = ''
            else:
                temp += i
        return " ".join(s[::-1])