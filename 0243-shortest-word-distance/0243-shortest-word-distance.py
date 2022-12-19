class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        idx1, idx2 = -1, -1
        dist = len(wordsDict)
        
        for i in range(len(wordsDict)):
            
            if wordsDict[i] == word1:
                idx1 = i
                
            elif wordsDict[i] == word2:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1:
                dist = min(dist, abs(idx2 - idx1))
            
            
        return dist