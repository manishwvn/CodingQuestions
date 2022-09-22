class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def helper(open_, close_, path):
            if n == open_ == close_:
                result.append("".join(path.copy()))
                return 
                
            if open_ < n:
                path.append("(")
                helper(open_ + 1, close_, path)
                path.pop()
                
            if close_ < open_:
                path.append(")")
                helper(open_, close_ + 1, path)
                path.pop()
        
        helper(0, 0, [])
        return result