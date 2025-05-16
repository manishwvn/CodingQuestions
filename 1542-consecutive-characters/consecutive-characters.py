class Solution:
    def maxPower(self, s: str) -> int:

        curr, max_count = 0, 0
        prev = None

        for char in s:
            if char == prev:
                curr += 1

            else:
                prev = char
                curr = 1

            max_count = max(curr, max_count)
        return max_count

