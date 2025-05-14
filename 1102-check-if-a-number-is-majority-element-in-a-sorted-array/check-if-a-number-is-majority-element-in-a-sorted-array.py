class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:


        n = len(nums)
        freq = Counter(nums)
        for num in freq:
            if num == target and freq[num] > n // 2:
                return True

        return False
        