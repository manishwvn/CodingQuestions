from copy import deepcopy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        nums2 = deepcopy(nums)
        print(nums2)
        nums2.extend(nums)
        return nums2
        