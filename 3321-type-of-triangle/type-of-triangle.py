class Solution:
    def triangleType(self, nums: List[int]) -> str:

        if (nums[0] + nums[1] > nums[2]) and \
        (nums[1] + nums[2] > nums[0]) and \
        (nums[2] + nums[0] > nums[1]):
            if nums[1] == nums[2] == nums[0]:
                return "equilateral"
            elif (nums[1] == nums[2]) or (nums[0] == nums[2]) or (nums[1] == nums[0]):
                return "isosceles"
            else:
                return "scalene"

        else:
            return "none"
        