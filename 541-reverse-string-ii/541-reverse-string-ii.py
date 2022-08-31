class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for i in range(0, len(s_list), 2*k):
            s_list[i:i+k] = reversed(s_list[i:i+k])
            
        print(s_list)
        return "".join(s_list)
        
        