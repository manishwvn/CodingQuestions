from collections import defaultdict
import heapq
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)

        # Process scores while maintaining only the top 5 using a min-heap
        for student, score in items:
            heapq.heappush(scores[student], score)  # Add the score
            if len(scores[student]) > 5:  # If more than 5 scores, remove the smallest
                heapq.heappop(scores[student])

        # Generate result sorted by student ID
        result = []
        for student in sorted(scores):  # Ensure output is sorted by student ID
            avg = sum(scores[student]) // 5  # Compute average of top 5 scores
            result.append([student, avg])

        return result