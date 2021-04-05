class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hm = {}
        for i in range(len(nums1)):
            hm[nums1[i]] = nums1.count(nums1[i])
                
        result = []
        
        for i in range(len(nums2)):
            if nums2[i] not in result:
                if nums2[i] in hm:
                    result.append(nums2[i])
                    hm[nums2[i]] -= 1
                
        return result
        