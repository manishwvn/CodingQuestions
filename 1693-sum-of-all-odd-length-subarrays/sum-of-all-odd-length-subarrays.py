class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        total = 0

        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                if (j - i + 1) % 2 == 1:
                    total += sum(arr[i:j+1])
        return total

        