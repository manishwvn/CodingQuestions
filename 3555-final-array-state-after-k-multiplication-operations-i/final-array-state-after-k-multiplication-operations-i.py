class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for _ in range(k):
            idx = 0
            for i in range(len(nums)):
                if nums[i] < nums[idx]:
                    idx = i
            nums[idx] *= multiplier

        return nums
        