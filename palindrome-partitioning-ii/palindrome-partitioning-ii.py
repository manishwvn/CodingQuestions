def isPal(s):
    left, right = 0, len(s) - 1
    while(left < right):
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

class Solution:
    def minCut(self, s: str) -> int:
        
        arr = [[False for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)):
            arr[i][i] = True
            
        for length in range(2, len(s)+1):
            for i in range(0, len(s) - length + 1):
                j = i + length - 1
                if length == 2:
                    arr[i][j] = (s[i] == s[j])
                    
                else:
                    arr[i][j] = (s[i] == s[j]) and arr[i+1][j-1]
                
        cuts = [float('inf') for i in s]
        for i in range(len(s)):
            if arr[0][i]:
                cuts[i] = 0
            else:
                cuts[i] = cuts[i-1] + 1
                for j in range(1, i):
                    if arr[j][i] and cuts[j-1] + 1 < cuts[i]:
                        cuts[i] = cuts[j-1] + 1
                        
        return cuts[-1]