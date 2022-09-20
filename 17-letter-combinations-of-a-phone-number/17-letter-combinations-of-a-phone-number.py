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
        
        def helper(pos, path):
            
            if pos == len(digits):
                result.append("".join(path))
                return 
            
            chars = hm[digits[pos]]
            for char in chars:
                path.append(char)
                helper(pos + 1, path)
                path.pop()

        helper(0, [])
        return result
        
        