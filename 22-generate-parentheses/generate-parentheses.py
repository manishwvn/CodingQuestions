class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #brute force backtracking
        result = []

        def valid_par(string):
            count = 0

            for char in string:
                if char == '(':
                    count += 1
                
                else:
                    count -= 1
                
                if count < 0:
                    return False

            return count == 0



        def generate(curr_string):
            if len(curr_string) == 2 * n:
                if valid_par(curr_string):
                    result.append("".join(curr_string))
                
                return

            # curr_string.append('(')
            # generate(curr_string)
            # curr_string.pop()

            # curr_string.append(')')
            # generate(curr_string)
            # curr_string.pop()

            for char in ['(', ')']:
                curr_string.append(char)
                generate(curr_string)
                curr_string.pop()
            
        curr_string = []
        generate(curr_string)
        return result