class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def is_sym(num_str):
            n = len(num_str)
            first = num_str[:n//2]
            last = num_str[n//2:]
            if sum([int(x) for x in first]) == sum([int(x) for x in last]):
                return True
            else:
                return False
            

        res = 0
        for num in range(low, high + 1):
            num_str = str(num)
            if len(num_str) % 2 == 0:
                if is_sym(num_str):
                    res += 1
        return res