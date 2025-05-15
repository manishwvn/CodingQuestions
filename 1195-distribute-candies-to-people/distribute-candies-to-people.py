class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 1

        while candies > 0:
            give = min(i, candies)
            res[(i - 1) % num_people] += give
            candies -= give
            i += 1

        return res