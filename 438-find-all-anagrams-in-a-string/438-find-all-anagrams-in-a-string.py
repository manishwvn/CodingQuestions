class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        result = []
        counts = Counter(p)
        match = 0
    
        for i in range(len(s)):
            
            #incoming character
            inc = s[i]
            if inc in counts:
                counts[inc] -= 1
                if counts[inc] == 0:
                    match += 1
                
            #outgoing character
            if i >= len(p):
                out = s[i - len(p)]
                if out in counts:
                    counts[out] += 1
                    if counts[out] == 1:
                        match -= 1
        
            if match == len(counts):
                print(match)
                result.append(i - len(p) + 1)
                
        return result
                    
        
        
        