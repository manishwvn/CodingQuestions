class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        h_map = collections.defaultdict(list)
        
        for s in strs:
            charset = [0]*26
            
            for char in s:
                charset[ord(char)-ord('a')]+=1
                
            h_map[tuple(charset)].append(s)
            
        return [i for i in h_map.values()]