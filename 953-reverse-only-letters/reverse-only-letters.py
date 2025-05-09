class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        s_list = list(s)
        l, r = 0, len(s_list) - 1

        while l <= r:
            if s_list[l].isalpha() and s_list[r].isalpha():
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1

            elif not s_list[l].isalpha():
                l += 1
            elif not s_list[r].isalpha():
                r -= 1
        
        return ''.join(char for char in s_list)


        