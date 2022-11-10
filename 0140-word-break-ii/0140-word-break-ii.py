class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        memo = {}
        
        def helper(string):
            if string in memo: return memo[string]
            
            result = []
            
            for i in range(len(string)):
                prefix = string[:i+1]
                
                if prefix in word_set:
                    if prefix == string:
                        result.append(string)
                        
                    else:
                        rest = helper(string[i+1:])
                        for word in rest:
                            phrase = prefix + " " + word
                            result.append(phrase)
            
            memo[string] = result
            return result
            
            
                
                
            
            
        
        
        return helper(s)