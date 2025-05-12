class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0

        for i in range(len(colors)-1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)

        for j in range(len(colors)):
            if colors[j] != colors[-1]:
                max_dist = max(max_dist, len(colors) -1 -j)

        return max_dist



        