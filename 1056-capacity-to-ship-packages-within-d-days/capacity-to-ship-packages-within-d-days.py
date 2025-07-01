class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity):
            day_count = 1
            total = 0
            for w in weights:
                if total + w > capacity:
                    day_count += 1
                    total = 0
                total += w
            return day_count <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid  # try smaller capacity
            else:
                left = mid + 1  # need more capacity

        return left