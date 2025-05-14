class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        if tickets[k] == 1:
            return k + 1

        time = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return time

                if tickets[i] != 0:
                    tickets[i] -= 1
                    time += 1
            
        return time