from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # default to 0 (no warmer day found)

        for i in range(n - 2, -1, -1):  # start from 2nd last day
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i  # found warmer day
                    break
                elif result[j] == 0:
                    break  # no warmer day after j either
                else:
                    j += result[j]  # jump ahead using known info

        return result