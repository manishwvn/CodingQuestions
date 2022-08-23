class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for char in s:
            if char in visited:
                return char
            visited.add(char)
        
        
        