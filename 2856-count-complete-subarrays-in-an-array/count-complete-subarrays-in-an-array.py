class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        num_dist = len(set(nums))
        l = 0
        max_count = 0
        hm = defaultdict(int)
        for r in range(len(nums)):
            hm[nums[r]] += 1

            while len(hm) == num_dist:
                hm[nums[l]] -= 1
                if hm[nums[l]] == 0:
                    del hm[nums[l]]
                l += 1
            
            max_count += l

        return max_count
            

        