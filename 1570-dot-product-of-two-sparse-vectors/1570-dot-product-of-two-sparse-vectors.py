class SparseVector:
    def __init__(self, nums: List[int]):
        self.hm = {}
        for i, val in enumerate(nums):
            if val:
                self.hm[i] = val
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, val in self.hm.items():
            if i in vec.hm:
                result += self.hm[i] * vec.hm[i]
                
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)