class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num <=0: return False

        sum_ = 0

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum_ += i
                if i * i != num:
                    sum_ += num // i
        return sum_ - num  == num
        