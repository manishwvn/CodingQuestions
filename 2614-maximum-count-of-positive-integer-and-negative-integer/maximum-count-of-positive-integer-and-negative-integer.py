class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        # first index where pos numbers begin
        def bs_pos(nums):
            
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > 0:
                    r = mid - 1

                else:
                    l = mid + 1

            return l


        #last index where neg numbers end
        def bs_neg(nums):
            
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < 0:
                    l = mid + 1

                else:
                    r = mid - 1

            return r
        
        print(bs_pos(nums))
        print(bs_neg(nums))

        pos = len(nums) - bs_pos(nums)
        neg = bs_neg(nums) + 1

        return max(pos, neg)
