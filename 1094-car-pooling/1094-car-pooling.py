class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        changes = [0] * 1001
        
        for trip in trips:
            num, start, end = trip
            changes[start] += num
            changes[end] -= num
            
        curr = 0 
        for change in changes:
            curr += change
            
            if curr > capacity:
                return False
            
        return True
            
        
        