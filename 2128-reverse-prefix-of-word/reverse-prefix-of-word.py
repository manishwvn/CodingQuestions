class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        def reverse(string):
            str_list = list(string)
            l, r = 0, len(str_list) - 1
            while l < r:
                str_list[l], str_list[r] = str_list[r], str_list[l]
                l += 1
                r -= 1
            return "".join(str_list)

        for i in range(len(word)):
            if word[i] == ch:
                rev_str = reverse(word[:i+1])
                return rev_str + word[i+1:]

        return word