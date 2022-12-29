class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #inefficient - O(n * k * log(k))
        
        
        hm = defaultdict(list)
        
        for word in strs:
            sortWord = "".join(sorted(word))
            hm[sortWord].append(word)
            
        return hm.values()
        
        
        
        
        
            
            
        
        