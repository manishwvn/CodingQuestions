from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = [(0, [])]  # stack holds tuples: (start_index, current_path)

        while stack:
            start, path = stack.pop()
            result.append(path)

            for i in range(len(nums) - 1, start - 1, -1):
                stack.append((i + 1, path + [nums[i]]))

        return result