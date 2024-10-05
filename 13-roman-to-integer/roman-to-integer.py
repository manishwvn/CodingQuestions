class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        result = 0
        i = 0
        while i < len(s) - 1:
            
            num = s[i]
            num2 = ''

            num2 = num + s[i+1]
            if num2 in symbols:
                result += symbols[num2]
                i += 2
            
            else:
                result += symbols[num]
                i += 1

        if i == len(s) - 1:
            result += symbols[s[i]]

        return result

        