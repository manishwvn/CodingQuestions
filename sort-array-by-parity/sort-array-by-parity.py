class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        even, odd = [], []
        
        for i in range(len(A)):
            even.append(A[i]) if A[i] % 2 == 0 else odd.append(A[i])
            
        even.extend(odd)
        
        return even
        
        