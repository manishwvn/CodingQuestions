class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check_pal(pal_list):
            start, end = 0, len(pal_list) - 1
            while start < end:
                if pal_list[start] == pal_list[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
            
        
        if len(s) == 1:
            return True
        pal_list = []
        for char in s:
            if char.isalnum():
                pal_list.append(char.lower())
                
        return check_pal(pal_list)
        