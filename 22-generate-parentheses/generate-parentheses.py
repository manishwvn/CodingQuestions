class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #optimized backtracking
        result = []

        def generate(curr_string, left_count, right_count):
            if len(curr_string) == 2 * n:
                result.append("".join(curr_string))
                return

            if left_count < n:
                curr_string.append('(')
                generate(curr_string, left_count + 1, right_count)
                curr_string.pop()

            if right_count < left_count:
                curr_string.append(')')
                generate(curr_string, left_count, right_count + 1)
                curr_string.pop()

        curr_string = []
        left_count, right_count = 0, 0 
        generate(curr_string, left_count, right_count)
        return result