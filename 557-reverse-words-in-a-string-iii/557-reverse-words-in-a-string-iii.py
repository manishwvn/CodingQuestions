class Solution:
    def reverseWords(self, s: str) -> str:
        def rev_help(string):
            str_list = [char for char in string]
            str_list = list(reversed(str_list))
            print(str_list)
            return "".join(str_list)
        
        arr = s.split(' ')
        for i in range(len(arr)):
            arr[i] = rev_help(arr[i])
            
        return " ".join(arr)
        