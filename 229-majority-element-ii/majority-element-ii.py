class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if len(counts) <= 2:
                continue
            
            new_counts = defaultdict(int)
            for num, count in counts.items():

                if count > 1:
                    new_counts[num] = count - 1
            counts = new_counts
                

        res = []
        for num in counts:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res



        