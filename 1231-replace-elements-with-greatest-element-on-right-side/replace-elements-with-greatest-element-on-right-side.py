class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        #base case - len(arr) == 1
        if len(arr) == 1: return [-1]

        max_val = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            val = arr[i]
            arr[i] = max_val
            # max_val = max(val, max_val)
            if val > max_val: max_val = val

        arr[-1] = -1
        return arr 