class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque(i for i in range(len(tickets)))

        time = 0

        while queue:
            time += 1

            front = queue.popleft()
            tickets[front] -= 1

            if k == front and tickets[front] == 0:
                return time
            
            if tickets[front] != 0:
                queue.append(front)

        return time

