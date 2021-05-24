def keypadCombinations(digits, keypadcodes):
    if len(digits) == 0:
        return ['']
    
    firstchar = digits[0]
    remdigits = digits[1:]
    
    recresult = keypadCombinations(remdigits, keypadcodes)
    result = []
    
    chars = keypadcodes[int(firstchar)]
    for i in range(0, len(chars)):
        charcode = chars[i]
        for recstring in recresult:
            result.append(charcode + recstring)
            
    return result
        


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        keypadcodes = ["", "", "abc", "def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        if digits == "":
            return []
        result = keypadCombinations(digits, keypadcodes)
        return result
        