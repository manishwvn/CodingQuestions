class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:  # If it's an opening bracket
                stack.append(char)

        return not stack  # Return True if stack is empty, else False