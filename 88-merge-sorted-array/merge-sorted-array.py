class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p3, p1, p2 = m + n - 1, m - 1, n - 1

        while p1 > -1 and p2 > -1:
            if nums1[p1] >= nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1

        # If there are remaining elements in nums2, copy them over to nums1
        while p2 > -1:
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1