class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.lookup = []
        for i in range(len(nums)):
            if nums[i] != 0:
                self.lookup.append((i, nums[i]))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        result = 0
        
        p1, p2 = 0, 0
        
        while p1 < len(self.lookup) and p2 < len(vec.lookup):
            if self.lookup[p1][0] == vec.lookup[p2][0]:
                result += self.lookup[p1][1] * vec.lookup[p2][1]
                p1 += 1
                p2 += 1
            elif self.lookup[p1][0] < vec.lookup[p2][0]:
                p1 += 1
            else:
                p2 += 1
                
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)