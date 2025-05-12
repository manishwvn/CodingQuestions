class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        cons = 0

        for num in arr:
            if num % 2 == 1:
                cons += 1
            else:
                cons = 0

            if cons == 3:
                return True

        return False
        