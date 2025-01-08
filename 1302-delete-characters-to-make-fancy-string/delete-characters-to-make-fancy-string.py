class Solution:
    def makeFancyString(self, s: str) -> str:

        prev, ans = s[0], s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                count = 1

            if count < 3:
                ans += s[i]

        return ans


        