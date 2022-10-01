class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        n, m  = len(nums1), len(nums2)
        
        l, r = 0, n
        
        while l <= r:
            part_x = (l + r) // 2
            part_y = ((n + m) // 2) - part_x
            
            l1 = -float('inf') if part_x == 0 else nums1[part_x - 1]
            r1 = float('inf') if part_x == n else nums1[part_x]
            
            l2 = -float('inf') if part_y == 0 else nums2[part_y - 1]
            r2 = float('inf') if part_y == m else nums2[part_y]
            
            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
                
            elif l1 > r2:
                r = part_x - 1
                
            else:
                l = part_x + 1