class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack = []
        visited = set()
        
        hm = {}
        for i, char in enumerate(s):
            hm[char] = i
            
        for i in range(len(s)):
            
            if s[i] not in visited:
                
                while stack and s[i] < stack[-1] and i < hm[stack[-1]]:
                    char = stack.pop()
                    if char in visited:
                        visited.remove(char)
                        
                visited.add(s[i])
                stack.append(s[i])
                
        return "".join(stack)
        