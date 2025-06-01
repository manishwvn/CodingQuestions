class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def decode(s, i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]

            # first digit
            count = decode(s, i + 1)

            #2 digits
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += decode(s, i+2)
            
            #store the counts in memo for index i
            memo[i] = count
            
            return count

        return decode(s, 0)
        