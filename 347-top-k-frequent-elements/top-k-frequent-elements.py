class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #3rd approach Bucket sort/bucketing

        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        buckets = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            buckets[count].append(num)

        res = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res