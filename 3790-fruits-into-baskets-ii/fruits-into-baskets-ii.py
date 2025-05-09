class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        placed = [False] * len(baskets)

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    if placed[j] == False:
                        placed[j] = True
                        break
                    else:
                        continue

        print(placed)
        count = 0
        for val in placed:
            if val == False:
                count += 1

        return count
