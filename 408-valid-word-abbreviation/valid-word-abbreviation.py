class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        n, m, i, j = len(word), len(abbr), 0, 0

        while i < n and j < m:

            #if character
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

            #if digit
            else:
                #if leading 0
                if abbr[j] == '0':
                    return False

                #form the number
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                i += num

        return i == len(word) and j == len(abbr)


        