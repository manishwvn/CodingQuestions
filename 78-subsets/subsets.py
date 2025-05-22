class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def get_subsets(nums, i, path):
            result.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                get_subsets(nums, j+1, path)
                path.pop()

        result = []
        get_subsets(nums, 0, [])
        return result
        