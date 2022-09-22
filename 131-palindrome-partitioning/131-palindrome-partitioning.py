class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pal(string):
            return string == string[::-1]
    
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
        