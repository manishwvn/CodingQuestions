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
        
        def helper(pos, substr):
            
            if len(substr) == len(digits):
                result.append(substr)
                return 
            
            if pos > len(digits): return
            
            chars = hm[digits[pos]]
            for char in chars:
                # substr = substr + char
                helper(pos + 1, substr + char)
                

        helper(0, "")
        return result
        
        