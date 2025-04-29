class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digit_sum(num):
            sum_ = 0
            while num:
                sum_ += num % 10
                num //= 10

            return sum_

        hm = {}
        max_val = 0
        for i in range(1,n+1):
            key = digit_sum(i)

            if key in hm:
                hm[key] += 1
            else:
                hm[key] = 1
            
            max_val = max(max_val, hm[key])
        
        print(max_val)
        res = 0

        for val in hm.values():
            if val == max_val:
                res += 1

        return res
        