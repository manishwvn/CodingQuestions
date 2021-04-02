class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 1 and digits[0] == 0:
            return [1]
    
        rev_digits = digits[::-1]
        carry = 0    
        
        for i in range(len(rev_digits)):    
            if rev_digits[i] != 9:
                rev_digits[i] += 1
                carry = 0
                break
                
            else:
                carry = 1
                rev_digits[i] = (rev_digits[i] + carry) % 10
                
        
        if carry == 1:
            rev_digits.append(carry)
        return rev_digits[::-1]