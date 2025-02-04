class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1) - 1, len(num2) - 1

        carry = 0
        result = []
        
        while i > -1 or j > -1:
            cur_i = int(num1[i]) if i >= 0 else 0
            cur_j = int(num2[j]) if j >= 0 else 0

            sum_ = int(cur_i + cur_j) + carry
            result.append(str(sum_%10))
            carry = sum_ // 10

            i -= 1
            j -= 1
        
        if carry:
            result.append(str(carry))

        output = ""
        for i in range(len(result)-1, -1, -1):
            output += result[i]

        return output