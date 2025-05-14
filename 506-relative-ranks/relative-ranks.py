class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        heap = []
        ranks = [None] * len(score)

        for i, s in enumerate(score):
            heappush(heap, [-s, i])

        place = 1

        while heap:
            s, idx = heappop(heap)
            if place == 1:
                ranks[idx] = "Gold Medal"
            elif place == 2:
                ranks[idx] = "Silver Medal"
            elif place == 3:
                ranks[idx] = "Bronze Medal"
            else:
                ranks[idx] = str(place)
            place += 1

        return ranks
        