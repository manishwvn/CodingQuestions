class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        result = []
        potions.sort()

        for spell in spells:
            l, r = 0, len(potions) - 1
            # idx = len(potions)
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid - 1
                    # idx = mid
                else:
                    l = mid + 1
            
            result.append(len(potions) - l)

        return result
        