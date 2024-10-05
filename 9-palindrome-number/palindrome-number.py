class Solution:
    def isPalindrome(self, x: int) -> bool:

        if (x < 0) or (x % 10 == 0 and x != 0): return False

        input_num, reverse = x, 0

        while x > 0:
            mod = x % 10
            reverse = reverse * 10 + mod
            x //= 10

        return reverse == input_num


        