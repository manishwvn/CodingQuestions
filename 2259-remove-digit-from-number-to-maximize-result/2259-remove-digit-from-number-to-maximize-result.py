class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        n = len(number)
        result = []
        for i in range(n):
            if i == n-1 and number[i] == digit:
                result.append(int(number[:n-1]))
            
            if number[i] == digit:
                result.append(int(number[:i] + number[i+1:n]))
        print(result)
        return str(max(result))
                
        