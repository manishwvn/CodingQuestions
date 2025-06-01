class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            
            else:
                #1 digit
                dp[i] += dp[i+1]
                
                #2 digits
                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]

        print(dp)
        return dp[0]
        