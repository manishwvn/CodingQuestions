class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        if len(s) == 1:
            return True if s[0] == '1' else 0
        
        curr_len_1, max_len_1 = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                curr_len_1 += 1
            else:
                curr_len_1 = 0
                
            max_len_1 = max(curr_len_1, max_len_1)
            
            
        curr_len_0, max_len_0 = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                curr_len_0 += 1
            else:
                curr_len_0 = 0
                
            max_len_0 = max(curr_len_0, max_len_0)
            
        return True if max_len_1 > max_len_0 else False
        