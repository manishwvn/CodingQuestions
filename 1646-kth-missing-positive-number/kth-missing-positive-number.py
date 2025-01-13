class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        hs = set(arr)
        i = 1

        while k:
            if i not in hs:
                k -= 1
                if k == 0:
                    return i
            i += 1

        