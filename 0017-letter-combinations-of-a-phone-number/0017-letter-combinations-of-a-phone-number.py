class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        hm = {  '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
             }
        
        if len(digits) == 1:
            return [x for x in hm[digits[0]]]
        
        result = []
        
        
        def backtrack(pos, currStr):
            if len(currStr) == len(digits):
                result.append(currStr)
                return 
                
            chars = hm[digits[pos]]
            for char in chars:
                backtrack(pos+1, currStr + char)
        
        backtrack(0, "")
        
        return result
        