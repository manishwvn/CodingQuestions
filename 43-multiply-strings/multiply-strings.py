class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # Maximum possible digits in result

        # Reverse iteration to multiply digits
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))  # Convert char to int and multiply
                sum_ = mul + result[i + j + 1]  # Add to existing value at position
                
                result[i + j + 1] = sum_ % 10  # Store unit place
                result[i + j] += sum_ // 10    # Carry to previous index

        # Convert result list to string and remove leading zeros
        res_str = "".join(map(str, result)).lstrip('0')
        return res_str if res_str else "0"