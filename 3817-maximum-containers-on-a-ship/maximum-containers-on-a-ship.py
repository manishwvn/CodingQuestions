class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        l, r = 1, n*n
        result = 0
        while l <= r:
            mid = (l + r) // 2

            if (mid * w) > maxWeight:
                r = mid - 1
            else:
                l = mid + 1
                result = mid
        return result
           