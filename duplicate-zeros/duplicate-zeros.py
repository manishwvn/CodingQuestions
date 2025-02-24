class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        zeroes = 0
        for num in arr:
            if num == 0:
                zeroes += 1
        
        n = len(arr)
        i = n - 1
        j = n + zeroes - 1

        while i != j:
            if j < n:
                arr[j] = arr[i]
            j -= 1
            
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
            i -= 1

        