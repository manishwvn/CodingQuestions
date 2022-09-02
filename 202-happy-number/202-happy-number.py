class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

    # find number of digits of n
        temp = n
        sqr_sum = 0
        visited = set()
        while n:

            # for i in range(digits+1):
            #     rem = n % 10
            #     sqr_sum += rem ** 2
            #     n //= 10

            rem = n % 10
            sqr_sum += rem ** 2
            n //= 10

            if n == 0:
                if sqr_sum == 1:
                    return True
                        

                else:
                    if sqr_sum in visited:
                        return False
                    visited.add(sqr_sum)
                    n = sqr_sum
                    sqr_sum = 0

            if n > 2 ** 31 -1:
                break

        return False
            
            
            
        