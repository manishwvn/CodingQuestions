class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if not firstList or not secondList: return []
        
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        result = []
        
        while i < m and j < n:
    
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
                
            if start <= end:
                result.append([start, end])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
                
            else:
                j += 1
        
        print(result)
        return result
                 
            
            
        
        
        