class Solution:
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hm = {}
        
        for i, char in enumerate(order):
            hm[char] = i
        
        def is_not_sorted(first, second):
            i = 0
            while i < len(first) and i < len(second):
                if first[i] != second[i]:
                    return hm[first[i]] > hm[second[i]]
                
                i += 1
                
            if len(first) > len(second): return True
            return False
        
        
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            if is_not_sorted(first, second):
                return False
            
        return True
                    
        