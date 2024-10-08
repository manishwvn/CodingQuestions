class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_word = s.lower().split()
        s_list = []

        for word in s_word:
            for x in word:
                if x.isalnum():
                    s_list.append(x)
        start, end = 0, len(s_list) - 1
        print(s_list)

        

        while start <= end:
            if s_list[start] == s_list[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

        
        