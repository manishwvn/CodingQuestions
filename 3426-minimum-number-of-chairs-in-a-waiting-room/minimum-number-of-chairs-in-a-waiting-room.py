class Solution:
    def minimumChairs(self, s: str) -> int:

        curr, maxm = 0, 0

        for p in s:
            if p == 'E':
                curr += 1
            else:
                curr -= 1

            maxm = max(curr, maxm)
        return maxm


        