class Solution:
    def totalMoney(self, n: int) -> int:

        res = 0
        mon = 1

        while n > 0:
            for day in range(min(n, 7)):
                res += mon + day

            n -= 7
            mon += 1
        return res

        