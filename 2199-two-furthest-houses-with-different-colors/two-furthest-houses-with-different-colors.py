class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        # Scan from end to find farthest j where colors[j] != colors[0]
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                dist1 = j
                break

        # Scan from start to find farthest i where colors[i] != colors[n-1]
        for i in range(n):
            if colors[i] != colors[n - 1]:
                dist2 = n - 1 - i
                break

        return max(dist1, dist2)