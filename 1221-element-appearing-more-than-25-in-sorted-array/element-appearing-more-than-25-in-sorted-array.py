class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
 
        count = 1
        for i in range(1,n):
            if arr[i-1] == arr[i]:
                count += 1
            else:
                if count > n / 4:
                    return arr[i-1]
                count = 1

        if count > n / 4:
            return arr[-1]        