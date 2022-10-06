class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        result = ""
        
        for i in range(1, len(s)):
            if not stack or s[i] != stack[-1][0]:
                stack.append([s[i], 1])
            
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    
        for item in stack:
            char, count = item
            result += (char * count)
            
        return result
            
            
        