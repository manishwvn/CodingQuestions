class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        nums = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i != j and j != k and k != i:
                        a, b, c = digits[i], digits[j], digits[k]
                        if a != 0 and c % 2 == 0:
                            num = a * 100 + b * 10 + c
                            nums.add(num)


        return sorted(list(nums))