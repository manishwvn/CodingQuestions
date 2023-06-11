class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        def helper(a, b):
            set1, set2 = set(), set(b)
            
            for num in a:
                if num not in set2:
                    set1.add(num)
                    
            
            return list(set1)
            
            
        
        
        return helper(nums1, nums2), helper(nums2, nums1)