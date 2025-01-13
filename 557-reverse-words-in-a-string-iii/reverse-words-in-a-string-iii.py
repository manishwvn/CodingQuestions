class Solution:
    def reverseWords(self, s: str) -> str:

        s_list = list(s)
        i = 0
        for j in range(len(s_list)):
            if s[j] == " " or j == len(s_list) - 1:
                l, r = i, j - 1

                if j == len(s_list) - 1:
                    r = j

                while l < r:
                    s_list[l], s_list[r] = s_list[r], s_list[l]
                    l += 1
                    r -= 1
                i = j + 1
        
        return "".join(s_list)
        