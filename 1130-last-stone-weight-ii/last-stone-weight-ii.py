class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        def algo(i, total, dp):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum - total))
            
            if (i, total) in dp:
                return dp[(i, total)]

            #min(not choose, choose)
            dp[(i,total)] = min(algo(i + 1, total, dp), algo(i+1, total+stones[i], dp))
            return dp[(i, total)]


        stone_sum = sum(stones)
        target = ceil(stone_sum / 2)
        dp = {}
        return algo(0, 0, dp)

        