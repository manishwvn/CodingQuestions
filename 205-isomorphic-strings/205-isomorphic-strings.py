class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) == 1 and len(t) == 1:
            return True
        
        s_map, t_map = {},{}        
        for i in range(len(s)):
            s_map[s[i]] = i
        
        for i in range(len(t)):
            t_map[t[i]] = i
            
        print(s_map.values())
        print(t_map.values())
        return list(s_map.values()) == list(t_map.values())
            

        