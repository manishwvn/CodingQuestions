class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1: return 1
        
        index = 0
        i = 0
        
        while i < len(chars):
            j = i
            
            while j < len(chars) and (chars[i] == chars[j]):
                j += 1
            
            
            chars[index] = chars[i]
            index += 1
            
            if j - i > 1:
                counts = str(j - i)
                for c in counts:
                    chars[index] = c
                    index += 1
                    
            i = j
            
        return index
        
        
        