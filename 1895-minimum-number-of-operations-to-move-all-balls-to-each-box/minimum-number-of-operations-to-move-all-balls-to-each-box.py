class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        count = 0
        ops = 0
        for i in range(n):
            result[i] += ops
            count += int(boxes[i])
            ops += count

        count = ops = 0

        for i in range(n-1, -1, -1):
            result[i] += ops
            count += int(boxes[i])
            ops += count

        return result
        
        