class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts, checks = Counter(arr), set()
        
        for count in counts.values():
            if count in checks: return False
            checks.add(count)
            
        return True
        
        
        