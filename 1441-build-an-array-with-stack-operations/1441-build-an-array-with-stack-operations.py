class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        result = []
        best = 0
        target = set(target)
        for i in range(1, n + 1):
            if i in target:
                result.append("Push")
                best = max(len(result), best)
                
            else:
                result.append("Push")
                result.append("Pop")
        
        while result[-1] == "Pop":
            result.pop()
            
        return result[:best]
            