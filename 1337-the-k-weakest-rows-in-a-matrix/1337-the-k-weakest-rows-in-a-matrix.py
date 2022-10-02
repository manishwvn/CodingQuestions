class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        
        def bs(row):
            l, r = 0, n
            
            while l < r:
                mid = (l + r) // 2
                
                if row[mid] == 1:
                    l = mid + 1
                    
                else:
                    r = mid
                    
            return l
            
        
        heap = []
        
        for i, row in enumerate(mat):
            strn = bs(row)
            item = (-strn, -i)
            if len(heap) < k or item > heap[0]:
                heappush(heap, item)
            if len(heap) > k:
                heappop(heap)
                
        indices = []
        while heap:
            strn, i = heappop(heap)
            indices.append(-i)
            
        return indices[::-1]
            
        
        
        