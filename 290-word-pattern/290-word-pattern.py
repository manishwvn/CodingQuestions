class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False
    
        pmap, smap = {}, {}
        for i in range(len(s_list)):
            if pmap.get(pattern[i], -1) != smap.get(s_list[i], -1):
                return False
            pmap[pattern[i]] = i
            smap[s_list[i]] = i
        
        return True
            
        