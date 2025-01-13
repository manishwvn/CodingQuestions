class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = []
        maxm = max(candies)

        for num in candies:
            if num + extraCandies >= maxm:
                result.append(True)
            else:
                result.append(False)
        
        return result
        