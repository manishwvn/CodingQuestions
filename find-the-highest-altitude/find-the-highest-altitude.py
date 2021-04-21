class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alts = [0]
        j = 0
        
        for i in range(len(gain)):
            val = gain[i] + alts[j]
            alts.append(val)
            j +=1 
            
        return max(alts)
        
        