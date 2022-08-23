class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num != 0:
                s.add(num)
                
        return len(s)
        