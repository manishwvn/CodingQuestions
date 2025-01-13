class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        counts = Counter(arr)

        for key, val in counts.items():
            if val > n / 4:
                return key
        