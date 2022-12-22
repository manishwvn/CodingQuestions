class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def helper(i, path, target):
            # base case
            if target == 0:
                result.append(path.copy())
                return

            if target < 0 or i == len(nums):
                return
            #not choose
            helper(i+1, path, target)

            # choose
            # action
            path.append(nums[i])
            # recursion
            helper(i, path, target-nums[i])
            # backtrack
            path.pop()

        helper(0, [], target)
        return result
        