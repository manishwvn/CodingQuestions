class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        hm = {}

        for i in range(len(arr)):
            if (2 * arr[i]) in hm or (arr[i] % 2 == 0 and arr[i] // 2 in hm):
                    return True
                
            else:
                hm[arr[i]] = i

        return False
        