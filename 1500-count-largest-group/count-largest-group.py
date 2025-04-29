class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digit_sum(num):
            sum_ = 0
            while num:
                sum_ += num % 10
                num //= 10

            return sum_

        hm = {}
        max_size = 0
        for i in range(1,n+1):
            key = digit_sum(i)

            if key in hm:
                hm[key].append(i)
            else:
                hm[key] = [i]
            
            curr_size = len(hm[key])
            max_size = max(curr_size, max_size)
        
        res = 0

        for k, v in hm.items():
            if len(v) == max_size:
                res += 1
        
        return res
            
        