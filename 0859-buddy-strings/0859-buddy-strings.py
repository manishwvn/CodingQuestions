class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
    
        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))

        print(diff)
        return len(diff) == 2 and diff[0] == diff[1][::-1]
        