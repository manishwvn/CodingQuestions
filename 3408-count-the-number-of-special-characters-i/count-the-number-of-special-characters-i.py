class Solution(object):
    def numberOfSpecialChars(self, word):
        small = [0] * 26
        capital = [0] * 26
        count = 0
        
        for char in word:
            if char >= 'a' and char <= 'z':
                small[ord(char) - ord('a')] = 1
            else:
                capital[ord(char) - ord('A')] = 1
        
        for i in range(26):
            if small[i] == 1 and capital[i] == 1:
                count += 1
        
        return count