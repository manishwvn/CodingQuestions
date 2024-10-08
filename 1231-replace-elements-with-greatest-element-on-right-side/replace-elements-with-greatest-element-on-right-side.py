class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        result = [-1] * len(arr)
        largest = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            result[i] = largest
            largest = max(largest, arr[i])

        return result 
        