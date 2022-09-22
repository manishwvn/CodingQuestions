class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pal(string):
            start, end = 0, len(string) - 1
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
                
            return True
    
        result = []

        def helper(pos, path):
            #base
            if pos == len(s):
                result.append(path.copy())
                return 
            
            #logic
            for i in range(pos, len(s)):
                substr = s[pos:i+1]
                
                if is_pal(substr):
                    #action
                    path.append(substr)
                    
                    #recurse
                    helper(i+1, path)
                    
                    #backtrack
                    path.pop()
        
        helper(0, [])
        return result
        