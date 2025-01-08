class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x, y = list(a), list(b)
        x.reverse()
        y.reverse()

        i, j = 0, 0
        carry = 0
        result = []

        while i < len(x) or j < len(y):
            val = carry
            if i < len(x):
                val += int(x[i])
                i += 1
            if j < len(y):
                val += int(y[j])
                j += 1

            result.append(str(val%2))
            carry = val // 2

        if carry:
            result.append(str(carry))
        
        result.reverse()
        return ''.join(result)




        