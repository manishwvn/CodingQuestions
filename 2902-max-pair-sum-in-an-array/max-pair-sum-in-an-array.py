class Solution:
    def maxSum(self, nums: List[int]) -> int:
        groups = defaultdict(list)

        def max_digit(n):
            return max(int(d) for d in str(n))

        # Group numbers by their largest digit
        for num in nums:
            d = max_digit(num)
            groups[d].append(num)

        max_sum = -1

        # For each group with at least 2 elements, find top 2 and compute sum
        for g in groups.values():
            if len(g) >= 2:
                g.sort(reverse=True)
                max_sum = max(max_sum, g[0] + g[1])

        return max_sum