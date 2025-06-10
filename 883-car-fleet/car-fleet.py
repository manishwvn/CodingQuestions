class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort(reverse = True)

        res = prev = 0

        for pair in pairs:
            p, s = pair
            time = (target - p) / s

            if prev < time:
                res += 1
                prev = time

        return res

