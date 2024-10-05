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
            # 'IV' : 4,
            # 'IX' : 9,
            # 'XL' : 40,
            # 'XC' : 90,
            # 'CD' : 400,
            # 'CM' : 900
        }

        result = 0
        i = 0
        
        while i < len(s):

            if i + 1 < len(s) and symbols[s[i]] < symbols[s[i+1]]:
                result += symbols[s[i+1]] - symbols[s[i]]
                i += 2

            else:
                result += symbols[s[i]]
                i += 1

        return result
        