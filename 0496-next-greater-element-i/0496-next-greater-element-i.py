class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = [-1] * len(nums1)
        hm = {n : i for i, n in enumerate(nums1)}
        
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                value = stack.pop()
                idx = hm[value]
                res[idx] = nums2[i]
                
            if nums2[i] in hm:
                stack.append(nums2[i])
            
        return res
        