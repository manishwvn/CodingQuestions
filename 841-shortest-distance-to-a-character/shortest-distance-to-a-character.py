class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = []
        pos = -n
        for i in range(n):
            if s[i] == c:
                pos = i
            
            result.append(i - pos)

        print(result)
        for i in range(n-1, -1, -1):
            if s[i] == c:
                pos = i

            result[i] = min(result[i], abs(i - pos))

        return result


        
        