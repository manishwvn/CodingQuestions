from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Build a max heap using negative frequency
        max_heap = []
        for num, freq in freq_map.items():
            heappush(max_heap, (-freq, num))  # negate freq to simulate max heap

        # Step 3: Extract top k elements
        res = []
        for _ in range(k):
            res.append(heappop(max_heap)[1])

        return res