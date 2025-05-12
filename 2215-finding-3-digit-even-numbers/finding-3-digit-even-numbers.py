from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_count = [0] * 10
        for d in digits:
            digit_count[d] += 1

        result = []

        for num in range(100, 1000, 2):  # even numbers only
            temp = [0] * 10
            a = num // 100
            b = (num // 10) % 10
            c = num % 10
            temp[a] += 1
            temp[b] += 1
            temp[c] += 1

            # check if num can be built from digits
            is_valid = True
            for d in range(10):
                if temp[d] > digit_count[d]:
                    is_valid = False
                    break

            if is_valid:
                result.append(num)

        return sorted(result)