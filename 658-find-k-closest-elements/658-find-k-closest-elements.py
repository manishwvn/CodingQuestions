class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #using two pointers
        
        aux = []
        for i in range(len(arr)):
            val = abs(arr[i] - x)
            aux.append(val)
            
        l, r = 0, len(aux) - 1
        
        while(r - l + 1 > k):
            if aux[l] > aux[r]:
                l += 1
                
            else:
                r -= 1
            
        return arr[l:r+1]
        