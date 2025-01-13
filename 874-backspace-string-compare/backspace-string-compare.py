class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        #using stack
        def build(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            
            return stack

        s_ = build(s)
        t_ = build(t)

        return s_ == t_
        