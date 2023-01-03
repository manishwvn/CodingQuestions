class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        count = 0
        hm = defaultdict(list)
        
        for word in words:
            hm[word[0]].append(word[1:])
            
        print(hm)
        
        for char in s:
            prev = hm[char]
            hm[char] = []
            
            for rem in prev:
                if rem == '':
                    count += 1
                    
                else:
                    hm[rem[0]].append(rem[1:])
                    
        return count
        