class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts = Counter(arr)
        
        checks = set()
        
        for count in counts.values():
            if count in checks: return False
            checks.add(count)
            
        return True
        