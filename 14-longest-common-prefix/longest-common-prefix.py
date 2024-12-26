class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Handle empty input
            return ""

        # Find the shortest string without using min(..., key=len)
        min_len = float('inf')
        min_str = ""
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                min_str = s

        if not min_str: #handle empty string in the list
            return ""

        result = ""
        for j in range(len(min_str)):
            for i in range(len(strs)):
                if j >= len(strs[i]) or min_str[j] != strs[i][j]:
                    return result  # Important: Return immediately if mismatch
            result += min_str[j] #only add to result if all match

        return result