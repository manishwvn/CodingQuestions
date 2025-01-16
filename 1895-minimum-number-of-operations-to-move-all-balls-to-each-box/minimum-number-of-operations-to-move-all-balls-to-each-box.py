class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        # Left-to-right pass
        count = 0  # Number of balls encountered so far
        operations = 0  # Cumulative operations to move balls from the left
        
        for i in range(n):
            answer[i] += operations
            count += int(boxes[i])  # Add the current box's ball if it's '1'
            operations += count  # Increment operations by the number of balls
        
        # Right-to-left pass
        count = 0  # Reset the ball count
        operations = 0  # Reset the cumulative operations
        
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            count += int(boxes[i])  # Add the current box's ball if it's '1'
            operations += count  # Increment operations by the number of balls
        
        return answer