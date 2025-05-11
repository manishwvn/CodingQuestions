class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #using sorting

        #1. find counts
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        #2. create array of [[count, num]] and sort it.
        arr = []
        for num, count in counts.items():
            arr.append([count, num])

        arr.sort()

        #3.create res and pop k elements[1](i.e. num) from arr.
        res = []
        while k > 0:
            res.append(arr.pop()[1])
            k -= 1
        
        return res

