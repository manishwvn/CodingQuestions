class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        
        queue = deque()
        visited = set()
        result = []
        
        queue.append((0, ""))
        
        while queue:
            i, cs = queue.popleft()
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in word_set:
                    
                    queue.append((j, cs + " " + s[i:j]))
                    if j == len(s):
                        result.append((cs + " " + s[i:j]).strip())
                        
                    
            # visited.add(i)
            
        return result