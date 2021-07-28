class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        hashMap = {}
        while n:
            if str(cells) in hashMap:
                n %= hashMap[str(cells)] - n
            hashMap[str(cells)] = n
            
            if n > 0:
                tempArray = [0] * 8
                for i in range(1, 7):
                    if cells[i-1] == cells[i+1]:
                        tempArray[i] = 1

                    else:
                        tempArray[i] = 0
                    
                cells = tempArray
                n -= 1
            
        return cells