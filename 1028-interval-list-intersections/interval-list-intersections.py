class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # Find the intersection between A and B, if any
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            # If they intersect
            if start <= end:
                result.append([start, end])

            # Move the pointer with the smaller end time
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return result